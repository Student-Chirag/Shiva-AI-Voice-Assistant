import datetime
import winsound
def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, '%I:%M %p'))
    altime = altime[11:-3]
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Minreal = altime[3:5]
    Minreal = int(Minreal)
    print("Alarm set for: " + str(Horeal) + ":" + str(Minreal))
    while True:
        if Horeal == datetime.datetime.now().hour and Minreal == datetime.datetime.now().minute:
            print("Wake up!")
            winsound.PlaySound('abc', winsound.SND_LOOP)
        
        elif Minreal < datetime.datetime.now().minute:
            break

if __name__ == "__main__":
    alarm('2:40 AM')
    

