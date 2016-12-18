from itertools import combinations
import heapq

# hardcoded input
polonium, thulium, promethium, ruthenium, cobalt, elerium, dilithium = 1, 2, 3, 4, 5, 6, 7
initial = (0, (
    tuple(sorted((polonium, thulium, -thulium, promethium, ruthenium, -ruthenium, cobalt, -cobalt, elerium, -elerium, dilithium, -dilithium))),
    tuple(sorted((-polonium, -promethium,))), (), ()
))

def correct(floor):
    if not floor or floor[-1] < 0: # no generators
        return True
    return all(-chip in floor for chip in floor if chip < 0)

frontier = []
heapq.heappush(frontier, (0, initial))
cost_so_far = {initial: 0}

while frontier:
    _, current = heapq.heappop(frontier)
    our_floor, floors_state = current
    if our_floor == 3 and all(len(f) == 0 for f in floors_state[:-1]): #goal!
        break

    possible_directions = [dir for dir in (-1, 1) if 0 <= our_floor + dir < 4]
    moves = list(combinations(floors_state[our_floor], 2)) + list(combinations(floors_state[our_floor], 1)) #what can i carry
    for move in moves:
        for direction in possible_directions:
            new_floors = list(floors_state)
            new_floors[our_floor] = tuple(x for x in floors_state[our_floor] if x not in move)
            new_floors[our_floor+direction] = tuple(sorted(floors_state[our_floor+direction] + move))

            if not correct(new_floors[our_floor]) or not correct(new_floors[our_floor+direction]):
                continue

            next = (our_floor+direction, tuple(new_floors))
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost - len(new_floors[3]) * 10
                heapq.heappush(frontier, (priority, next))

print(cost_so_far[current], current)
