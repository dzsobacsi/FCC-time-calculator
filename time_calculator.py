def add_time(start, duration, day=None):

    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day is not None:
            day = DAYS.index(day.lower())

    am_pm = 0 if start[-2:] == 'AM' else 1
    start_hh, start_mm = [int(x) for x in start[:-3].split(':')]
    duration_hh, duration_mm = [int(x) for x in duration.split(':')]

    res_mm = (start_mm + duration_mm) % 60
    extra_hours = (start_mm + duration_mm) // 60
    
    res_hh = (start_hh + duration_hh + extra_hours) % 12
    if res_hh == 0:
            res_hh = 12
    extra_half_days = (start_hh + duration_hh + extra_hours) // 12
    
    res_am_pm = am_pm if extra_half_days % 2 == 0 else 1 - am_pm
    extra_days = extra_half_days // 2 if am_pm == 0 else (extra_half_days + 1) // 2
    
    res_day = None
    if day is not None:
            res_day = (day + extra_days) % 7
            res_day = DAYS[res_day].capitalize()

    result = str(res_hh) + ':' + str(res_mm).zfill(2) + ' ' + ('PM' if res_am_pm == 1 else 'AM')
    if res_day is not None:
        result += ', ' + res_day
    if extra_days:
        result += f" ({'next day' if extra_days == 1 else f'{extra_days} days later'})"

    return result