from datetime import datetime, timedelta

def add(moment):
    giga_second = 1e9 # 1*10**9
    future_moment = moment + timedelta(seconds = giga_second)
    return future_moment