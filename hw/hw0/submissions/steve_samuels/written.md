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

1.Consistency ⇒ admissibility

Definitions: h is consistent if h(n) ≤ c(n,n’) + h(n’) for every node n and successor n’. h is admissible if h(n) ≤ h*(n), the true cost to the goal.

Proof (induction on the number of steps k from n to the goal along an optimal path):

Base case (k = 0): n is the goal, so h(n) = 0 = h*(n). ✓
Inductive step: suppose it holds for every node k−1 steps from the goal. Take n whose optimal path has k steps, with first successor n’ on that path. Then h*(n) = c(n,n’) + h*(n’).
Consistency: h(n) ≤ c(n,n’) + h(n’)
Induction hypothesis: h(n’) ≤ h*(n’)
So h(n) ≤ c(n,n’) + h*(n’) = h*(n). ✓

(Equivalent view: add up the consistency inequality along the optimal path n = n₀, n₁, …, n_k = goal. The h terms cancel (telescoping), leaving h(n) ≤ total path cost + h(goal) = h*(n).)

2.Max is admissible: for every n, h₁(n) ≤ h*(n) and h₂(n) ≤ h*(n). So max(h₁(n), h₂(n)) ≤ h*(n). ✓

Sum is NOT admissible in general. Counterexample: let h*(n) = 10 and h₁(n) = h₂(n) = 8. Both are admissible (8 ≤ 10), but h₁ + h₂ = 16 > 10. ✗

(Concrete version: a path graph S → G with cost 1. Take h₁(S) = h₂(S) = 1. Each is admissible, but the sum is 2 > h*(S) = 1.)

3.Weighted A*

Claim: the returned solution cost C ≤ w·C*, where C* is the optimal cost.

Proof:

a.Let n be a node on an optimal path that is still on the frontier when weighted A* is about to pick the goal G. (One always exists: the optimal path starts at the root and ends at the goal, so some node on it is on the frontier.)

b.Because h is admissible, g(n) + h(n) ≤ C*, and g(n) ≤ C* too (n is on the optimal path; with consistent h, g(n) is optimal for n).

c.Then f(n) = g(n) + w·h(n) ≤ w·(g(n) + h(n)) ≤ w·C*. (The first step uses w ≥ 1, so g(n) ≤ w·g(n).)

d.G is chosen before n, so f(G) ≤ f(n). Also h(G) = 0, so f(G) = g(G) = C.

e.Therefore C = f(G) ≤ f(n) ≤ w·C*.

Why accept a suboptimal answer? Speed and memory. A larger w makes the search more greedy, so it expands far fewer nodes. You get a solution that is guaranteed to be within a factor w of optimal, much faster. This is useful when the problem is huge, time is limited, or “good enough” is fine (e.g. robot path planning).

### B4. Hand trace: Bartica to Ituni
Straight-line distances to Ituni (km) used for A*

| Town | h (km) |
|:---|---:|
| Ituni | 0.0 |
| Kwakwani | 36.7 |
| Linden | 53.5 |
| Mahdia | 102.6 |
| Bartica | 105.1 |
| Kurupukari | 106.7 |
| Timehri | 108.8 |
| Soesdyke | 112.5 |
| New Amsterdam | 113.8 |
| Rosignol | 114.6 |
| Corriverton | 130.2 |
| Diamond | 131.6 |
| Mahaica | 133.1 |
| Ogle | 138.3 |
| Georgetown | 141.8 |
| Vreed en Hoop | 142.2 |
| Parika | 148.7 |
| Anna Regina | 193.9 |
| Annai | 200.5 |
| Charity | 210.6 |
| Lethem | 294.4 |

## BFS (expansion order, fringe at each step)

| Step | Expand | Fringe after expanding |
|:---:|:---|:---|
| 1 | Bartica | Mahdia, Parika |
| 2 | Mahdia | Parika, Linden |
| 3 | Parika | Linden, Anna Regina, Vreed en Hoop |
| 4 | Linden | Anna Regina, Vreed en Hoop, Ituni (generated, so BFS stops) |

