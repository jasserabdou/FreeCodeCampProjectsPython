def add_time(start, duration, start_day=None):

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    if period == "PM":
        start_hour += 12

    duration_hour, duration_minute = map(int, duration.split(":"))

    total_minutes = start_hour * 60 + start_minute + \
        duration_hour * 60 + duration_minute

    new_hour, new_minute = divmod(total_minutes, 60)
    days_later = new_hour // 24
    new_hour %= 24

    new_period = "AM" if new_hour < 12 else "PM"
    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour -= 12

    days_of_week = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
    if start_day:
        start_day = start_day.lower().capitalize()
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_later) % 7
        new_day = ", " + days_of_week[new_day_index]
    else:
        new_day = ""

    result = f"{new_hour:02d}:{new_minute:02d} {new_period}{new_day}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result


if __name__ == "__main__":
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))
