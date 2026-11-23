from guyanaRoutes import RoadMap, haversineKm

GOAL = "Ituni"

roadMap = RoadMap()
goal_coord = roadMap.coords[GOAL]

print(f"{'Town':<15}{'h (km)':>8}")
for town in roadMap.towns():                      # towns() returns them sorted
    h = haversineKm(roadMap.coords[town], goal_coord)
    print(f"{town:<15}{h:>8.1f}")