from django.core.management import BaseCommand
from Taskify_main.models import SystemVariables
import os
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.init_system_variables()

    def init_system_variables(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_variables.json')

        with open(file_path) as json_file:
            data = json.load(json_file)

        for variables in data:
            sv, is_created = SystemVariables.objects.get_or_create(
                code=variables["code"],
                title=variables["title"],
                value=variables["value"]
            )
            wrt_out = str(sv)
            if is_created:
                wrt_out = self.style.SUCCESS(wrt_out)
            self.stdout.write(wrt_out)
