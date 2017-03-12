from setuptools import setup

setup(name='sandman',
    version='0.1',
    description='sandman is a script that suspends your homeserver when it\'s not in use.',
    url='https://github.com/SLCoding/sandman',
    author='SourceLan',
    author_email='daniel.wiesendorf@googlemail.com, schuette.marcus@googlemail.com',
    license='MIT',
    packages=[
        'sandman',
        'sandman.api',
        'sandman.coreplugins'],
    scripts=[
        'bin/sandman'],
    install_requires=[
        'configparser',
        'localconfig',
        'pydbus'
    ],
    setup_requires=[
        'pytest-runner'],
    tests_require=[
        'pytest'],
    zip_safe=False)
