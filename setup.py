import pathlib
from setuptools import setup, find_packages

BASE_DIR = pathlib.Path(__file__).parent.absolute()


def get_version():
    with open(BASE_DIR / 'VERSION') as file:
        return file.readline().strip()


def get_license():
    with open(BASE_DIR / 'LICENSE') as file:
        return file.read().strip()


def get_desc():
    with open(BASE_DIR / 'README.md') as file:
        return file.read().strip()


def get_packages():
    with open(BASE_DIR / 'requirements.txt') as file:
        return [
            package.strip()
            for package in file
            if package or not package.startswith('#')
        ]


setup(
    name='asrv',
    vetsion=get_version(),
    author='Yulia',
    author_email='admin@google.com',
    # url='https://doc.site.com' # repositories url
    packages=find_packages('.', include=['asrv', 'asrv.*'], exclude=['*texts*.py', 'test*']),
    package_dir={'asrv.*': 'asrv'},
    include_package_data=True,
    license=get_license(),
    description='My lib',
    long_description=get_desc(),
    long_description_content_type='text/markdown',
    install_requires=get_packages(),
    python_required='≥3.11',
    classifiers=[
        'Framework :: AnyIO',
        'Framework :: Django :: 2',
        'Development Status :: 3 - Alpha'
        if 'dev' in get_version()
        else 'Development Status :: 4 Beta'
        if 'rc' in get_version()
        else 'Development Status :: 5 Production/Stable'
    ],
    entry_points={
        'console_scripts': ['asrv_runer = asrv.app:run']
    }
)
