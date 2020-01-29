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
           'msg_join': '_Please_ \nJoin {} First',
           'b_back': 'Back ↩️',
           'b_help': 'Help 📋',
           'b_support': 'Support ⚙️',
           'b_ch_lang': 'Choose a language 🌍',
           'b_add_me': 'Add Me 👥',
           't_make': 'Make a Choose',
           't_dev': 'Under Development',
           't_sup_cap1': 'Unsupported Feature!',
           't_start': ['start'],
           't_help': ['help', 'Help'],
           't_id': ['id', 'Id', 'iD', 'myinfo'],
           't_id_cap': "*Fullname:* {}\n*Username:* @{}\n*ID:* `{}`",
           't_piv_admin': 'You aren\'t a Admin',
           't_ban': ['ban', 'Ban'],
           't_ban_cap1': 'Ban @{} Done!',
           't_ban_cap2': 'I can\'t ban myself!!!',
           't_ban_cap3': 'I can\'t ban you',
           't_ban_cap4': 'Only the Creator @{} can ban me!',
           't_ban_cap5': 'I can\'t ban the Creator @{}.',
           't_ban_cap6': 'Only the Creator @{}\ncan ban the admin @{}',
           't_unban': ['unban', 'unban'],
           't_unban_cap1': 'Unban @{} Done!',
           't_unban_cap2': 'I can\'t unban myself!!!',
           't_unban_cap3': 'I can\'t unban you',
           't_unban_cap4': 'Only the Creator @{} can unban me!',
           't_unban_cap5': 'I can\'t unban the Creator @{}.',
           't_unban_cap6': 'Only Creator @{}\nCan Unban The admin @{}',
           't_kick': ['kick', 'Kick'],
           't_kick_cap1': 'Kick @{} Done!',
           't_kick_cap2': 'I can\'t kick myself!!!',
           't_kick_cap3': 'I can\'t kick you',
           't_kick_cap4': 'Only the Creator @{} can kick me!',
           't_kick_cap5': 'I can\'t kick the Creator @{}.',
           't_kick_cap6': 'Only the Creator @{}\ncan kick the admin @{}',
           't_kickme': ['kickme', 'Kickme'],
           't_kickme_cap1': 'Kick @{} Done!',
           't_pin': ['pin', 'Pin'],
           't_pin_cap1': 'You {} are not allowed to pin messages!!!',
           't_unpin': ['unpin', 'Unpin'],
           't_unpin_cap1': 'You {} are not allowed to unpin messages!!!',
           }


def ch_lang(user_lang):
    if user_lang == 'ar':
        return ar_lang
    elif user_lang == 'en':
        return en_lang
    else:
        return None
