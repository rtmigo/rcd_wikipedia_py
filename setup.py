from pathlib import Path


from setuptools import setup, find_packages


def load_module_dict(filename: str) -> dict:
    import importlib.util as ilu
    filename = Path(__file__).parent / filename
    spec = ilu.spec_from_file_location('', filename)
    module = ilu.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__dict__


name = "rcd_wikipedia"
constants = load_module_dict(f'{name}/_constants.py')

readme = (Path(__file__).parent / 'README.md').read_text(encoding="utf-8")
readme = "# " + readme.partition("\n#")[-1]

setup(
    name=name,
    version=constants['__version__'],

    author="Artëm IG",
    author_email="ortemeo@gmail.com",
    url='https://github.com/rtmigo/znuploader_py',

    packages=find_packages(include=['rcd_wikipedia/*']),

    install_requires=[
        "rcd@ git+https://github.com/rtmigo/rcd_py",
    ],

    # description="Command-line tool for managing Python virtual environments",

    long_description=readme,
    long_description_content_type='text/markdown',

    license="MIT",

    keywords="".split(),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: BSD License',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Environment :: Console",
        "Typing :: Typed",
        "Topic :: Software Development :: Build Tools",
        "Operating System :: POSIX",
        # "Operating System :: Microsoft :: Windows"
    ],

    test_suite="test_unit.suite"
)
