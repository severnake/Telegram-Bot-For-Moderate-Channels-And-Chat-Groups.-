""" USER LANGUAGE UTILITY """
ar_lang = {}
en_lang = {
    'start_msg': "<b>Welcome!</b> {} 🎉\
        \nI'm here to manage your\
        \nchannels and chat groups\
        \njust add me to it 👀,\
        \n\nI made with <code>tgbotapi</code>\
        \ncheck it at <code>PYPI</code> 🔰\
        \nhttps://pypi.org/project/tgbotapi\
        \n\nFor more information contact ⤵️\
        \n@MA24th 🛠 - @grid9x ⚙️ ",
    'creator_help': "<b>HELP MENU</b> 📋\
        \n============\
        \n<u><b>User Actions</b></u> 🚻\
        \n🔘 <code>ban</code>: <i>Ban User</i>\
        \n🔘 <code>unban</code>: <i>Unban Banned Member</i>\
        \n🔘 <code>kick</code>: <i>Remove User Without Ban</i>\
        \n🔘 <code>pin</code>: <i>Pin Message</i>\
        \n🔘 <code>unpin</code>: <i>Unpin Message</i>\
        \n🔘 <code>promote</code>: <i>Promote a Member</i>\
        \n🔘 <code>demote</code>: <i>Demote an Admin</i>\
        \n\n<u><b>Group Permissions</b></u> 🔣 \
        \n Command + Enable or Disable\
        \n🔘 <code>Send Message</code>: {gcsm}\
        \n🔘 <code>Send Media</code>: {gcsmm}\
        \n🔘 <code>Send Stickers & GIFs</code>: {gcsom}\
        \n🔘 <code>Send Polls</code>: {gcsp}\
        \n🔘 <code>Embed Links</code>: {gcawpp}\
        \n🔘 <code>Add Users</code>: {gciu}\
        \n🔘 <code>Pin Messages</code>: {gcpm}\
        \n🔘 <code>Change Chat Info</code>: {gcci}",
    'admin_help': "<b>Help Menu</b> 📋\
        \n============\
        \n<u><b>User Actions</b></u> 🚻\
        \n🔘 <code>ban</code>: Ban User\
        \n🔘 <code>unban</code>: Unban Banned Member\
        \n🔘 <code>kick</code>: Remove User Without Ban\
        \n🔘 <code>kickme</code>: Leave The Group\
        \n🔘 <code>pin</code>: Pin Message\
        \n🔘 <code>unpin</code>: Unpin Message\
        \n🔘 <code>promote</code>: Promote a Member\
        \n🔘 <code>demote</code>: Demote an Admin\
        \n\n<u><b>Group Permissions</b></u> 🔣 \
        \n Command + Enable or Disable\
        \n🔘 <code>Send Message</code>: {gcsm}\
        \n🔘 <code>Send Media</code>: {gcsmm}\
        \n🔘 <code>Send Stickers & GIFs</code>: {gcsom}\
        \n🔘 <code>Send Polls</code>: {gcsp}\
        \n🔘 <code>Embed Links</code>: {gcawpp}\
        \n🔘 <code>Add Users</code>: {gciu}\
        \n🔘 <code>Pin Messages</code>: {gcpm}\
        \n🔘 <code>Change Chat Info</code>: {gcci}",
    'member_help': "<b>Help Menu</b> 📋\
        \n============\
        \n<u><b>Commands</b></u>\
        \n🔘 <code>help</code>: Show this menu\
        \n🔘 <code>info</code>: replay your info\
        \n🔘 <code>kickme</code>: Leave The Group\
        \n🔘 <code>pin</code>: Pin Message\
        \n🔘 <code>unpin</code>: Unpin Message",
    'h_channel': "<b>Channel</b> 📰\
        \n========== \
        \nIn order to make me work\
        \nI\'m must be an admin \
        \nAnd should observe all permissions:\
        \n<i>Change chat info</i>\
        \n<i>Post messages</i>\
        \n<i>Edit messages of others\
        \n<i>Delete messages of others</i>\
        \n<i>Add members</i>\
        \n<i>Add new admins</i>\
        \n",
    'h_group': "<b>Group</b> 👥\
        \n========= \
        \nIn order to make me work\
        \nI\'m must be an admin \
        \nAnd should observe all permissions:\
        \n<i>Change chat info</i>\
        \n<i>Delete messages</i>\
        \n<i>Ban users</i>\
        \n<i>Invite users via link</i>\
        \n<i>Pin messages</i>\
        \n<i>Add new admins</i>\
        \n',
    'h_private': "<b>Private</b> 👤\
        \n=========\
        \n/start :welcome message\
        \n/id : show your info",
    'msg_join': '<i>Please</i> \nJoin {} First',
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
    't_info': ['id', 'Id', 'my id', 'My id','info', 'Info', 'INFO'],
    't_info_p_user': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {fn}\
        \n<b>Username</b>: @{un}\
        \n<b>ID</b>: <code>{id}</code>",
    't_info_user': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {fn}\
        \n<b>Username</b>: @{un}\
        \n<b>ID</b>: <code>{id}</code>\
        \n<b>Statu</b>s: {us}",
    't_info_admin': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {fn}\
        \n<b>Username</b>: @{un}\
        \n<b>ID</b>: <code>{id}</code>\
        \n<b>Status</b>: {us}\
        \n\n<u><b>Permissions</b></u>\
        \n🔘 <code>Editable</code>: {cbe}\
        \n🔘 <code>Add Users</code>: {uciu}\
        \n🔘 <code>Restrict Users</code>: {ucru}\
        \n🔘 <code>Promote Users</code>: {ucpu}\
        \n🔘 <code>Pin Messages</code>: {ucpm}\
        \n🔘 <code>Delete Messages</code>: {ucdm}\
        \n🔘 <code>Change Chat Info</code>: {ucci}",
    't_info_member': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {fn}\
        \n<b>Username</b>: @{un}\
        \n<b>ID</b>: <code>{id}</code>\
        \n<b>Status</b>: {us}\
        \n<b>Until Date</b>: {ud}\
        \n\n<u><b>Permissions</b></u>\
        \n🔘 <code>Pin Messages</code>: {ucpm}\
        \n🔘 <code>Send Message</code>: {ucsm}\
        \n🔘 <code>Send Media</code>: {ucsmm}\
        \n🔘 <code>Send Stickers & GIFs</code>: {ucsom}\
        \n🔘 <code>Send Polls</code>: {ucsp}\
        \n🔘 <code>Embed Links</code>: {ucawpp}\
        \n🔘 <code>Add Users</code>: {uciu}\
        \n🔘 <code>Change Chat Info</code>: {ucci}",
    't_piv_admin': 'You aren\'t a Admin',
    't_user_until_date_cap1': 'Forever',
    't_ban': ['ban', 'Ban', 'BAN'],
    't_ban_cap1': 'Ban @{} Done!',
    't_ban_cap2': 'I can\'t ban myself!!!',
    't_ban_cap3': 'I can\'t ban you',
    't_ban_cap4': 'Only the Creator @{} can ban me!',
    't_ban_cap5': 'I can\'t ban the Creator @{}.',
    't_ban_cap6': 'Only the Creator @{}\ncan ban @{}',
    't_ban_cap7': 'Yor aren\'t allowed to ban @{}',
    't_unban': ['unban', 'Unban', 'UNBAN'],
    't_unban_cap1': 'Unban @{} Done!',
    't_unban_cap2': 'I can\'t unban myself!!!',
    't_unban_cap3': 'I can\'t unban you',
    't_unban_cap4': 'Only the Creator @{} can unban me!',
    't_unban_cap5': 'I can\'t unban the Creator @{}.',
    't_unban_cap6': 'Only Creator @{}\nCan Unban The admin @{}',
    't_unban_cap7': 'Yor aren\'t allowed to unban @{}',
    't_kick': ['kick', 'Kick', 'KICK'],
    't_kick_cap1': 'Kick @{} Done!',
    't_kick_cap2': 'I can\'t kick myself!!!',
    't_kick_cap3': 'I can\'t kick you',
    't_kick_cap4': 'Only the Creator @{} can kick me!',
    't_kick_cap5': 'I can\'t kick the Creator @{}.',
    't_kick_cap6': 'Only the Creator @{}\ncan kick the admin @{}',
    't_kickme': ['kickme', 'Kickme', 'KICKME'],
    't_kickme_cap1': 'Kick @{} Done!',
    't_pin': ['pin', 'Pin', 'PIN'],
    't_pin_cap1': 'You {} are not allowed to pin messages!!!',
    't_unpin': ['unpin', 'Unpin', 'UNPIN'],
    't_unpin_cap1': 'You {} are not allowed to unpin messages!!!',
    't_promote': ['promote', 'Promote', 'PROMOTE'],
    't_promote_cap1': 'Promote @{} Done!',
    't_demote': ['demote', 'Demote', 'DEMOTE'],
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
