filename = "../results/ida-and-wida/wida-16-results.txt"
fo = open(filename)

total_expansions = 0
totoal_length = 0
total_problems = 0
total_time = 0
fo.readline()
for line in fo.readlines():
    line = line.rstrip()
    line = line.split()
    totoal_length += int(line[1])
    total_expansions += int(line[3])
    total_time += float(line[4])
    total_problems += 1

print(total_expansions, total_problems, total_time, totoal_length)

print(filename)
print("largo total:", totoal_length)
print("expansiones totales:", total_expansions)
print()
print("promedio de largo por problema", totoal_length/67)
print("promedio de expansiones por problema", total_expansions/67)
