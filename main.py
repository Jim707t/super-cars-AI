import pygame as pg



pg.init()
window = pg.display.set_mode((900, 700))

# Load Cars and road
car1 = pg.image.load("img/car1.png")
car2 = pg.image.load("img/car2.png")
road = pg.image.load("img/road.png")

cars = [car1, car2]

CAR_WIDTH, CAR_HEIGHT = 120, 120
# initial position of the car images
car_x, car_y = 0, 0
road_x, road_y  = 0, 0

# Create a Pygame surface for the road
road_surface = pg.Surface((road.get_width(), road.get_height()))
car_speed = 20

while True:
    # Check for keyboard events
    events = pg.event.get()
    for event in events:
        
        # Check if the user pressed a key
            # Check which key was pressed and update the position of the car
            if pg.key.get_pressed()[pg.K_LEFT]:
                car_x -= car_speed
            if pg.key.get_pressed()[pg.K_RIGHT]:
                car_x += car_speed
            if pg.key.get_pressed()[pg.K_UP]:
                car_y -= car_speed
            if pg.key.get_pressed()[pg.K_DOWN]:
                car_y += car_speed

    # Blit the road onto the surface
    road_surface.blit(road, (road_x, road_y))
    
    # Add the cars in the road
    for car in cars:
        car = pg.transform.scale(car, (CAR_WIDTH, CAR_HEIGHT))
        road_surface.blit(car, (car_x, car_y))

    # Blit the surface onto the Pygame window
    window.blit(road_surface, (0, 0))

    # Update the Pygame window
    pg.display.update()