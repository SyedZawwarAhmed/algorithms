def get_current_date():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(get_current_date())