import string
import time

RawString = "test876$$sd677_)(*)"

rmSpecialChar = lambda x: x.translate(str.maketrans("", "", string.punctuation))
#print(rmSpecialChar(RawString))


def rmPunc(RawString):
    return "".join([c for c in RawString if c in string.punctuation])

#rmPunc(RawString)

start_time_1 = time.time()
rmSpecialChar(RawString)
end_time_1 = time.time()
exec_time_1 = end_time_1 - start_time_1

# Exe Time rmPunc
start_time_2 = time.time()
rmPunc(RawString)
end_time_2 = time.time()
exec_time_2 = end_time_2 - start_time_2

# Compare the execution times
if exec_time_1 < exec_time_2:
    print("rmSpecialChar is faster.")
elif exec_time_1 > exec_time_2:
    print("rmPunc is faster.")
else:
    print("Both functions have similar execution times.")
    
print(f"Execution time of rmSpecialChar: {exec_time_1} seconds")
print(f"Execution time of rmPunc: {exec_time_2} seconds")

