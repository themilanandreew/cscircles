# goal: print out the number of seconds in a week
secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 60  # todo: check this!
secondsPerDay = secondsPerHour * 24
daysPerWeek = 7
# daysPerWeek = daysPerWeek + 2 # weekends are disabled!?
print(secondsPerDay * daysPerWeek)
