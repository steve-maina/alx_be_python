task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            reminder =f"'{task}' is a {priority} priority task that requires immediate attention today!"
            print("Reminder: {reminder}")
        else :
            reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
            print("Note: {reminder}")
    case "medium":
        if time_bound == "yes":
            reminder =f"'{task}' is a {priority} priority task that requires immediate attention today!"
            print("Reminder: {reminder}")
        else :
            reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
            print("Note: {reminder}")
    case "low":
        if time_bound == "yes":
            reminder =f"'{task}' is a {priority} priority task that requires immediate attention today!"
            print("Reminder: {reminder}")
        else :
            reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
            print("Note: {reminder}")


    