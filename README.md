# Flask IP App

A tiny Flask app that shows the client's IP on a beautiful index page and also via a JSON API.

## Run

```bash
pip install -r requirements.txt
python app.py
# open http://localhost:8000
```

## Endpoints

- `/` — pretty HTML page showing your IP
- `/api/ip` — JSON: `{ "ip": "x.x.x.x" }`
