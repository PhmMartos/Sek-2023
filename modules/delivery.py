from modules.motors import *
from modules.beeps import *
from modules.claw import *

from pybricks.tools import StopWatch

crono = StopWatch()

def go_to_check_point():
    turn_right(90)
    move_backward(1200)
    turn_left(90)

def tube_library():
    
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 600:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)  
    turn_left(90)
    
    crono.reset()
    while not is_yellow_left() and not is_yellow_right():
        andar_reto(360)
    tempo = crono.time()
    brake_motors()
    found_door()
    
    move_forward(300) # Indo para a entrega
    Open()
    move_backward(600) # Volta para a área de coleta a msm distância de ir
    
    turn_left(200)
    
    while not is_blue():
        andar_reto(360)
    brake_motors()
    
        
    
def tube_city_hall():
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 3200: # Tenho que olhar isso
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left(90)
    move_forward(1000) # Está indo em direção ao objeto J
    
    if has_obstacle(): #sensor identificou objeto "J":
        move_backward(1000)
        turn_right(180)
        while not is_blue():
            andar_reto(360)
        brake_motors()
        while is_blue():
            andar_reto(-360)
        turn_left(90)
        branco = 88 
        azul = 14 #22
        threshold = (branco + azul) / 2  # = 40
        vel = 100
        crono.reset()
        while crono.time() < 6500: # Tenho que olhar isso
            delta = red_right() - threshold
            kp = 0.5
            erro = delta * kp
            motors.drive(vel, erro)
            
        turn_left(90)
        move_forward(3000)
        turn_left(90)
        move_forward(2000)
        Open()
        #retorna para a área de coleta
        move_backward(2000)
        turn_left(90)
        while not is_blue():
            andar_reto(360)
        brake_motors()
    
    else:
        #objeto J não existe
        move_forward(2500)#Distancia pequena 3500
        turn_right(90)
        
        #tentativa de se alinhar
        while not is_yellow_left() and not is_yellow_right():
            andar_reto(360)
        brake_motors()
        
        move_forward(1000)
        Open()
        #retorna para a área de coleta
        move_backward(1500)
        turn_right(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        

    
def tube_school():
    
    crono.reset()
    branco = 88 
    azul = 14 #22 
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 9500:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left(90)
    move_forward(1000)
    
    if has_obstacle(): #sensor identificou objeto "i":
        move_backward(1000)
        turn_left(180)
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
        
        while is_blue():
            andar_reto(-360)
        brake_motors()
        turn_right(90)
        branco = 80
        azul = 10
        threshold = (branco + azul) / 2  # = 40
        vel = 100
        crono.reset()
        
        
        while crono.time() < 6500:
            delta = threshold - red_left()
            kp = 0.8
            erro = delta * kp
            motors.drive(vel, erro)
        turn_right(90)
        #De frente para o J
        move_forward(6000)
        
        #G
        turn_right(90)
        move_forward(1000)
        if has_obstacle(): #Objeto "G":
            move_backward(1000)
            turn_left(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            cor_vista = "PAREDE"
            brake_motors()
            ajust_color(cor_vista)
            move_backward(500)
            turn_right(90)#
            
            
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_visita = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho")
            move_backward(2800)
            turn_right(90)
            move_forward(6500)
            turn_left(90)
            
            
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_visita = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho 2")
            
            move_backward(500)
            turn_right(90)
            move_forward(1000)
            Open()
            move_backward(1000)
            turn_right(90)
            
            #começa caminho de volta
            
            move_forward(3000)
            turn_right(90)
            while not is_black_left() and not is_black_right():
                andar_reto(360)
            brake_motors()
            cor_vista = "PAREDE"
            ajust_color(cor_vista)
            move_backward(1000)
            turn_left(90)
            while not is_red_left() and not is_red_right():
                andar_reto(360)
            brake_motors()
            cor_visita = "VERMELHO"
            ajust_color(cor_vista)
            print("Bati no vermelho")
            move_backward(3500)
            turn_left(90)
            while not is_blue():
                andar_reto(540)
        else:
            #abre e retorna
            Open()
            move_backward(2)
            turn_right(90)
            move_forward(6)
            turn_left(90)
            move_forward(4)
    else:
        move_forward(2500)#Distancia pequena 3500
        turn_right(90)
        
        #tentativa de se alinhar
        while not is_yellow_left() and not is_yellow_right():
            andar_reto(360)
        brake_motors()
        
        move_forward(1000)
        Open()
        #retorna para a área de coleta
        move_backward(1500)
        turn_right(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
def tube_museum():
    
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  
    vel = 100
    while crono.time() < 3500: #4000
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left(90)
    move_forward(1000) # Está indo em direção ao objeto J
    
    if has_obstacle(): #sensor identificou objeto "j":
        turn_right(90)
        move_forward(4)
        turn_left(90)
        move_forward(4)
        turn_left(90)
        move_forward(2)
        if has_obstacle(): #sensor identificou objeto G:
            move_backward(2)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
            turn_right(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            move_forward(8)
        else:
            move_forward(6)
            turn_right(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(2)
            turn_right(90)
            move_forward(4) 
            
    else: # objeto J não existe
        print("Não existe J")
        move_forward(3000, 540)
        turn_left(90)
        move_forward(1000)
    
    if has_obstacle(): #Objeto "H":
        turn_right(90)
        move_forward(2)
        turn_left(90)
        move_forward(2)
        # Abre e retorna
        move_backward(2)
        turn_left(90)
        move_forward(6)
        
    else: #Objeto "H" não existe
        print("Não existe H")
        while not is_red_left() and not is_red_right():
            andar_reto(360)
        brake_motors()
        
        print("Achou vermelho")
        cor_vista = "VERMELHO"
        ajust_color(cor_vista)
        
        move_backward(500)
        
        turn_right(90)
        move_forward(1300)
        
        Open()
        
        #retorna para a área de coleta
        move_backward(1500)
        turn_right(90)
        move_forward(3000)
        turn_right(90)
        
        # No futuro, tentar ver a mudança do J
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
                
def tube_drugstore():
    
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 3250:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left(90)
    move_forward(1000)
    
    if has_obstacle(): #Objeto "J":
        turn_right(90)
        move_forward(4)
        turn_left(90)
        move_forward(4)
        turn_left(90)
        
        if has_obstacle(): #Objeto "G":
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(2)
            turn_left(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_left(90)
            move_forward(3)
            turn_right(90)
            move_forward(8)
        else:    
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_right(90)
            move_forward(4)
    else:
        move_forward(4000) # Mesmo valor do museum
        turn_right(90)
    
    if has_obstacle(): #Objeto "G":
        turn_left(90)
        if has_obstacle(): #Objeto "E":
            move_backward(5)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(9)
            turn_left(90)
            move_forward(3)
            turn_left(90)
            move_forward(2)
            #Abre e solta
            move_backward(2)
            turn_left(90)
            move_forward(3)
            turn_right(90)
            move_forward(9) 
        else:
            move_forward(4)
            turn_right(90)
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_left(90)
            move_forward(8)
    else:
        move_forward(2500)
        turn_left(90)
        move_forward(1000)
        
        
        Open() #Entregou
        
        move_backward(1000)
        turn_left(90)
        move_forward(2000)
        turn_left(90)
        
        # Voltando para área de coleta
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
def tube_bakery():
    crono.reset()
    branco = 88 
    azul = 14 #22
    threshold = (branco + azul) / 2  # = 40
    vel = 100
    while crono.time() < 9500:
        delta = red_right() - threshold
        kp = 0.5
        erro = delta * kp
        motors.drive(vel, erro)

    brake_motors()
    turn_left(95)
    move_forward(1000)
    
    if has_obstacle(): #Objeto "I":
        turn_left(90)
        move_forward(5)
        turn_right(90)
        move_forward(4)
        if has_obstacle(): #objeto "E":
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
        else:
            move_forward(4)
            turn_right(90)
        
        if has_obstacle(): #OBJETO B"
            turn_right(90)
            move_forward(5)
            turn_left(90)
            move_forward(4)
            turn_left(90)
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(3)
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
        else:
            move_forward(4)
        if has_obstacle(): #objeto "A":
            turn_right(90)
            move_forward(3)
            turn_left(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(2)
            turn_right(90)
            move_forward(5)
            turn_left(90)
            move_forward(4)
        else:
            move_forward(2)
            turn_right(90)
            move_forward(2)
            #Abre e retorna
            move_backward(2)
            turn_right(90)
            move_forward(6)
            turn_left(90)
            move_forward(8)
    else:
        move_forward(7200)
    
    if has_obstacle(): #Objeto "D":
        turn_left(90)
        move_forward(1)
        if has_obstacle(): #Objeto "G":
            turn_left(90)
            move_forward(4)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            move_forward(8)
            
        
        if has_obstacle(): #objeto "A":
            move_back()
            turn_right(90)
            move_forward()
            turn_left(90)
            move_forward()
            #Abre e retorna
        
        move_backward()
        turn_right(90)
        move_forward()
        turn_left(90)
        move_forward()        
        #Abre e retorna
    else:
        turn_right(90)
        move_forward(2500)
        
        
        Open() #Entregou
        
        move_backward(2500)
        turn_right(90)
        
        while not is_blue():
            andar_reto(360)
        brake_motors()
        
    
def tube_park():
    move_forward(3500)
    turn_left(90)
    if has_obstacle(): #objeto "J":
        turn_right(90)
        move_forward(4)
        turn_left(90)
        move_forward(4)
        if has_obstacle(): #objeto "D":
            turn_left(90)
            move_forward(4)
            turn_right(90)
            move_forward(4)
            turn_right(90)
            if has_obstacle(): #objeto "B":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
                move_backward(2)
                turn_right(90)
                move_forward(4)
                turn_right(90)
                move_forward(4)
                turn_left(90)
                move_forward(4)
                turn_right(90)
                move_forward(2)
            else:
                move_forward(4)
                turn_left(90)
                move_forward(2)
                #Abre e retorna
        else:
            move_forward(4)
            turn_right(90)
            if has_obstacle(): #objeto "A":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(2)
                turn_left(90)
                move_forward(2)
                #Abre e retorna
    else:
        move_forward(4750)
        if has_obstacle(): #objeto "E":
            turn_right(90)
            move_forward(4)
            turn_left(90)
            move_forward(4)
            turn_right(90)
            if has_obstacle(): #objeto "A":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(2)
                turn_left(90)
                move_forward(2)
                #Abre e retorna
        else:
            move_forward(7000)
            turn_right(90)
            if has_obstacle(): #objeto "B":
                turn_180()
                move_forward(2)
                turn_right(90)
                move_forward(2)
                #Abre e retorna
            else:
                move_forward(3500)
                turn_left(90)
                move_forward(1750)
                #Abre e retorna