#!/usr/bin/env python3
from setuptools import setup, find_packages
from io import open


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(name='guardbot',
      version='0.0.1',
      description='Telegram Bot For Managing Chat Groups And Channels',
      long_description=read('README.rst'),
      long_description_content_type="text/x-rst",
      author='Mustafa Asaad',
      author_email='ma24th@yahoo.com',
      url='https://github.com/MA24th/GuardBot',

      packages=find_packages(),
      entry_points={
            'console_scripts': ['guardbot = guardbot.__main__:start']
      },
      scripts=['bin/guardbot'],
      #   data_files=[
      #       ('share/dict', ['wordlist-top4800-probable.txt'])
      #   ],
      include_package_data=True,
      exclude_package_data={"": ["README.md"]},

      install_requires=[
          'pytest', 'telebotapi', 'redis'
      ],
      test_suite='pytest',
      tests_require=['pytest'],

      license='GNU GPLv2',
      keywords='bot, telegram_bot, telebotapi, guardbot, GuardBot',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Programming Language :: Python :: 3.7',
                   'License :: Freeware',
                   'Operating System :: POSIX',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: MacOS :: MacOS X',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'],
      )
