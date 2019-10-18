import telebotapi
import configparser
import logging
import os
import datetime


# read api token.
def read_cfg(config):
    parser = configparser.ConfigParser()
    parser.read(config)
    api_token = parser.get('creds' , 'token')
    bot_id = api_token.split(':')[0]
    sudo_username = parser.get('creds', 'sudo_username')
    chat_username = parser.get('creds', 'chat_username')
    return api_token, bot_id, sudo_username, chat_username


config_bot = read_cfg('config')
api_token = config_bot[0]
bot_id = [].append(config_bot[1])
sudo_username = config_bot[2]

chat_username = config_bot[3]
bot = telebotapi.TBot(api_token)
know_user_info = []
know_user_id = []

creators_ids = []
admins_ids = []


# Logger
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
