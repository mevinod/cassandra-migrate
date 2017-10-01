from setuptools import setup

VERSION = '0.2.3'

setup(name='cassandra-migrate',
      packages=['cassandra_migrate'],
      version=VERSION,
      description='Simple Cassandra database migration program',
      long_description=open('README.rst').read(),
      url='https://github.com/Cobliteam/cassandra-migrate',
      download_url='https://github.com/Cobliteam/cassandra-migrate/archive/{}.tar.gz'.format(VERSION),
      author='Daniel Miranda',
      author_email='daniel@cobli.co',
      license='MIT',
      install_requires=[
          'cassandra-driver',
          'future',
          'pyyaml',
          'arrow',
          'tabulate',
          "enum34; python_version < '3.4'"
      ],
      entry_points={
          'console_scripts': ['cassandra-migrate=cassandra_migrate.cli:main']
      },
      keywords='cassandra schema migration')
