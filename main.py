import pygame as py
import time
import sys
import sprt_master
import random

py.init()
py.mixer.init()
py.mixer.set_num_channels(11)

clock=py.time.Clock()

screen_w=1344
screen_h=756
clicked=False

current_time=0
pirate_time=0
roach_time=0
fire_time=0
check_time=0
boom_time=0
suffocate_time=0
enemy_time=0
fuel_time=0
fire_sound_timer=0

o2_low_timer=0
infest_alarm_timer=0
fire_alarm_timer=0
pirate_alarm_timer=0
ship_sound_timer=0

#sounds
bruh=py.mixer.Sound("sounds/misc/bruh_sound_effect_#2.wav")
horror_trigger=True

walk_sound=py.mixer.Sound("sounds/misc/walk.wav")
walk_sound.set_volume(0.5)

fire_extinguisher_sound=py.mixer.Sound("sounds/misc/fire-extinguisher.wav")
fire_extinguisher_sound.set_volume(0.5)

success_sound=py.mixer.Sound("sounds/misc/success.wav")
success_sound.set_volume(0.5)

button_sound=py.mixer.Sound("sounds/misc/btn_selection.wav")
button_sound.set_volume(0.3)

gun_pickup=py.mixer.Sound("sounds/gun/shotgun_acquire.wav")
gun_pickup.set_volume(0.4)
shoot_sound=py.mixer.Sound("sounds/gun/shotgun-shot.wav")
shoot_sound.set_volume(0.3)
laser_sound=py.mixer.Sound("sounds/gun/laser_fire.wav")
laser_sound.set_volume(0.5)
pirate_explosion=py.mixer.Sound("sounds/misc/pirate_explosion.wav")
pirate_explosion.set_volume(0.5)

fire_sound=py.mixer.Sound("sounds/misc/fire.wav")
fire_sound.set_volume(0.5)
valve_sound1=py.mixer.Sound("sounds/misc/valve1.wav")
valve_sound1.set_volume(0.5)
valve_sound2=py.mixer.Sound("sounds/misc/valve2.wav")
valve_sound2.set_volume(0.5)
valve_sounds=[valve_sound1,valve_sound2]
toolbox_sound=py.mixer.Sound("sounds/misc/toolbox.wav")
toolbox_sound.set_volume(0.3)

#game_over_sounds
ship_explosion_sound=py.mixer.Sound("sounds/game_over/ship_explode.wav")
artifact_broken_sound=py.mixer.Sound("sounds/game_over/artifact_broken.wav")

jerry_pickup=py.mixer.Sound("sounds/refills/jerry_can_pickup.wav")
jerry_pickup.set_volume(0.5)
refule_sound=py.mixer.Sound("sounds/refills/refulling.wav")
refule_sound.set_volume(0.5)
o2_pickup=py.mixer.Sound("sounds/refills/o2_pickup.wav")
o2_pickup.set_volume(0.5)
o2_refill=py.mixer.Sound("sounds/refills/o2_refill.wav")
o2_refill.set_volume(0.5)

clock=py.time.Clock()

rc=0
pc=0
fc=0
previous_time=time.time()
delta_time=0

BLACK=(0,0,0)
YELLOW=(255,255,0)
GREEN=(34,139,34)
font=py.font.Font("font/Early GameBoy.ttf",30)
font2=py.font.Font("font/Pixellari.ttf",150)

screen=py.display.set_mode((screen_w,screen_h))
py.display.set_caption("manage")

#big empty
empty_img=py.image.load("sprites/nada.png").convert_alpha()
empty=sprt_master.Tool(screen, 1000, 100, empty_img,120,120)

#poster
inspire=py.image.load("sprites/cat.png").convert_alpha()
inspire=py.transform.scale(inspire,(300,300))
despair=py.image.load("sprites/despair.png").convert_alpha()
despair=py.transform.scale(despair,(300,300))

#cursors
cursor_img=py.image.load("sprites/Da_Aim.png").convert_alpha()
cursor_img=py.transform.scale(cursor_img, (30,30))
cursor_img1=py.image.load("sprites/broom_hair.png").convert_alpha()
cursor_img1=py.transform.scale(cursor_img1, (100,100))
cursor_img2=py.image.load("sprites/ext_hair.png").convert_alpha()

crosshair=sprt_master.Crosshair(cursor_img)
crosshair_group=py.sprite.Group()
crosshair_group.add(crosshair)

crosshair1=sprt_master.Crosshair(cursor_img1)
crosshair_group1=py.sprite.Group()
crosshair_group1.add(crosshair1)

crosshair2=sprt_master.Crosshair(cursor_img2)
crosshair_group2=py.sprite.Group()
crosshair_group2.add(crosshair2)

