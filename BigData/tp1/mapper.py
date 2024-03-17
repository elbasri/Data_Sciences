#!/usr/bin/env python3
import sys

def extract_temperature(temp_str):
    """Extract and convert the temperature from the raw string in the CSV."""
    try:
        temp_value = int(temp_str.split(',')[0]) / 10.0
        return temp_value
    except ValueError:
        return None

for line in sys.stdin:
    if line.startswith('"STATION"') or not line.strip():
        continue
    
    columns = line.strip().split(',')
    
    if len(columns) > 13:
        date = columns[1].strip('"')
        year = date[:4]
        
        temp_str = columns[13].strip('"')
        
        if temp_str and temp_str != "+9999" and temp_str != "":
            temperature = extract_temperature(temp_str)
            if temperature is not None:
                print(f'{year}\t{temperature}')

