""" USER LANGUAGE UTILITY """
ar_lang = {}
en_lang = {
    'start_msg': "<b>Welcome!</b> {0} ๐\
        \nI'm here to moderate your\
        \nchannels and chat groups\
        \njust add me to it ๐,\
        \n\nI made with <code>tgbotapi</code>\
        \ncheck it at <code>PYPI</code> ๐ฐ\
        \nhttps://pypi.org/project/tgbotapi\
        \n\nFor more information contact โคต๏ธ\
        \n{1} ๐  - {2} โ๏ธ ",
    'b_main': 'Main Menu ๐ฑ',
    'b_back': 'Back โฉ๏ธ',
    'b_help': 'Help ๐',
    'b_support': 'Support โ๏ธ',
    'b_ch_lang': 'Choose a language ๐',
    'b_add': 'Add Me ๐ฒ',
    'b_id': 'ID ๐ณ',
    't_make': 'Make a Choose',
    'b_channel': 'Channel ๐ฐ',
    'b_group': 'Group ๐ฅ',
    'b_private': 'Private ๐ค',
    't_choose': 'Make a Choose',
    't_dev': 'Under Development ๐',
    't_sup_cap1': 'Unsupported Feature!',
    't_start': ['/start', 'start'],
    'help_pattern': ['help', 'Help'],
    'h_channel': "<b>Channel</b> ๐ฐ\
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
    'h_group': "<b>Group</b> ๐ฅ\
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
    'h_private': "<b>Private</b> ๐ค\
        \n=========\
        \n/start : Welcome message\
        \nID : show your info",
    'h_creator': "<b>HELP MENU</b> ๐\
        \n============\
        \n<u><b>User Actions</b></u> ๐ป\
        \n๐ <code>ban</code>: <i>Ban User</i>\
        \n๐ <code>unban</code>: <i>Unban Banned Member</i>\
        \n๐ <code>kick</code>: <i>Remove User Without Ban</i>\
        \n๐ <code>pin</code>: <i>Pin Message</i>\
        \n๐ <code>unpin</code>: <i>Unpin Message</i>\
        \n๐ <code>promote</code>: <i>Promote a Member</i>\
        \n๐ <code>demote</code>: <i>Demote an Admin</i>\
        \n\n<u><b>Group Permissions</b></u> ๐ฃ \
        \n Command + Enable or Disable\
        \n๐ <code>Send Message</code>: {0}\
        \n๐ <code>Send Media</code>: {1}\
        \n๐ <code>Send Stickers & GIFs</code>: {2}\
        \n๐ <code>Send Polls</code>: {3}\
        \n๐ <code>Embed Links</code>: {4}\
        \n๐ <code>Add Users</code>: {5}\
        \n๐ <code>Pin Messages</code>: {6}\
        \n๐ <code>Change Chat Info</code>: {7}",
    'h_admin': "<b>Help Menu</b> ๐\
        \n============\
        \n<u><b>User Actions</b></u> ๐ป\
        \n๐ <code>ban</code>: Ban User\
        \n๐ <code>unban</code>: Unban Banned Member\
        \n๐ <code>kick</code>: Remove User Without Ban\
        \n๐ <code>kickme</code>: Leave The Group\
        \n๐ <code>pin</code>: Pin Message\
        \n๐ <code>unpin</code>: Unpin Message\
        \n๐ <code>promote</code>: Promote a Member\
        \n๐ <code>demote</code>: Demote an Admin\
        \n\n<u><b>Group Permissions</b></u> ๐ฃ \
        \n Command + Enable or Disable\
        \n๐ <code>Send Message</code>: {0}\
        \n๐ <code>Send Media</code>: {1}\
        \n๐ <code>Send Stickers & GIFs</code>: {2}\
        \n๐ <code>Send Polls</code>: {3}\
        \n๐ <code>Embed Links</code>: {4}\
        \n๐ <code>Add Users</code>: {5}\
        \n๐ <code>Pin Messages</code>: {6}\
        \n๐ <code>Change Chat Info</code>: {7}",
    'h_member': "<b>Help Menu</b> ๐\
        \n============\
        \n<u><b>Commands</b></u>\
        \n๐ <code>help</code>: Show this menu\
        \n๐ <code>info</code>: replay your info\
        \n๐ <code>kickme</code>: Leave The Group\
        \n๐ <code>pin</code>: Pin Message\
        \n๐ <code>unpin</code>: Unpin Message\
        \n\n<u><b>Your Permissions</b></u>\
        \n๐ <code>Pin Messages</code>: {0}\
        \n๐ <code>Send Message</code>: {1}\
        \n๐ <code>Send Media</code>: {2}\
        \n๐ <code>Send Stickers & GIFs</code>: {3}\
        \n๐ <code>Send Polls</code>: {4}\
        \n๐ <code>Embed Links</code>: {5}\
        \n๐ <code>Add Users</code>: {6}\
        \n๐ <code>Change Chat Info</code>: {7}",
    'info_pattern': ['id', 'Id', 'my id', 'My id', 'info', 'Info', 'INFO'],
    'i_user': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>",
    'i_creator': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Statu</b>s: {3}",
    'i_admin': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Status</b>: {3}\
        \n\n<u><b>Permissions</b></u>\
        \n๐ <code>Editable</code>: {4}\
        \n๐ <code>Add Users</code>: {5}\
        \n๐ <code>Restrict Users</code>: {6}\
        \n๐ <code>Promote Users</code>: {7}\
        \n๐ <code>Pin Messages</code>: {8}\
        \n๐ <code>Delete Messages</code>: {9}\
        \n๐ <code>Change Chat Info</code>: {10}",
    'i_member': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Status</b>: {3}\
        \n\n<u><b>Permissions</b></u>\
        \n๐ <code>Editable</code>: {4}\
        \n๐ <code>Add Users</code>: {5}\
        \n๐ <code>Restrict Users</code>: {6}\
        \n๐ <code>Promote Users</code>: {7}\
        \n๐ <code>Pin Messages</code>: {8}\
        \n๐ <code>Delete Messages</code>: {9}\
        \n๐ <code>Change Chat Info</code>: {10}",
    'i_restricted': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>{3}</b>: {4}",
    'i_cu1': "<u><b>Details</b></u>\
        \n<b>Fullname</b>: {0}\
        \n<b>Username</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Statu</b>s: {3}",
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
    'start_msg': "<b>Bienvenido!</b> {0} ๐\
        \nEstoy aquรญ para admnistrar tus\
        \ncanales y gropos\
        \nsolo aรฑademe a ellos ๐ ,\
        \n\nEstoy hecho con <code>tgbotapi</code>\
        \nechale uun vistazo en <code>PYPI</code> ๐ฐ \
        \nhttps://pypi.org/project/tgbotapi \
        \n\nPara mรกs informaciรณn contacta a โคต๏ธ \
        \n{1} ๐  - {2} โ๏ธ ",
    'b_main': 'Menรบ principal ๐ฑ',
    'b_back': 'Atras โฉ๏ธ',
    'b_help': 'Ayuda ๐',
    'b_support': 'Soporte โ๏ธ',
    'b_ch_lang': 'Selecciona una Idioma ๐',
    'b_add': 'Aรฑademe ๐ฒ',
    'b_id': 'ID ๐ณ',
    't_make': 'Selecciona una opciรณn:',
    'b_channel': 'Canal ๐ฐ',
    'b_group': 'Grupo ๐ฅ',
    'b_private': 'Privado ๐ค',
    't_choose': 'Selecciona una opciรณn',
    't_dev': 'En Desarrollo ๐',
    't_sup_cap1': 'ยกCaracterรญstica no soportada!',
    't_start': ['start'],
    'help_pattern': ['help', 'Help'],
    'h_channel': '<b>Canal</b> ๐ฐ\
        \n========== \
        \nPara poder trabajar\
        \nNecesito ser administrador \
        \nY necesito estos permisos:\
        \n<i>Cambiar informaciรณn del chat</i>\
        \n<i>Enviar mensajes</i>\
        \n<i>Editar mensajes de otros</i>\
        \n<i>Eliminar mensajes de otros</i>\
        \n<i>Aรฑadir miembros</i>\
        \n<i>Aรฑadir nuevos administradores</i>\
        \n',
    'h_group': '*Grupo* ๐ฅ\
        \n========= \
        \nPara poder trabajar\
        \nNecesito ser administrador \
        \nY necesito estos permisos:\
        \n<i>Change chat info</i>\
        \n<i>Eliminar mensajes</i>\
        \n<i>Banear usuarios</i>\
        \n<i>Invitar a usuarios mediante enlace</i>\
        \n<i>Fijar mensajes</i>\
        \n<i>Aรฑadir nuevos administradores</i>\
        \n',
    'h_private': "<b>Privado</b> ๐ค\
        \n=========\
        \n/start : Mensaje de inicio\
        \nID : Mostrar tu informaciรณn",
    'h_creator': "<b>MENU DE AYUDA</b> ๐\
        \n==============\
        \n<u><b>Acciones de Usuario</b></u> ๐ป \
        \n๐ <code>ban</code>: <i>Banear Usuario</i>\
        \n๐ <code>unban</code>: <i>Desbanear Miembro Baneado</i>\
        \n๐ <code>kick</code>: <i>Eliminar Usuario Sin Banear</i>\
        \n๐ <code>pin</code>: <i>Fijar Mensaje</i>\
        \n๐ <code>unpin</code>: <i>Quitar Mensaje Fijado</i>\
        \n๐ <code>promote</code>: <i>Promover uun Miembro</i>\
        \n๐ <code>demote</code>: <i>Degradar uun Adminstrador</i>\
        \n\n<u><b>Permisos de Grupo</b></u> ๐ฃ \
        \n Comando + Enabe or Disable\
        \n๐ <code>Enviar Mensaje</code>: {0}\
        \n๐ <code>Enviar Multimedia</code>: {1}\
        \n๐ <code>Enviar Stickers y GIFs</code>: {2}\
        \n๐ <code>Enviar Encuestas</code>: {3}\
        \n๐ <code>Enlaces Incrustados</code>: {4}\
        \n๐ <code>Aรฑadir Usuarios</code>: {5}\
        \n๐ <code>Fijar Mensajes</code>: {6}\
        \n๐ <code>Cambiar Informaciรณn del Chat</code>: {7}",
    'h_admin': "*MENU DE AYUDA* ๐\
        \n============\
        \n<u><b>Acciones de Usuario</b></u> ๐ป \
        \n๐ <code>ban</code>: <i>Banear Usuario</i>\
        \n๐ <code>unban</code>: <i>Desbanear Miembro Baneado</i>\
        \n๐ <code>kick</code>: <i>Eliminar Usuario Sin Banear</i>\
        \n๐ <code>pin</code>: <i>Fijar Mensaje</i>\
        \n๐ <code>unpin</code>: <i>Quitar Mensaje Fijado</i>\
        \n๐ <code>promote</code>: <i>Promover uun Miembro</i>\
        \n๐ <code>demote</code>: <i>Degradar uun Adminstrador</i>\
        \n\n<u><b>Permisos de Grupo</b></u> ๐ฃ \
        \n Comando + Enabe or Disable\
        \n๐ <code>Enviar Mensaje</code>: {0}\
        \n๐ <code>Enviar Multimedia</code>: {1}\
        \n๐ <code>Enviar Stickers y GIFs</code>: {2}\
        \n๐ <code>Enviar Encuestas</code>: {3}\
        \n๐ <code>Enlaces Incrustados</code>: {4}\
        \n๐ <code>Aรฑadir Usuarios</code>: {5}\
        \n๐ <code>Fijar Mensajes</code>: {6}\
        \n๐ <code>Cambiar Informaciรณn del Chat</code>: {7}",
    'h_member': "<b>Menรบ De Ayuda</b> ๐\
        \n============\
        \n<u><b>Comandos</b></u>\
        \n๐ <code>help</code>: Mostrar este Menรบ\
        \n๐ <code>info</code>: Mostrar tu informaciรณn\
        \n๐ <code>kickme</code>: Dejar el Grupo\
        \n๐ <code>pin</code>: Fijar Mensaje\
        \n๐ <code>unpin</code>: Quitar Mensaje Fijado",
    'info_pattern': ['id', 'Id', 'my id', 'info', 'my info'],
    'i_user': "<u><b>Detalles</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Apellido</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>",
    'i_creator': "<u><b>Detalles</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Estado</b>: {3}",
    'i_admin': "<u><b>Details</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Estado</b>: {3}\
        \n\n<u><b>Permisos</b></u>\
        \n๐<code>Editable</code>: {4}\
        \n๐<code>Aรฑadir Usuarios</code>: {5}\
        \n๐<code>Restringir Usuarios</code>: {6}\
        \n๐<code>Promover Usuarios</code>: {7}\
        \n๐<code>Fijar Mensajes</code>: {8}\
        \n๐<code>Eliminar Mensajes</code>: {9}\
        \n๐<code>Cambiar Informaciรณn del Chat</code>: {10}",
    'i_member': "<u><b>Detalles</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Estado</b>: {3}\
        \n<b>Hasta la Fecha</b>: {4}\
        \n\n<u><b>Permisos</b></u>\
        \n๐<code>Fijar Mensajes</code>: {5}\
        \n๐<code>Enviar Mensajes</code>: {6}\
        \n๐<code>Enviar Multimedia</code>: {7}\
        \n๐<code>Enviar Stickers y GIFs</code>: {8}\
        \n๐<code>Enviar Encuestas</code>: {9}\
        \n๐<code>Links embebidos</code>: {10}\
        \n๐<code>Aรฑadir Usuarios</code>: {11}\
        \n๐<code>Cambiar Informaciรณn del Chat</code>: {12}",
    'i_restricted': "<u><b>Details</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>{3}</b>: {4}",
    'i_cu1': "<u><b>Details</b></u>\
        \n<b>Nombre completo</b>: {0}\
        \n<b>Nombre de usuario</b>: @{1}\
        \n<b>ID</b>: <code>{2}</code>\
        \n<b>Estado</b>: {3}",
    't_piv_admin': 'No eres Administrador',
    't_user_until_date_cap1': 'Para siempre',
    't_ban': ['ban', 'Ban'],
    't_ban_cap1': 'ยก@{} Baneado!',
    't_ban_cap2': 'ยกยกยกNo puedo banearme a mรญ mismo!!!',
    't_ban_cap3': 'ยกNo puedo banearte!',
    't_ban_cap4': 'ยกSolo el Creador @{} puede banearme!',
    't_ban_cap5': 'No puedo banear al creador @{}.',
    't_ban_cap6': 'Solo el creador @{}\npuede banear a @{}',
    't_ban_cap7': 'No te estรก permitido banear @{}',
    't_unban': ['unban', 'unban'],
    't_unban_cap1': 'ยก@{} desbaneado!',
    't_unban_cap2': 'ยกยกยกNo puedo desbanearme a mรญ mismo!!!',
    't_unban_cap3': 'ยกNo puedo desbanearte!',
    't_unban_cap4': 'ยกSolo el creador @{} puede desbanearme!',
    't_unban_cap5': 'No puedo desbanear al Creador @{}.',
    't_unban_cap6': 'Solo el creador @{}\nPuede desbanear al Administrador @{}',
    't_unban_cap7': 'No puedes desbanear @{}',
    't_kick': ['kick', 'Kick'],
    't_kick_cap1': 'Kick @{} Done!',
    't_kick_cap2': 'ยกยกยกNo puedo echarme a mรญ mismo!!!',
    't_kick_cap3': 'No puedo echarte',
    't_kick_cap4': 'Solo el Creador @{} puede echarme!',
    't_kick_cap5': 'No puedo hechar al Creador @{}.',
    't_kick_cap6': 'Solo el Creador @{}\npuede hechar al Administrador @{}',
    't_kickme': ['kickme', 'Kickme'],
    't_kickme_cap1': 'ยก@{} expulsado!',
    't_pin': ['pin', 'Pin'],
    't_pin_cap1': 'ยกยกยกTรบ {} no tienes permitido fijar mensajes!!!',
    't_unpin': ['unpin', 'Unpin'],
    't_unpin_cap1': 'ยกยกยกTu {} no tienes permitido quitar mensajes fijados!!!',
    't_promote': ['promote', 'Promote'],
    't_promote_cap1': 'ยก@{} Promovido!',
    't_demote': ['demote', 'Demote'],
    't_demote_cap1': 'ยก@{} Degradado!',
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
