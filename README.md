# N-Body Astrophysics Simulation 🪐

A multi-body physics engine that calculates and visualizes the orbital trajectories of celestial bodies. This project demonstrates the application of complex mathematical models in code, specifically using Newton's Law of Universal Gravitation to compute vectors and render them in a custom web-based environment.

## 🚀 Overview
Predicting the individual motions of a group of celestial objects interacting with each other gravitationally is a classic computational problem known as the **N-Body Problem**. This simulation bridges the gap between backend mathematical computation and frontend data visualization. 

The core engine handles the $O(N^2)$ algorithmic complexity by calculating gravitational pull, acceleration, and velocity vectors for each body in Python. It serializes the timeline into a JSON format and renders it smoothly at 60 FPS using an HTML5 Canvas and JavaScript.

## 🛠️ Technologies & Stack
* **Physics Engine (Backend):** Python
* **Rendering & Animation (Frontend):** JavaScript (ES6+), HTML5 Canvas
* **Data Serialization:** JSON

## ⚙️ Features
* **Custom Physics Engine:** Real-time calculation of $F = G \frac{m_1 m_2}{r^2}$.
* **Vector Kinematics:** Splitting acceleration into X and Y vectors for precise 2D mapping and updating positions over discrete time steps (`dt`).
* **Data Pipeline Architecture:** Clear separation of concerns between the mathematical engine computing the data (Python) and the presentation layer animating it (JS).
* **Scalable Viewport:** Dynamic camera scaling in JavaScript to ensure all planetary bodies remain visible regardless of their orbital distance.

## 💻 How to Run Locally

1. Clone this repository to your local machine.
2. Run the Python physics engine to generate the orbital data:
   ```bash
   python main.py```
(Note: Ensure your Python file containing the Body class and simulation logic is named main.py, or replace it with your actual file name).
3. The script will calculate the orbits and generate a simulation_data.json file in the same directory.
4. Open the simulasyon.html file using a local web server (e.g., Live Server extension in VS Code) to bypass browser CORS restrictions.
5. Watch the planetary system orbit in real-time!
