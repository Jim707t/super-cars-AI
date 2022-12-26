import pygame as pg




pg.init()
window = pg.display.set_mode((900, 700))

blue = (0, 0, 255)
bg_surface = pg.Surface((900, 700))
bg_surface.fill(blue)

class Car:
    def __init__(self, skin, x, y, car_speed, fr, turn_speed, direction, CAR_WIDTH, CAR_HEIGHT):
        self.skin = skin
        self.x = x
        self.y = y
        self.car_speed = car_speed
        #  resistive force
        self.fr = fr
        self.turn_speed = turn_speed
        self.direction = direction
        self.CAR_WIDTH = CAR_WIDTH
        self.CAR_HEIGHT = CAR_HEIGHT
        
class Env:
    def __init__(self, bg, x, y):
        self.bg = bg
        self.x = x
        self.y = y   
         
class Road:
    def __init__(self, skin, x, y, CAR_WIDTH, CAR_HEIGHT):
        self.skin = skin
        self.x = x
        self.y = y
        self.CAR_WIDTH = CAR_WIDTH
        self.CAR_HEIGHT = CAR_HEIGHT
            
car1 =  Car(pg.image.load("img/car1.png"), 555, 555, 22, 0, 15, 0, 40, 40)
env = Env(bg_surface, 0, 0)
road = Road(pg.image.load("img/road.png"), 0, 0, 900, 700)

print(car1) 

env_surface = pg.Surface((env.bg.get_width(), env.bg.get_height()))

pg.key.set_repeat(500, 100)
while True:
    # Decrease car's speed by Coefficient of Friction
    car1.car_speed *= (1 - car1.fr)
    MAX_SPEED = 30
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            if pg.key.get_pressed()[pg.K_LEFT]:
                car1.x -= car1.car_speed
            if pg.key.get_pressed()[pg.K_RIGHT]:
                car1.x += car1.car_speed
            if pg.key.get_pressed()[pg.K_UP]:
                car1.y -= car1.car_speed
                car1.car_speed += 0.2
                if car1.car_speed > MAX_SPEED:
                   car1.car_speed = MAX_SPEED
            if pg.key.get_pressed()[pg.K_DOWN]:
                car1.y += car1.car_speed
                
            if pg.key.get_pressed()[pg.K_SPACE]:
                car1.car_speed -= car1.car_speed % 2

    env_surface.blit(env.bg, (env.x, env.y))
    
    car_s = pg.transform.scale(car1.skin, (car1.CAR_WIDTH, car1.CAR_HEIGHT))
    road_s = pg.transform.scale(road.skin, (road.CAR_WIDTH, road.CAR_HEIGHT))
    env_surface.blit(road_s, (0, 0))
    env_surface.blit(car_s, (car1.x, car1.y))


    window.blit(env_surface, (0, 0)) 


    pg.display.update()