#da trick of da trade
inv=py.image.load("sprites/da_inventory.png").convert()
inv=py.transform.scale(inv,(110,110))
shell=py.image.load("sprites/Da_Shell.png").convert_alpha()
shell=py.transform.scale(shell,(100,100))

alert_img=py.image.load("sprites/btns/alert.png").convert_alpha()
alert_img=py.transform.scale(alert_img,(70,70))
#buttons
arrow=py.image.load("sprites/Da_arrow.png").convert_alpha()
arrow_r=sprt_master.Button(screen, 1290, screen_h/2, arrow, 120, 120)
arrow1=py.image.load("sprites/Da_arrow1.png").convert_alpha()
arrow_u=sprt_master.Button(screen, screen_w/2, 70, arrow1, 120, 120)
arrow2=py.image.load("sprites/Da_arrow2.png").convert_alpha()
arrow_l=sprt_master.Button(screen, 50, screen_h/2, arrow2, 120, 120)
arrow3=py.image.load("sprites/Da_arrow3.png").convert_alpha()
arrow_d=sprt_master.Button(screen, screen_w/2, 700, arrow3, 120, 120)
arrow4=py.image.load("sprites/Da_arrow3.png").convert_alpha()
arrow_d1=sprt_master.Button(screen, 465, 630, arrow3, 120, 120)

start_img=py.image.load("sprites/btns/start_btn.png").convert_alpha()
start_btn=sprt_master.Button(screen, 300, screen_h/2, start_img, 300, 300)
quit_img=py.image.load("sprites/btns/quit_btn.png").convert_alpha()
quit_btn=sprt_master.Button(screen, 1000, screen_h/2, quit_img, 300, 300)
quit_btn2=sprt_master.Button(screen, 1050, screen_h/2, quit_img, 300, 300)
rerty_img=py.image.load("sprites/btns/retry_btn.png").convert_alpha()
retry_btn=sprt_master.Button(screen, 300, screen_h/2, rerty_img, 300, 300)
menu_img=py.image.load("sprites/btns/menu_btn.png").convert_alpha()
menu_btn=sprt_master.Button(screen, 300, screen_h/2, menu_img, 300, 300)

#fire
fire_group=py.sprite.Group()
for i in range(2):
    fire=sprt_master.Fire(random.randint(900,1200),500,"Da_Fire")
    fire_group.add(fire)

#da huds
fuel=sprt_master.HUD_master(45,65,"Da_Fuel",8)
fuel_group=py.sprite.Group()
fuel_group.add(fuel)

pressure=sprt_master.HUD_master(1290,65,"Da_pressure",7)
pressure_group=py.sprite.Group()
pressure_group.add(pressure)

ox2=sprt_master.HUD_master(50,710,"Da_O2",7)
o2_group=py.sprite.Group()
o2_group.add(ox2)

#tools
jerry_img=py.image.load("sprites/Da_gas.png")
jerry_icon=py.transform.scale(jerry_img,(90,90))
jerry1=sprt_master.Tool(screen, 950, 325, jerry_img,150,150)
jerry2=sprt_master.Tool(screen, 1050, 325, jerry_img,150,150)
jerry3=sprt_master.Tool(screen, 950, 480, jerry_img,150,150)
jerry_list=[jerry1,jerry2,jerry3]

otoo_img=py.image.load("sprites/Da_Oxygen.png").convert_alpha()
otoo_icon=py.transform.scale(otoo_img,(90,90))
otoo1=sprt_master.Tool(screen, 600, 650, otoo_img,150,200)
otoo2=sprt_master.Tool(screen, 700, 650, otoo_img,150,200)
otoo_list=[otoo1,otoo2]

broom_img=py.image.load("sprites/Da_Broom.png").convert_alpha()
broom=sprt_master.Tool(screen, 260, 260, broom_img,150,150)
broom_icon=py.transform.scale(broom.image,(90,90))

wrench=py.image.load("sprites/Da_Wrench.png").convert_alpha()
wrench=py.transform.scale(wrench,(90,90))

extinguisher_img=py.image.load("sprites/Da_Extinguisher.png").convert_alpha()
extinguisher_icon=py.transform.scale(extinguisher_img,(80,110))
extinguisher=sprt_master.Tool(screen,275, 680, extinguisher_img,150,150)

#Da enemies >:(
pirate_group=py.sprite.Group()
pirate_img=py.image.load("sprites/Da_Enemy.png").convert_alpha()
for i in range(4):
    r_x=random.randint(100,900)
    r_y=random.randint(50,600)
    pirate=sprt_master.Enemy(screen,r_x,r_y,pirate_img,200,200)
    pirate_group.add(pirate)

