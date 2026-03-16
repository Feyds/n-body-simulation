import math
import json

class Body:
    def __init__(self, name, mass, x, y, vx, vy, color):
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def update_velocity(self, bodies, G, dt):
        """Diğer tüm cisimlerin bu cisme uyguladığı kütle çekimini hesaplar ve hızı günceller."""
        for other in bodies:
            if other == self:
                continue
            
            dx = other.x - self.x
            dy = other.y - self.y
            distance_sq = dx**2 + dy**2
            distance = math.sqrt(distance_sq)

            if distance == 0:
                continue

            acceleration = G * other.mass / distance_sq

            ax = acceleration * (dx / distance)
            ay = acceleration * (dy / distance)

            self.vx += ax * dt
            self.vy += ay * dt

    def update_position(self, dt):
        """Güncel hıza göre konumu günceller."""
        self.x += self.vx * dt
        self.y += self.vy * dt

def run_simulation():
    G = 0.1 
    dt = 1.0
    steps = 2000

    sun = Body("Sun", 10000, 0, 0, 0, 0, "#FDB813")
    planet1 = Body("Planet 1", 10, 200, 0, 0, 2.2, "#3B82F6")
    planet2 = Body("Planet 2", 20, -350, 0, 0, -1.5, "#EF4444")
    planet3 = Body("Planet 3", 30, 300, 0, 0, 1.5, "#00FF00")

    bodies = [sun, planet1, planet2, planet3]
    
    simulation_data = []

    for step in range(steps):
        step_data = []

        for body in bodies:
            body.update_velocity(bodies, G, dt)

        for body in bodies:
            body.update_position(dt)
            step_data.append({
                "name": body.name,
                "x": round(body.x, 2),
                "y": round(body.y, 2),
                "color": body.color
            })
            
        simulation_data.append(step_data)

    with open('simulation_data.json', 'w') as f:
        json.dump(simulation_data, f)
    
    print(f"Simülasyon tamamlandı! {steps} karelik veri 'simulation_data.json' dosyasına kaydedildi.")

if __name__ == "__main__":
    run_simulation()