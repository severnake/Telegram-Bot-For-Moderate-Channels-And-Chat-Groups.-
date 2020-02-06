"""USER LANGUAGE UTILITY"""
ar_lang = {}
en_lang = {'start_msg': "*Welcome!* {} 🎉\
                        \nI'm here to manage your\
                        \nchannels and chat groups\
                        \njust add me to it 👀 \
                        \n\nthis bot made with `telebotapi`\
                        \ncheck it at `PYPI` 🔰 \
                        \nhttps://pypi.org/project/telebotapi \
                        \n\nFor activation contact ⤵️ \
                        \n@MA24th 🛠 - @grid9x ⚙️ ",
           'private_help': "*Help Menu* 📋\
                                \n\=\=\=\=\=\=\=\=\=\=\=\=\
                                \n\/start : start message\
                                \n\/help : help menu\
                                \n\/id : replay your info",
           'creator_help': "*HELP MENU* 📋\
                                \n\=\=\=\=\=\=\=\=\=\=\=\=\
                                \n__*User Actions*__ 🚻 \
                                \n🔘 `ban`: _Ban User_\
                                \n🔘 `unban`: _Unban Banned Member_\
                                \n🔘 `kick`: _Remove User Without Ban_\
                                \n🔘 `pin`: _Pin Message_\
                                \n🔘 `unpin`: _Unpin Message_\
                                \n🔘 `promote`: _Promote a Member_\
                                \n🔘 `demote`: _Demote an Admin_\
                                \n\n__*Group Permissions*__ 🔣 \
                                \n Command Name\+ Enable or Disable\
                                \n🔘 `Send Message`: {gcsm}\
                                \n🔘 `Send Media`: {gcsmm}\
                                \n🔘 `Send Stickers & GIFs`: {gcsom}\
                                \n🔘 `Send Polls`: {gcsp}\
                                \n🔘 `Embed Links`: {gcawpp}\
                                \n🔘 `Add Users`: {gciu}\
                                \n🔘 `Pin Messages`: {gcpm}\
                                \n🔘 `Change Chat Info`: {gcci}",
           'admin_help': "*Help Menu* 📋\
                                \n\=\=\=\=\=\=\=\=\=\=\=\=\
                                \n__*User Actions*__ 🚻\
                                \n🔘 `ban`: Ban User\
                                \n🔘 `unban`: Unban Banned Member\
                                \n🔘 `kick`: Remove User Without Ban\
                                \n🔘 `kickme`: Leave The Group\
                                \n🔘 `pin`: Pin Message\
                                \n🔘 `unpin`: Unpin Message\
                                \n🔘 `promote`: Promote a Member\
                                \n🔘 `demote`: Demote an Admin\
                                \n\n__*Group Permissions*__ 🔣 \
                                \n Command Name\+ Enable or Disable\
                                \n🔘 `Send Message`: {gcsm}\
                                \n🔘 `Send Media`: {gcsmm}\
                                \n🔘 `Send Stickers & GIFs`: {gcsom}\
                                \n🔘 `Send Polls`: {gcsp}\
                                \n🔘 `Embed Links`: {gcawpp}\
                                \n🔘 `Add Users`: {gciu}\
                                \n🔘 `Pin Messages`: {gcpm}\
                                \n🔘 `Change Chat Info`: {gcci}",
           'member_help': "*Help Menu* 📋\
                                \n\=\=\=\=\=\=\=\=\=\=\=\=\
                                \n__*Commands*__\
                                \n🔘 `help`: Show this menu\
                                \n🔘 `info`: replay your info\
                                \n🔘 `kickme`: Leave The Group\
                                \n🔘 `pin`: Pin Message\
                                \n🔘 `unpin`: Unpin Message",
           'h_group': '*Group Commands* 📋 \
                      \n================== \
                      \n\nIn order to make bot works  \
                      \nthe bot must be an admin \
                      \nand should observe all permissions:\
                      \n\n_Change Group Info\
                      \nDelete Messages\
                      \nBan Users\
                      \nInvite Users via Link\
                      \nPin Messages\
                      \nAdd New Admins_',
           'h_channel': '*Channel Commands* 📋',
           'msg_join': '_Please_ \nJoin {} First',
           'b_main': 'Main Menu 📱',
           'b_back': 'Back ↩️',
           'b_help': 'Help 📋',
           'b_support': 'Support ⚙️',
           'b_ch_lang': 'Choose a language 🌍',
           'b_add_me': 'Add Me 📲',
           't_make': 'Make a Choose',
           'b_group': 'Group Commands 👥',
           'b_channel': 'Channel Commands 📰',
           't_dev': 'Under Development 📝',
           't_sup_cap1': 'Unsupported Feature!',
           't_start': ['start'],
           't_help': ['help', 'Help'],
           't_info': ['id', 'Id', 'my id', 'info', 'my info'],
           't_info_p_user': "__*Details*__\
                     \n*Fullname:* {fn}\
                     \n*Username:* @{un}\
                     \n*ID:* `{id}`",
           't_info_user': "__*Details*__\
                     \n*Fullname:* {fn}\
                     \n*Username:* @{un}\
                     \n*ID:* `{id}`\
                     \n*Status*: {us}",
           't_info_admin': "__*Details*__\
                     \n*Fullname:* {fn}\
                     \n*Username:* @{un}\
                     \n*ID:* `{id}`\
                     \n\n__*Permissions*__\
                     \n*Status*: {us}\
                     \n🔘 `Editable`: {cbe}\
                     \n🔘 `Add Users`: {uciu}\
                     \n🔘 `Restrict Users`: {ucru}\
                     \n🔘 `Promote Users`: {ucpu}\
                     \n🔘 `Pin Messages`: {ucpm}\
                     \n🔘 `Delete Messages`: {ucdm}\
                     \n🔘 `Change Chat Info`: {ucci}",
           't_info_member': "__*Details*__\
                     \n*Fullname:* {fn}\
                     \n*Username:* @{un}\
                     \n*ID:* `{id}`\
                     \n*Status*: {us}\
                     \n\n__*Permissions*__\
                     \n🔘 `Until Date`: {ud}\
                     \n🔘 `Editable`: {cbe}\
                     \n🔘 `Pin Messages`: {ucpm}\
                     \n🔘 `Send Message`: {ucsm}\
                     \n🔘 `Send Media`: {ucsmm}\
                     \n🔘 `Send Stickers & GIFs`: {ucsom}\
                     \n🔘 `Send Polls`: {ucsp}\
                     \n🔘 `Embed Links`: {ucawpp}\
                     \n🔘 `Add Users`: {uciu}\
                     \n🔘 `Change Chat Info`: {ucci}",
           't_piv_admin': 'You aren\'t a Admin',
           't_ban': ['ban', 'Ban'],
           't_ban_cap1': 'Ban @{} Done!',
           't_ban_cap2': 'I can\'t ban myself!!!',
           't_ban_cap3': 'I can\'t ban you',
           't_ban_cap4': 'Only the Creator @{} can ban me!',
           't_ban_cap5': 'I can\'t ban the Creator @{}.',
           't_ban_cap6': 'Only the Creator @{}\ncan ban @{}',
           't_ban_cap7': 'Yor aren\'t allowed to ban @{}',
           't_unban': ['unban', 'unban'],
           't_unban_cap1': 'Unban @{} Done!',
           't_unban_cap2': 'I can\'t unban myself!!!',
           't_unban_cap3': 'I can\'t unban you',
           't_unban_cap4': 'Only the Creator @{} can unban me!',
           't_unban_cap5': 'I can\'t unban the Creator @{}.',
           't_unban_cap6': 'Only Creator @{}\nCan Unban The admin @{}',
           't_unban_cap7': 'Yor aren\'t allowed to unban @{}',
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
           't_promote': ['promote', 'Promote'],
           't_promote_cap1': 'Promote @{} Done!',
           't_demote': ['demote', 'Demote'],
           't_demote_cap1': 'Demote @{} Done!',
           't_user_can_send_messages': ['can send messages', 'Can Send Messages'],
           't_user_can_send_messages_cap1': '@{} Done!',
           't_user_can_send_messages_cap7': 'Yor aren\'t allowed to restrict users',
           'r_enable': 'en',
           'r_disable': 'di',

           }


def ch_lang(user_lang):
    if user_lang == 'ar':
        return ar_lang
    elif user_lang == 'en':
        return en_lang
    else:
        return None