roach_group=py.sprite.Group()
roach_img=py.image.load("sprites/Da_Roach.png").convert_alpha()
for i in range(4):
    r_x=random.randint(295,1034)
    r_y=random.randint(280,528)
    roach=sprt_master.Enemy(screen,r_x+20,r_y+20,roach_img,100,100)
    roach_group.add(roach)

#Da warnings
fire_alert=py.image.load("sprites/alert_signs/Fire_Hazard.png").convert_alpha()
fire_alert=py.transform.scale(fire_alert,(150,150))
pirate_attack=py.image.load("sprites/alert_signs/Pirate_attack.png").convert_alpha()
pirate_attack=py.transform.scale(pirate_attack,(150,150))
infestation=py.image.load("sprites/alert_signs/infestation_warning.png").convert_alpha()
infestation=py.transform.scale(infestation,(150,150))

#Da progress
diff_group=py.sprite.Group()
diff_changer_img=py.image.load("sprites/diff_spike.png").convert_alpha()
diff_changer1=sprt_master.Marker(screen,566,673, diff_changer_img,50,10)
diff_changer2=sprt_master.Marker(screen,602,673, diff_changer_img,50,10)
diff_changer3=sprt_master.Marker(screen,652,673, diff_changer_img,50,10)
diff_changer4=sprt_master.Marker(screen,685,673, diff_changer_img,50,10)
diff_changer5=sprt_master.Marker(screen,739,673, diff_changer_img,50,10)
diff_changer6=sprt_master.Marker(screen,775,673, diff_changer_img,50,10)
diff_list=[diff_changer1,diff_changer2,diff_changer3,diff_changer4,diff_changer5,diff_changer6]

ship_img=py.image.load("sprites/ship_icon.png").convert_alpha()
ship=sprt_master.Mini_Ship(screen,550,670, ship_img,50,50)
ship_group=py.sprite.Group()
ship_group.add(ship)

progress_bar=py.image.load("sprites/progress_bar.png").convert_alpha()
progress_bar=py.transform.scale(progress_bar,(300,300))

checkpoint=py.image.load("sprites/checkpoint.png").convert_alpha()
check_flag=sprt_master.Marker(screen,632,670,checkpoint,50,50)
check_flag1=sprt_master.Marker(screen,715,670,checkpoint,50,50)
flag_group=py.sprite.Group()
flag_group1=py.sprite.Group()
flag_group.add(check_flag)
flag_group1.add(check_flag1)

#backgrounds
b1=py.image.load("back/bridge.png").convert()
b2=py.image.load("back/engine.png").convert()
b3=py.image.load("back/storage.png").convert()
b4=py.image.load("back/space.png").convert()
b5=py.image.load("back/package.png").convert()
start_back=py.image.load("back/start_screen.png").convert()
game_over_back=py.image.load("back/game_over_screen.png").convert()
game_over_back=py.transform.scale(game_over_back,(screen_w,screen_h))
win_back=py.image.load("back/win_screen.png").convert()
win_back=py.transform.scale(win_back,(screen_w,screen_h))

#events
occupation=False
locknload=False
on_fire=False
pirate_att=False
infest=False

hull=10000
package_health=2500
ammo=9

fuel_use=0.002
o2_use=0.003
pressure_change=0
diff=7
nf=0

running=False

def reset():
    global hull, package_health,ammo,occupation,locknload,on_fire,pirate_att,infest, diff, nf, rc, pc, fuel_use,o2_use,pressure_change
    diff_group.add(diff_changer1,diff_changer2,diff_changer3,diff_changer4,diff_changer5,diff_changer6)
    hull=10000
    package_health=3000
    ammo=9
    occupation=False
    locknload=False
    on_fire=False
    pirate_att=False
    infest=False
    ship.x=550
    fuel_use=0.002
    o2_use=0.001
    pressure_change=0
    diff=7
    nf=0
    fuel.current_sprite=0
    ox2.current_sprite=0
    pressure.current_sprite=0
    rc=0
    pc=0

    for count, i in enumerate(jerry_list):
        i.rect.center=(i.x,i.y)
    for count, i in enumerate(otoo_list):
        i.rect.center=(i.x,i.y)
    
    extinguisher.rect.center=(extinguisher.x,extinguisher.y)
    broom.rect.center=(broom.x,broom.y)
    empty.image=empty_img

