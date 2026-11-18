# HW0 Written Answers

**Name: Steve Samuels**

**Student ID: 1036804**

Q1: I implemented the DFS function with help from Copilot.
A stack was used as the data structure, tiny maze had a cost of 10,medium maze had a cost of 130, and big maze 210.
Autograder gave a 3/3 grading.

Q2: I implemented the BFS function with help from Copilot.
A queue was used as the data structure, medium maze had a cost of 68, and big maze 210.
BFS did gain a lower cost.
The implementation also ran the 8puzzle search and completed it successfully.
Autograder gave a 3/3 grading.

Q3: I implemented the UCS function with help from Copilot.
A priority queue was used as the data structure. Medium maze had a cost of 68, mediumDottedMaze had a cost of 1, and mediumScaryMaze had a cost of 68719479864. As seen, an extremely low and high cost was given from the two different search agents.
Autograder gave a 3/3 grading.

Q4: I implemented the A* function with help from Copilot.
A priority queue was used as the data structure. BigMaze had a cost of 210, 549 search nodes expanded using A* with the manhattanHeuristic.

**OpenMaze Results:**
A* and heuristic manhattanHeuristic: Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 535
Pacman emerges victorious! Score: 456

DFS: Path found with total cost of 298 in 0.0 seconds
Search nodes expanded: 576
Pacman emerges victorious! Score: 212

BFS: Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 682
Pacman emerges victorious! Score: 456

UCS: Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 682
Pacman emerges victorious! Score: 456

Autograder gave a 3/3 grading.

Q5: I implemented the `CornersProblem` search problem in searchAgents.py with help from Copilot. Each search state stores Pacman's position and a tuple recording which of the four corners have been visited. This avoids including irrelevant game information, while preserving the information needed to recognize the goal. Legal moves have a step cost of 1, so BFS finds a shortest path that visits all four corners.

**tinyCorners Results:**
BFS found a path with a total cost of 28, matching the expected shortest path.
Search nodes expanded: 252
Pacman emerges victorious! Score: 512

**mediumCorners Results:**
BFS found a path with a total cost of 106.
Search nodes expanded: 1966
Pacman emerges victorious! Score: 434

Autograder gave a 6/6 grading.

Q6: I implemented the `cornersHeuristic` function with help from Copilot. The heuristic estimates the remaining path cost by finding the maze distance from Pacman to the nearest unvisited corner, then adding the minimum spanning tree cost connecting all remaining corners. I used maze distances that respect walls, and cached the distance maps so they could be reused during A* search. This estimate is admissible because any route that visits every remaining corner must at least reach one of them and connect all of them.

**mediumCorners Results:**
A* with cornersHeuristic found a path with a total cost of 106.
Search nodes expanded: 196
Pacman emerges victorious! Score: 434

Autograder gave a 6/6 grading.

Q7: I implemented the `foodHeuristic` function with help from Copilot. The heuristic finds the maze distance between Pacman's position and each remaining food dot, and between pairs of remaining food dots. It returns the greatest of those distances. Since any complete route must connect every remaining food location, its length must be at least this greatest pairwise distance. The heuristic is non-negative, returns 0 when no food remains, and uses maze distances that account for walls. Distance maps are cached in `problem.heuristicInfo` to avoid repeating the same breadth-first searches.

**testSearch Results:**
A* found a path with a total cost of 7 in 0.0 seconds.
Search nodes expanded: 8
Pacman emerges victorious! Score: 513

**trickySearch Results:**
A* found a path with a total cost of 60 in 0.0 seconds.
Search nodes expanded: 1130
Pacman emerges victorious! Score: 570

Autograder gave a 8/7 grading, including the extra-credit.

Q8: I implemented `findPathToClosestDot` and `AnyFoodSearchProblem.isGoalState` functions with help from Copilot. The goal test returns true when Pacman's current position contains food. `findPathToClosestDot` runs BFS on this problem, which returns a shortest path to any remaining dot. The agent repeats this process after eating each dot.

This greedy strategy is not guaranteed to find the shortest path for eating all the dots. Each BFS finds the nearest dot from Pacman's current position, but it does not consider how the choice affects the distance to the dots left afterward. For example, consider a small weighted maze graph with start S and food dots A, B, C, and D. If the shortest-path distances are S-to-(A,B,C,D) = (19, 19, 15, 20), A-to-(B,C,D) = (22, 25, 29), B-to-(C,D) = (13, 21), and C-to-D = 20, greedy chooses C, then B, D, and A, for a total of 78. The order A, B, C, D costs 19 + 22 + 13 + 20 = 74. Thus, repeatedly choosing the nearest dot can produce a longer total route.

**bigSearch Results:**
ClosestDotSearchAgent found a path with a total cost of 350.
Pacman emerges victorious! Score: 2360

Autograder gave a 3/3 grading.
---

## Part B: Written Problems

### B1. State spaces and uninformed search

1.State space for states 1 to 15
2.![alt text](Scan_20261116_192718.jpg)
3.Bidirectional search

Bidirectional search works very well here.
Forward branching factor: 2. Each state k has successors 2k and 2k+1.
Backward branching factor: 1. Each state k > 1 has exactly one predecessor, ⌊k/2⌋. From 11 the backward path is 11 → 5 → 2 → 1.

