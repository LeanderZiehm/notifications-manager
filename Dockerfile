FROM python:3.12-slim

WORKDIR /usr/src/app

COPY src/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app .

# Run FastAPI using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
