# AI Image Generator (AImage)

AI 모델 기반 그림 생성 web page

<br>

## Summary

사용자가 prompt를 제공하면 그 설명을 바탕으로 AI가 그림을 생성해 주는 웹사이트입니다. OpenAI에서 제공하는 그림 생성 모델 DALL·E를 기반으로 한 API를 사용하였습니다.

<br>

## Tech. Stack(s)

- Front-end: Bootstrap, Django
- Back-end: Django
- Database: SQLite3

<br>

## Setup

1. Install Python virtual environment.

   ```
   python3 -m venv .venv
   ```

2. Application setup

   ```
   pip3 install -r requirements.txt

   python3 manage.py makemigrations ai_image_generator
   python3 manage.py migrate
   python3 manage.py runserver
   ```