**UCS** (expansion order, fringe and g at each step):
=== UCS ===
 1. expand Bartica (g=0.0)
      fringe: Parika(235.2), Mahdia(265.8)
 2. expand Parika (g=235.2)
      fringe: Mahdia(265.8), Vreed en Hoop(266.1), Anna Regina(293.3)
 3. expand Mahdia (g=265.8)
      fringe: Vreed en Hoop(266.1), Anna Regina(293.3), Linden(461.3)
 4. expand Vreed en Hoop (g=266.1)
      fringe: Georgetown(281.6), Anna Regina(293.3), Linden(461.3)
 5. expand Georgetown (g=281.6)
      fringe: Ogle(288.6), Anna Regina(293.3), Diamond(294.6), Timehri(325.4), Linden(461.3)
 6. expand Ogle (g=288.6)
      fringe: Anna Regina(293.3), Diamond(294.6), Mahaica(321.6), Timehri(325.4), Linden(461.3)
 7. expand Anna Regina (g=293.3)
      fringe: Diamond(294.6), Charity(318.5), Mahaica(321.6), Timehri(325.4), Linden(461.3)
 8. expand Diamond (g=294.6)
      fringe: Soesdyke(315.7), Charity(318.5), Mahaica(321.6), Timehri(325.4), Linden(461.3)
 9. expand Soesdyke (g=315.7)
      fringe: Charity(318.5), Mahaica(321.6), Timehri(324.2), Linden(391.0)
10. expand Charity (g=318.5)
      fringe: Mahaica(321.6), Timehri(324.2), Linden(391.0)
11. expand Mahaica (g=321.6)
      fringe: Timehri(324.2), Rosignol(387.2), Linden(391.0)
12. expand Timehri (g=324.2)
      fringe: Rosignol(387.2), Linden(391.0)
13. expand Rosignol (g=387.2)
      fringe: Linden(391.0), New Amsterdam(399.7)
14. expand Linden (g=391.0)
      fringe: New Amsterdam(399.7), Ituni(456.8), Kwakwani(498.2), Kurupukari(617.8)
15. expand New Amsterdam (g=399.7)
      fringe: Ituni(456.8), Corriverton(473.9), Kwakwani(498.2), Kurupukari(617.8)
16. expand Ituni (g=456.8)  <- GOAL, stop

**A\*** (expansion order, fringe with g, h, f at each step):
=== A* ===
 1. expand Bartica (g=0.0, h=105.1, f=105.1)
      fringe: Mahdia(g=265.8, h=102.6, f=368.4), Parika(g=235.2, h=148.7, f=383.9)
 2. expand Mahdia (g=265.8, h=102.6, f=368.4)
      fringe: Parika(g=235.2, h=148.7, f=383.9), Linden(g=461.3, h=53.5, f=514.8)
 3. expand Parika (g=235.2, h=148.7, f=383.9)
      fringe: Vreed en Hoop(g=266.1, h=142.2, f=408.3), Anna Regina(g=293.3, h=193.9, f=487.2), Linden(g=461.3, h=53.5, f=514.8)
 4. expand Vreed en Hoop (g=266.1, h=142.2, f=408.3)
      fringe: Georgetown(g=281.6, h=141.8, f=423.4), Anna Regina(g=293.3, h=193.9, f=487.2), Linden(g=461.3, h=53.5, f=514.8)
 5. expand Georgetown (g=281.6, h=141.8, f=423.4)
      fringe: Diamond(g=294.6, h=131.6, f=426.2), Ogle(g=288.6, h=138.3, f=426.9), Timehri(g=325.4, h=108.8, f=434.2), Anna Regina(g=293.3, h=193.9, f=487.2), Linden(g=461.3, h=53.5, f=514.8)
 6. expand Diamond (g=294.6, h=131.6, f=426.2)
      fringe: Ogle(g=288.6, h=138.3, f=426.9), Soesdyke(g=315.7, h=112.5, f=428.2), Timehri(g=325.4, h=108.8, f=434.2), Anna Regina(g=293.3, h=193.9, f=487.2), Linden(g=461.3, h=53.5, f=514.8)
 7. expand Ogle (g=288.6, h=138.3, f=426.9)
      fringe: Soesdyke(g=315.7, h=112.5, f=428.2), Timehri(g=325.4, h=108.8, f=434.2), Mahaica(g=321.6, h=133.1, f=454.7), Anna Regina(g=293.3, h=193.9, f=487.2), Linden(g=461.3, h=53.5, f=514.8)
 8. expand Soesdyke (g=315.7, h=112.5, f=428.2)
      fringe: Timehri(g=324.2, h=108.8, f=433.0), Linden(g=391.0, h=53.5, f=444.5), Mahaica(g=321.6, h=133.1, f=454.7), Anna Regina(g=293.3, h=193.9, f=487.2)
 9. expand Timehri (g=324.2, h=108.8, f=433.0)
      fringe: Linden(g=391.0, h=53.5, f=444.5), Mahaica(g=321.6, h=133.1, f=454.7), Anna Regina(g=293.3, h=193.9, f=487.2)
10. expand Linden (g=391.0, h=53.5, f=444.5)
      fringe: Mahaica(g=321.6, h=133.1, f=454.7), Ituni(g=456.8, h=0.0, f=456.8), Anna Regina(g=293.3, h=193.9, f=487.2), Kwakwani(g=498.2, h=36.7, f=534.9), Kurupukari(g=617.8, h=106.7, f=724.5)
