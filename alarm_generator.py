import random
from datetime import datetime

# alarms the generator can pick from
alarm_types = [
    "Unscheduled Open",
    "Late Close",
    "Sensor Trouble",
    "Burg Alarm",
    "Thermo Fisher Alarm",
    "Fire Alarm"
]

# fake store numbers for now
stores = [
    "Store 101",
    "Store 205",
    "Store 322",
    "Store 417"
]

# priority for each alarm, higher number means more important
alarm_priorities = {
    "Unscheduled Open": 1,
    "Late Close": 2,
    "Sensor Trouble": 3,
    "Burg Alarm": 4,
    "Thermo Fisher Alarm": 5,
    "Fire Alarm": 6
}


def generate_alarm():
    # randomly picks what kind of alarm comes in
    alarm_type = random.choice(alarm_types)

    # creates one random alarm
    alarm = {
        "store": random.choice(stores),
        "alarm_type": alarm_type,

        # looks up the priority based on the alarm that was picked
        "priority": alarm_priorities[alarm_type],

        # gets the current date and time
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return alarm


# make one alarm to test it
alarm = generate_alarm()

print(alarm)