def ressuply():
    global on_fire,infest,pirate_att,ammo,hull,package_health,rc,pc,fc,nf
    fire_group.empty()
    roach_group.empty()
    pirate_group.empty()
    ammo+=22
    hull+=3000
    package_health=3000
    rc=4
    fc=2
    pc=4
    nf=0
    for count, i in enumerate(jerry_list):
        i.rect.center=(i.x,i.y)
    for count, i in enumerate(otoo_list):
        i.rect.center=(i.x,i.y)

def hazards():
    global fc, rc, pc, package_health,hull, o2_use, enemy_time, infest, pirate_att, on_fire, diff, infest_alarm_timer, fire_alarm_timer, pirate_alarm_timer, o2_low_timer

    if infest_alarm_timer>0:
        infest_alarm_timer-=1
    if fire_alarm_timer>0:
        fire_alarm_timer-=1
    if pirate_alarm_timer>0:
        pirate_alarm_timer-=1
    if o2_low_timer>0:
        o2_low_timer-=1

    if diff<7 and len(pirate_group)>0:
        if current_time-enemy_time>random.randint(7000,diff*15000):
            pirate_att=True
    else:
        pirate_att=False

    if pressure.current_sprite>=4 and len(fire_group)>0:
        on_fire=True
    else:
        on_fire=False
        o2_use=0.001
        
    if diff<7 and len(roach_group)>0:
        if current_time-enemy_time>random.randint(9000,diff*20000):
            infest=True
    else:
        infest=False

    if pressure.current_sprite>=4:
            if current_time-fire_time>10000 and len(fire_group)<2:
                while fc>0:
                    r_x=random.randint(900,1200)
                    fire=sprt_master.Fire(r_x,500,"Da_Fire")
                    fire_group.add(fire)
                    fc-=1
    if current_time-pirate_time>(diff*random.randint(5000,10000)) and len(pirate_group)<4:
            while pc>0:
                r_x=random.randint(100,900)
                r_y=random.randint(50,600)
                pirate=sprt_master.Enemy(screen,r_x+20,r_y+20,pirate_img,200,200)
                pirate_group.add(pirate)
                pc-=1
    if current_time-roach_time>(diff*random.randint(5000,10000)) and len(roach_group)<4:
            while rc>0:
                r_x=random.randint(295,1034)
                r_y=random.randint(280,528)
                roach=sprt_master.Enemy(screen,r_x+20,r_y+20,roach_img,100,100)
                roach_group.add(roach)
                rc-=1
    
    if infest==True:
        if infest_alarm_timer<=0:
            infest_alarm_timer=30
            py.mixer.Channel(1).set_volume(0.2)
            py.mixer.Channel(1).play(py.mixer.Sound("sounds/alerts/infestation_alarm.wav"))
        package_health-=(0.50*(len(roach_group)))
    
    if pirate_att==True:
        if pirate_alarm_timer<=0:
            pirate_alarm_timer=30
            py.mixer.Channel(3).play(py.mixer.Sound("sounds/alerts/pirate_alarm.wav"))
        hull-=(1*(len(pirate_group)))
    
    if on_fire==True:
        if fire_alarm_timer<=0:
            fire_alarm_timer=30
            py.mixer.Channel(2).set_volume(0.2)
            py.mixer.Channel(2).play(py.mixer.Sound("sounds/alerts/fire_alarm.wav"))
        o2_use=0.005
    
    if ox2.current_sprite>=6:
        if o2_low_timer<=0:
            o2_low_timer=40
            py.mixer.Channel(4).set_volume(0.2)
            py.mixer.Channel(4).play(py.mixer.Sound("sounds/alerts/low_o2.wav"))
    
    clock.tick(60)
    
def is_game_over():
    global running, boom_time, fuel_time, suffocate_time, nf, hull, package_health
    if pressure.current_sprite>=6:
        boom_time+=1
        if boom_time>300:
            py.mixer.Channel(6).set_volume(0.5)
            py.mixer.Channel(6).play(py.mixer.Sound("sounds/game_over/ship_explode.wav"))
            game_over()
            running=False

    elif on_fire==True:
        boom_time+=1
        if boom_time>700:
            py.mixer.Channel(6).set_volume(0.5)
            py.mixer.Channel(6).play(py.mixer.Sound("sounds/game_over/ship_explode.wav"))
            game_over()
            running=False
    else:
        boom_time=0
    
    if fuel.current_sprite>=7:
        if nf>2:
            fuel_time+=1
            if fuel_time>600:
                bruh.play()
                game_over()
                running=False
    else:
        fuel_time=0
    
    if ox2.current_sprite>=6:
        suffocate_time+=1
        if suffocate_time>2000:
            bruh.play()
            game_over()
            running=False
    else:
        suffocate_time=0
    
    if hull<=0:
        py.mixer.Channel(6).set_volume(0.5)
        py.mixer.Channel(6).play(py.mixer.Sound("sounds/game_over/ship_explode.wav"))
        game_over()
        running=False
    
    if package_health<=0:
        py.mixer.Channel(6).set_volume(0.5)
        py.mixer.Channel(6).play(py.mixer.Sound("sounds/game_over/artifact_broken.wav"))
        game_over()
        running=False

