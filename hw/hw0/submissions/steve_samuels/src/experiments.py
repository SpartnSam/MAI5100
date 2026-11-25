"""Generate the C3.1 results table (Markdown) from your own search.py / guyanaRoutes.py."""
import time
import guyanaRoutes as gr
import search

QUERIES = [
    ("Bartica", "Ituni", "km"),
    ("Bartica", "Ituni", "hours"),
    ("Georgetown", "Lethem", "km"),
    ("Georgetown", "Lethem", "hours"),
    ("Charity", "Corriverton", "km"),
    ("Charity", "Corriverton", "hours"),
    ("Corriverton", "Ituni", "km"),
    ("Corriverton", "Ituni", "hours"),
]
REPEATS = 200   # average the runtime over many runs, since one run takes ~0.05 ms

ALGS = [
    ("BFS",    lambda p: search.breadthFirstSearch(p)),
    ("DFS",    lambda p: search.depthFirstSearch(p)),
    ("UCS",    lambda p: search.uniformCostSearch(p)),
    ("Greedy", lambda p: gr.greedySearch(p, gr.straightLineHeuristic)),
    ("A*",     lambda p: search.aStarSearch(p, gr.straightLineHeuristic)),
]

roadMap = gr.RoadMap()
print("| Start > Goal | Mode | Algorithm | Cost | Expanded | ms | Route |")
print("|:---|:---|:---|---:|---:|---:|:---|")
for start, goal, mode in QUERIES:
    for name, alg in ALGS:
        problem = gr.GuyanaRouteProblem(roadMap, start, goal, mode)
        path = alg(problem)                      # one run for cost and expanded
        cost, expanded = problem.getCostOfActions(path), problem._expanded
        t0 = time.perf_counter()
        for _ in range(REPEATS):
            alg(gr.GuyanaRouteProblem(roadMap, start, goal, mode))
        ms = (time.perf_counter() - t0) * 1000 / REPEATS
        fmt = f"{cost:.1f}" if mode == "km" else f"{cost:.2f}"     # hours need 2 decimals
        print(f"| {start} > {goal} | {mode} | {name} | {fmt} | {expanded} | {ms:.2f} | "
              + " > ".join([start] + path) + " |")