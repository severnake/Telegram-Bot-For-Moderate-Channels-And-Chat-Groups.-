#!/usr/bin/env python3
from setuptools import setup, find_packages
from io import open
from guardbot.config import version


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(name='guardbot',
      version=version,
      description='Telegram Bot For Moderate Chat Groups And Channels',
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
      include_package_data=True,
      exclude_package_data={"": ["README.md"]},

      install_requires=[
          'pytest', 'tgbotapi', 'redis'
      ],
      test_suite='pytest',
      tests_require=['pytest'],

      license='GNU GPLv2',
      keywords='bot, telegram_bot, telegram_bot_api, tgbotapi, guardbot, GuardBot',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'License :: Freeware',
                   'Operating System :: POSIX',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: MacOS :: MacOS X',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'],
      )
