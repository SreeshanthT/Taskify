from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': "localhost",
        'USER': "TaskifyUser",
        'PASSWORD': "Taskify123",
        'NAME': "Taskify",
        'PORT': "3306",
    }
}