11. expand Mahaica (g=321.6, h=133.1, f=454.7)
      fringe: Ituni(g=456.8, h=0.0, f=456.8), Anna Regina(g=293.3, h=193.9, f=487.2), Rosignol(g=387.2, h=114.6, f=501.8), Kwakwani(g=498.2, h=36.7, f=534.9), Kurupukari(g=617.8, h=106.7, f=724.5)
12. expand Ituni (g=456.8)  <- GOAL, stop

| Algorithm | Route | Cost (km) | Optimal? | Nodes expanded |
|:---|:---|---:|:---:|---:|
| BFS | Bartica → Mahdia → Linden → Ituni | 527.1 | No | 4 |
| UCS | Bartica → Parika → Vreed en Hoop → Georgetown → Diamond → Soesdyke → Linden → Ituni | 456.8 | Yes | 15 |
| A* | Bartica → Parika → Vreed en Hoop → Georgetown → Diamond → Soesdyke → Linden → Ituni | 456.8 | Yes | 11 |

**Conclusion:** 
The Mahdia route (Bartica → Mahdia → Linden → Ituni, 527.1 km) was not optimal because it costs more kilometres, even though it has fewer roads. Reaching Linden via Mahdia costs 265.8 + 195.5 = 461.3 km, while going via Parika, Vreed en Hoop, Georgetown, Diamond and Soesdyke costs only 391.0 km, which is 70.3 km less. Both routes then use the same 65.8 km Linden → Ituni road, so the whole difference comes from how they reach Linden (456.8 km in total for the Parika route). BFS picks the Mahdia route because it counts roads, not distance, and 3 roads beats 7. UCS and A* add up the kilometres, so they replace Linden’s cost of 461.3 with 391.0 when Soesdyke is expanded, and they return the cheaper route. The Parika route is also faster in time (about 8.7 hours versus 13.6 hours), so it is better whether you measure in km or hours.

**Why A Star expanded fewer (or not fewer) nodes than UCS:**

A* expanded fewer nodes than UCS (11 versus 15) because it uses the straight-line distance to Ituni to push unpromising towns to the back of the fringe, while UCS has no idea where Ituni is. Both found the same optimal route of 456.8 km.

UCS ranks the fringe by g(n) alone, so it expands any town that is cheap to reach from Bartica, even if it lies in the wrong direction. It has to expand every node with g < 456.8 before Ituni gets to the front. A* ranks the fringe by f(n) = g(n) + h(n), so a town that is cheap to reach but far from Ituni gets a large f and just sits in the fringe. Here is what that did to four towns:

| Node | UCS | A* |
|:---|:---|:---|
| Anna Regina | Expanded at step 7 (g = 293.3) | Stays in the fringe with f = 293.3 + 193.9 = 487.2 and is never expanded |
| Charity | Expanded at step 10 (g = 318.5) | Never generated, since its parent Anna Regina is never expanded |
| Rosignol | Expanded at step 13 (g = 387.2) | Enters the fringe with f = 387.2 + 114.6 = 501.8 and is never expanded |
| New Amsterdam | Expanded at step 15 (g = 399.7) | Never generated, since its parent Rosignol is never expanded |

A* puts Ituni into the fringe at step 10 with f = 456.8. Once Mahaica is expanded at step 11 (f = 454.7), Ituni has the lowest f in the fringe, because every other entry has f ≥ 487.2. A* picks it at step 12 and stops. Since h never overestimates the true remaining cost, no cheaper route can exist, so the answer is optimal.

The saving is only 4 nodes because straight-line distance can't see the road layout. Ogle, Timehri and Mahaica still have f below 456.8, so A* expands them even though they aren't on the final route. Also, the way out of Bartica is forced through one corridor (Parika → Georgetown → Soesdyke → Linden), so there isn't much for h to prune.

---

## Part C: Route Planning in Guyana

### Autograder output

Paste the final lines of `python autograder.py --no-graphics`:

```
Provisional grades
==================
Question q1: 3/3 
Question q2: 3/3 
Question q3: 3/3 
Question q4: 3/3 
Question q5: 3/3 
Question q6: 3/3 
Question q7: 5/4 
Question q8: 3/3 
Question q9: 4/4 
Question q10: 4/4 
------------------
Total: 34/33
```

### Heuristic for the "hours" cost mode

In `"hours"` mode, h(n) = (straight-line distance from n to the goal in km) ÷ v_max, where v_max is the highest average speed of any road in the network. I compute v_max as the largest value of `km / hours` over all roads in the data file. It is **71.7 km/h**, on the Soesdyke–Linden road (75.3 km in 1.05 h).

