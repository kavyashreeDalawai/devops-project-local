# Stage 1: Build dependencies
FROM python:3.11-alpine AS builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev postgresql-dev libffi-dev

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.11-alpine AS runner

WORKDIR /app

RUN apk add --no-cache libpq

# Copy installed dependencies from builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV FLASK_APP=service:create_app
ENV FLASK_DEBUG=0

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
