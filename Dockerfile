FROM python:3.8

EXPOSE 8080

WORKDIR app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

#COPY . .
COPY main.py main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]