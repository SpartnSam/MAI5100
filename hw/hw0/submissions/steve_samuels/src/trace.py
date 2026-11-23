"""Hand-trace helper: BFS, UCS, A* from Bartica to Ituni (prints every step)."""

import math
from collections import deque
from guyanaRoutes import RoadMap, haversineKm

START, GOAL = "Bartica", "Ituni"

def load(_path=None):
    rm = RoadMap()
    # graph[town] = {neighbour: km}, built from your RoadMap
    graph = {t: {nbr: km for nbr, km, hrs, ferry in rm.roads[t]} for t in rm.roads}
    return rm.coords, graph

def heuristics(towns, goal):
    return {t: haversineKm(towns[t], towns[goal]) for t in towns}

# ---------- helpers ----------
def route_of(parent, goal):
    path, n = [goal], goal
    while n in parent:
        n = parent[n]
        path.append(n)
    return path[::-1]

def route_cost(graph, path):
    return sum(graph[a][b] for a, b in zip(path, path[1:]))

# ---------- 3. BFS (goal test when GENERATED) ----------
def bfs(graph):
    print("\n=== BFS ===")
    fringe, parent, seen, expanded = deque([START]), {}, {START}, []
    step = 0
    while fringe:
        n = fringe.popleft(); step += 1; expanded.append(n)
        for m in sorted(graph[n]):                    # alphabetical tie-break
            if m in seen: continue
            seen.add(m); parent[m] = n; fringe.append(m)
            if m == GOAL:
                print(f"{step:>2}. expand {n:<14} fringe: {list(fringe)}   <- {GOAL} generated, stop")
                return route_of(parent, GOAL), expanded
        print(f"{step:>2}. expand {n:<14} fringe: {list(fringe)}")

# ---------- 4. UCS (key = g) and 5. A* (key = g + h), same loop ----------
def best_first(graph, h=None):
    print("\n=== " + ("A*" if h else "UCS") + " ===")
    fringe = {START: 0.0}           # node -> best g found so far
    parent, closed, expanded, step = {}, set(), [], 0
    key = (lambda n: (fringe[n] + h[n], n)) if h else (lambda n: (fringe[n], n))
    while fringe:
        n = min(fringe, key=key)                      # ties -> alphabetical (n is 2nd key)
        g = fringe.pop(n); closed.add(n); step += 1
        if n == GOAL:
            print(f"{step:>2}. expand {n} (g={g:.1f})  <- GOAL, stop")
            return route_of(parent, GOAL), expanded
        expanded.append(n)
        for m, cost in sorted(graph[n].items()):
            if m in closed: continue
            ng = g + cost
            if m not in fringe or ng < fringe[m] - 1e-9:   # new, or cheaper path found
                fringe[m] = ng; parent[m] = n
        if h:
            items = sorted(fringe, key=key)
            txt = ", ".join(f"{m}(g={fringe[m]:.1f}, h={h[m]:.1f}, f={fringe[m]+h[m]:.1f})" for m in items)
            head = f"expand {n} (g={g:.1f}, h={h[n]:.1f}, f={g+h[n]:.1f})"
        else:
            items = sorted(fringe, key=key)
            txt = ", ".join(f"{m}({fringe[m]:.1f})" for m in items)
            head = f"expand {n} (g={g:.1f})"
        print(f"{step:>2}. {head}\n      fringe: {txt}")

# ---------- 6. Run everything ----------
if __name__ == "__main__":
    towns, graph = load()
    h = heuristics(towns, GOAL)
    print("h table (km to", GOAL + "):")
    for t in sorted(h, key=h.get):
        print(f"  {t:<14}{h[t]:7.1f}")

    results = {}
    results["BFS"] = bfs(graph)
    results["UCS"] = best_first(graph)
    results["A*"]  = best_first(graph, h)

    ucs_cost = route_cost(graph, results["UCS"][0])
    print("\n=== SUMMARY ===")
    print(f"{'Algo':<5}{'Cost':>8}  {'Optimal':<8}{'Expanded':<9}Route")
    for name, (path, expanded) in results.items():
        c = route_cost(graph, path)
        print(f"{name:<5}{c:>8.1f}  {str(abs(c-ucs_cost)<1e-6):<8}{len(expanded):<9}{' -> '.join(path)}")