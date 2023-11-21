from pathlib import Path
import os
from decouple import config, Csv
# settings.py
import sentry_sdk

sentry_sdk.init(
    dsn="https://64a54e24f1fc2bf2013576d28734285a@o4506253473742848.ingest.sentry.io/4506253475512320",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# Decoupled environment settings
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Authentication
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "blog",                         # Blog articles by the author (and by guests?)
    "guests",                       # Contact page and guestbook
    "locos",                        # All details associated primarily with locomotives
    "people",                       # All details associated primarily with CME's etc...
    "sites",                        # All details associated primarily with depots/works/scrapyards etc...
    "reports",                      # The reports page
    "news",                         # News and Views (to be decided ...)
    "home",                         # Index page and introduction
    "dbase",                        # All models - better this way as many apps use many models
    "api",                          # API to allow for either use of React and/or data distribution

    "cms",                          # BRDatabase Wagtail CMS - may not be necessary

    # Wagtail
    "wagtail.contrib.forms",        # Models for creating forms on your pages and viewing submissions.
    "wagtail.contrib.redirects",    # Admin interface for creating arbitrary redirects on your site.
    "wagtail.embeds",               # Module governing oEmbed and Embedly content in Wagtail rich text fields.
    "wagtail.sites",                # Management UI for Wagtail sites.
    "wagtail.users",                # User editing interface.
    "wagtail.snippets",             # Editing interface for non-Page models and objects.
    "wagtail.documents",            # The Wagtail document content type.
    "wagtail.images",               # The Wagtail image content type.
    "wagtail.search",               # Search framework for Page content.
    "wagtail.admin",                # The administration interface for Wagtail, including page edit handlers.
    "wagtail",                      # The core functionality of Wagtail, such as the Page class, the Wagtail tree, and model fields.

    # Wagtail 
    "taggit",                       # Tagging framework for Django. This is used internally within Wagtail for image and document tagging and is available for your own models as well. 
    "modelcluster",                 # Extension of Django ForeignKey relation functionality, which is used in Wagtail pages for on-the-fly related object creation.

    # Allauth
    # https://docs.allauth.org/en/latest/installation/quickstart.html
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # Allauth... include the providers you want to enable:
    "allauth.socialaccount.providers.facebook",

    # Django-extensions
    # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#installing
    "django_extensions",

    # REST framework
    # https://www.django-rest-framework.org/#quickstart
    "rest_framework",

    # Django GUID
    # https://django-guid.readthedocs.io/en/latest/configuration.html
    "django_guid",

    # Easy thumbnails
    # https://pypi.org/project/easy-thumbnails/
    "easy_thumbnails",

    # Django Import Export
    # https://django-import-export.readthedocs.io/en/latest/installation.html
    "import_export",

    # Django Compressor
    # https://django-compressor.readthedocs.io/en/stable/quickstart.html#installation
    "compressor",

    # Django Filters
    # https://django-filter.readthedocs.io/en/stable/guide/install.html
    "django_filters",

    # Django Debug Toolbar
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    "debug_toolbar",

    # Cors Headers
    # https://pypi.org/project/django-cors-headers/
    "corsheaders",

    # Simple History
    # https://django-simple-history.readthedocs.io/en/latest/quick_start.html#install
    "simple_history",

    # Django-storages
    # https://django-storages.readthedocs.io/en/latest/
    # When ready, follow these instructions: https://django-storages.readthedocs.io/en/latest/backends/dropbox.html

    # Django Swagger
    # https://django-rest-swagger.readthedocs.io/en/latest/
    "rest_framework_swagger",
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': 'xyz'
        }
    }
}

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

DJANGO_GUID = {
    'GUID_HEADER_NAME': 'Correlation-ID',
    'VALIDATE_GUID': True,
    'RETURN_HEADER': True,
    'EXPOSE_HEADER': True,
    'INTEGRATIONS': [],
    'UUID_LENGTH': 32,
    'UUID_FORMAT': 'hex',
}

