from ..config import channel_username

"""USER LANGUAGE UTILITY"""
ar_lang = {'start_msg': "*مرحبا!* 🎉\nانا اهنا اقوم بادارة\
                                \nالقنوات والمجموعات المحادثة\
                                \nفقط اضفني 👀 \
                                \n\nهذا البوت صنع بواسطة `telebotapi`\
                                \nتحقق منه على `PYPI` 🔰 \
                                \nhttps://pypi.org/project/telebotapi \
                                \n\nللتفعيل التواصل مع ⤵️ \
                                \n@MA24th 🛠 - @grid9x ⚙️",

           'private_help': "*قائمة الاوامر* 📋\
                                \n============\
                                \n/ابدأ`: القائمة العامة` \
                                \n/ايدي`: اظهار معلومات المستخدم`",
           'creator_help': "*قائمة الاوامر* 📋\
                                \n============\
                                \n`ban`: replay to msg user\
                                \n`unban`: replay to msg user\
                                \n`kick`: replay to msg user\
                                \n`kickme`: send `kickme`\
                                \n`pin`: replay to msg\
                                \n`unpin`: send `unpin`",
           'admin_help': "*Help Menu* 📋\
                                \n============\
                                \n`ban`: replay to msg user\
                                \n`unban`: replay to msg user\
                                \n`kick`: replay to msg user\
                                \n`kickme`: send `kickme`\
                                \n`pin`: replay to msg\
                                \n`unpin`: send `unpin`",
           'member_help': "*Help Menu* 📋\
                                \n============\
                                \n`اطردني`: طرد المستخدم\
                                \n`تثبيت`: تثبيت رسالة\
                                \n`unpin`: send `unpin`",
           'b_back': 'الرجوع ↩️',
           'b_help': 'مساعدة 📋',
           'b_support': 'الدعم ⚙️',
           'b_ch_lang': 'تغير اللغة 🌍',
           'b_add_me': 'اضفني الى مجموعة 👥',
           't_dev': 'جاري التطوير',
           't_make': 'اختار'}

en_lang = {'start_msg': "*Welcome!* 🎉\nI'm here to manage your\
                                \nchannels and chat groups\
                                \njust add me to it 👀 \
                                \n\nthis bot made with `telebotapi`\
                                \ncheck it at `PYPI` 🔰 \
                                \nhttps://pypi.org/project/telebotapi \
                                \n\nFor activation contact ⤵️ \
                                \n@MA24th 🛠 - @grid9x ⚙️ ",

           'private_help': "*Help Menu* 📋\
                                \n============\
                                \n/start : start message\
                                \n/id : replay your info",
           'creator_help': "*Help Menu* 📋\
                                \n============\
                                \n`ban`: replay to msg user\
                                \n`unban`: replay to msg user\
                                \n`kick`: replay to msg user\
                                \n`kickme`: send `kickme`\
                                \n`pin`: replay to msg\
                                \n`unpin`: send `unpin`",
           'admin_help': "*Help Menu* 📋\
                                \n============\
                                \n`ban`: replay to msg user\
                                \n`unban`: replay to msg user\
                                \n`kick`: replay to msg user\
                                \n`kickme`: send `kickme`\
                                \n`pin`: replay to msg\
                                \n`unpin`: send `unpin`",
           'member_help': "*Help Menu* 📋\
                                \n============\
                                \n`kickme`: send `kickme`\
                                \n`pin`: replay to msg\
                                \n`unpin`: send `unpin`",
           'msg_join': f'_Please_ \nJoin {channel_username} First',
           'b_back': 'Back ↩️',
           'b_help': 'Help 📋',
           'b_support': 'Support ⚙️',
           'b_ch_lang': 'Choose a language 🌍',
           'b_add_me': 'Add Me 👥',
           't_make': 'Make a Choose',
           't_dev': 'Under Development',
           't_help': ['help', 'Help'],
           't_id': ['id', 'Id', 'iD', 'myinfo']}


def ch_lang(user_lang):
    if user_lang == 'ar':
        return ar_lang
    elif user_lang == 'en':
        return en_lang
    else:
        return None


print(ch_lang(user_lang='en')['start_msg'])
