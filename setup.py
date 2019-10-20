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