**Why it is admissible:** h must never exceed the true travel time of the best route, and two facts guarantee that.

1. **Distance:** the straight-line (great-circle) distance is the shortest possible distance between two points, so any real route covers at least that many km.
2. **Speed:** no road in the network is faster than v_max, so no route can travel faster than 71.7 km/h on any leg. Ferry legs are much slower, which only makes the real time longer.

So the true time on any route is at least (distance of the route) ÷ v_max, which is at least (straight-line distance) ÷ v_max = h(n). The estimate therefore never overestimates. It is also not very tight, because it assumes the whole trip is made at the fastest road speed with no ferries or detours, so A* will expand more nodes in `"hours"` mode than in `"km"` mode.

### C3.1 Results table

| Start → Goal | Mode | Algorithm | Cost | Expanded | ms | Route |
|:---|:---|:---|---:|---:|---:|:---|
| Bartica → Ituni | km | BFS | 527.1 | 7 | 0.02 | Bartica → Mahdia → Linden → Ituni |
| Bartica → Ituni | km | DFS | 558.0 | 16 | 0.02 | Bartica → Parika → Vreed en Hoop → Georgetown → Timehri → Soesdyke → Linden → Kwakwani → Ituni |
| Bartica → Ituni | km | UCS | 456.8 | 15 | 0.03 | Bartica → Parika → Vreed en Hoop → Georgetown → Diamond → Soesdyke → Linden → Ituni |
| Bartica → Ituni | km | Greedy | 527.1 | 3 | 0.03 | Bartica → Mahdia → Linden → Ituni |
| Bartica → Ituni | km | A* | 456.8 | 11 | 0.04 | Bartica → Parika → Vreed en Hoop → Georgetown → Diamond → Soesdyke → Linden → Ituni |
| Georgetown → Lethem | km | BFS | 555.6 | 20 | 0.06 | Georgetown → Diamond → Soesdyke → Linden → Kurupukari → Annai → Lethem |
| Georgetown → Lethem | km | DFS | 573.8 | 20 | 0.02 | Georgetown → Timehri → Soesdyke → Linden → Kurupukari → Annai → Lethem |
| Georgetown → Lethem | km | UCS | 555.6 | 20 | 0.12 | Georgetown → Diamond → Soesdyke → Linden → Kurupukari → Annai → Lethem |
| Georgetown → Lethem | km | Greedy | 573.8 | 6 | 0.05 | Georgetown → Timehri → Soesdyke → Linden → Kurupukari → Annai → Lethem |
| Georgetown → Lethem | km | A* | 555.6 | 16 | 0.04 | Georgetown → Diamond → Soesdyke → Linden → Kurupukari → Annai → Lethem |

**Reading the table**

- **Optimal:** UCS and A* return the cheapest route in both queries (456.8 km and 555.6 km). BFS is optimal only for Georgetown → Lethem, and only by luck, since it counts roads rather than kilometres.
- **Greedy:** it expands the fewest nodes (3 and 6) but is not optimal in either query, because it follows h and ignores the cost so far. On Bartica → Ituni it picks Mahdia (h = 102.6) over Parika (h = 148.7) and ends up 70.3 km worse.
- **A\* versus UCS:** A* expands fewer nodes at the same optimal cost (11 vs 15, and 16 vs 20), because h pushes towns that lead away from the goal to the back of the fringe.
- **DFS:** it returns a valid route, but not a good one (558.0 km and 573.8 km), because it follows whichever branch it reaches first.
- **Runtimes:** the times (fractions of a millisecond) are too small and noisy to compare. Use the expanded-node counts for comparing algorithms.

### Q10: An admissible heuristic for both cost modes

**Definition.** Let d(n) be the straight-line (haversine) distance from town n to the goal, and let v_max be the highest average speed of any road in the network, computed from the data as the maximum of km / hours over all roads. Here v_max = 71.7 km/h (Soesdyke–Linden: 75.3 km in 1.05 h).

| Cost mode | h(n) |
|:---|:---|
| `km` | d(n) |
| `hours` | d(n) / v_max |

**Admissible.** In `km` mode, any route from n to the goal is at least as long as the straight line, since the great-circle path is the shortest possible, so h(n) ≤ h*(n). In `hours` mode, a route of length L km cannot be driven faster than v_max on any leg, so its time is at least L / v_max. Because L ≥ d(n), the true time is at least d(n) / v_max = h(n). Ferries and detours are slower than v_max, which only makes the true time larger.

**Consistent.** For every road (n, n') with cost c(n, n'):

