FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip fontconfig

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 18412
EXPOSE 44950
EXPOSE 7335

CMD ["python3", "server.py", "0.0.0.0"]
