import configparser
import tgbotapi
import datetime
import logging
import os
from .utils import color

version = "1.0.0"
parsercfg = configparser.ConfigParser()


def print_banner():
    """ Displays ASCII Art """
    color.Color.pl(r'{G}┏━━━┓  {R}'+version+' {G} ┏┳━━┓╋╋╋┏┓')
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
    try:
        parsercfg.read(config)
    except KeyError:
        print('Creating config.ini')
        parsercfg['creds'] = {
            'token': 'bot-api-token',
            'sudo': 'your_username',
            'channel': 'channel_username'}
        with open(config, 'w') as f:
            parsercfg.write(f)
    parsercfg.read(config)
    token = parsercfg.get('creds', 'token')
    botid = token.split(':')[0]
    sudo = parsercfg.get('creds', 'sudo')
    channel = parsercfg.get('creds', 'channel')
    return token, botid, sudo, channel


# Write config
def write_cfg(config):
    print("Enter The Requirements without '@'")
    token = input('BOT_TOKEN: ')
    sudo = input('YOUR_USERNAME: ')
    channel = input('CHANNEL_USERNAME: ')
    parsercfg['creds'] = {
        'token': token,
        'sudo': '@'+ sudo,
        'channel': '@'+ channel
                    }
    with open(config, 'w') as f:
        parsercfg.write(f)


# Check for config data
def check_cfg(config):
    r = read_cfg(config)
    if r[0] != 'bot-token-api' and r[2] != 'your_username' and r[3] != 'channel_username':
        return read_cfg(config)
    else:
        write_cfg(config)
        return read_cfg(config)


# Logger
logger = tgbotapi.logger
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
bot = tgbotapi.TBot(token=botcfg[0], threaded=True, skip_pending=False, num_threads=100)
bot_id = botcfg[1]
sun = botcfg[2]
cun = botcfg[3]
bids = [952435061, int(bot_id)]
