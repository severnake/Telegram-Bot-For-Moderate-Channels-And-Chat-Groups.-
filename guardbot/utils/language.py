""" USER LANGUAGE UTILITY """
ar_lang = {}
en_lang = {'start_msg': "*Welcome!* {} 🎉\
                        \nI'm here to manage your\
                        \nchannels and chat groups\
                        \njust add me to it 👀 ,\
                        \n\nI made with `tgbotapi`\
                        \ncheck it at `PYPI` 🔰 \
                        \nhttps://pypi.org/project/tgbotapi \
                        \n\nFor more information contact ⤵️ \
                        \n@MA24th 🛠 - @grid9x ⚙️ ",
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
                                \n Command \+ Enable or Disable\
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
                                \n Command \+ Enable or Disable\
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
           'h_channel': '*Channel* 📰\
                      \n========== \
                      \nIn order to make me work\
                      \nI\'m must be an admin \
                      \nAnd should observe all permissions:\
                      \n_Change chat info\
                      \nPost messages\
                      \nEdit messages of others\
                      \nDelete messages of others\
                      \nAdd members\
                      \nAdd new admins_\
                      \n',
           'h_group': '*Group* 👥\
                      \n========= \
                      \nIn order to make me work\
                      \nI\'m must be an admin \
                      \nAnd should observe all permissions:\
                      \n_Change chat info\
                      \nDelete messages\
                      \nBan users\
                      \nInvite users via link\
                      \nPin messages\
                      \nAdd new admins_\
                      \n',
           'h_private': "*Private* 👤\
                      \n\=\=\=\=\=\=\=\=\=\
                      \n\/start : start message\
                      \n\/id : show your info",
           'msg_join': '_Please_ \nJoin {} First',
           'b_main': 'Main Menu 📱',
           'b_back': 'Back ↩️',
           'b_help': 'Help 📋',
           'b_support': 'Support ⚙️',
           'b_ch_lang': 'Choose a language 🌍',
           'b_add': 'Add Me 📲',
           'b_id': 'ID 💳',
           't_make': 'Make a Choose',
           'b_channel': 'Channel 📰',
           'b_group': 'Group 👥',
           'b_private': 'Private 👤',
           't_choose': 'Make a Choose',
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
                     \n*Status*: {us}\
                     \n\n__*Permissions*__\
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
                     \n🔘*Until Date*: {ud}\
                     \n\n__*Permissions*__\
                     \n🔘 `Pin Messages`: {ucpm}\
                     \n🔘 `Send Message`: {ucsm}\
                     \n🔘 `Send Media`: {ucsmm}\
                     \n🔘 `Send Stickers & GIFs`: {ucsom}\
                     \n🔘 `Send Polls`: {ucsp}\
                     \n🔘 `Embed Links`: {ucawpp}\
                     \n🔘 `Add Users`: {uciu}\
                     \n🔘 `Change Chat Info`: {ucci}",
           't_piv_admin': 'You aren\'t a Admin',
           't_user_until_date_cap1': 'Forever',
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
           't_user_can_send_messages': ['can send messages enable', 'Can Send Messages', 'send messages', 'Send Messages', 'Send Messages'],
           't_user_can_send_messages_cap1': '@{} Done!',
           't_user_can_send_messages_cap7': 'Yor aren\'t allowed to restrict users',
           'r_enable': 'en',
           'r_disable': 'di',

           }

