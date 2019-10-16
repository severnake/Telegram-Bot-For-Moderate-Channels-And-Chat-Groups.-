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


# start message.
@bot.message_handler(commands=['start'])
def replay_info_cmd(message):
    dev_user_name = '@MA24th'
    dev_channel_user_name = '@grid9x'
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    user_full_name = str(user_first_name) + " " + str(user_last_name)
    msg_start= "*Welcome {}*\nI'm here to manage your\nchannels and chat groups\nthis bot made with `telebotapi`\ncheck it at PYPI\n[https://pypi.org/project/telebotapi/]\n\nFor activation contact\n {} - {} ".format(user_full_name, dev_user_name, dev_channel_user_name)
    
    bot.reply_to(message, text=msg_start, parse_mode='markdown')