import dbus
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
foto_DIR = str(BASE_DIR.joinpath('foto_temp.png'))

from zapzap.app_info import APPLICATION_NAME


def show(q_notification):
    item = "org.freedesktop.Notifications"
    path = "/org/freedesktop/Notifications"
    interface = "org.freedesktop.Notifications"
    id_num_to_replace = 0
    icon = convertImage(q_notification.icon())
    actions = {}
    app_name = APPLICATION_NAME
    hints = {}
    time = 1000   # Use seconds x 1000
    bus = dbus.SessionBus()
    notif = bus.get_object(item, path)

    notify = dbus.Interface(notif, interface)
    notify.Notify(app_name, id_num_to_replace, icon,
                  q_notification.title(), q_notification.message(), actions, hints, time)

def convertImage(img):
    path = foto_DIR
    confirm = img.save(path)
    print(confirm)
    if(confirm):
        return path
    else:
        return 'com.rtosta.zapzap'