es_lang = {'start_msg': "*Bienvenido!* {} 🎉\
                        \nEstoy aquí para admnistrar tus\
                        \ncanales y gropos\
                        \nsolo añademe a ellos 👀 ,\
                        \n\nEstoy hecho con `tgbotapi`\
                        \nechale un vistazo en `PYPI` 🔰 \
                        \nhttps://pypi.org/project/tgbotapi \
                        \n\nPara más información contacta a ⤵️ \
                        \n@MA24th 🛠 - @grid9x ⚙️ ",
           'creator_help': "*MENU DE AYUDA* 📋\
                                \n\=\=\=\=\=\=\=\=\=\=\=\=\
                                \n__*Acciones de Usuario*__ 🚻 \
                                \n🔘 `ban`: _Banear Usuario_\
                                \n🔘 `unban`: _Desbanear Miembro Baneado_\
                                \n🔘 `kick`: _Eliminar Usuario Sin Banear_\
                                \n🔘 `pin`: _Fijar Mensaje_\
                                \n🔘 `unpin`: _Quitar Mensaje Fijado_\
                                \n🔘 `promote`: _Promover un Miembro_\
                                \n🔘 `demote`: _Degradar un Adminstrador_\
                                \n\n__*Permisos de Grupo*__ 🔣 \
                                \n Comando \+ Enabe or Disable\
                                \n🔘 `Enviar Mensaje`: {gcsm}\
                                \n🔘 `Enviar Multimedia`: {gcsmm}\
                                \n🔘 `Enviar Stickers y GIFs`: {gcsom}\
                                \n🔘 `Enviar Encuestas`: {gcsp}\
                                \n🔘 `Enlaces Incrustados`: {gcawpp}\
                                \n🔘 `Añadir Usuarios`: {gciu}\
                                \n🔘 `Fijar Mensajes`: {gcpm}\
                                \n🔘 `Cambiar Información del Chat`: {gcci}",
           'admin_help': "*MENU DE AYUDA* 📋\
                                \n\=\=\=\=\=\=\=\=\=\=\=\=\
                                \n__*Acciones de Usuario*__ 🚻 \
                                \n🔘 `ban`: _Banear Usuario_\
                                \n🔘 `unban`: _Desbanear Miembro Baneado_\
                                \n🔘 `kick`: _Eliminar Usuario Sin Banear_\
                                \n🔘 `pin`: _Fijar Mensaje_\
                                \n🔘 `unpin`: _Quitar Mensaje Fijado_\
                                \n🔘 `promote`: _Promover un Miembro_\
                                \n🔘 `demote`: _Degradar un Adminstrador_\
                                \n\n__*Permisos de Grupo*__ 🔣 \
                                \n Comando \+ Enabe or Disable\
                                \n🔘 `Enviar Mensaje`: {gcsm}\
                                \n🔘 `Enviar Multimedia`: {gcsmm}\
                                \n🔘 `Enviar Stickers y GIFs`: {gcsom}\
                                \n🔘 `Enviar Encuestas`: {gcsp}\
                                \n🔘 `Enlaces Incrustados`: {gcawpp}\
                                \n🔘 `Añadir Usuarios`: {gciu}\
                                \n🔘 `Fijar Mensajes`: {gcpm}\
                                \n🔘 `Cambiar Información del Chat`: {gcci}",
           'member_help': "*Menú De Ayuda* 📋\
                                \n\=\=\=\=\=\=\=\=\=\=\=\=\
                                \n__*Comandos*__\
                                \n🔘 `help`: Mostrar este Menú\
                                \n🔘 `info`: Mostrar tu información\
                                \n🔘 `kickme`: Dejar el Grupo\
                                \n🔘 `pin`: Fijar Mensaje\
                                \n🔘 `unpin`: Quitar Mensaje Fijado",
           'h_channel': '*Canal* 📰\
                      \n========== \
                      \nPara poder trabajar\
                      \nNecesito ser administrador \
                      \nY necesito estos permisos:\
                      \n_Cambiar información del chat\
                      \nEnviar mensajes\
                      \nEditar mensajes de otros\
                      \nEliminar mensajes de otros\
                      \nAñadir miembros\
                      \nAñadir nuevos administradores_\
                      \n',
           'h_group': '*Grupo* 👥\
                      \n========= \
                      \nPara poder trabajar\
                      \nNecesito ser administrador \
                      \nY necesito estos permisos:\
                      \n_Change chat info\
                      \nEliminar mensajes\
                      \nBanear usuarios\
                      \nInvitar a usuarios mediante enlace\
                      \nFijar mensajes\
                      \nAñadir nuevos administradores_\
                      \n',
           'h_private': "*Privado* 👤\
                      \n\=\=\=\=\=\=\=\=\=\
                      \n\/start : Mensaje de inicio\
                      \n\/id : Mostrar tu información",
           'msg_join': '_Por favor_ Primero \nIngresa a {}',
           'b_main': 'Menú principal 📱',
           'b_back': 'Atras ↩️',
           'b_help': 'Ayuda 📋',
           'b_support': 'Soporte ⚙️',
           'b_ch_lang': 'Selecciona una Idioma 🌍',
           'b_add': 'Añademe 📲',
           'b_id': 'ID 💳',
           't_make': 'Selecciona una opción:',
           'b_channel': 'Canal 📰',
           'b_group': 'Grupo 👥',
           'b_private': 'Privado 👤',
           't_choose': 'Selecciona una opción',
           't_dev': 'En Desarrollo 📝',
           't_sup_cap1': '¡Característica no soportada!',
           't_start': ['start'],
           't_help': ['help', 'Help'],
           't_info': ['id', 'Id', 'my id', 'info', 'my info'],
           't_info_p_user': "__*Detalles*__\
                     \n*Nombre completo:* {fn}\
                     \n*Apellido:* @{un}\
                     \n*ID:* `{id}`",
           't_info_user': "__*Detalles*__\
                     \n*Nombre completo:* {fn}\
                     \n*Nombre de usuario:* @{un}\
                     \n*ID:* `{id}`\
                     \n*Estado*: {us}",
           't_info_admin': "__*Details*__\
                     \n*Nombre completo:* {fn}\
                     \n*Nombre de usuario:* @{un}\
                     \n*ID:* `{id}`\
                     \n*Estado*: {us}\
                     \n\n__*Permisos*__\
                     \n🔘 `Editable`: {cbe}\
                     \n🔘 `Añadir Usuarios`: {uciu}\
                     \n🔘 `Restringir Usuarios`: {ucru}\
                     \n🔘 `Promover Usuarios`: {ucpu}\
                     \n🔘 `Fijar Mensajes`: {ucpm}\
                     \n🔘 `Eliminar Mensajes`: {ucdm}\
                     \n🔘 `Cambiar Información del Chat`: {ucci}",
           't_info_member': "__*Detalles*__\
                     \n*Nombre completo:* {fn}\
                     \n*Nombre de usuario:* @{un}\
                     \n*ID:* `{id}`\
                     \n*Estado*: {us}\
                     \n🔘*Hasta la Fecha*: {ud}\
                     \n\n__*Permisos*__\
                     \n🔘 `Fijar Mensajes`: {ucpm}\
                     \n🔘 `Enviar Mensajes`: {ucsm}\
                     \n🔘 `Enviar Multimedia`: {ucsmm}\
                     \n🔘 `Enviar Stickers y GIFs`: {ucsom}\
                     \n🔘 `Enviar Encuestas`: {ucsp}\
                     \n🔘 `Links embebidos`: {ucawpp}\
                     \n🔘 `Añadir Usuarios`: {uciu}\
                     \n🔘 `Cambiar Información del Chat`: {ucci}",
           't_piv_admin': 'No eres Administrador',
           't_user_until_date_cap1': 'Para siempre',
           't_ban': ['ban', 'Ban'],
           't_ban_cap1': '¡@{} Baneado!',
           't_ban_cap2': '¡¡¡No puedo banearme a mí mismo!!!',
           't_ban_cap3': '¡No puedo banearte!',
           't_ban_cap4': '¡Solo el Creador @{} puede banearme!',
           't_ban_cap5': 'No puedo banear al creador @{}.',
           't_ban_cap6': 'Solo el creador @{}\npuede banear a @{}',
           't_ban_cap7': 'No te está permitido banear @{}',
           't_unban': ['unban', 'unban'],
           't_unban_cap1': '¡@{} desbaneado!',
           't_unban_cap2': '¡¡¡No puedo desbanearme a mí mismo!!!',
           't_unban_cap3': '¡No puedo desbanearte!',
           't_unban_cap4': '¡Solo el creador @{} puede desbanearme!',
           't_unban_cap5': 'No puedo desbanear al Creador @{}.',
           't_unban_cap6': 'Solo el creador @{}\nPuede desbanear al Administrador @{}',
           't_unban_cap7': 'No puedes desbanear @{}',
           't_kick': ['kick', 'Kick'],
           't_kick_cap1': 'Kick @{} Done!',
           't_kick_cap2': '¡¡¡No puedo echarme a mí mismo!!!',
           't_kick_cap3': 'No puedo echarte',
           't_kick_cap4': 'Solo el Creador @{} puede echarme!',
           't_kick_cap5': 'No puedo hechar al Creador @{}.',
           't_kick_cap6': 'Solo el Creador @{}\npuede hechar al Administrador @{}',
           't_kickme': ['kickme', 'Kickme'],
           't_kickme_cap1': '¡@{} expulsado!',
           't_pin': ['pin', 'Pin'],
           't_pin_cap1': '¡¡¡Tú {} no tienes permitido fijar mensajes!!!',
           't_unpin': ['unpin', 'Unpin'],
           't_unpin_cap1': '¡¡¡Tu {} no tienes permitido quitar mensajes fijados!!!',
           't_promote': ['promote', 'Promote'],
           't_promote_cap1': '¡@{} Promovido!',
           't_demote': ['demote', 'Demote'],
           't_demote_cap1': '¡@{} Degradado!',
           't_user_can_send_messages': ['can send messages enable', 'Can Send Messages', 'send messages', 'Send Messages', 'Send Messages'],
           't_user_can_send_messages_cap1': '@{} hecho!',
           't_user_can_send_messages_cap7': 'No tienes permitido restringir usuarios',
           'r_enable': 'en',
           'r_disable': 'di',

           }


def ch_lang(user_lang):
    if user_lang == 'ar':
        return ar_lang
    elif user_lang == 'en':
        return en_lang
    else:
        raise ValueError('UNDEFINED USER LANGUAGE:', user_lang)