def start():
    global running, current_time
    run=True
    while run:
        screen.blit(start_back,(0,0))
        text=font2.render("IT'S FINE",True,YELLOW)
        screen.blit(text,(350,50))

        if start_btn.draw(screen):
            button_sound.play()
            reset()
            running=True
            bridge()
            run=False

        if quit_btn.draw(screen):
            py.quit()
            sys.exit()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        
        py.display.update()

def game_over():
    global running
    run=True
    diff_group.empty()
    while run:
        sprt_master.ship_sound.stop()
        screen.blit(game_over_back,(0,0))
        text=font2.render("GAME OVER!",True,YELLOW)
        screen.blit(text,(275,60))
        py.mouse.set_visible(True)

        if retry_btn.draw(screen):
            button_sound.play()
            reset()
            running=True
            bridge()
            run=False
            

        if quit_btn.draw(screen):
            py.quit()
            sys.exit()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        
        py.display.update()
        clock.tick(60)

def win():
    global running
    running=False
    run=True
    diff_group.empty()
    py.mixer.Channel(7).set_volume(0.5)
    py.mixer.Channel(7).play(py.mixer.Sound("sounds/misc/success.wav"))
    while run:
        sprt_master.ship_sound.stop()
        screen.blit(win_back,(0,0))
        text=font2.render("Package",True,GREEN)
        text2=font2.render("Delivered",True,GREEN)
        screen.blit(text,(350,60))
        screen.blit(text2,(350,200))

        if menu_btn.draw(screen):
            button_sound.play()
            run=False
            start()
            
        if quit_btn2.draw(screen):
            py.quit()
            sys.exit()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        
        py.display.update()

def bridge():
    global running, fuel_use, o2_use, pressure_change, occupation, ammo, on_fire, pirate_att, infest, diff, current_time, enemy_time, check_time, fc, ship_sound_timer
    previous_time=time.time()
    while running:
        curr_time=time.time()
        delta_time=curr_time-previous_time
        previous_time=curr_time

        current_time=py.time.get_ticks()
        is_game_over()
        hazards()

        if ship_sound_timer>0:
            ship_sound_timer-=1

        text=font.render(str(ammo),True,BLACK)
        screen.blit(b1,(0,0))
        screen.blit(inv,(930,40))
        screen.blit(progress_bar,(520,490))

        check_flag.draw(screen)
        check_flag1.draw(screen)

        for i in diff_list:
            i.draw(screen)

        ship.draw(screen)
        ship.move(800, delta_time,60,fuel.current_sprite, ship_sound_timer)
        
        if ox2.current_sprite>=6:
            screen.blit(alert_img,(100,650))

        pos=py.mouse.get_pos()

        fuel_group.draw(screen)
        if fuel.current_sprite<7:
            fuel_group.update(fuel_use)

        pressure_group.draw(screen)
        if pressure.current_sprite<6:
            pressure_group.update(pressure_change)

        o2_group.draw(screen)
        if ox2.current_sprite<6:
            o2_group.update(o2_use)

        empty.draw(screen)

        extinguisher.draw(screen)

        if extinguisher.rect.collidepoint(pos) and occupation==False:
                if clicked==True:
                    extinguisher.rect.center=(3000,3000)
                    empty.image=extinguisher_icon
                    occupation=True

        if empty.rect.collidepoint(pos) and occupation==True and extinguisher.rect.center==(3000,3000) and empty.image==extinguisher_icon:
                if clicked==True:
                    extinguisher.rect.center=(extinguisher.x,extinguisher.y)
                    empty.image=empty_img
                    occupation=False

        if arrow_l.draw(screen):
            fuel_use=0.002
            pressure_change=0
            walk_sound.play()
            storage()
            
        if arrow_u.draw(screen):
            fuel_use=0.002
            pressure_change=0
            walk_sound.play()
            space()
            
        if arrow_r.draw(screen):
            fuel_use=0.002
            pressure_change=0
            walk_sound.play()
            engine()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            
            if event.type==py.KEYDOWN:
                if event.key==py.K_w:
                    if fuel.current_sprite<=7:
                        pressure_change=0.01
                        fuel_use=0.005

            elif event.type==py.KEYUP:
                    fuel_use=0.002
                    pressure_change=0

            if event.type == py.MOUSEBUTTONDOWN:
                clicked = True
                if empty.image==broom_icon and ammo>0:
                    if (py.mouse.get_pos()[0] > 1224 and\
                        py.mouse.get_pos()[1] < 412 and\
                        py.mouse.get_pos()[0] < 1340 and\
                        py.mouse.get_pos()[1] > 345)==False and\
                        (py.mouse.get_pos()[0] > 5 and\
                        py.mouse.get_pos()[1] < 420 and\
                        py.mouse.get_pos()[0] < 110 and\
                        py.mouse.get_pos()[1] > 335)==False and\
                        (py.mouse.get_pos()[0] > 635 and\
                        py.mouse.get_pos()[1] < 130 and\
                        py.mouse.get_pos()[0] < 705 and\
                        py.mouse.get_pos()[1] > 22)==False and\
                        (py.mouse.get_pos()[0] > 930 and\
                        py.mouse.get_pos()[1] < 149 and\
                        py.mouse.get_pos()[0] < 1038 and\
                        py.mouse.get_pos()[1] > 40)==False:
                            ammo-=1
            else:
                clicked = False
        
        check=py.sprite.groupcollide(ship_group,flag_group, False, True,py.sprite.collide_mask)
        check1=py.sprite.groupcollide(ship_group,flag_group1, False, True,py.sprite.collide_mask)
        spike=py.sprite.groupcollide(ship_group,diff_group,False,True,py.sprite.collide_mask)

        if check or check1:
            py.mixer.Channel(4).set_volume(0.3)
            py.mixer.Channel(4).play(py.mixer.Sound("sounds/misc/checkpoint.wav"))
            ressuply()
            fuel.current_sprite=0
            ox2.current_sprite=0
            pressure.current_sprite=0
            check_time=py.time.get_ticks()

        if current_time-check_time<1000:
            check_text=font.render("CHECKPOINT REACHED",True,GREEN)
            screen.blit(check_text,(425,200))
        
        if locknload==True:
            screen.blit(shell,(1040,50))
            screen.blit(text,(1130,50))
            py.mouse.set_visible(False)
            crosshair_group1.draw(screen)
            crosshair_group1.update()
        else:
            py.mouse.set_visible(True)

        if spike:
            diff-=1
            enemy_time=py.time.get_ticks()
        
        if on_fire==True:
            screen.blit(fire_alert,(100,5))
        if pirate_att==True:
            screen.blit(pirate_attack,(200,-10))
        if infest==True:
            screen.blit(infestation,(130,75))
        
        if ship.x==800:
            win()

        py.display.update()
        clock.tick(60)


