from puzzle_nn import Puzzle
from preferred_astar import PrefAstar


def load_problems(amount_of_problems=False):  # carga los problemas en memoria
    f = open('problems.txt')
    problems = []
    counter = 0
    while f:
        counter += 1
        if amount_of_problems and counter > amount_of_problems:
            break
        line = f.readline()
        line = line.rstrip()
        numlist = line.split(' ')
        if len(numlist) < 15:
            break
        problems.append(Puzzle([int(x) for x in numlist[1:]]))
    return problems


show_solutions = False        # mostramos las soluciones?
AMOUNT_OF_PROBLEMS = False

problems = load_problems(AMOUNT_OF_PROBLEMS)
heuristic = Puzzle.manhattan
total_time, total_cost, total_expansions = 0, 0, 0

print('%5s%10s%10s%10s%10s%10s' %
      ('#prob', '#exp', '#gen', '|sol|', 'tiempo', 'maxsubopt'))

i = -1
for problem in problems:
    i += 1
    if i+1 <= 66:
        continue
    s = PrefAstar(problem, heuristic, 1)
    result = s.search()
    print('%5d%10d%10d%10d%10.2f' % (i+1, s.expansions,
                                     len(s.generated), result.g, s.end_time-s.start_time))

    total_time += s.end_time - s.start_time
    total_cost += result.g
    total_expansions += s.expansions

    if show_solutions:
        print(result.trace())

print('Tiempo total:        %.2f' % (total_time))
print('Expansiones totales: %d' % (total_expansions))
print('Costo total:         %d' % (total_cost))
