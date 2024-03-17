#!/usr/bin/env python3
import sys

current_year = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    year, temperature = line.split('\t', 1)

    try:
        temperature = float(temperature)
    except ValueError:
        continue

    if current_year == year:
        current_sum += temperature
        current_count += 1
    else:
        if current_year:
            # Output the average temperature for the current year
            print(f'{current_year}\t{current_sum / current_count}')
        current_year = year
        current_sum = temperature
        current_count = 1

# Don't forget to output the last year's average temperature
if current_year:
    print(f'{current_year}\t{current_sum / current_count}')
