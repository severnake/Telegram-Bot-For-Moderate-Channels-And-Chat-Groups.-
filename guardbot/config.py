import configparser
import telebotapi
import datetime
import logging
import os
from .utils import color

parsercfg = configparser.ConfigParser()
version = "0.0.1"


def print_banner():
    """ Displays ASCII Art """
    color.Color.pl(r'{G}┏━━━┓  {R}v0.0.1{G} ┏┳━━┓╋╋╋┏┓')
    color.Color.pl(r'{G}┃┏━┓┃ {R}@grid9x{G} ┃┃┏┓┃╋╋┏┛┗┓')
    color.Color.pl(r'{G}┃┃╋┗╋┓┏┳━━┳━┳━┛┃┗┛┗┳━┻┓┏┛')
    color.Color.pl(r'{G}┃┃┏━┫┃┃┃┏┓┃┏┫┏┓┃┏━┓┃┏┓┃┃')
    color.Color.pl(r'{G}┃┗┻━┃┗┛┃┏┓┃┃┃┗┛┃┗━┛┃┗┛┃┗┓')
    color.Color.pl(r'{G}┗━━━┻━━┻┛┗┻┛┗━━┻━━━┻━━┻━┛')
    color.Color.pl(r'{P}Author: Mustafa Asaad')
    color.Color.pl(r'{P}Email: ma24th@yahoo.com')
    color.Color.pl(r'{W}=========================')


# Read config
def read_cfg(config):
    parsercfg.read(config)
    token = parsercfg.get('creds', 'token')
    botid = token.split(':')[0]
    sudo = parsercfg.get('creds', 'sudo')
    channel = parsercfg.get('creds', 'channel')
    return token, botid, sudo, channel


# Write config
def write_cfg(config):
    token = input('BOT_TOKEN: ')
    sudo = input('SUDO_USERNAME: ')
    channel = input('CHANNEL_USERNAME: ')
    parsercfg['creds'] = {
        'token': token,
        'sudo': '@'+sudo,
        'channel': '@'+channel
                    }
    with open(config, 'w') as f:
        parsercfg.write(f)


# Check for config data
def check_cfg(config):
    if read_cfg(config)[2] != '@your_username':
        return read_cfg(config)
    else:
        write_cfg(config)
        return read_cfg(config)


# Logger
logger = telebotapi.logger
logger.setLevel(logging.DEBUG)
# format log
log_format = logging.Formatter(
    '[%(asctime)s] {%(pathname)s:%(lineno)d}\n%(levelname)s - %(message)s', '%Y.%m.%d-%H.%M.%S')
# create log folder if not exists.
if not os.path.exists("logs"):
    os.mkdir("logs")
# format log file name.
format_handler = logging.FileHandler(
    "logs/" + datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S") + ".log")
# set log_format and add handler.
format_handler.setFormatter(log_format)
logger.addHandler(format_handler)

botcfg = check_cfg('config.ini')

bot = telebotapi.TBot(botcfg[0])
bot_id = botcfg[1]
sudo_username = botcfg[2]
channel_username = botcfg[3]
bots_ids = [bot_id]
creators_ids = []
admins_ids = []
vusers_ids = []
vusers_info = []
