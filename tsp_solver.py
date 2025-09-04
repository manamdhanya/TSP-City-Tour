import math
from distance import distance_matrix

def path_length(path, dist):
    return sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))

def nearest_neighbor(dist, start=0):
    n = len(dist)
    unvisited = set(range(n))
    path = [start]
    unvisited.remove(start)
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda j: dist[last][j])
        path.append(next_city)
        unvisited.remove(next_city)
    return path

def two_opt(path, dist):
    improved = True
    best = path[:]
    best_len = path_length(best, dist)
    while improved:
        improved = False
        for i in range(1, len(best)-2):
            for j in range(i+1, len(best)):
                if j-i == 1: 
                    continue
                new_path = best[:]
                new_path[i:j] = best[j-1:i-1:-1]
                new_len = path_length(new_path, dist)
                if new_len < best_len:
                    best, best_len = new_path, new_len
                    improved = True
        path = best
    return best
