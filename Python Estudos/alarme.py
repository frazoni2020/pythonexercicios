import time
import winsound
from win10toast import ToastNotifier

def timer(message,minutes):
    notificator = ToastNotifier()
    notificator.show_toast("Alarm",
    f"Alarme vai desligar em {minutes} minutes..", duration=50)
    time.sleep(minutes*60)
    winsound.Beep(frequency=2500,duration=1000)

    notificator.show_toast(f"Alarm",message,duration=50)

if __name__ == "__main__":
    message = "Postei"
    minutes = 1
    timer(message,minutes)