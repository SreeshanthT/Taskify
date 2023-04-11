# Basic Configuration

## Path Configuration
Add the following code to the top of the file to add the Django project directory to the Python path:
```
    import os
    import sys
    
    sys.path.insert(0, os.path.abspath('..'))
```

## Project information

In Sphinx, you can provide information about your project by setting various configuration options in the conf.py file. Here are some of the most commonly used project information options:

In Sphinx, you can provide information about your project by setting various configuration options in the conf.py file. Here are some of the most commonly used project information options:

- `project`: The name of your project.
- `author`: The name(s) of the author(s) of your project.
- `copyright`: The copyright information for your project.
- `version`: The version number of your project.
- `release`: The release number of your project.
- `language`: The primary language of your documentation.
- `master_doc`: The name of the root document of your documentation.

Here's an example of how to set these options in your conf.py file:
```
# -- project informations --
project = 'My Project'
author = 'John Doe'
copyright = 'Copyright (c) 2023'
version = '1.0'
release = '1.0.1'
language = 'en'
master_doc = 'index'
```

## General configuration 
Here are some of the most important options in the "General configuration" section of conf.py:

- The `extensions` configuration option in Sphinx allows you to specify a list of extensions to use when building your documentation. Extensions are plugins that add functionality to Sphinx, such as support for different markup languages, automatic generation of documentation from source code, and more.
  Here's an example of how to enable some commonly used extensions in your conf.py:
  ```
  extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'myst_parser',
  ]
  ```
- The `templates_path` configuration option in Sphinx allows you to specify a list of directories where Sphinx should look for templates. Templates are used to define the structure and layout of your documentation pages, and Sphinx provides a number of built-in templates that you can use as a starting point.
  By default, Sphinx looks for templates in the `_templates` directory in your documentation root directory, but you can add additional directories to `templates_path` if you want to use custom templates or override built-in templates.
  ```
  templates_path = ['_templates', 'my_templates']
  ```
- The `exclude_patterns` configuration option in Sphinx allows you to specify a list of file patterns to exclude from your documentation. This can be useful if you have files or directories that you don't want to include in your documentation for some reason (e.g. test files, data files, build artifacts, etc.).
  ```
  exclude_patterns = [
      'build',  # Exclude the build directory
      'venv',  # Exclude the virtual environment directory
      '**/tests',  # Exclude any test directories and files
      '**/__pycache__'  # Exclude any Python bytecode directories
  ]
  ```
- `source_suffix` specifies the file extensions of the source files for your documentation. By default, Sphinx expects source files to have the extension .rst (reStructuredText), but you can use other formats such as .md (Markdown) or .txt by setting source_suffix to a list of file extensions that you want to use.
  ```
    source_suffix = ['.rst', '.md']
  ```
  The file extensions of source files. Sphinx considers the files with this suffix as sources. The value can be a dictionary mapping file extensions to file types. For example:
  ```
  source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
  }
  ```
- `source_parsers` If given, a dictionary of parser classes for different source suffices. The keys are the suffix, the values can be either a class or a string giving a fully-qualified name of a parser class. The parser class can be either docutils.parsers.Parser or sphinx.parsers.Parser. Files with a suffix that is not in the dictionary will be parsed with the default reStructuredText parser. For example:
  ```
  source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}
  ```
- `pygments_style` is a configuration option in Sphinx that controls the syntax highlighting style used by Pygments, the syntax highlighting engine used by Sphinx.
  ```
  pygments_style = 'monokai'
  ```