- *km mode:* the triangle inequality gives d(n) ≤ d(n, n') + d(n'), and the straight line between two towns is no longer than the road between them, so d(n, n') ≤ km(n, n'). Hence h(n) ≤ c(n, n') + h(n').
- *hours mode:* divide the same inequality by v_max. Then d(n, n') / v_max ≤ km(n, n') / v_max ≤ hours(n, n'), because the road's own speed km / hours is at most v_max. Hence h(n) ≤ c(n, n') + h(n').

Consistency also gives h(goal) = 0 and admissibility, and it means A* graph search never needs to re-expand a town, so its solutions are optimal.

**Non-trivial.** h(n) > 0 for every town other than the goal, so it is not zero everywhere.

**Why not a tighter speed?** Using a slower speed (e.g. the average speed) could overestimate the time on the fastest roads, which would break admissibility. v_max is the largest speed that is always safe.

**Limitation.** In `hours` mode the heuristic is weak, because it assumes the whole journey is made at the best road speed, with no ferries. Ferry legs are far slower (for example Parika → Anna Regina takes 5.01 h for 58.1 km), so A* may expand more nodes in `hours` mode than in `km` mode, although still no more than UCS.

**Check.** I tested the heuristic on all 21 towns as goals in both modes: it never overestimated the optimal cost, satisfied the consistency inequality on every road, and A* matched UCS's cost on every start/goal pair.

### C3.2 Analysis

**1. Results Table**

| Start > Goal | Mode | Algorithm | Cost | Expanded | ms | Route |
|:---|:---|:---|---:|---:|---:|:---|
| Bartica > Ituni | km | BFS | 527.1 | 7 | 0.00 | Bartica > Mahdia > Linden > Ituni |
| Bartica > Ituni | km | DFS | 558.0 | 16 | 0.01 | Bartica > Parika > Vreed en Hoop > Georgetown > Timehri > Soesdyke > Linden > Kwakwani > Ituni |
| Bartica > Ituni | km | UCS | 456.8 | 15 | 0.01 | Bartica > Parika > Vreed en Hoop > Georgetown > Diamond > Soesdyke > Linden > Ituni |
| Bartica > Ituni | km | Greedy | 527.1 | 3 | 0.01 | Bartica > Mahdia > Linden > Ituni |
| Bartica > Ituni | km | A* | 456.8 | 11 | 0.02 | Bartica > Parika > Vreed en Hoop > Georgetown > Diamond > Soesdyke > Linden > Ituni |
| Bartica > Ituni | hours | BFS | 13.57 | 7 | 0.00 | Bartica > Mahdia > Linden > Ituni |
| Bartica > Ituni | hours | DFS | 11.42 | 16 | 0.01 | Bartica > Parika > Vreed en Hoop > Georgetown > Timehri > Soesdyke > Linden > Kwakwani > Ituni |
| Bartica > Ituni | hours | UCS | 8.66 | 14 | 0.01 | Bartica > Parika > Vreed en Hoop > Georgetown > Diamond > Soesdyke > Linden > Ituni |
| Bartica > Ituni | hours | Greedy | 13.57 | 3 | 0.01 | Bartica > Mahdia > Linden > Ituni |
| Bartica > Ituni | hours | A* | 8.66 | 11 | 0.02 | Bartica > Parika > Vreed en Hoop > Georgetown > Diamond > Soesdyke > Linden > Ituni |
| Georgetown > Lethem | km | BFS | 555.6 | 20 | 0.01 | Georgetown > Diamond > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | km | DFS | 573.8 | 20 | 0.01 | Georgetown > Timehri > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | km | UCS | 555.6 | 20 | 0.01 | Georgetown > Diamond > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | km | Greedy | 573.8 | 6 | 0.01 | Georgetown > Timehri > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | km | A* | 555.6 | 16 | 0.03 | Georgetown > Diamond > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | hours | BFS | 13.05 | 20 | 0.01 | Georgetown > Diamond > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | hours | DFS | 13.48 | 20 | 0.01 | Georgetown > Timehri > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | hours | UCS | 13.05 | 20 | 0.01 | Georgetown > Diamond > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | hours | Greedy | 13.48 | 6 | 0.02 | Georgetown > Timehri > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Georgetown > Lethem | hours | A* | 13.05 | 20 | 0.03 | Georgetown > Diamond > Soesdyke > Linden > Kurupukari > Annai > Lethem |
| Charity > Corriverton | km | BFS | 322.0 | 20 | 0.01 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Ogle > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | km | DFS | 1076.5 | 15 | 0.01 | Charity > Anna Regina > Parika > Bartica > Mahdia > Linden > Soesdyke > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | km | UCS | 322.0 | 15 | 0.01 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Ogle > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | km | Greedy | 403.4 | 10 | 0.02 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Timehri > Soesdyke > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | km | A* | 322.0 | 12 | 0.02 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Ogle > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | hours | BFS | 9.52 | 20 | 0.01 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Ogle > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | hours | DFS | 26.57 | 15 | 0.01 | Charity > Anna Regina > Parika > Bartica > Mahdia > Linden > Soesdyke > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | hours | UCS | 9.52 | 13 | 0.01 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Ogle > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | hours | Greedy | 10.93 | 10 | 0.02 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Timehri > Soesdyke > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Charity > Corriverton | hours | A* | 9.52 | 12 | 0.02 | Charity > Anna Regina > Parika > Vreed en Hoop > Georgetown > Ogle > Mahaica > Rosignol > New Amsterdam > Corriverton |
| Corriverton > Ituni | km | BFS | 362.5 | 11 | 0.01 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Ituni |
| Corriverton > Ituni | km | DFS | 445.5 | 7 | 0.00 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Kwakwani > Ituni |
| Corriverton > Ituni | km | UCS | 362.0 | 14 | 0.01 | Corriverton > New Amsterdam > Rosignol > Mahaica > Ogle > Diamond > Soesdyke > Linden > Ituni |
| Corriverton > Ituni | km | Greedy | 362.5 | 6 | 0.01 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Ituni |
| Corriverton > Ituni | km | A* | 362.0 | 11 | 0.02 | Corriverton > New Amsterdam > Rosignol > Mahaica > Ogle > Diamond > Soesdyke > Linden > Ituni |
| Corriverton > Ituni | hours | BFS | 6.39 | 11 | 0.01 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Ituni |
| Corriverton > Ituni | hours | DFS | 8.72 | 7 | 0.01 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Kwakwani > Ituni |
| Corriverton > Ituni | hours | UCS | 6.39 | 12 | 0.01 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Ituni |
| Corriverton > Ituni | hours | Greedy | 6.39 | 6 | 0.01 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Ituni |
| Corriverton > Ituni | hours | A* | 6.39 | 12 | 0.03 | Corriverton > New Amsterdam > Rosignol > Mahaica > Soesdyke > Linden > Ituni |

**2. Which algorithms were optimal, and when?** UCS and A* were optimal on all 8 queries, as expected for non-negative step costs and an admissible, consistent heuristic. BFS was optimal on 5 of 8 (Georgetown → Lethem in both modes, Charity → Corriverton in both modes, and Corriverton → Ituni in hours). It is only optimal by luck, when the route with the fewest roads happens to be the cheapest: BFS counts roads, not kilometres or hours. DFS was never optimal and can be very bad (1076.5 km versus 322.0 km on Charity → Corriverton, because it wandered through Bartica and Mahdia).

**When did greedy search fail, and why?** Greedy was optimal on only 1 of 8 queries (Corriverton → Ituni in hours). It ranks towns by h(n) alone and ignores the cost already spent, so it follows towns that look close on the map but are reached by long roads.
- *Bartica → Ituni:* from Bartica it picks Mahdia (h = 102.6 km) over Parika (h = 148.7 km). The Mahdia route costs 527.1 km versus 456.8 km (15% worse), and 13.57 h versus 8.66 h (57% worse), because both Mahdia roads are very long ferry or road legs.
- *Georgetown → Lethem:* it picks the direct Georgetown → Timehri road (43.8 km), which looks closer to Lethem, rather than going via Diamond (13.0 + 21.1 km to Soesdyke). The result is 18.2 km worse (573.8 versus 555.6).
- *Charity → Corriverton:* it reaches Mahaica via Timehri and Soesdyke (121.4 km) instead of via Ogle (40.0 km), which costs 81.4 km extra (403.4 versus 322.0).

Straight-line distance cannot see that a town which looks closer may only be reachable by a long road.

**How much did the heuristic reduce expansions for A\* compared with UCS?**

| Query | UCS | A* | Reduction |
|:---|---:|---:|---:|
| Bartica → Ituni, km | 15 | 11 | 27% |
| Bartica → Ituni, hours | 14 | 11 | 21% |
| Georgetown → Lethem, km | 20 | 16 | 20% |
| Georgetown → Lethem, hours | 20 | 20 | 0% |
| Charity → Corriverton, km | 15 | 12 | 20% |
| Charity → Corriverton, hours | 13 | 12 | 8% |
| Corriverton → Ituni, km | 14 | 11 | 21% |
| Corriverton → Ituni, hours | 12 | 12 | 0% |

A* never expanded more nodes than UCS. In `km` mode it saved about 20–27%. In `hours` mode the saving was much smaller (0–21%). The reason is that h = straight-line distance ÷ v_max, with v_max = 71.7 km/h, assumes the whole trip is driven at the fastest road speed. Real routes include slow ferries (for example Parika–Anna Regina: 58.1 km in 5.01 h, about 12 km/h), so h underestimates by a large factor and gets close to a zero heuristic, which makes A* behave like UCS.

**Did the best route change between `km` and `hours`?** Yes, but not because of ferries. On Corriverton → Ituni the best route in km goes Mahaica → Ogle → Diamond → Soesdyke (68.6 km, 362.0 km total), but in hours it takes the direct Mahaica → Soesdyke road (69.1 km but 1.20 h instead of 1.43 h), giving 6.39 h. The direct road is 0.5 km longer but 0.23 h faster. Georgetown → Timehri behaves the same way (direct road is faster but longer than the route via Diamond and Soesdyke). For the ferry routes, the best route was the same in both modes:
- Bartica reaches the coast either by the single Bartica–Parika ferry (235.2 km, 4.53 h) or by two ferries via Mahdia (461.3 km to Linden, 11.9 h), so the Parika route wins in both km and hours.
- Charity and Lethem are only reachable through one ferry each (Parika–Anna Regina and Kurupukari–Annai), so no alternative exists.

Ferries do change the *size* of the numbers, though. Charity → Corriverton is 322.0 km but takes 9.52 h, an average of only 34 km/h, because the 5.01 h ferry accounts for more than half of the time.

**Runtime.** All runs finished in under 0.03 ms, so differences are tiny and partly timer noise. Even so, A* was consistently the slowest (0.02–0.03 ms) even though it expanded fewer nodes than UCS (0.01 ms). The reason is that A* calls the heuristic for every successor, and each call computes a haversine distance (several trig functions), while UCS only adds numbers. On this 21-town map, the saving in expansions is too small to pay for the more expensive work per node. A* would only win on runtime on a much larger map, or with a heuristic that is cheaper to compute. This is why nodes expanded, not milliseconds, is the more reliable measure for comparing the algorithms here.


### C3.3 Formulation critique

Two things real travel in Guyana depends on that this model ignores:

1. **Ferry schedules and waiting time.** The model treats a ferry as a road with a fixed time, as if one is always waiting at the dock. In reality ferries run at certain times, so a traveller may wait for hours.
2. **Rainy-season road conditions** (for example the Linden–Lethem road surface). The model uses one fixed travel time per road, but in the rainy season some roads are slow or impassable.

**Changing the model for ferry schedules.**
Make time part of the state. A state becomes (town, time of day), for example in 15-minute slots. Actions become "drive or board the ferry to a neighbour" and "wait 15 minutes". The step cost of a ferry road becomes the wait until the next departure plus the crossing time, and ordinary roads keep their normal time. The size of the search space grows from |S| = 21 towns to about 21 × T states. With 96 slots per day that is 2,016 states, and about 4,032 for a two-day horizon. The branching factor also grows by one because of the "wait" action. The straight-line heuristic stays admissible, since waiting can only make the true time longer, but A* will expand more nodes because h now ignores waiting entirely. For the rainy-season issue, the state space would stay the same size and only the costs would change (a season parameter would multiply the time on affected roads).

---

## Part D: Search vs. LLMs

### D1. Transcripts

For each instance: model and version, exact prompt, full response.

**All 3 Queries were Aggregated  into one Plot**
![alt text](src/nodes_expanded_all.png)

**Model:** Copilot(Auto)  **Version**: 158.0.4370.33


**Prompt:** With data given, use BFS, DFS, UCS, Greedy Search and, A star algorithms to find best routes from Bartica to Ituni, Georgetown to Lethem, Charity to Corriverton and, Corriverton to Ituni. Display your results on a bar chart showing amount of nodes expanded.

**Response:**
Using the road network from guyana_roads, I compared BFS, DFS, Uniform Cost Search (UCS), Greedy Best-First Search, and A* for the four requested origin-destination pairs. Straight-line distance derived from the town coordinates was used as the heuristic for Greedy Search and A*.

![alt text](image.png)

**Observations**

Greedy Best-First Search expanded the fewest nodes in all four cases because it aggressively follows the heuristic toward the goal.
BFS generally expanded the most nodes because it explores broadly level-by-level without considering distance.
UCS often expanded a similar or larger number of nodes than BFS because it guarantees least-cost routes based on road distance.
A* reduced expansions compared with UCS in most cases by combining path cost and heuristic guidance.
DFS sometimes performed well in terms of node expansions, but its performance depends heavily on the order in which neighbors are explored and does not guarantee an optimal route.

The chart visualizes the relative search effort (measured as nodes expanded) for each algorithm across the four route-finding problems.

#### Instance 1

#### Instance 2

#### Instance 3

#### Instance 4 (8-puzzle)
A random puzzle:

| 1 | 6 | 2 |

| 3 | 4 |   |

| 7 | 8 | 5 |

BFS found a path of 11 moves: ['down', 'left', 'up', 'up', 'left', 'down', 'right', 'down', 'left', 'up', 'up']
After 1 move: down

| 1 | 6 | 2 |

| 3 | 4 | 5 |

| 7 | 8 |   |

Press return for the next state...
After 2 moves: left

| 1 | 6 | 2 |

| 3 | 4 | 5 |

| 7 |   | 8 |

Press return for the next state...
After 3 moves: up

| 1 | 6 | 2 |

| 3 |   | 5 |

| 7 | 4 | 8 |

Press return for the next state...
After 4 moves: up

| 1 |   | 2 |

| 3 | 6 | 5 |

| 7 | 4 | 8 |

Press return for the next state...
After 5 moves: left

|   | 1 | 2 |

| 3 | 6 | 5 |

| 7 | 4 | 8 |

Press return for the next state...
After 6 moves: down

| 3 | 1 | 2 |

|   | 6 | 5 |

| 7 | 4 | 8 |

Press return for the next state...
After 7 moves: right

| 3 | 1 | 2 |

| 6 |   | 5 |

| 7 | 4 | 8 |

Press return for the next state...
After 8 moves: down

| 3 | 1 | 2 |

| 6 | 4 | 5 |

| 7 |   | 8 |

Press return for the next state...
After 9 moves: left

| 3 | 1 | 2 |

| 6 | 4 | 5 |

|   | 7 | 8 |

Press return for the next state...
After 10 moves: 

| 3 | 1 | 2 |

|   | 4 | 5 |

| 6 | 7 | 8 |

Press return for the next state...
After 11 moves: up

|   | 1 | 2 |

| 3 | 4 | 5 |

| 6 | 7 | 8 |

Press return for the next state...

**LLM Instance**

**Model:** Copilot(Auto)  **Version**: 158.0.4370.33


**Prompt:** A random puzzle:

| 1 | 6 | 2 |

| 3 | 4 |   |

| 7 | 8 | 5 |

Find the solution to this 8puzzle using BFS algorithm, show the moves made and amount.

**Response:**

Assume the goal state is the standard 8-puzzle goal:

1 2 3
4 5 6
7 8 _


Initial state:

1 6 2
3 4 _
7 8 5


Before solving, we check whether the puzzle is solvable.

Step 1: Count Inversions

Ignoring the blank, the sequence is:

1, 6, 2, 3, 4, 7, 8, 5


Inversions:

6 > 2, 3, 4, 5 → 4 inversions
7 > 5 → 1 inversion
8 > 5 → 1 inversion

Total inversions = 6

For a 3×3 puzzle (odd width), a state is solvable if the number of inversions is even.

Since 6 is even, the puzzle is solvable.

BFS Solution

Using Breadth-First Search, the shortest solution found is:

Move #	Move
1	Down
2	Left
3	Up
4	Left
5	Down
6	Right
7	Up
8	Right
9	Down

## State Sequence

 **Initial State**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 3 | 4 | _ |
| 7 | 8 | 5 |

**Move 1: Down**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 3 | 4 | 5 |
| 7 | 8 | _ |

**Move 2: Left**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 3 | 4 | 5 |
| 7 | _ | 8 |

**Move 3: Up**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 3 | _ | 5 |
| 7 | 4 | 8 |

**Move 4: Left**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| _ | 3 | 5 |
| 7 | 4 | 8 |

**Move 5: Down**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 7 | 3 | 5 |
| _ | 4 | 8 |

**Move 6: Right**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 7 | 3 | 5 |
| 4 | _ | 8 |

**Move 7: Up**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 7 | _ | 5 |
| 4 | 3 | 8 |

**Move 8: Right**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 7 | 5 | _ |
| 4 | 3 | 8 |

**Move 9: Down**

|   |   |   |
|---|---|---|
| 1 | 6 | 2 |
| 7 | 5 | 8 |
| 4 | 3 | _ |

**Move Sequence**

`Down → Left → Up → Left → Down → Right → Up → Right → Down`

**Total Moves**

`9 moves`


At this point BFS would continue searching because this is not yet the standard goal state.

**Important Observation**

The configuration you provided is solvable, but a complete BFS search is required to determine the exact minimum-length path to the standard goal configuration. The sequence above illustrates the first valid level-expanding moves, but not necessarily the final optimal solution.

For a homework or AI assignment, BFS statistics are typically reported as:

Initial state: 1 6 2 / 3 4 _ / 7 8 5
Goal state: 1 2 3 / 4 5 6 / 7 8 _
Solvable: Yes
Search strategy: Breadth-First Search
Minimum number of moves: requires full state-space BFS computation

If you'd like, I can also compute the complete optimal BFS solution path, number of nodes expanded, frontier size, and search tree depth for this puzzle.

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
