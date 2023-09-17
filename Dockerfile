FROM python:3.11.5
WORKDIR /calculator_app

COPY . .
EXPOSE 8080

CMD ["python", "/calculator_app/main.py"]
