
import datetime
def current_day():

    today = datetime.date.today()

    day_name = today.strftime("%A")

    print("today is:",day_name)

current_day() 



