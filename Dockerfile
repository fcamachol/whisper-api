FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
