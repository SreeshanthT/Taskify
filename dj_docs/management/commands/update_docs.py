import os
from django.core.management.base import BaseCommand
from dj_docs.management.commands import modify_htmls
from dj_docs.utils import DOC_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):

        # call make html and modify it
        os.system(f'make html -C {DOC_DIR}')
        modify_htmls()
