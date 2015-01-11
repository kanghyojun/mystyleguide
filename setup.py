from setuptools import setup, find_packages

install_requires = [
    'click == 3.3', 'Jinja2 == 2.7.3', 'docutils == 0.12',
]

setup(
    name='mystyleguide',
    version='0.0.1',
    author='Kang Hyojun',
    author_email='hyojun@admire.kr',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': 'mystyleguide = mystyleguide.cli:cli'
    }
)
