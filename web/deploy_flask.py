# Deploy Flask com Gunicorn
# gunicorn -w 4 flask_exemplo:app
# Dockerfile exemplo:
# FROM python:3.11
# WORKDIR /app
# COPY . .
# RUN pip install flask gunicorn
# CMD ["gunicorn", "-w", "4", "flask_exemplo:app"]
