from datetime import datetime, timedelta
def display_current_datetime():
    current_date =  datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

def calculate_future_date():
    num_days = int(input("Enter number of days:"))
    future_date = timedelta(days=num_days) + datetime.datetime.now()
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(formatted_future_date)