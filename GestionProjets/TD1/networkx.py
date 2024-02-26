# We will incorporate the information provided from the image into the code.
# First, let's define the tasks with their durations and dependencies.

tasks = {
    'A': {'duration': 2, 'dependencies': []},
    'B': {'duration': 18, 'dependencies': []},
    'C': {'duration': 1, 'dependencies': []},
    'D': {'duration': 2, 'dependencies': []},
    'E': {'duration': 6, 'dependencies': ['A']},
    'F': {'duration': 1, 'dependencies': ['A']},
    'G': {'duration': 0.5, 'dependencies': ['B']},
    'H': {'duration': 10, 'dependencies': ['B']},
    'I': {'duration': 12, 'dependencies': ['B']},
    'J': {'duration': 1.5, 'dependencies': ['C']},
    'K': {'duration': 3.5, 'dependencies': ['D']},
    'L': {'duration': 1.5, 'dependencies': ['D']},
    'M': {'duration': 6, 'dependencies': ['D']},
    'N': {'duration': 6, 'dependencies': ['E']},
    'O': {'duration': 3, 'dependencies': ['F', 'G']},
    'P': {'duration': 2, 'dependencies': ['H']},
    'Q': {'duration': 10, 'dependencies': ['I']},
    'R': {'duration': 1.5, 'dependencies': ['J', 'K']},
    'S': {'duration': 6, 'dependencies': ['L']},
    'T': {'duration': 4.5, 'dependencies': ['N']},
    'U': {'duration': 0.5, 'dependencies': ['O']},
    'V': {'duration': 3, 'dependencies': ['P']},
    'W': {'duration': 3, 'dependencies': ['S']},
    'X': {'duration': 2, 'dependencies': ['M', 'Q', 'R', 'W']},
    'Y': {'duration': 1, 'dependencies': ['X']}
}

# Initialize early start (ES) and late start (LS) for each task
for task in tasks:
    tasks[task]['es'] = 0  # Early start
    tasks[task]['ls'] = float('inf')  # Late start

# Compute early start (ES)
for task in tasks:
    if not tasks[task]['dependencies']:
        continue
    tasks[task]['es'] = max(tasks[dep]['es'] + tasks[dep]['duration'] for dep in tasks[task]['dependencies'])

# Assuming the project must finish at 12 (This is your project deadline time)
project_finish_time = 12

# Compute late start (LS) by reverse iteration
for task in sorted(tasks, key=lambda x: tasks[x]['es'], reverse=True):
    if not tasks[task]['dependencies']:
        tasks[task]['ls'] = project_finish_time - tasks[task]['duration']
        continue
    tasks[task]['ls'] = min(tasks[dep]['ls'] - tasks[task]['duration'] for dep in tasks[task]['dependencies'])

# Identify critical path tasks
critical_path_tasks = [task for task in tasks if tasks[task]['es'] == tasks[task]['ls']]
critical_path_duration = sum(tasks[task]['duration'] for task in critical_path_tasks)

# Calculate the start time for the project to finish at the project deadline
start_time_for_on_time_finish = project_finish_time - critical_path_duration

# Display the critical path and the start time
print("Chemin critique:", critical_path_tasks)
print("L'heure de commencement:", start_time_for_on_time_finish)
