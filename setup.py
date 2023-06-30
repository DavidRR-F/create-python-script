from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Create Python Script CLI'
LONG_DESCRIPTION = 'Creates boilerplate files for python projects'

setup(
        name="create-python-script", 
        version=VERSION,
        author="David Rose-Franklin",
        author_email="david.rosefranklin96@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['click'],
        keywords=['create', 'command'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Automation",
            "Programming Language :: Python :: 3+",
            "Operating System :: Microsoft :: Windows",
        ],
        entry_points='''
        [console_scripts]
        create-python-project=create-python-project.project_generator:create_python_project
    ''',
)