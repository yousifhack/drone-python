def check_battery(battery_percent):
    if battery_percent < 15:
        return "critical"
    elif battery_percent < 30:
        return "low"
    else:
        return "sufficient"

battery_history = []

while True:
    battery_text = input("Enter battery percentage, or q to quit: ")

    if battery_text == "q":
        break

    

    try:
        battery_percent = int(battery_text)
    except ValueError:
        print("Please enter a whole number.")
        continue

    

    if battery_percent < 0 or battery_percent > 100:
        print("Battery percentage must be between 0 and 100.")
        continue
    
    
    battery_history.append(battery_percent)
    battery_status = check_battery(battery_percent)
    print("Battery status:", battery_status)
    print("Battery history:", battery_history)
    battery_drop = battery_history[0] - battery_history[-1]
    print("Drop since first reading:", battery_drop, "percentage points")