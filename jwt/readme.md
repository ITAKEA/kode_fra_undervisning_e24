# JWT Demo med Flask-JWT-Extended

Dette er en simpel demonstration af hvordan man kan bruge JSON Web Tokens (JWT) i en Flask applikation ved hjælp af flask-jwt-extended modulet.

## Installation
```bash
git clone https://github.com/ITAKEA/kode_fra_undervisning_e24.git
cd jwt
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```

## Funktionalitet i demo
Denne demo viser:
- Hvordan man laver login og får et access token
- Hvordan man beskytter routes med @jwt_required decorator
- Hvordan man får bruger information fra token
- Hvordan man gemmer og læser en token i en cookie

Demoen følger som udgangspunkt denne dokumentation:

* https://flask-jwt-extended.readthedocs.io/en/stable

## Kør demo
```bash
python app.py
