from guardbot.config import bot, print_banner
from guardbot.utils import color
Color = color.Color


def start():
    try:
        from guardbot.handlers import channels
        from guardbot.handlers import groups
        from guardbot.handlers import private
    except Exception as e:
        Color.pexception(e)
        Color.pl('\n{!} {R}Exiting{W}\n')

    Color.clear_line()
    print_banner()
    bot.polling(none_stop=True)
