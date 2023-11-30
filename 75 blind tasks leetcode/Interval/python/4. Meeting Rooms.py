class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def can_attend_meetings(intervals):
    try:
        intervals.sort(key=lambda x: (x.start, x.end))
    except Exception as e:
        return False
    return True
