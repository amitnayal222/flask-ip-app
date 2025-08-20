FROM python:3.13-alpine AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt
COPY . .

FROM python:3.13-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY --from=builder /app /app

EXPOSE 8000
CMD ["python", "app.py"]

