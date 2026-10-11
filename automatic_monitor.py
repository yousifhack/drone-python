def check_battery(battery_percent):
    if battery_percent < 15:
        return "critical"
    elif battery_percent < 30:
        return "low"
    else:
        return "sufficient"


def calculate_drop(previous_reading, current_reading):
    return previous_reading - current_reading


def choose_action(battery_status):
    if battery_status == "critical":
        return "stop mission requested"
    elif battery_status == "low":
        return "return requested"
    else:
        return "continue monitoring"


simulated_readings = [95, 90, 85, 70, 25, 10]
battery_history = []

for battery_percent in simulated_readings:
    battery_history.append(battery_percent)

    battery_status = check_battery(battery_percent)
    mission_action = choose_action(battery_status)

    print("Battery percentage:", battery_percent)
    print("Battery status:", battery_status)
    print("Practice action:", mission_action)

    if len(battery_history) >= 2:
        previous_reading = battery_history[-2]
        recent_drop = calculate_drop(previous_reading, battery_percent)

        print("Drop since previous reading:", recent_drop, "percentage points")

        if recent_drop >= 10:
            print("Warning: large drop between readings.")

    print("--------------------")

print("Monitoring finished.")
print("Complete history:", battery_history)