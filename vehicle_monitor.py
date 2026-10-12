def check_battery(battery_percent):
    if battery_percent < 15:
        return "critical"
    elif battery_percent < 30:
        return "low"
    else:
        return "sufficient"


def check_altitude(altitude_m, altitude_limit_m):
    if altitude_m > altitude_limit_m:
        return "above limit"
    else:
        return "within limit"


def calculate_drop(previous_reading, current_reading):
    return previous_reading - current_reading


def choose_action(battery_status, altitude_status):
    if battery_status == "critical":
        return "critical battery response requested"
    elif battery_status == "low":
        return "return requested"
    elif altitude_status == "above limit":
        return "reduce altitude requested"
    else:
        return "continue monitoring"


altitude_limit_m = 10

simulated_readings = [
    {"battery": 95, "altitude_m": 0},
    {"battery": 90, "altitude_m": 3},
    {"battery": 85, "altitude_m": 8},
    {"battery": 70, "altitude_m": 12},
    {"battery": 25, "altitude_m": 8},
    {"battery": 10, "altitude_m": 3},
]

battery_history = []

for reading in simulated_readings:
    battery_percent = reading["battery"]
    altitude_m = reading["altitude_m"]

    battery_status = check_battery(battery_percent)
    altitude_status = check_altitude(altitude_m, altitude_limit_m)
    mission_action = choose_action(battery_status, altitude_status)

    battery_history.append(battery_percent)

    print("Battery percentage:", battery_percent)
    print("Battery status:", battery_status)
    print("Altitude in meters:", altitude_m)
    print("Altitude status:", altitude_status)
    print("Practice action:", mission_action)

    if len(battery_history) >= 2:
        previous_reading = battery_history[-2]
        recent_drop = calculate_drop(previous_reading, battery_percent)

        print("Battery drop:", recent_drop, "percentage points")

        if recent_drop >= 10:
            print("Warning: large battery drop between readings.")

    print("--------------------")

print("Monitoring finished.")
print("Battery history:", battery_history)