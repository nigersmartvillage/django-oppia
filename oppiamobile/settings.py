"""
Django settings for OppiaMobile project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.utils.translation import gettext_lazy as _

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uzekt30thl4&hw)p@c#ht=b8mn!3l080kmnuk7ez+g5l%lb*p9'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

ALLOWED_HOSTS = []
DEBUG = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oppia.middleware.LoginRequiredMiddleware',

]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.i18n',
                'oppia.context_processors.get_points',
                'oppia.context_processors.get_version',
                'oppia.context_processors.get_settings'
            ],
            'debug': True,
        },
    },
]

INSTALLED_APPS = [
    'quiz',
    'profile',
    'content',
    'av',
    'settings',
    'summary',
    'reports',
    'activitylog',
    'viz',
    'gamification',
    'oppia',
    'tastypie',
    'helpers',
    'integrations',
    'crispy_forms',
    'sass_processor',
    'sorl.thumbnail',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TIME_ZONE = 'UTC'
USE_TZ = True
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

ROOT_URLCONF = 'oppiamobile.urls'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


# Email
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/'
SERVER_EMAIL = 'adming@email.org'
EMAIL_SUBJECT_PREFIX = '[SUBJECT_PREFIX]: '


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-GB'
USE_I18N = True
USE_L10N = True

LANGUAGES = ('en', _('English'))

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login and logout settings
# https://docs.djangoproject.com/en/1.11/ref/settings/#login-redirect-url
LOGIN_URL = '/profile/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# Exempt URLs (used by LoginRequiredMiddleware)
LOGIN_EXEMPT_URLS = (
    r'^server/$',
    r'^profile/login/$',
    r'^profile/register/',
    r'^profile/reset/',
    r'^profile/setlang/$',
    r'^profile/delete/complete/$',
    r'^$',
    r'^about/$',
    r'^terms/$',
    r'^api/',  # allow any URL under api/* - auth handled by api_key
    r'^modules/api/',  # allow any URL under modules/api/* - auth by api_key
    r'^badges/api/',  # allow any URL under badges/api/* - auth by api_key
    r'^content/video-embed-helper/$',
    r'^media/temp/',
    r'^media/uploaded/',
    r'^api/activitylog/',
    r'^view/$',
)

# OppiaMobile Settings
COURSE_UPLOAD_DIR = os.path.join(ROOT_DIR, 'upload')

OPPIA_METADATA = {
    'NETWORK': True,
    'DEVICE_ID': True,
    'SIM_SERIAL': True,
    'WIFI_ON': True,
    'NETWORK_CONNECTED': True,
    'BATTERY_LEVEL': True,
    'GPS': False,
}

# turns on/off ability for users to self register
OPPIA_ALLOW_SELF_REGISTRATION = True
OPPIA_SHOW_GRAVATARS = True

# prevents anyone without is_staff status being able to upload courses,
# setting to False allows any registered user to upload a course
OPPIA_STAFF_ONLY_UPLOAD = True

# determines if the points system is enabled
OPPIA_POINTS_ENABLED = True

# if OPPIA POINTS_ENABLED is false, then the next 3 settings are ignored
# prevent staff from earning points
OPPIA_STAFF_EARN_POINTS = False

# stops owners of courses earning points
OPPIA_COURSE_OWNERS_EARN_POINTS = False
# stops teachers of courses earning points
OPPIA_TEACHERS_EARN_POINTS = False
# determines if the badges system is enabled
OPPIA_BADGES_ENABLED = True

BADGE_AWARD_METHOD_ALL_ACTIVITIES = 'all activities'
BADGE_AWARD_METHOD_FINAL_QUIZ = 'final quiz'
BADGE_AWARD_METHOD_ALL_QUIZZES = 'all quizzes'

BADGE_AWARDING_METHOD = BADGE_AWARD_METHOD_ALL_ACTIVITIES

OPPIA_GOOGLE_ANALYTICS_ENABLED = False
OPPIA_GOOGLE_ANALYTICS_CODE = 'YOUR_GOOGLE_ANALYTICS_CODE'
OPPIA_GOOGLE_ANALYTICS_DOMAIN = 'YOUR_DOMAIN'

OPPIA_MAX_UPLOAD_SIZE = 5242880  # max course file upload size - in bytes

OPPIA_VIDEO_FILE_TYPES = ("video/m4v", "video/mp4", "video/3gp", "video/3gpp")
OPPIA_AUDIO_FILE_TYPES = ("audio/mpeg", "audio/amr", "audio/mp3")
OPPIA_MEDIA_FILE_TYPES = OPPIA_VIDEO_FILE_TYPES + OPPIA_AUDIO_FILE_TYPES
OPPIA_MEDIA_IMAGE_FILE_TYPES = ("image/png", "image/jpeg")

OPPIA_UPLOAD_TRACKER_FILE_TYPES = [("application/json")]

# Android app PackageId - for Google Play link and opening activities
# from digest
OPPIA_ANDROID_DEFAULT_PACKAGEID = 'org.digitalcampus.mobile.learning'
OPPIA_ANDROID_PACKAGEID = 'org.digitalcampus.mobile.learning'

# if the app is not on Google Play, we rely on the core version for store
# links
OPPIA_ANDROID_ON_GOOGLE_PLAY = True

API_LIMIT_PER_PAGE = 0

SCREENSHOT_GENERATOR_PROGRAM = "ffmpeg"
SCREENSHOT_GENERATOR_PROGRAM_PARAMS = \
    "-i %s -r 0.02 -s %dx%d -f image2 %s/frame-%%03d.png"

MEDIA_PROCESSOR_PROGRAM = "ffprobe"
MEDIA_PROCESSOR_PROGRAM_PARAMS = ""

# Import secret_settings.py (if exists)
# > see settings_secret.py.template for reference
try:
    from oppiamobile.settings_secret import *
except ImportError:
    print("settings_secret.py file could not be found.")
