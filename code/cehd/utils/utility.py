import datetime
import json


def get_current_week():
    """
    Helper function to get the current week details
    """
    # add current week dates
    today = datetime.date.today()
    dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
    week_day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    week_dates = {week_day[i]: dates[i].strftime("%Y-%m-%d") for i in range(7)}
    return week_dates


def get_current_semester():
    """
    Helper function to get the current semester details
    """
    with open("config.json") as json_config_file:
        config = json.load(json_config_file)
    semester = None
    semester_ui = None
    today_date = datetime.date.today()
    for k, v in config["semester"].items():
        sem_start = today_date.replace(month=v["start_month"], day=v["start_day"])
        sem_end = today_date.replace(month=v["end_month"], day=v["end_day"])
        if sem_start <= today_date <= sem_end:
            semester = k
            semester_ui = v["name"]
            break
    return semester, semester_ui        


def get_current_year():
    """
    Helper function to get the current year details
    """
    return datetime.date.today().year
