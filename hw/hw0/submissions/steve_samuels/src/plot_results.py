"""Plot nodes expanded per algorithm for the C3 queries. Run from your submission src folder."""
import matplotlib.pyplot as plt
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
ALGS = [
    ("BFS",    lambda p: search.breadthFirstSearch(p)),
    ("DFS",    lambda p: search.depthFirstSearch(p)),
    ("UCS",    lambda p: search.uniformCostSearch(p)),
    ("Greedy", lambda p: gr.greedySearch(p, gr.straightLineHeuristic)),
    ("A*",     lambda p: search.aStarSearch(p, gr.straightLineHeuristic)),
]

# ---- collect data by running your own algorithms ----
roadMap = gr.RoadMap()
labels = [f"{s} → {g}\n({m})" for s, g, m in QUERIES]
expanded = {name: [] for name, _ in ALGS}
for start, goal, mode in QUERIES:
    for name, alg in ALGS:
        problem = gr.GuyanaRouteProblem(roadMap, start, goal, mode)
        alg(problem)
        expanded[name].append(problem._expanded)

def grouped_bars(names, filename, title):
    n = len(names)
    width = 0.8 / n
    fig, ax = plt.subplots(figsize=(12, 5))
    for i, name in enumerate(names):
        xs = [x + (i - (n - 1) / 2) * width for x in range(len(QUERIES))]
        bars = ax.bar(xs, expanded[name], width, label=name)
        ax.bar_label(bars, fontsize=8)
    ax.set_xticks(range(len(QUERIES)))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Nodes expanded")
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    fig.savefig(filename, dpi=200)
    print("saved", filename)

# Figure 1: all five algorithms
grouped_bars([n for n, _ in ALGS], "nodes_expanded_all.png",
             "Nodes expanded by algorithm (lower is cheaper)")
# Figure 2: UCS vs A* only (the comparison asked for in the analysis)
grouped_bars(["UCS", "A*"], "ucs_vs_astar.png",
             "A* vs UCS: nodes expanded (both return optimal routes)")