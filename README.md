# N-Body Astrophysics Simulation 🪐

A multi-body physics engine that calculates and visualizes the orbital trajectories of celestial bodies. This project demonstrates the application of mathematical models in code, specifically using Newton's Law of Universal Gravitation to compute vectors and render them in a custom web-based environment.

## 🚀 Overview
Predicting the individual motions of a group of celestial objects interacting with each other gravitationally is a classic computational problem (The N-Body Problem). This simulation bridges the gap between backend mathematical computation and frontend data visualization. 

The core engine handles the $O(N^2)$ algorithmic complexity by calculating gravitational pull, acceleration, and velocity vectors for each body in Python, serializing the timeline into a JSON format, and rendering it smoothly at 60 FPS using an HTML5 Canvas and JavaScript.

## 🛠️ Technologies & Stack
* **Physics Engine (Backend):** Python
* **Rendering & Animation (Frontend):** JavaScript (ES6+), HTML5 Canvas
* **Data Serialization:** JSON

## ⚙️ Features
* **Custom Physics Engine:** Real-time calculation of $F = G \frac{m_1 m_2}{r^2}$.
* **Vector Math:** Splitting acceleration into X and Y vectors for precise 2D mapping.
* **Microservice Approach:** Separation of concerns between the mathematical engine (Python) and the presentation layer (JS).
* **Scalable Viewport:** Dynamic camera scaling to ensure all planetary bodies remain visible regardless of orbital distance.

## 💻 How to Run Locally
1. Clone this repository to your local machine.
2. Run the Python physics engine to generate the orbital data:
   ```bash
   python trading_engine.py 
   # Note: File name is generic, run the respective python file.
