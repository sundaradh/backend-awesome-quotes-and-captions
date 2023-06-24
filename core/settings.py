from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o-j%7b9rfu##h1b0bc7hosx5yt%bhq2s#l3%x4z(4r$i!bekvd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # ...
    'baton',
    'django.contrib.admin',
    # ... (place baton.autodiscover at the very end)

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'baton.autodiscover',
    'rest_framework',
    'django_admin_generator',
    'import_export',
    # local apps
    'users',
    'category',
    'post',
    'notification',

]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),

    # for json only in api link
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    # )
}

BATON = {
    'SITE_HEADER': 'Awmrit',
    'SITE_TITLE': '',
    'INDEX_TITLE': 'Site administration',
    'SUPPORT_HREF': 'https://github.com/iamawmrit',
    'COPYRIGHT': 'copyright © 2022 <a href="https://amrit-adhikari.com.np/" target="_blank" >Amrit</a>',
    'POWERED_BY': '<a href="https://amrit-adhikari.com.np/" target="_blank" >Amrit Adhikari</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    # 'SEARCH_FIELD': {

    'MENU': (
        {
            'type': 'title',
            'label': 'Main',
            'apps': ('auth', 'baton', 'users', 'category', 'post', 'notification', 'likes', 'favorite', 'authtoken'),
        },

        # {
        #
        #     'type': 'app',
        #     'name': 'auth',
        #     'label': 'Authentication',
        #     'icon': 'fas fa-lock',
        #     'models': (
        #
        #         {
        #             'name': 'email_token',
        #             'label': 'email_token',
        #             'icon': 'fas fa-users',
        #
        #         },
        #     ),
        #
        # },

        {
            'type': 'app',
            'name': 'users',
            'label': 'Users',
            'icon': 'fas fa-user',
            'models': (

                {

                    'name': 'user',
                    'label': 'Users',
                    'icon': 'fas fa-user',
                },
                {
                    'name': 'payment',
                    'label': 'Payment',
                    'icon': 'fas fa-money-bill',
                },

                {
                    'name': 'userprofile',
                    'label': 'User Profile',
                    'icon': 'fas fa-user',
                },

            ),
        },
        {
            'type': 'app',
            'name': 'category',
            'label': 'Category',
            'icon': 'fas fa-box',
            'models': (
                {
                    'name': 'category',
                    'label': 'Category',
                    'icon': 'fas fa-box',

                },
            ),

        },
        {
            'type': 'app',
            'name': 'post',

            'label': 'Post',
            'icon': 'fas fa-list',
            'models': (
                {
                    'name': 'post',
                    'label': 'Post',
                    'icon': 'fas fa-list',

                },
                {
                    'name': 'like',
                    'label': 'Like',
                    'icon': 'fas fa-heart',

                },
                {
                    'name': 'favorite',
                    'label': 'Favorite',
                    'icon': 'fas fa-star',
                },
            ),
        },
        {
            'type': 'app',
            'name': 'notification',
            'label': 'Notification',
            'icon': 'fas fa-bell',
            'models': (
                {
                    'name': 'notification',
                    'label': 'Notification',
                    'icon': 'fas fa-bell',

                },
            ),
        },

    ),

}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'core.urls'
AUTH_USER_MODEL = 'users.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "post.context_processors.get_admin_stats",
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'amritcom_awesome',
#         'USER': 'amritcom_awmrit',
#         'PASSWORD': 'amritcom_awesome',
#         'HOST': '148.163.122.62',
#         'PORT': '3306',
#     }
# }

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'awesome',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.codem/en/4.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
