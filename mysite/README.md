# mysite Django Project

A small Django project containing apps: `myapp`, `newyear`, and `tasks`.

This README provides quick setup, run, and testing instructions for development on macOS (zsh).

## Requirements

- Python 3.8+ (3.11 recommended)
- pip
- (optional) virtualenv or venv

## Setup (development)

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

If a `requirements.txt` exists, run:

```bash
pip install -r requirements.txt
```

If no `requirements.txt` is present, install Django:

```bash
pip install django
```

3. Apply migrations

```bash
python manage.py migrate
```

4. Create a superuser (optional, to access admin)

```bash
python manage.py createsuperuser
```

5. Collect static files (for production)

```bash
python manage.py collectstatic
```

## Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Tests

Run tests with:

```bash
python manage.py test
```

## Project layout

- `manage.py` - Django management script
- `mysite/` - Project settings and WSGI/ASGI entry points
- `myapp/`, `newyear/`, `tasks/` - Django apps, each with models, views, templates
- `db.sqlite3` - SQLite database file (development)

## Notes

- This README assumes development on macOS with zsh. Adjust virtualenv activation on other shells/platforms.
- If your project uses additional dependencies (e.g., `django-crispy-forms`, `requests`), add them to `requirements.txt`.
- Static files are located in app `static/` directories. Templates are under each app's `templates/` directory.

## Troubleshooting

- "ModuleNotFoundError: No module named 'django'": install Django in the active environment.
- Database issues: remove `db.sqlite3` and re-run `python manage.py migrate` to recreate a fresh database (this will remove existing data).

## Contact

For questions, check project files in the repository or contact the repository owner.
