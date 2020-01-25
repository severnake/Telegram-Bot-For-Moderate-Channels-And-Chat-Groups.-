#!/usr/bin/env python3
from src.config import bot

from src.handlers import channels
from src.handlers import groups
from src.handlers import private

bot.polling(True)
