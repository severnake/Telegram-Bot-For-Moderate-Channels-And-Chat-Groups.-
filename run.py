#!/usr/bin/env python3

# Author: Mustafa Asaad
# Date: OCT 10, 2019
# Email: ma24th@yahoo.com

try:
    from guardbot import __main__
except ImportError as e:
    raise Exception('You may need to reinstall GuardBot)', e)

__main__.start()
