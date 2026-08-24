from setuptools import setup, find_packages

setup(
    name='infraguard',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'paramiko', 'psutil', 'fastapi', 'uvicorn',
        'rich', 'click', 'pyyaml', 'jinja2', 'aiohttp'
    ],
    entry_points='''
        [console_scripts]
        infraguard=src.cli:cli
    '''
)
