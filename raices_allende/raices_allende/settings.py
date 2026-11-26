"""Configuración del proyecto Raíces Allende."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# CLAVE SECRETA: en un proyecto real no la compartas ni la subas a internet.
SECRET_KEY = 'dEwU-4gpBRf5EtELatXzFofbFBXtQ-pB9eFgnyMPBgU8QWb7N6qYZbOYlgOnd3vWTx8'

# MODO DESARROLLO (cuando lo subas a internet cámbialo a False)
DEBUG = True

ALLOWED_HOSTS = ['*']  # permite cualquier dirección mientras desarrollas

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',  # nuestra app con las páginas del sitio
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'raices_allende.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'templates'],
        'APP_DIRS': True,  # busca plantillas dentro de cada app (templates/)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'raices_allende.wsgi.application'

# Base de datos (por defecto SQLite, no necesitas instalar nada más)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔒 Configuración de cierre de sesión
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Se cierra sesión al cerrar el navegador
SESSION_COOKIE_AGE = 86400  # 24 horas como respaldo