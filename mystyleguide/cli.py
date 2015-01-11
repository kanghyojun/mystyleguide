""" :mod:`mystyleguide.cli` --- Command Line Interface for mystyleguide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from docutils.core import publish_string
from pathlib import Path

import click

from . import render_styleguides


@click.group()
def cli():
    pass


@click.command()
def hello():
    """Hello
    """
    click.echo('Hello :)')


@click.command()
@click.option('--output', default='./out', help='Set output directory')
def build(output):
    """Build styleguides.
    """
    out_path = Path(output)
    try:
        out_path.mkdir(mode=0o777)
    except FileExistsError as e:
        pass
    for name, guide in render_styleguides():
        with open(str(out_path / '{}.html'.format(name)), 'w') as f:
            html = publish_string(guide, writer_name='html')
            f.write(html.decode('utf-8'))


cli.add_command(hello)
cli.add_command(build)
