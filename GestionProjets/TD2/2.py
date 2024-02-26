from itertools import product

reductions = {
    'B': [(2, 400), (4, 800)],
    'C': [(2, 800)],
    'G': [(2, 300), (4, 900)],
    'H': [(2, 300)],
    'I': [(2, 200), (4, 300)],
    'K': [(2, 200), (4, 400), (6, 1200)]
}

initial_duration = 68
duration_reduction_needed = initial_duration - 48
total_cost = 0

all_combinations = list(product(*[[(task, *option) for option in options] for task, options in reductions.items()]))

valid_combinations = []
for combination in all_combinations:
    total_reduction = sum(option[1] for option in combination)
    total_cost = sum(option[2] for option in combination)
    if total_reduction >= duration_reduction_needed:
        valid_combinations.append((combination, total_reduction, total_cost))

min_cost_combination = min(valid_combinations, key=lambda x: x[2])

print(min_cost_combination)
