import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def notification_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            Notify.init("Notification")
            notification = Notify.Notification.new("Success", "Method executed successfully", "dialog-information")
            notification.show()
            return result
        except Exception as e:
            Notify.init("Notification")
            notification = Notify.Notification.new("Error", str(e), "dialog-error")
            notification.show()
    return wrapper
