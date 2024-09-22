task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

    
reminder = f"Reminder: You have a task '{task}' with {priority} priority."


match priority:
    case "high":
        reminder += " This is urgent!"
    case "medium":
        reminder += " This is important."
    case "low":
        reminder += " This can be done later."
    case _:
        reminder += " Priority not recognized."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

    print(reminder)