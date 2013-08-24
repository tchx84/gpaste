from setuptools import setup

setup(name='gpaste',
    keywords=['restful', 'pygobject', 'pastebin'],
    version='0.1.0',
    description='Use fedora pastebin service in your Glib2 code.',
    url='http://github.com/tchx84/gpaste',
    author='Martin Abente Lahaye',
    author_email='martin.abente.lahaye@gmail.com',
    license='LGPL',
    packages=['gpaste'],
    install_requires=[
        'grestful',
    ],
    zip_safe=False)
