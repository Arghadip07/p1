# Smart City Pathfinding Visualizer 🚦🗺️

A sophisticated, highly modular A* (A-Star) Pathfinding visualization tool built in Python and Pygame. This project simulates real-time urban navigation routing, operating similarly to modern GPS systems. 

## 🚀 Features
* **8-Way Directional Movement**: Optimised Euclidean heuristic algorithms allow diagonal traversal.
* **Dynamic Urban Constraints**: 
  * 🏢 **Buildings (White):** Impassable walls.
  * 🚧 **Rough Lanes (Brown):** High traversal cost (x5).
  * 🚙 **Traffic Jams (Blue):** Extreme congestion cost (x10).
  * 🚦 **Dynamic Traffic Signals (Red/Green):** Nodes that actively toggle between passable and impassable states in real time.
* **Resource Management**: The algorithm operates on a `MAX_FUEL` constraint. If a route requires too many detours or rough roads, the path fails.
* **Instant GPS Mode**: Calculates the absolute fastest route in milliseconds, dropping a futuristic footprint (Pink/Purple) of the nodes it scanned.
* **Map Auto-Generation**: Press a single key to instantly build a completely random city block layout.

## 🛠️ Installation
1. Clone the repository: `git clone <your-repo-link>`
2. Install dependencies: `pip install pygame`
3. Run the application: `python main.py`

## 🎮 Controls
* **`G`** - Auto-generate a random dynamic city layout.
* **`Spacebar`** - Run the A* algorithm instantly to find the best route.
* **`C`** - Clear the grid entirely.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page or fork the repository to add your own heuristics or terrain types.