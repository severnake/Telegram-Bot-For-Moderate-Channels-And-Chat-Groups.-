from src.config import bot


def guardbot():
    from src.handlers import channels
    from src.handlers import groups
    from src.handlers import private
    bot.polling(True)
