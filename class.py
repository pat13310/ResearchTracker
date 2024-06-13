class Time:
    def __init__(self, minutes, seconds=0):

        if isinstance(minutes, str):
            time = minutes.split(":")
            minutes = int(time[0])
            seconds = int(time[1])

        if minutes >= 0 and seconds < 59:
            self.minutes = minutes

        if seconds >= 0 and seconds < 59:
            self.seconds = seconds

