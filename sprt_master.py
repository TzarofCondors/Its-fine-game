import pygame as py
py.init()
py.mixer.init()

ship_sound=py.mixer.Sound("sounds/misc/ship_move.wav")
ship_sound.set_volume(0.3)

class HUD_master(py.sprite.Sprite):
    def __init__(self, x, y,name,amount):
        super().__init__()
        self.sprites=[]
        self.name=name
        self.amount=int(amount)
        self.x=int(x)
        self.y=int(y)
        self.current_sprite=0

        for i in range(amount):
            img=py.image.load(f'huds/{self.name}/{i}.png')
            self.sprites.append(img)

        self.image=self.sprites[self.current_sprite]
        self.rect=self.image.get_rect(center=(self.x,self.y))
    
    def update(self,speed):
        self.current_sprite+=speed
        if self.current_sprite>=len(self.sprites):
            self.current_sprite=0
        self.image=self.sprites[int(self.current_sprite)]

class Crosshair(py.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
    def shoot():
        pass
    def update(self):
        self.rect.center=py.mouse.get_pos()

class Tool(py.sprite.Sprite):
    def __init__(self, surface, x, y, image, size_x, size_y):
        super().__init__()
        self.img=image
        self.size_x=size_x
        self.size_y=size_y
        self.x=x
        self.y=y
        self.image = py.transform.scale(self.img, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.clicked = False
        self.surface = surface
        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Button():
    def __init__(self, surface, x, y, image, size_x, size_y):
        self.image = py.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.surface = surface

    def draw(self, surface):
        action = False
        pos = py.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if py.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if py.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class Mini_Ship(py.sprite.Sprite):
    def __init__(self, surface, x, y, image, size_x, size_y):
        super().__init__()
        self.image = py.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.x=int(x)
        self.y=int(y)
        self.rect.center = (x,y)
        self.vel=0
        self.surface = surface
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def move(self, limit,delta_time,target_fps,is_fuel,sound_timer):
        self.vel=0
        keys=py.key.get_pressed()
        if keys[py.K_w]:
            if is_fuel<=7:
                if sound_timer<=0:
                    sound_timer=100
                    ship_sound.play()
                self.vel=0.037*delta_time*target_fps
        else:
            ship_sound.stop()
        
        self.x+=self.vel
        self.limit=limit

        self.rect.center=(self.x, self.y)

        if self.x>=self.limit:
            self.x=self.limit

class Marker(py.sprite.Sprite):
    def __init__(self, surface,x, y, image, size_x, size_y):
        super().__init__()
        self.image = py.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.x=int(x)
        self.y=int(y)
        self.rect.center = (x, y)
        self.surface = surface
    def draw(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(py.sprite.Sprite):
    def __init__(self, surface,x, y, image, size_x, size_y):
        super().__init__()
        self.image = py.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.x=int(x)
        self.y=int(y)
        self.rect.center = (x, y)
        self.surface = surface

    def draw(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self):
        pos = py.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if py.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
    
            if py.mouse.get_pressed()[0] == 0:
                self.clicked = False

class Fire(py.sprite.Sprite):
    def __init__(self, x, y,name):
        super().__init__()
        self.sprites=[]
        self.name=name
        self.x=int(x)
        self.y=int(y)
        self.current_sprite=0

        for i in range(5):
            img=py.image.load(f'sprites/{self.name}/{i}.png')
            img=py.transform.scale(img,(200,200))
            self.sprites.append(img)

        self.image=self.sprites[self.current_sprite]
        self.rect=self.image.get_rect(center=(self.x,self.y))
    
    def update(self,speed):
        self.current_sprite+=speed
        if self.current_sprite>=len(self.sprites):
            self.current_sprite=0
        self.image=self.sprites[int(self.current_sprite)]