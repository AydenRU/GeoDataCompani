FROM python:3.13.3

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "-m", "app.main"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
