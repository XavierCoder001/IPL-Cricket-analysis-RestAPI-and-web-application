# IPL Cricket Analysis — REST API & Web Application

A two-service Python project for querying IPL (Indian Premier League) cricket statistics. The REST API serves match and player data, and the web application provides a browser-based UI that consumes the API.

## Project Structure

```
├── IPL_API_SERVICE/   # Flask REST API (runs on port 5000)
│   ├── app.py         # API routes
│   ├── ipl.py         # Team vs team logic
│   └── juggad.py      # Batsman, bowler, and team record logic
│
└── ipl-web-app/       # Flask web frontend (runs on port 8080)
    ├── app.py          # Web routes
    └── templates/
        └── index.html  # UI — team selector, batsman & bowler lookup
```

## Features

- **Team vs Team** — head-to-head record between any two IPL teams
- **Team Record** — overall wins/losses/no-results + record against every opponent
- **Batsman Record** — runs, average, strike rate, 50s, 100s, highest score, MoM awards (overall and against each team)
- **Bowler Record** — wickets, economy, average, strike rate, best figures, 3W+ hauls (overall and against each team)

Data is pulled live from Google Sheets (IPL matches and ball-by-ball datasets).

## Setup

**Requirements:** Python 3.x, Flask, pandas, numpy, requests

```bash
pip install flask pandas numpy requests
```

## Running the App

Start both services in separate terminals:

**Terminal 1 — API service (port 5000):**
```bash
cd IPL_API_SERVICE
python app.py
```

**Terminal 2 — Web app (port 8080):**
```bash
cd ipl-web-app
python app.py
```

Then open `http://127.0.0.1:8080` in your browser.

## API Endpoints

All endpoints are served from `http://127.0.0.1:5000`.

| Method | Endpoint | Query Params | Description |
|--------|----------|--------------|-------------|
| GET | `/api/teams` | — | List all IPL teams |
| GET | `/api/teamvteam` | `team1`, `team2` | Head-to-head record |
| GET | `/api/team-record` | `team_name` | Full team record |
| GET | `/api/batsman-record` | `batsman_name` | Batsman statistics |
| GET | `/api/bowling-record` | `bowler_name` | Bowler statistics |

**Example requests:**
```
GET /api/teamvteam?team1=Mumbai Indians&team2=Chennai Super Kings
GET /api/batsman-record?batsman_name=MS Dhoni
GET /api/bowling-record?bowler_name=JJ Bumrah
```

## Tech Stack

- **Backend:** Python, Flask
- **Data:** pandas, numpy
- **Data Source:** Google Sheets (IPL matches + ball-by-ball CSV)
- **Frontend:** Jinja2 templates (HTML)