def storage():
    global running, occupation, locknload, ammo, horror_trigger

    while running:
        is_game_over()
        hazards()
        sprt_master.ship_sound.stop()

        text=font.render(str(ammo),True,BLACK)
        screen.blit(b3,(0,0))
        screen.blit(inv,(930,40))

        if ship.x<660:
            screen.blit(inspire,(470,220))
        else:
            screen.blit(despair,(470,220))
            if horror_trigger==True:
                horror_trigger=False
                py.mixer.Channel(5).set_volume(0.5)
                py.mixer.Channel(5).play(py.mixer.Sound("sounds/misc/shoebill.wav"))

        fuel_group.draw(screen)
        if fuel.current_sprite<7:
            fuel_group.update(fuel_use)

        pressure_group.draw(screen)
        if pressure.current_sprite<6:
            pressure_group.update(pressure_change)

        o2_group.draw(screen)
        if ox2.current_sprite<6:
            o2_group.update(o2_use)

        empty.draw(screen)

        pos=py.mouse.get_pos()

        for i in jerry_list:
             i.draw(screen)
        
        for count, i in enumerate(jerry_list):
            if i.rect.collidepoint(pos) and occupation==False:
                if clicked==True:
                    jerry_pickup.play()
                    i.rect.center=(3000,3000)
                    empty.image=jerry_icon
                    occupation=True
            
            if empty.rect.collidepoint(pos) and occupation==True and empty.image==jerry_icon and i.rect.center==(3000,3000):
                if clicked==True:
                    jerry_pickup.play()
                    i.rect.center=(i.x,i.y)
                    empty.image=empty_img
                    occupation=False

        for i in otoo_list:
             i.draw(screen)
        
        for count, i in enumerate(otoo_list):
            if i.rect.collidepoint(pos) and occupation==False:
                if clicked==True:
                    o2_pickup.play()
                    i.rect.center=(3000,3000)
                    empty.image=otoo_icon
                    occupation=True
            
            if empty.rect.collidepoint(pos) and occupation==True and empty.image==otoo_icon and i.rect.center==(3000,3000):
                if clicked==True:
                    o2_pickup.play()
                    i.rect.center=(i.x,i.y)
                    empty.image=empty_img
                    occupation=False

        broom.draw(screen)

        if broom.rect.collidepoint(pos) and occupation==False:
            if clicked==True:
                gun_pickup.play()
                broom.rect.center=(3000,3000)
                empty.image=broom_icon
                occupation=True
                locknload=True
        
        if empty.rect.collidepoint(pos) and occupation==True and empty.image==broom_icon:
            if clicked==True:
                gun_pickup.play()
                broom.rect.center=(broom.x,broom.y)
                empty.image=empty_img
                occupation=False
                locknload=False
        
        if (py.mouse.get_pos()[0] > 118 and\
            py.mouse.get_pos()[1] < 710 and\
            py.mouse.get_pos()[0] < 245 and\
            py.mouse.get_pos()[1] > 626 and\
            occupation==False):
            if clicked==True:
                toolbox_sound.play()
                empty.image=wrench
                occupation=True
        
        if empty.rect.collidepoint(pos) and occupation==True and empty.image==wrench:
            if clicked==True:
                toolbox_sound.play()
                empty.image=empty_img
                occupation=False

        if arrow_r.draw(screen):
            walk_sound.play()
            bridge()
            
        if arrow_d1.draw(screen):
            walk_sound.play()
            package()
        
        if locknload==True:
            screen.blit(shell,(1040,50))
            screen.blit(text,(1130,50))
            py.mouse.set_visible(False)
            crosshair_group1.draw(screen)
            crosshair_group1.update()
        else:
            py.mouse.set_visible(True)
    
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                clicked = True
                if empty.image==broom_icon and ammo>0:
                    if (py.mouse.get_pos()[0] > 431 and\
                        py.mouse.get_pos()[1] < 679 and\
                        py.mouse.get_pos()[0] < 510 and\
                        py.mouse.get_pos()[1] > 580)==False and\
                        (py.mouse.get_pos()[0] > 1224 and\
                        py.mouse.get_pos()[1] < 412 and\
                        py.mouse.get_pos()[0] < 1340 and\
                        py.mouse.get_pos()[1] > 345)==False and\
                        (py.mouse.get_pos()[0] > 930 and\
                        py.mouse.get_pos()[1] < 149 and\
                        py.mouse.get_pos()[0] < 1038 and\
                        py.mouse.get_pos()[1] > 40)==False:
                            ammo-=1
                            shoot_sound.play()
            else:
                clicked = False
            
        py.display.update()
        clock.tick(60)

