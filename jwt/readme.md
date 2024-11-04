# JWT Demo med Flask-JWT-Extended

Dette er en simpel demonstration af hvordan man kan bruge JSON Web Tokens (JWT) i en Flask applikation ved hjælp af flask-jwt-extended modulet.

## Installation
```bash
pip install flask-jwt-extended
```

## Funktionalitet i demo
Denne demo viser:
- Hvordan man laver login og får et access token
- Hvordan man beskytter routes med @jwt_required decorator
- Hvordan man refresher tokens
- Hvordan man får bruger information fra token

## Kør demo
```bash
python app.py
