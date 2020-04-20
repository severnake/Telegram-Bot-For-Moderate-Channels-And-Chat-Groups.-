""" USER LANGUAGE UTILITY """
ar_lang = {}
en_lang = {
    'start_msg': "<b>Welcome!</b> {0} 🎉\
        \nI'm here to moderate your\
        \nchannels and chat groups\
        \njust add me to it 👀,\
        \n\nI made with <code>tgbotapi</code>\
        \ncheck it at <code>PYPI</code> 🔰\
        \nhttps://pypi.org/project/tgbotapi\
        \n\nFor more information contact ⤵️\
        \n{1} 🛠 - {2} ⚙️ ",
    'h_channel': "<b>Channel</b> 📰\
        \n========== \
        \nIn order to make me work\
        \nI\'m must be an admin \
        \nAnd should observe all permissions:\
        \n<i>Change chat info</i>\
        \n<i>Post messages</i>\
        \n<i>Edit messages of others</i>\
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
        \n",
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
    't_start': ['/start', 'start'],
    't_help': ['help', 'Help'],
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
        \n🔘 <code>Send Message</code>: {0}\
        \n🔘 <code>Send Media</code>: {1}\
        \n🔘 <code>Send Stickers & GIFs</code>: {2}\
        \n🔘 <code>Send Polls</code>: {3}\
        \n🔘 <code>Embed Links</code>: {4}\
        \n🔘 <code>Add Users</code>: {5}\
        \n🔘 <code>Pin Messages</code>: {6}\
        \n🔘 <code>Change Chat Info</code>: {7}",
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
        \n🔘 <code>Send Message</code>: {0}\
        \n🔘 <code>Send Media</code>: {1}\
        \n🔘 <code>Send Stickers & GIFs</code>: {2}\
        \n🔘 <code>Send Polls</code>: {3}\
        \n🔘 <code>Embed Links</code>: {4}\
        \n🔘 <code>Add Users</code>: {5}\
        \n🔘 <code>Pin Messages</code>: {6}\
        \n🔘 <code>Change Chat Info</code>: {7}",
    'member_help': "<b>Help Menu</b> 📋\
        \n============\
        \n<u><b>Commands</b></u>\
        \n🔘 <code>help</code>: Show this menu\
        \n🔘 <code>info</code>: replay your info\
        \n🔘 <code>kickme</code>: Leave The Group\
        \n🔘 <code>pin</code>: Pin Message\
        \n🔘 <code>unpin</code>: Unpin Message",
    't_info': ['id', 'Id', 'my id', 'My id', 'info', 'Info', 'INFO'],
    't_info_p_user': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>",
    't_info_user': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Statu</b>s: {3}",
    't_info_creator': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Statu</b>s: {3}",
    't_info_admin': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Status</b>: {3}\
        \n\n<u><b>Permissions</b></u>\
        \n🔘 <code>Editable</code>: {4}\
        \n🔘 <code>Add Users</code>: {5}\
        \n🔘 <code>Restrict Users</code>: {6}\
        \n🔘 <code>Promote Users</code>: {7}\
        \n🔘 <code>Pin Messages</code>: {8}\
        \n🔘 <code>Delete Messages</code>: {9}\
        \n🔘 <code>Change Chat Info</code>: {10}",
    't_info_member': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Status</b>: {3}\
        \n<b>Until Date</b>: {4}\
        \n\n<u><b>Permissions</b></u>\
        \n🔘 <code>Pin Messages</code>: {5}\
        \n🔘 <code>Send Message</code>: {6}\
        \n🔘 <code>Send Media</code>: {7}\
        \n🔘 <code>Send Stickers & GIFs</code>: {8}\
        \n🔘 <code>Send Polls</code>: {9}\
        \n🔘 <code>Embed Links</code>: {10}\
        \n🔘 <code>Add Users</code>: {11}\
        \n🔘 <code>Change Chat Info</code>: {12}",
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
sp_lang = {
    'start_msg': "<b>Bienvenido!</b> {0} 🎉\
        \nEstoy aquí para admnistrar tus\
        \ncanales y gropos\
        \nsolo añademe a ellos 👀 ,\
        \n\nEstoy hecho con <code>tgbotapi</code>\
        \nechale uun vistazo en <code>PYPI</code> 🔰 \
        \nhttps://pypi.org/project/tgbotapi \
        \n\nPara más información contacta a ⤵️ \
        \n{1} 🛠 - {2} ⚙️ ",
    'h_channel': '<b>Canal</b> 📰\
        \n========== \
        \nPara poder trabajar\
        \nNecesito ser administrador \
        \nY necesito estos permisos:\
        \n<i>Cambiar información del chat</i>\
        \n<i>Enviar mensajes</i>\
        \n<i>Editar mensajes de otros</i>\
        \n<i>Eliminar mensajes de otros</i>\
        \n<i>Añadir miembros</i>\
        \n<i>Añadir nuevos administradores</i>\
        \n',
    'h_group': '*Grupo* 👥\
        \n========= \
        \nPara poder trabajar\
        \nNecesito ser administrador \
        \nY necesito estos permisos:\
        \n<i>Change chat info</i>\
        \n<i>Eliminar mensajes</i>\
        \n<i>Banear usuarios</i>\
        \n<i>Invitar a usuarios mediante enlace</i>\
        \n<i>Fijar mensajes</i>\
        \n<i>Añadir nuevos administradores</i>\
        \n',
    'h_private': "<b>Privado</b> 👤\
        \n=========\
        \n/start : Mensaje de inicio\
        \n/id : Mostrar tu información",
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
    'creator_help': "<b>MENU DE AYUDA</b> 📋\
        \n==============\
        \n<u><b>Acciones de Usuario</b></u> 🚻 \
        \n🔘 <code>ban</code>: <i>Banear Usuario</i>\
        \n🔘 <code>unban</code>: <i>Desbanear Miembro Baneado</i>\
        \n🔘 <code>kick</code>: <i>Eliminar Usuario Sin Banear</i>\
        \n🔘 <code>pin</code>: <i>Fijar Mensaje</i>\
        \n🔘 <code>unpin</code>: <i>Quitar Mensaje Fijado</i>\
        \n🔘 <code>promote</code>: <i>Promover uun Miembro</i>\
        \n🔘 <code>demote</code>: <i>Degradar uun Adminstrador</i>\
        \n\n<u><b>Permisos de Grupo</b></u> 🔣 \
        \n Comando + Enabe or Disable\
        \n🔘 <code>Enviar Mensaje</code>: {0}\
        \n🔘 <code>Enviar Multimedia</code>: {1}\
        \n🔘 <code>Enviar Stickers y GIFs</code>: {2}\
        \n🔘 <code>Enviar Encuestas</code>: {3}\
        \n🔘 <code>Enlaces Incrustados</code>: {4}\
        \n🔘 <code>Añadir Usuarios</code>: {5}\
        \n🔘 <code>Fijar Mensajes</code>: {6}\
        \n🔘 <code>Cambiar Información del Chat</code>: {7}",
    'admin_help': "*MENU DE AYUDA* 📋\
        \n============\
        \n<u><b>Acciones de Usuario</b></u> 🚻 \
        \n🔘 <code>ban</code>: <i>Banear Usuario</i>\
        \n🔘 <code>unban</code>: <i>Desbanear Miembro Baneado</i>\
        \n🔘 <code>kick</code>: <i>Eliminar Usuario Sin Banear</i>\
        \n🔘 <code>pin</code>: <i>Fijar Mensaje</i>\
        \n🔘 <code>unpin</code>: <i>Quitar Mensaje Fijado</i>\
        \n🔘 <code>promote</code>: <i>Promover uun Miembro</i>\
        \n🔘 <code>demote</code>: <i>Degradar uun Adminstrador</i>\
        \n\n<u><b>Permisos de Grupo</b></u> 🔣 \
        \n Comando + Enabe or Disable\
        \n🔘 <code>Enviar Mensaje</code>: {0}\
        \n🔘 <code>Enviar Multimedia</code>: {1}\
        \n🔘 <code>Enviar Stickers y GIFs</code>: {2}\
        \n🔘 <code>Enviar Encuestas</code>: {3}\
        \n🔘 <code>Enlaces Incrustados</code>: {4}\
        \n🔘 <code>Añadir Usuarios</code>: {5}\
        \n🔘 <code>Fijar Mensajes</code>: {6}\
        \n🔘 <code>Cambiar Información del Chat</code>: {7}",
    'member_help': "<b>Menú De Ayuda</b> 📋\
        \n============\
        \n<u><b>Comandos</b></u>\
        \n🔘 <code>help</code>: Mostrar este Menú\
        \n🔘 <code>info</code>: Mostrar tu información\
        \n🔘 <code>kickme</code>: Dejar el Grupo\
        \n🔘 <code>pin</code>: Fijar Mensaje\
        \n🔘 <code>unpin</code>: Quitar Mensaje Fijado",
    't_info_p_user': "<u><b>Detalles</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Apellido</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>",
    't_info_user': "<u><b>Detalles</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Estado</b>: {3}",
    't_info_admin': "<u><b>Details</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Estado</b>: {3}\
        \n\n<u><b>Permisos</b></u>\
        \n🔘<code>Editable</code>: {4}\
        \n🔘<code>Añadir Usuarios</code>: {5}\
        \n🔘<code>Restringir Usuarios</code>: {6}\
        \n🔘<code>Promover Usuarios</code>: {7}\
        \n🔘<code>Fijar Mensajes</code>: {8}\
        \n🔘<code>Eliminar Mensajes</code>: {9}\
        \n🔘<code>Cambiar Información del Chat</code>: {10}",
    't_info_member': "<u><b>Detalles</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Estado</b>: {3}\
        \n<b>Hasta la Fecha</b>: {4}\
        \n\n<u><b>Permisos</b></u>\
        \n🔘<code>Fijar Mensajes</code>: {5}\
        \n🔘<code>Enviar Mensajes</code>: {6}\
        \n🔘<code>Enviar Multimedia</code>: {7}\
        \n🔘<code>Enviar Stickers y GIFs</code>: {8}\
        \n🔘<code>Enviar Encuestas</code>: {9}\
        \n🔘<code>Links embebidos</code>: {10}\
        \n🔘<code>Añadir Usuarios</code>: {11}\
        \n🔘<code>Cambiar Información del Chat</code>: {12}",
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


def lang(user_lang):
    if user_lang == 'ar':
        return ar_lang
    elif user_lang == 'en':
        return en_lang
    elif user_lang == 'sp':
        return sp_lang
    else:
        return en_lang