def engine():
    global running, occupation, ammo, o2_use, fire_time, fc, on_fire, nf, fire_sound_timer

    while running:
        is_game_over()
        hazards()

        if fire_sound_timer>0:
            fire_sound_timer-=1

        text=font.render(str(ammo),True,BLACK)
        screen.blit(b2,(0,0))
        screen.blit(inv,(930,40))

        empty.draw(screen)

        if arrow_l.draw(screen):
            walk_sound.play()
            bridge()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                ded=py.sprite.groupcollide(crosshair_group2,fire_group, False, True, py.sprite.collide_mask)
                if ded:
                    fire_extinguisher_sound.play()
                    fire_time=py.time.get_ticks()
                    fc+=1
                if (py.mouse.get_pos()[0] > 190 and\
                    py.mouse.get_pos()[1] < 620 and\
                    py.mouse.get_pos()[0] < 300 and\
                    py.mouse.get_pos()[1] > 464 and\
                    empty.image==otoo_icon):
                    if ox2.current_sprite>=1:
                        o2_refill.play()
                        if ox2.current_sprite>=2:
                            occupation=False
                            empty.image=empty_img
                            o2_group.update(-2)
                        elif ox2.current_sprite>=3:
                            occupation=False
                            empty.image=empty_img
                            o2_group.update(-3)
                        else:
                            occupation=False
                            empty.image=empty_img
                            o2_group.update(-1)

                if (py.mouse.get_pos()[0] > 737 and\
                    py.mouse.get_pos()[1] < 540 and\
                    py.mouse.get_pos()[0] < 783 and\
                    py.mouse.get_pos()[1] > 450 and\
                    empty.image==jerry_icon and on_fire==False):
                    if fuel.current_sprite>=1:
                        refule_sound.play()
                        if fuel.current_sprite>=2:
                            fuel_group.update(-2)
                            occupation=False
                            empty.image=empty_img
                            nf+=1
                        else:
                            fuel_group.update(-1)
                            occupation=False
                            empty.image=empty_img
                            nf+=1
                    
                
                if (py.mouse.get_pos()[0] > 1140 and\
                    py.mouse.get_pos()[1] < 545 and\
                    py.mouse.get_pos()[0] < 1180 and\
                    py.mouse.get_pos()[1] > 485 and\
                    empty.image==wrench and on_fire==False):
                    if pressure.current_sprite>0:
                        random.choice(valve_sounds).play()
                        pressure_group.update(-1)
                
                if empty.image==broom_icon and ammo>0:
                    if (py.mouse.get_pos()[0] > 5 and\
                        py.mouse.get_pos()[1] < 420 and\
                        py.mouse.get_pos()[0] < 110 and\
                        py.mouse.get_pos()[1] > 335)==False and\
                        (py.mouse.get_pos()[0] > 930 and\
                        py.mouse.get_pos()[1] < 149 and\
                        py.mouse.get_pos()[0] < 1038 and\
                        py.mouse.get_pos()[1] > 40)==False:
                            shoot_sound.play()
                            ammo-=1

        if on_fire==True:
            if fire_sound_timer<=0:
                fire_sound.play()
                fire_sound_timer=200
            fire_group.draw(screen)
            fire_group.update(0.5)
        else:
            fire_sound.stop()

        fuel_group.draw(screen)
        if fuel.current_sprite<7:
            fuel_group.update(fuel_use)

        pressure_group.draw(screen)
        if pressure.current_sprite<6:
            pressure_group.update(pressure_change)

        o2_group.draw(screen)
        if ox2.current_sprite<6:
            o2_group.update(o2_use)
        
        if locknload==True:
            screen.blit(shell,(1040,50))
            screen.blit(text,(1130,50))
            py.mouse.set_visible(False)
            crosshair_group1.draw(screen)
            crosshair_group1.update()
        elif empty.image==extinguisher_icon:
            crosshair_group2.draw(screen)
            crosshair_group2.update()
            py.mouse.set_visible(False)
        else:
            py.mouse.set_visible(True)

        py.display.update()
        clock.tick(60)

