# Florist Community Website

A Django web app built as a capstone project for a retail-florist platform: user accounts, an article feed with comments, image uploads for customers and experts, and a real-time chat room over WebSockets.

> Status: early prototype (2020), kept as a reference project. See [Roadmap](#roadmap).

## Features

- **Accounts** – registration, login and logout on top of `django.contrib.auth`
- **Articles & comments** – paginated article feed (8 per page); visitors can leave comments
- **Customer / expert pages** – profile forms with photo upload (`ImageField`)
- **Real-time chat** – WebSocket chat room built with Django Channels (`/ws/chatroom/<room>/`)
- **Admin** – content management through the Django admin

## Tech stack

Python · Django · Django Channels (ASGI) · django-crispy-forms · SQLite (default) or MySQL · HTML/CSS/JS (Amaze UI)

## Project layout

```
web/
├── web/        # project settings, URLs, ASGI/WSGI
├── main/       # landing pages, customer/expert models, photo upload
├── register/   # auth views, articles and comments
└── chat/       # Channels consumer, routing and chat templates
```

## Getting started

```bash
git clone https://github.com/lrddrl/website.git
cd website
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cd web
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```

Open http://127.0.0.1:8000/.

### Configuration

Settings are read from environment variables; the defaults are for local development only.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | insecure dev key | Set to a long random value in any shared environment |
| `DJANGO_DEBUG` | `True` | Set to `False` in production |
| `DJANGO_ALLOWED_HOSTS` | *(empty)* | Comma-separated host names |
| `DB_ENGINE` | `sqlite` | Set to `mysql` to use MySQL |
| `DB_NAME` / `DB_USER` / `DB_PASSWORD` / `DB_HOST` / `DB_PORT` | `capstone` / `root` / *(empty)* / `localhost` / `3306` | MySQL connection (only with `DB_ENGINE=mysql`) |

## Roadmap

- [ ] Tests for auth, article pagination and comments (`register/tests.py` is still a stub)
- [ ] Replace `locals()` template contexts with explicit ones
- [ ] Remove `main.Customer` (it has a plain-text password field and should be replaced by `auth.User`)
- [ ] Channel layer + persisted chat messages
- [ ] Product catalogue, cart and checkout (the "e-commerce" part of the original plan)
- [ ] Move to a current Django LTS and add CI

## License

No license has been chosen yet; all rights reserved by the author until one is added.
