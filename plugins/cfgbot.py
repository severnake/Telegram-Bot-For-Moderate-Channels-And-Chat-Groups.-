import telebotapi
import configparser
import logging
import os
import datetime


# read api token.
def read_cfg(config):
    parser = configparser.ConfigParser()
    parser.read(config)
    return parser.get('creds', 'api')


# import token.
bot = telebotapi.TBot(read_cfg("config.cfg"))

# logger
logger = telebotapi.logger
logger.setLevel(logging.DEBUG)
# format log
log_format = logging.Formatter('[%(asctime)s] %(thread)d' +
                               '{%(pathname)s:%(lineno)d}\n%(levelname)s \n-%(message)s',
                               '%Y.%m.%d-%H.%M.%S')

# Create log folder if not exists.
if not os.path.exists("logs"):
    os.mkdir("logs")

# format log file name.
format_handler = logging.FileHandler("logs/" +
                                     datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S") + ".log")

# set log_format and add handler.
format_handler.setFormatter(log_format)
logger.addHandler(format_handler)
