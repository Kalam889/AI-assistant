import datetime

def tell_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%I:%M %p")
    print("JARVIS: The current time is", formatted_time)
    
def tell_date():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%d-%m-%Y")
    print("JARVIS: Today's date is", formatted_date)