# Deploy Django com Daphne
# daphne -b 0.0.0.0 -p 80 exemplo_django.asgi:application
# Dockerfile exemplo:
# FROM python:3.11
# WORKDIR /app
# COPY . .
# RUN pip install django daphne
# CMD ["daphne", "-b", "0.0.0.0", "-p", "80", "exemplo_django.asgi:application"]
