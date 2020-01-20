import telebotapi
import configparser
import logging
import os
import datetime


# Read configration.
def read_cfg(config):
    parser = configparser.ConfigParser()
    parser.read(config)
    api_token = parser.get('creds', 'token')
    bot_id = api_token.split(':')[0]
    sudo_username = parser.get('creds', 'sudo_username')
    channel_username = parser.get('creds', 'channel_username')
    return api_token, bot_id, sudo_username, channel_username


config_bot = read_cfg('config.ini')

api_token = config_bot[0]
bot_id = config_bot[1]
sudo_username = config_bot[2]
channel_username = config_bot[3]

bot = telebotapi.TBot(api_token)

know_user_info = []
know_user_id = []
creators_ids = []
admins_ids = []


# Logger
logger = telebotapi.logger
logger.setLevel(logging.DEBUG)
# format log
log_format = logging.Formatter(
    '[%(asctime)s] %(thread)d {%(pathname)s:%(lineno)d}\n%(levelname)s - %(message)s\n\n', '%Y.%m.%d-%H.%M.%S')
# create log folder if not exists.
if not os.path.exists("logs"):
    os.mkdir("logs")
# format log file name.
format_handler = logging.FileHandler(
    "logs/" + datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S") + ".log")
# set log_format and add handler.
format_handler.setFormatter(log_format)
logger.addHandler(format_handler)

from configparser import ConfigParser


logo = '\n\u001b[32m┏━━━┓ @MA24th ┏┳━━┓╋╋╋┏┓\
                  \n┃┏━┓┃ @grid9x ┃┃┏┓┃╋╋┏┛┗┓\
                  \n┃┃╋┗╋┓┏┳━━┳━┳━┛┃┗┛┗┳━┻┓┏┛\
                  \n┃┃┏━┫┃┃┃┏┓┃┏┫┏┓┃┏━┓┃┏┓┃┃\
                  \n┃┗┻━┃┗┛┃┏┓┃┃┃┗┛┃┗━┛┃┗┛┃┗┓\
                  \n┗━━━┻━━┻┛┗┻┛┗━━┻━━━┻━━┻━┛\u001b[0m'


print(logo)

token = input('BOT_TOKEN: ')
sudo_username = input('SUDO_USERNAME: ')
channel_username = input('CHANNEL_USERNAME: ')


config = ConfigParser()
config['creds'] = {
    'token' : token,
    'sudo_username': sudo_username,
    'channel_username' : channel_username
    }

with open('config.ini', 'w') as f:
    config.write(f)
