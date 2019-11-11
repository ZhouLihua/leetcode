import sys
import math

def total_Hours(speed, pitches):
    totalHour = 0
    for pitch in pitches:
        totalHour += math.ceil(pitch / speed)
    return totalHour

if __name__ == "__main__":
    try:
        line = sys.stdin.readline().strip()
        if not line:
            raise Exception("negative")
        values = map(int, line.split())
        if len(values) < 2:
            raise Exception("negative")
        pitches = values[:-1]
        hour = values[-1]
        for item in pitches:
            if item <= 0:
                raise Exception("negative")
        if hour < len(pitches):
            raise Exception("negative")
        total = sum(pitches)
        min_speed = math.ceil(total / hour) if total >= hour else 1
        hours = sys.maxint
        import pdb
        pdb.set_trace()
        while hours > hour:
            hours = total_Hours(min_speed, pitches)
            min_speed += 1
        print int(min_speed - 1)
    except Exception:
        print -1
