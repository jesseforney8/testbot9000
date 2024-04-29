FROM python:3.8-slim-buster

WORKDIR /app

COPY discord/requirements.txt .

COPY pokemon_testing/ .

RUN pip install -r requirements.txt



CMD ["python3", "lan9000.py", "import pokebase as pd.py"]
