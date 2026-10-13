import math


def validate_reading(reading):
    battery = reading.get("battery")
    altitude = reading.get("altitude_m")

    if battery is None or altitude is None:
        return "Missing battery or altitude reading."

    if type(battery) not in (int, float) or type(altitude) not in (int, float):
        return "Battery and altitude must be numbers."

    if not math.isfinite(battery) or not math.isfinite(altitude):
        return "Battery and altitude must be finite numbers."

    if battery < 0 or battery > 100:
        return "Battery percentage must be between 0 and 100."

    if altitude < 0:
        return "This practice monitor expects altitude at or above zero."

    return None


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
    {"battery": 150, "altitude_m": 8},
    {"altitude_m": 8},
    {"battery": "unknown", "altitude_m": 8},
    {"battery": 70, "altitude_m": 12},
    {"battery": 25, "altitude_m": 8},
    {"battery": 10, "altitude_m": 3},
]

battery_history = []

for reading in simulated_readings:
    validation_error = validate_reading(reading)

    if validation_error is not None:
        print("Invalid reading:", validation_error)
        print("Practice action: investigate telemetry; no normal decision made.")
        print("--------------------")
        continue

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