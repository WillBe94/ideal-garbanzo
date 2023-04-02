import requests
import webbrowser
from win10toast_click import ToastNotifier


termNumber = 3210
classNumber = 8747

baseCap = 49
baseTotal = 49
#baseWaitCap = 2
#baseWaitTotal = 1


toaster = ToastNotifier()

data = requests.get("https://www.uml.edu/student-dashboard/api/ClassSchedule/RealTime/Search/?term="+str(termNumber)+"&classNumber="+str(classNumber)).json()
URL = "https://www.uml.edu/student-dashboard#class-search/class?term="+str(termNumber)+"&cn="+str(classNumber)

def open_url():
    try:
        webbrowser.open_new(URL)
    except:
        print("Failed to open URL")

cap = (data["data"]["Classes"][0]["Details"]["EnrollmentCapacity"])
total = (data["data"]["Classes"][0]["Details"]["EnrollmentTotal"])
waitCap = (data["data"]["Classes"][0]["Details"]["WaitListCapacity"])
waitTotal = (data["data"]["Classes"][0]["Details"]["WaitListTotal"])

#toaster.show_toast("Scraper","Scraper is running.", duration=None, callback_on_click=open_url)

if(cap != baseCap):
    #sendping1
    toaster.show_toast("Scraper","Ge Database section capacity has changed!", duration=None, callback_on_click=open_url)

if(total != baseTotal):
    #sendping2
    toaster.show_toast("Scraper","Ge Database section total has changed!", duration=None, callback_on_click=open_url)
'''
if(waitCap != baseWaitCap):
    #sendping3
    toaster.show_toast("Scraper","Ge Database section waitlist has changed!", duration=None, callback_on_click=open_url)

if(waitTotal != baseWaitTotal):
    #sendping4
    toaster.show_toast("Scraper","Ge Database section waitlist size has changed!", duration=None, callback_on_click=open_url)
'''