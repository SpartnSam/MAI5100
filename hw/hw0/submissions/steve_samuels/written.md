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


---

## Part B: Written Problems

### B1. State spaces and uninformed search

1.
2.
3.
4.

### B2. Problem formulation and heuristics

1.
2.
3.
4.

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