Because the backward direction has no branching, it is a single path of length d. The forward search only needs to expand a few levels before meeting it. For goal 11, the two searches meet after a couple of steps, giving the solution 1 → 2 → 5 → 11.

In general, a single-direction search to depth d costs O(2^d), but the backward search alone costs only O(d) = O(log n) for goal n. You can even skip the forward search entirely and just follow predecessors back to 1. This is a case where the reverse direction is far cheaper than the forward one, so bidirectional search (or just backward search) is dramatically better than plain BFS or IDS.
4.Solution without search

Left appends a 0 bit and Right appends a 1 bit, so the actions for goal g are just the binary digits of g after the leading 1.
function solve(g):
    actions = []
    while g > 1:
        if g is odd: add "Right" to actions
        else:        add "Left" to actions
        g = g / 2   (integer division)
    return actions reversed

Example: g = 11 = 1011 in binary, so the actions are Left, Right, Right (1 → 2 → 5 → 11).

This takes O(log g) time with no search at all.

What this says about problem formulation: A good formulation can matter more than the search algorithm. BFS or IDS costs O(2^d), backward search costs O(d), and using the binary structure gives the answer directly. Looking for structure in the problem first (like a unique predecessor or a numeric pattern) can remove the need for search entirely.

### B2. Problem formulation and heuristics

1.State space size

Vehicles are distinguishable (order matters) and no two share a square. Vehicle 1 has n² choices, vehicle 2 has n² − 1, and so on:

|S| = n²(n² − 1)…(n² − n + 1) = (n²)! / (n² − n)!

(roughly (n²)ⁿ as an upper bound)

2.Branching factor

Each vehicle has 5 choices (up, down, left, right, stay), and all vehicles move at the same time. So:

b ≈ 5ⁿ joint actions.

This is an upper bound, since some actions are illegal (off-grid or collisions). Hops add a few extra options per vehicle (a hop is a 2-square move over a stationary neighbour), so the strict bound is ≤ 9ⁿ, but 5ⁿ is the usual answer.

3.Heuristic for vehicle i at (x, y)

The goal is (n − i + 1, n). The Manhattan distance is

dᵢ = |x − (n − i + 1)| + |n − y|

A hop moves a vehicle 2 squares in one step, so dᵢ can overestimate in the full problem. To be safe:

hᵢ = (|x − (n − i + 1)| + |n − y|) / 2

This is admissible because a vehicle covers at most 2 squares of distance per step. It’s nontrivial since it’s > 0 away from the goal. (If you ignore hops, plain Manhattan distance works.)

4. Which are admissible for the whole problem?

(a) ∑ hᵢ: not admissible. All vehicles move simultaneously in one step, so one step can reduce every hᵢ at once. The sum counts the same time step n times and overestimates. Example: n vehicles each needing 1 move takes 1 step, but the sum is n·hᵢ.

(b) maxᵢ hᵢ: admissible. Every vehicle must reach its goal, so the total time is at least the time the slowest vehicle needs on its own. Ignoring the other vehicles only removes constraints, so this is a lower bound on the true cost. It’s also the tightest of the three.

(c) minᵢ hᵢ: admissible, but weak. minᵢ hᵢ ≤ maxᵢ hᵢ ≤ true cost, so it never overestimates. It’s less informative, though, because it only reflects the vehicle closest to its goal (and is often 0).

### B3. Proofs about heuristics

1.
2.
3.

### B4. Hand trace: Bartica to Ituni

Straight-line distances to Ituni (km) used for A*:

| Town | h (km) |
|---|---|
| | |

**BFS** (expansion order, fringe at each step):

**UCS** (expansion order, fringe and g at each step):

**A\*** (expansion order, fringe with g, h, f at each step):

| Algorithm | Route | Cost (km) | Optimal? |
|---|---|---|---|
| BFS | | | |
| UCS | | | |
| A* | | | |

Why A* expanded fewer (or not fewer) nodes than UCS:

---

## Part C: Route Planning in Guyana

### Autograder output

Paste the final lines of `python autograder.py --no-graphics`:

```
```

### Heuristic for the "hours" cost mode

Explain the speed you divide by and why it guarantees admissibility:

### C3.1 Results table

| Start → Goal | Mode | Algorithm | Cost | Expanded | ms | Route |
|---|---|---|---|---|---|---|
| | | BFS | | | | |
| | | DFS | | | | |
| | | UCS | | | | |
| | | Greedy | | | | |
| | | A* | | | | |

### C3.2 Analysis

### C3.3 Formulation critique

---

## Part D: Search vs. LLMs

### D1. Transcripts

For each instance: model and version, exact prompt, full response.

#### Instance 1

#### Instance 2

#### Instance 3

#### Instance 4 (8-puzzle)

#### Instance 5 (8-puzzle)

### D2. Evaluation

| Instance | LLM answer valid? | LLM cost | Optimal cost (A*/BFS) | Hallucinations? |
|---|---|---|---|---|
| | | | | |

### D3. Reflection (200–300 words)

---

## Generative AI Log

List every use of generative AI for this homework, excluding the Part D experiments above.

| Tool | What I asked | How I used the answer |
|---|---|---|
| | | |
