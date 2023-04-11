from django.conf import settings
import os

try:
    DOC_DIR = settings.DOC_DIR
except:
    DOC_DIR = os.path.join(settings.BASE_DIR, 'docs')
