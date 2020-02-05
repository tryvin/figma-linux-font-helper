FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 18412
EXPOSE 7335

CMD ["python", "server.py", "0.0.0.0"]