def space():
    global running, pirate_time, pc, hull, diff, pirate_att, hull
    while running:
        sprt_master.ship_sound.stop()
        is_game_over()
        hazards()

        screen.blit(b4,(0,0))

        if fuel.current_sprite<7:
            fuel_group.update(fuel_use)

        if pressure.current_sprite<6:
            pressure_group.update(pressure_change)

        if ox2.current_sprite<6:
            o2_group.update(o2_use)

        py.mouse.set_visible(False)

        if arrow_d.draw(screen):
            bridge()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                laser_sound.play()
                ded=py.sprite.groupcollide(crosshair_group,pirate_group, False, True, py.sprite.collide_mask)
                if ded:
                    pirate_explosion.play()
                    pirate_time=py.time.get_ticks()
                    pc+=1

        if pirate_att==True:
            pirate_group.draw(screen)

        crosshair_group.draw(screen)
        crosshair_group.update()

        py.display.update()
        clock.tick(60)

def package():
    global running, ammo, roach_time, package_health, rc, diff, infest
    
    while running:
        is_game_over()
        hazards()

        text=font.render(str(ammo),True,BLACK)
        screen.blit(b5,(0,0))
        screen.blit(inv,(930,40))

        if fuel.current_sprite<7:
            fuel_group.update(fuel_use)

        if pressure.current_sprite<6:
            pressure_group.update(pressure_change)

        if ox2.current_sprite<6:
            o2_group.update(o2_use)

        empty.draw(screen)

        if arrow_u.draw(screen):
            walk_sound.play()
            storage()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if empty.image==broom_icon and ammo>0:
                    if (py.mouse.get_pos()[0] > 630 and\
                        py.mouse.get_pos()[1] < 130 and\
                        py.mouse.get_pos()[0] < 710 and\
                        py.mouse.get_pos()[1] > 22)==False and\
                        (py.mouse.get_pos()[0] > 930 and\
                        py.mouse.get_pos()[1] < 149 and\
                        py.mouse.get_pos()[0] < 1038 and\
                        py.mouse.get_pos()[1] > 40)==False:
                            ammo-=1
                            shoot_sound.play()
                        
                    die=py.sprite.groupcollide(crosshair_group1,roach_group, False, True,py.sprite.collide_mask)
                    if die:
                        roach_time=py.time.get_ticks()
                        rc+=1

        if infest==True:
            roach_group.draw(screen)

        if locknload==True:
            screen.blit(shell,(1040,50))
            screen.blit(text,(1130,50))
            py.mouse.set_visible(False)
            crosshair_group1.draw(screen)
            crosshair_group1.update()
        else:
            py.mouse.set_visible(True)

        py.display.update()
        clock.tick(60)

start()
py.quit