LOGGING = {
    'filters': {
        'correlation_id': {
            '()': 'django_guid.log_filters.CorrelationId'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'medium',
            'filters': ['correlation_id'],
        }
    },
    'formatters': {
        'medium': {
            'format': '%(levelname)s %(asctime)s [%(correlation_id)s] %(name)s %(message)s'
        }
    },
    'loggers': {
        'django_guid': {
            'handlers': ['console', 'logstash'],
            'level': 'WARNING',
            'propagate': False,
        }
    }

}

# Required for using Debug Toolbar - only works on ip addresses listed below
INTERNAL_IPS = [
    "127.0.0.1",
]

# CORS headers
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]

CORS_ALLOW_ALL_ORIGINS: True

CORS_URLS_REGEX = r"^/api/.*$"

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

MIDDLEWARE = [
    # Django GUID
    "django_guid.middleware.guid_middleware",

    # Cors Headers
    "corsheaders.middleware.CorsMiddleware",

    # My bespoke middleware
    "middleware.undesirable_country_blocker.CountryDenyMiddleware",
    "middleware.query_blocker.BlockSQLInjection",
    "middleware.old_db_rerouter.OldBRDatabaseReRouter",

    # Standard Django middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Wagtail middleware - Wagtail provides a simple interface for adding arbitrary redirects to your site and this module makes it happen.
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",

    # Allauth - Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",

    # Django Debug Toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # Simple History
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates'),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "website.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('BRD_DJANGO_DB'),
        'HOST': config('BRD_DJANGO_HOST'),
        'PORT': config('BRD_DJANGO_PORT'),
        'USER': config('BRD_DJANGO_USER'),
        'PASSWORD': config('BRD_DJANGO_PWD'),
    },
    'brd_main': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('BRD_MAIN_DB'),
        'HOST': config('BRD_MAIN_HOST'),
        'PORT': config('BRD_MAIN_PORT'),
        'USER': config('BRD_MAIN_USER'),
        'PASSWORD': config('BRD_MAIN_PWD'),
    },
    'brd_log': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('BRD_LOG_DB'),
        'HOST': config('BRD_LOG_HOST'),
        'PORT': config('BRD_LOG_PORT'),
        'USER': config('BRD_LOG_USER'),
        'PASSWORD': config('BRD_LOG_PWD'),
    },
    'brd_blog': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('BRD_BLOG_DB'),
        'HOST': config('BRD_BLOG_HOST'),
        'PORT': config('BRD_BLOG_PORT'),
        'USER': config('BRD_BLOG_USER'),
        'PASSWORD': config('BRD_BLOG_PWD'),
    },

}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",

    # Django-compressor
    "compressor.finders.CompressorFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ADMINS = [
    ("BRDatabase", "theBRDatabase@gmail.com"),
]

MANAGERS = ADMINS

# Default to dummy email backend. Configure dev/production/local backend
# as per https://docs.djangoproject.com/en/stable/topics/email/#email-backends
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

EMAIL_SUBJECT_PREFIX = "[BRDatabase]"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See https://docs.djangoproject.com/en/stable/topics/logging for
# more details on how to customise your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# WAGTAIL SETTINGS

# This is the human-readable name of your Wagtail install
# which welcomes users upon login to the Wagtail admin.
WAGTAIL_SITE_NAME = 'BR Database'

WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", "https://www.example.com")
# Replace the search backend
#WAGTAILSEARCH_BACKENDS = {
#  'default': {
#    'BACKEND': 'wagtail.search.backends.elasticsearch8',
#    'INDEX': 'myapp'
#  }
#}

# Wagtail email notifications from address
# WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'wagtail@myhost.io'

# Wagtail email notification format
# WAGTAILADMIN_NOTIFICATION_USE_HTML = True

# Reverse the default case-sensitive handling of tags
TAGGIT_CASE_INSENSITIVE = True
