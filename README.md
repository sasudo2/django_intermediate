# Django reCAPTCHA Demo

A small Django project that demonstrates a simple form protected by Google reCAPTCHA.

## What this project does

- Collects a user name and email.
- Validates the form with reCAPTCHA using django-recaptcha.
- Returns a success message for valid submissions.
- Returns a bot-suspected message for invalid submissions.

## Tech stack

- Python
- Django 5.x
- django-recaptcha
- SQLite (default local database)

## Project structure

- `intermediate/`: Django project settings and root URL config.
- `captcha/`: App containing form, model, view, URL, and template.
- `db.sqlite3`: Local SQLite database.
- `manage.py`: Django management entrypoint.

## Prerequisites

- Python 3.10+ (recommended)
- pip

## Quick start

1. Create and activate a virtual environment.

   Linux/macOS:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows (PowerShell):
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install dependencies.

   ```bash
   pip install django django-recaptcha
   ```

3. Apply migrations.

   ```bash
   python manage.py migrate
   ```

4. Run the development server.

   ```bash
   python manage.py runserver
   ```

5. Open the app in your browser.

   - Form page: http://127.0.0.1:8000/captcha/
   - Admin page: http://127.0.0.1:8000/admin/

## URL routes

- `/captcha/` -> reCAPTCHA form page
- `/admin/` -> Django admin

## Configuration

reCAPTCHA keys are currently set directly in Django settings under:

- `RECAPTCHA_PUBLIC_KEY`
- `RECAPTCHA_PRIVATE_KEY`

For production use, move these values to environment variables and do not commit secret keys.

## App behavior

On POST to `/captcha/`:

- If form and captcha are valid: returns `Yay! you are human.`
- If invalid: returns `OOPS! Bot suspected.`

## Notes

- This project is configured for development (`DEBUG = True`).
- SQLite is suitable for local testing, not recommended for production workloads.
