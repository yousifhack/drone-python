while True:
    battery_text = input("Enter battery percentage, or q to quit: ")

    if battery_text == "q":
          break
    
    try:
        battery_percent = int(battery_text)
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.")
        continue
    
    if battery_percent < 0 or battery_percent > 100:
        print("Battery percentage must be between 0 and 100.")
        continue

    battery_percent = int(battery_text)

    if battery_percent < 15:
        print("Critical battery: stop mission requested")
    elif battery_percent < 30:
        print("Low battery: return requested")
    else:
        print("Battery sufficient: continue")
