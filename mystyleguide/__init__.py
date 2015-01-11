""" :mod:`mystyleguide` --- mystyleguide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from pathlib import Path

import os

from jinja2 import Environment, PackageLoader


#: template folder for style guide.
template_folder_name = 'templates'

def find_styleguides():
    """Find styleguide's name. styleguide's name is determined by
    directory's name under `template_folder_name` .

    .. sourcecode::

       $ tree mystyleguide
       mystyleguide
       ├── __init__.py
       ├── cli.py
       └── templates
           ├── coffee
           │   └── coffee.rst
           └── meta.rst

    if given templates same above, then :func:`find_styleguides` generate
    contains ``'coffee'`` in it.

    :return: a generator that yield guide's name.
    :rtype: generator object
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    base_path = Path(base_dir)
    template_path = base_path / template_folder_name
    for root, directory, files in os.walk(str(template_path)):
        for sub_directory in directory:
            yield sub_directory


def render_styleguides():
    """Render all styleguides.

    .. sourcecode::

       $ tree mystyleguide
       mystyleguide
       ├── __init__.py
       ├── cli.py
       └── templates
           ├── coffee
           │   └── coffee.rst
           └── meta.rst

    .. sourcecode::python

       from mystyleguide import render_styleguides

       for name, guide in render_styleguides():
           print(name) # coffee
           print(guide) # rendered guide

    :return: a generate that yield template's name and rendered styleguide.
    :rtype: generator object
    """
    mods = __name__.split('.')
    env = Environment(loader=PackageLoader(mods[0], template_folder_name))
    for template_name in find_styleguides():
        template = env.get_template('{s}/{s}.rst'.format(s=template_name))
        yield template_name, template.render()
