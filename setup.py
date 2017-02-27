from setuptools import setup

setup(name='server-sleep',
      version='0.1',
      description='server-sleep is a script that suspends your homeserver when it\'s not in use.',
      url='https://github.com/SLCoding/server-sleep',
      author='SourceLan',
      author_email='daniel.wiesendorf@googlemail.com, schuette.marcus@googlemail.com',
      license='MIT',
      packages=['serversleep'],
      scripts=['bin/server-sleep'],
      install_requires=[
          'server-sleep-api',
          'configparser'
      ],
      zip_safe=False)
