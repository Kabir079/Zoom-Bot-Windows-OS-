import subprocess
import pyautogui
import time
import csv
from datetime import datetime

def sign_in(meetingid):
    subprocess.call(r'C:\Users\Lenovo\AppData\Roaming\Zoom\bin\Zoom')

    time.sleep(2)

    #Clicks the INITIAL-JOIN button
    join_btn = pyautogui.locateCenterOnScreen('photo103.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Type the Meeting ID button
    meeting_id_btn = pyautogui.locateCenterOnScreen('photo2.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.write(meetingid)

    # Disabling both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('photo3.png')
    for a in media_btn:
        pyautogui.moveTo(a)
        pyautogui.click()
        time.sleep(1)

    # Clicking the FIRST-JOIN button
    join_btn = pyautogui.locateCenterOnScreen('photo4.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Writes the password for the meeting
    join_btn = pyautogui.locateCenterOnScreen('photo100.png')
    pyautogui.moveTo(join_btn)
    pyautogui.write("gitam123")

    # Clicking the FINAL-JOIN button
    join_btn = pyautogui.locateCenterOnScreen('photo102.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()


def extract(addinglist):
    return [item[0] for item in addinglist]
def newextract(addinglist):
    return [item[1] for item in addinglist]
def numextract(addinglist):
    return [item[2] for item in addinglist]

# Reading the CSV file
with open("timings.csv",newline='') as csvfile:
    rows = csv.reader(csvfile,delimiter=',')
    addinglist = []
    for i in rows:
        addinglist.append(i)

a = extract(addinglist)
b = newextract(addinglist)
c = numextract(addinglist)
print("The timings of all your meetings are :",a)
print("The Meeting ID's for all your respective meetings are :",b)
print("The Meeting ID's for all your respective meetings are :",c)

while True :
    now = datetime.now().strftime("%H:%M")
    if a[0] < now :
        a.pop(0)
        b.pop(0)
        c.pop(0)
    elif a[0] == now :
        sign_in(b[0])
        print("Signed in = 1st  meeting ",c[0])
        print("Sleeping = 1st time ")
        time.sleep(60)
        print("Bot = Online = 1th time")
        sign_in(b[1])
        print("Signed in = 2nd  meeting ",c[1])
        print("Sleeping = 2nd time")
        time.sleep(60)
        print("Online = 2nd time")
        sign_in(b[2])
        print("Signed in = 3rd  meeting ",c[2])
        print("Sleeping = 3rd")
        time.sleep(60)
        print("Online = 3rd time")
        sign_in(b[3])
        print("Signed in = 4th  meeting ",c[1])
        print("Sleeping = 4th")
        time.sleep(60)
        print("Online = 4th time")
        print("Finally all classes are done")
        break
    else:
        print("Not yet")
        time.sleep(5)
