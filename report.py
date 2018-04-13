from collections import Counter
import sys

minutc = int(sys.argv[1])
maxutc = 0xffffffffffff

report = Counter()
for line in sys.stdin:
    (task, begin, end) = line.split(' ', 2)
    if (int(begin) < minutc): continue

    duration = int(end) - int(begin)
    report[task] += duration

for task in report:
    print(task, report[task])
