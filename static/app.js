// Amharic Wordle frontend (pure client-side)
// Loads dictionary from wordle_words.txt, picks random 4-letter word, manages attempts.

const WORD_LENGTH = 4;
const MAX_ATTEMPTS = 6;

let dictionary = [];
let secret = ""; // uppercase
let attempts = []; // list of strings
let results = []; // list of letter state arrays
let gameOver = false;

const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const hintEl = document.getElementById("hint");
const guessForm = document.getElementById("guessForm");
const guessInput = document.getElementById("guessInput");
const newGameBtn = document.getElementById("newGameBtn");
const helpBtn = document.getElementById("helpBtn");
const helpModal = document.getElementById("helpModal");
const toastContainer = document.getElementById("toastContainer");
const infoBtn = document.getElementById("infoBtn");
const infoPanel = document.getElementById("infoPanel");

function loadDictionary() {
  return fetch("wordle_words.txt")
    .then(r => r.text())
    .then(text => {
      dictionary = text.split(/\r?\n/)
        .map(w => w.trim())
        .filter(w => w.length === WORD_LENGTH)
        .map(w => w.toUpperCase());
      if (dictionary.length === 0) {
        statusEl.textContent = "የ 4 ፊደል ቃላት አልተገኙም";
      }
    });
}

function pickSecret() {
  if (!dictionary.length) return;
  secret = dictionary[Math.floor(Math.random() * dictionary.length)].toUpperCase();
  // console.log("SECRET", secret); // For debugging only
}

function startGame() {
  attempts = [];
  results = [];
  gameOver = false;
  pickSecret();
  statusEl.textContent = "አዲስ ጨዋታ ተጀመረ";
  hintEl.textContent = "4 ፊደል ቃልን ይፈትኑ";
  guessInput.value = "";
  renderBoard();
}

function renderBoard() {
  boardEl.innerHTML = "";
  for (let i = 0; i < MAX_ATTEMPTS; i++) {
    const attempt = attempts[i];
    const result = results[i];
    for (let j = 0; j < WORD_LENGTH; j++) {
      const tile = document.createElement("div");
      tile.className = "tile";
      if (attempt) {
        tile.textContent = attempt[j];
        if (result) {
          // delay flip for cascade effect
          setTimeout(() => tile.classList.add("flip"), 60 * j + 10);
          if (result[j].inPosition) tile.classList.add("correct");
          else if (result[j].inWord) tile.classList.add("present");
          else tile.classList.add("absent");
        }
      }
      boardEl.appendChild(tile);
    }
  }
}

function computeResult(word) {
  // returns array of letter state objects {char, inWord, inPosition}
  const res = [];
  for (let i = 0; i < WORD_LENGTH; i++) {
    const ch = word[i];
    res.push({
      char: ch,
      inWord: secret.includes(ch),
      inPosition: secret[i] === ch
    });
  }
  return res;
}

function submitGuess(word) {
  if (gameOver) return;
  const up = word.trim().toUpperCase();
  if (up.length !== WORD_LENGTH) {
    setStatus(`ቃሉ መሆን አለበት ${WORD_LENGTH} ፊደል።`, true);
    showToast(`ፊደሉ አልተሟላም (${WORD_LENGTH})`, 'error');
    boardEl.classList.add('shake');
    setTimeout(() => boardEl.classList.remove('shake'), 360);
    return;
  }
  if (!dictionary.includes(up)) {
    setStatus("ቃሉ በዲክሽነሪ ውስጥ የለም።", true);
    showToast("የማይታወቅ ቃል", 'error');
    boardEl.classList.add('shake');
    setTimeout(() => boardEl.classList.remove('shake'), 360);
    return;
  }
  if (attempts.length >= MAX_ATTEMPTS) {
    setStatus("ሙከራዎቹ አልቋል።", true);
    return;
  }
  attempts.push(up);
  results.push(computeResult(up));
  renderBoard();

  if (up === secret) {
    setStatus("እንኳን ደስ አላቸው! ታሸነፍክ።", false);
    showToast("ተሸንፈርህ!", 'success');
    launchConfetti();
    gameOver = true;
    hintEl.textContent = `ቃሉ ነው: ${secret}`;
  } else if (attempts.length === MAX_ATTEMPTS) {
    setStatus("አልተሳካም።", false);
    showToast(`ተጨማሪ ሙከራ የለም | ${secret}`, 'error');
    gameOver = true;
    hintEl.textContent = `ቃሉ ነበረ: ${secret}`;
  } else {
    setStatus(`ቀረው ሙከራ: ${MAX_ATTEMPTS - attempts.length}`, false);
    showToast(`${MAX_ATTEMPTS - attempts.length} ሙከራ ቀርቷል`, 'info');
  }
  guessInput.value = "";
  guessInput.focus();
}

function setStatus(msg, isError) {
  statusEl.textContent = msg;
  statusEl.style.color = isError ? '#f87171' : '#9ca3af';
}

// Toasts
function showToast(message, type='info', timeout=2400) {
  const div = document.createElement('div');
  div.className = 'toast';
  if (type === 'error') div.classList.add('error');
  else if (type === 'success') div.classList.add('success');
  div.textContent = message;
  toastContainer.appendChild(div);
  requestAnimationFrame(() => div.classList.add('show'));
  setTimeout(() => {
    div.classList.remove('show');
    setTimeout(() => div.remove(), 300);
  }, timeout);
}

// Modal helpers
function openModal(modal) { modal.hidden = false; }
function closeModal(modal) { modal.hidden = true; }

helpBtn?.addEventListener('click', () => openModal(helpModal));
helpModal?.addEventListener('click', (e) => {
  if (e.target.dataset.close !== undefined || e.target.classList.contains('modal__backdrop')) {
    closeModal(helpModal);
  }
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && !helpModal.hidden) closeModal(helpModal);
});

// Confetti
function launchConfetti() {
  const colors = ['#22c55e', '#eab308', '#38bdf8', '#f472b6', '#a78bfa'];
  for (let i=0;i<50;i++) {
    const piece = document.createElement('div');
    piece.className = 'confetti';
    piece.style.left = Math.random()*100 + 'vw';
    piece.style.background = colors[Math.floor(Math.random()*colors.length)];
    const duration = 3000 + Math.random()*2000;
    piece.style.animation = `fall ${duration}ms linear forwards`;
    piece.style.animationDelay = (Math.random()*300) + 'ms';
    document.body.appendChild(piece);
    setTimeout(()=> piece.remove(), duration + 800);
  }
}

// Event listeners
guessForm.addEventListener("submit", (e) => {
  e.preventDefault();
  submitGuess(guessInput.value);
});
newGameBtn.addEventListener("click", () => { startGame(); showToast('አዲስ ጨዋታ', 'info'); });

// Info panel toggle
infoBtn?.addEventListener('click', () => {
  const isHidden = infoPanel.hasAttribute('hidden');
  if (isHidden) {
    infoPanel.removeAttribute('hidden');
    infoBtn.setAttribute('aria-expanded', 'true');
    showToast('Info panel opened', 'info', 1600);
  } else {
    infoPanel.setAttribute('hidden', '');
    infoBtn.setAttribute('aria-expanded', 'false');
  }
});

// Init
loadDictionary().then(() => startGame());
