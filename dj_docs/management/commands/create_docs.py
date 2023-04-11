import os
import re
import importlib
from django.core.management.base import BaseCommand
from django.conf import settings
from dj_docs.utils import (
    DOC_DIR, DOC_SOURCE, DOC_HTMLS, copy_paste_file, update_file_with_line, ModuleRST
)
from dj_docs.dj_docs.notepads import CONF


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_docs_directory()


def create_docs_directory():

    if os.path.exists(DOC_DIR):
        # Directory already exists, so remove it
        try:
            os.rmdir(DOC_DIR)
        except OSError:
            import shutil
            shutil.rmtree(DOC_DIR)

    # Create docs directory if it doesn't exist
    os.makedirs(DOC_DIR)

    # Call Sphinx-quickstart with default options
    os.system(f'sphinx-quickstart {DOC_DIR} --sep')
    create_config()
    create_hints()
    create_modules()

    # call make html and modify it
    os.system(f'make html -C {DOC_DIR}')
    modify_htmls()


def create_config():
    file_path = os.path.join(DOC_SOURCE, "conf.py")
    conf = importlib.import_module("docs.source.conf")
    project = getattr(conf, "project", "")
    copy_right = getattr(conf, "copyright", "")
    author = getattr(conf, "author", "")
    release = getattr(conf, "release", "0.1")
    exclude_patterns = getattr("doc.source.conf", "exclude_patterns", [])

    conf_dict = {
        'project': project,
        'copyright': copy_right,
        'author': author,
        'release': release,
        'exclude_patterns': exclude_patterns,
    }
    with open(file_path, "w") as f:
        configurations = CONF.format(**conf_dict)
        f.write(configurations)


def modify_htmls(document_html=DOC_HTMLS):
    pattern_static_href_from = r'href="_static'
    pattern_static_href_to = r'href="/docs/_static'
    pattern_static_src_from = r'src="_static'
    pattern_static_src_to = r'src="/docs/_static'

    for root, dirs, files in os.walk(document_html):
        for file_name in files:
            if file_name.endswith(".html"):
                # Read the HTML file
                file_path = os.path.join(root, file_name)
                with open(file_path, "r") as f:
                    content = f.read()

                # Replace the string
                updated_content = re.sub(pattern_static_href_from, pattern_static_href_to, content)
                updated_content = re.sub(pattern_static_src_from, pattern_static_src_to, updated_content)

                for re_file_name in files:
                    if file_name.endswith(".html"):
                        # replace the html link
                        a_ref = f'href="{re_file_name}'
                        a_ref_to = f'href="/docs/{re_file_name}'
                        updated_content = re.sub(a_ref, a_ref_to, updated_content)

                with open(file_path, "w") as f:
                    f.write(updated_content)


def create_hints():

    # copy hints source to destination
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(current_dir, 'hints')
    destination = DOC_SOURCE
    include_list = ['intro.md', 'configuration.md']
    copy_paste_file(source, destination, include_list)

    # update the hints module documentation
    index_path = os.path.join(DOC_SOURCE, 'index.rst')
    modules = [f'   {i}' for i in include_list]
    # Replace with the names of your content modules
    update_file_with_line(index_path, modules, ':caption: Contents:')


def create_modules():
    rst_files = set()
    for sections in settings.DOC_STRING_MODULES:
        section = sections.get('section')
        modules = sections.get('modules')
        for module in modules:
            module_name = module.get('module_name')
            synopsis = module.get('synopsis')
            klass = module.get('class') or None
            func = module.get('function') or None

            rst_file = ModuleRST(
                section, module_name, synopsis,
                klass=klass, func=func
            ).create()
            rst_files.add(rst_file)
            'configuration.md'
    index_path = os.path.join(DOC_SOURCE, 'index.rst')
    update_file_with_line(index_path, list(f'   {i}' for i in rst_files), 'configuration.md')



