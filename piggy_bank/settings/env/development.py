from pathlib import Path
from ..base import *
from ..security import *
from ..db import *
from ..locale import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

SQLITE_DB_PATH = Path(BASE_DIR).resolve().parent / "db" / "db.sqlite3"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": SQLITE_DB_PATH},
}

DEBUG = True
