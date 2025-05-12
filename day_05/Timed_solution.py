from collections import defaultdict
import time

start_time = time.perf_counter_ns()

with open("input.txt") as f: lines = [line.strip() for line in f]

# Part 1
transform_rule = lambda s: tuple(map(int, s.split('|')))
transform_page = lambda s: tuple(map(int, s.split(',')))

rules = [transform_rule(rule) for rule in lines[:lines.index('')]]
pages = [transform_page(page) for page in lines[lines.index('')+1:]]

valid_rules = [[rule for rule in rules if all(element in page for element in rule)] for page in pages]

def is_valid(page, i): # Index associated with the page: 'i'.
    return all(page.index(rule[0]) < page.index(rule[1]) for rule in valid_rules[i])

s1 = sum(page[len(page)//2] for i, page in enumerate(pages) if is_valid(page, i))

# Part 2
s2 = -s1
for i in range(len(valid_rules)):
    d = defaultdict(int)
    for rule in sorted(valid_rules[i]): d[rule[0]] += 1
    c_list = list(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)).keys()) # + [x for x in pages[i] if x not in d]
    s2 += c_list[len(c_list)//2]

print(s1)
print(s2)

# Timer ends
end_time = time.perf_counter_ns()
execution_time = end_time - start_time

# Execution time
print(f"Python program executed in {execution_time*1e-6:.3f} ms")