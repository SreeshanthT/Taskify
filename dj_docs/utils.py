from dj_docs import DOC_DIR
import os
import shutil
import importlib


def has_separate_source_and_build():
    build_path = os.path.join(DOC_DIR, 'build')
    source_path = os.path.join(DOC_DIR, 'build')
    return os.path.exists(build_path) and os.path.exists(source_path)

# TODO: no longer needful for choose separate source and build or not
# DOC_BUILD = os.path.join(DOC_DIR, '_build')
# DOC_SOURCE = DOC_DIR
# if has_separate_source_and_build():
#     DOC_BUILD = os.path.join(DOC_DIR, 'build')
#     DOC_SOURCE = os.path.join(DOC_DIR, 'source')


DOC_BUILD = os.path.join(DOC_DIR, 'build')
DOC_SOURCE = os.path.join(DOC_DIR, 'source')
DOC_CONF = os.path.join(DOC_SOURCE, 'conf.py')
DOC_HTMLS = os.path.join(DOC_BUILD, 'html')

DOC_STATIC_URL = '_static/'
DOC_STATIC_ROOT = os.path.join(DOC_HTMLS, '_static')


def get_variables(file_path):
    # conf_dict = {}
    # try:
    #     print('iam here')
    #     from docs.source import conf
    #     for name, value in conf.__dict__.items():
    #         print(name)
    #         if not name.startswith('__'):
    #             conf_dict[name] = value
    # except Exception as e:
    #     print(e)
    # return conf_dict

    # Create an empty dictionary to store the variables
    config_vars = {}

    # Use exec() to execute the code in the file
    with open(file_path, "r") as f:
        code = f.read()
    exec(code, config_vars)

    # Now you can access the variables in the dictionary
    print(config_vars)
    return config_vars


def get_line_number(file, search_string):

    with open(file, 'r') as index_file:
        lines = index_file.readlines()

    for i, line in enumerate(lines):
        if line.strip() == search_string:
            return i, lines
    else:
        # Handle case where `search_string` is not found
        return None, lines
    return None, lines


def update_file_with_line(file, update_list, update_after):

    line, lines = get_line_number(file, update_after)

    if line is not None:
        lines.insert(line + 1, '\n')
        next_line = line + 2
        for module_name in update_list:
            lines.insert(next_line, f'{module_name}\n')
            next_line += 1

    with open(file, 'w') as index_file:
        index_file.write(''.join(lines))


def create_files(root, file_name, contents):
    file_path = os.path.join(root, file_name)
    with open(file_path, "w") as f:
        f.write(contents)


def copy_paste_file(source, destination, include_list=[]):

    if include_list:
        for file in include_list:
            source_file_path = os.path.join(source, file)
            destination_file_path = os.path.join(destination, file)
            shutil.copy2(source_file_path, destination_file_path)
    else:
        files = os.listdir(source)
        for file in files:
            source_file_path = os.path.join(source, file)
            destination_file_path = os.path.join(destination, file)
            shutil.copy2(source_file_path, destination_file_path)


class RstModularError(Exception):
    pass


class ModuleRST(object):
    def __init__(self, section: str, module: str, synopsis: str, klass=None, func=None):
        self.section = section
        self.synopsis = synopsis
        self.module = module
        self.klass = klass
        self.func = func
        self.check_instances()

    def check_instances(self):
        if importlib.util.find_spec(self.module) is None:
            raise ImportError(f"Module '{self.module}' not found.")

    def create(self):
        if self.has_file_exists():
            with open(self.get_file_path(), "r") as file:
                contents = file.read()
            if self.get_contents() in contents:
                # TODO:raise an error if required
                pass
            else:
                with open(self.get_file_path(), "a") as file:
                    file.write("\n" + self.get_contents())
        else:
            with open(self.get_file_path(), "w") as file:
                file.write(self.get_contents())

        return self.get_file_name()

    def get_file_name(self):
        return f"{self.section.replace(' ', '_').lower()}.rst"

    def get_file_path(self):
        return os.path.join(DOC_SOURCE, self.get_file_name())

    def get_title(self):
        underline = ''.join(["=" for i in range(len(self.section) + 1)])
        return f"{self.section}\n{underline}\n"

    def has_file_exists(self):
        return os.path.isfile(self.get_file_path())

    def has_title(self):
        if self.has_file_exists():
            with open(self.get_file_path(), "r") as file:
                contents = file.read()
            return self.get_title() in contents
        return True

    def get_contents(self):
        contents = ""
        if not self.has_title():
            contents = self.get_title()
        if self.module:
            contents += f".. module:: {self.module}\n"
        if self.synopsis:
            contents += f"    :synopsis: {self.synopsis}\n"
        if self.klass:
            contents += f".. autoclass:: {self.klass}\n"
        if self.func:
            contents += f".. autofunction:: {self.func}\n"

        return contents
