# Amharic Wordle (Static Frontend)

A lightweight, fully client‑side Amharic Wordle you can deploy to Vercel as a static site. No backend required.

# Live site
https://amharic-wordle-game.vercel.app/

## Features
- 4-letter Amharic words from `wordle_words.txt`
- 6 attempts per game
- Colored feedback (green/yellow/gray) with flip animation
- Error feedback (shake), toast messages, and a help modal
- Confetti when you win 🎉

## Local preview (Windows PowerShell)
You can open `index.html` directly, but most browsers block `fetch()` for local files. Run a tiny static server instead:

```powershell
# Using Python 3 (recommended)
python -m http.server 5500 ; Start-Process http://localhost:5500/

# Or using Node (if installed)
# npx serve -l 5500
```

Then open http://localhost:5500/

## Deploying to Vercel
1. Push this folder to GitHub (or GitLab/Bitbucket).
2. In Vercel, click New Project → Import the repo.
3. Framework preset: "Other".
4. Build command: leave empty (static).
5. Output directory: `.` (project root).
6. Deploy.

Vercel will serve `index.html` and the `static/` assets directly.

## Project structure
```
index.html            # App shell
static/styles.css     # Theme and animations
static/app.js         # Game logic (client-side)
wordle_words.txt      # Dictionary (UTF-8, Amharic words)
```

Python files (`wordle.py`, `play_wordle.py`, etc.) are kept for reference; they aren't used by the web frontend.

## Customization
- Change word length: update `WORD_LENGTH` and `MAX_ATTEMPTS` in `static/app.js`, and ensure `wordle_words.txt` contains words of that length.
- Theme: tweak CSS variables at the top of `static/styles.css`.
- Messages: edit Amharic strings in `static/app.js` and modal text in `index.html`.

## Troubleshooting
- Blank board or no words: make sure `wordle_words.txt` is present and encoded as UTF‑8, and contains 4‑character Amharic words.
- Local file access error: run via a local server as shown above so `fetch()` can load the dictionary.

Enjoy! እንኳን ደስ አለዎት።
