import time
import pyttsx3
a =str(input("enter you name:"))
b = str(input("enter your professional field:"))
f = pyttsx3.init()
voice = f.getProperty("voices")
f.setProperty("voice",voice[1].id)
print(f"{a} are you enter my server:")
f.runAndWait()


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec,60)
        timeformat ='{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        time_sec -=1

    print("time complete!")
countdown(int(input("enter time:")))
f = pyttsx3.init()
voice = f.getProperty("voices")
f.setProperty("voice",voice[1].id)

f.say(f"{a} is a passionate {b} with expertise in creating efficient and user-friendly applications. He has a strong background in Python and JavaScript, with a keen interest in artificial intelligence and machine learning. Outside of work, John enjoys hiking, reading science fiction novels, and experimenting with new technologies to solve real-world problems.His collaborative spirit and dedication to continuous learning make him a valuable asset to any team.")
f.runAndWait()