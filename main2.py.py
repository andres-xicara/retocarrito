import time
import board
import digitalio
import pwmio
import digitalio
import time
from pwmio import PWMOut

#Motores adelante y atras
Dir_forward = 1
Dir_backward = -1

# Motores izquierda
LF_forward = 1
LF_backward = -1
LB_forward = 1
LB_backward = -1

# Motores derecha
RF_forward = -1
RF_backward = 1
RB_forward = -1
RB_backward = 1

#Mapeo de velocidad en PWM
def map(x, in_max, in_min, out_max, out_min):
    return (x - in_min) / (in_max - in_min) * (out_max - out_min) + out_min

#Configuracion motores
# Motor izquierdo frontal (M1)
Motor_LF_PWM = PWMOut(board.GP12)
Motor_LF_PWM.duty_cycle = 0
Motor_LF_Dir = digitalio.DigitalInOut(board.GP13)
Motor_LF_Dir.direction = digitalio.Direction.OUTPUT
Motor_LF_Dir.value = False

# Motor derecho frontal (M2)
Motor_RF_PWM = PWMOut(board.GP15)
Motor_RF_PWM.duty_cycle = 0
Motor_RF_Dir = digitalio.DigitalInOut(board.GP14)
Motor_RF_Dir.direction = digitalio.Direction.OUTPUT
Motor_RF_Dir.value = False

# Motor derecho trasero (M3)
Motor_RB_PWM = PWMOut(board.GP16)
Motor_RB_PWM.duty_cycle = 0
Motor_RB_Dir = digitalio.DigitalInOut(board.GP17)
Motor_RB_Dir.direction = digitalio.Direction.OUTPUT
Motor_RB_Dir.value = False

# Motor izquierdo trasero (M4)
Motor_LB_PWM = PWMOut(board.GP19)
Motor_LB_PWM.duty_cycle = 0
Motor_LB_Dir = digitalio.DigitalInOut(board.GP18)
Motor_LB_Dir.direction = digitalio.Direction.OUTPUT
Motor_LB_Dir.value = False

class Motor():
    def __init__(self):
        pass


    def motor_left_front(self, status, direction, speed):
        if status == 0:
            Motor_LF_Dir.value = False
            Motor_LF_PWM.duty_cycle = 0
        else:
            value = int(map(speed, 100, 0, 65535, 0))
            Motor_LF_Dir.value = False if direction == Dir_forward else True
            Motor_LF_PWM.duty_cycle = value if direction == Dir_forward else 65535 - value

    def motor_right_front(self, status, direction, speed):
        if status == 0:
            Motor_RF_Dir.value = False
            Motor_RF_PWM.duty_cycle = 0
        else:
            value = int(map(speed, 100, 0, 65535, 0))
            Motor_RF_Dir.value = False if direction == Dir_forward else True
            Motor_RF_PWM.duty_cycle = value if direction == Dir_forward else 65535 - value

    def motor_right_back(self, status, direction, speed):
        if status == 0:
            Motor_RB_Dir.value = False
            Motor_RB_PWM.duty_cycle = 0
        else:
            value = int(map(speed, 100, 0, 65535, 0))
            Motor_RB_Dir.value = False if direction == Dir_forward else True
            Motor_RB_PWM.duty_cycle = value if direction == Dir_forward else 65535 - value

    def motor_left_back(self, status, direction, speed):
        if status == 0:
            Motor_LB_Dir.value = False
            Motor_LB_PWM.duty_cycle = 0
        else:
            value = int(map(speed, 100, 0, 65535, 0))
            Motor_LB_Dir.value = False if direction == Dir_forward else True
            Motor_LB_PWM.duty_cycle = value if direction == Dir_forward else 65535 - value

    def motor_stop(self):
        Motor_LF_Dir.value = False
        Motor_LF_PWM.duty_cycle = 0
        Motor_LB_Dir.value = False
        Motor_LB_PWM.duty_cycle = 0
        Motor_RF_Dir.value = False
        Motor_RF_PWM.duty_cycle = 0
        Motor_RB_Dir.value = False
        Motor_RB_PWM.duty_cycle = 0

if __name__ == '__main__':
    motor = Motor()
    try:
        motor.motor_stop()
        time.sleep(5)
        # motor left back M4
        # motor right front M2
        # motor right back M3
        # motor left front M1

        # SECUENCIA 1 - Llevar carrito a estación 2
        print("Avanza hasta llegar al carrito...")
        motor.motor_left_back(1, LB_forward, 40)
        motor.motor_right_front(1, RF_forward, 40)
        motor.motor_right_back(1, RB_forward, 40)
        motor.motor_left_front(1, LF_forward, 40)
        time.sleep(4)  # Simula llegar al carrito

        print("Frena...")
        motor.motor_stop()
        time.sleep(1)

        print("Gancho ACTIVADO (simulado)")
        time.sleep(1)

        print("Avanza con el carrito hasta estación 2...")
        motor.motor_left_back(1, LB_forward, 40)
        motor.motor_right_front(1, RF_forward, 40)
        motor.motor_right_back(1, RB_forward, 40)
        motor.motor_left_front(1, LF_forward, 40)
        time.sleep(4)  # Simula llegar a estación 2

        print("Frena...")
        motor.motor_stop()
        time.sleep(1)

        print("Gancho DESACTIVADO (simulado)")
        time.sleep(1)

        print("Avanza un poco para separarse del carrito...")
        motor.motor_left_back(1, LB_forward, 40)
        motor.motor_right_front(1, RF_forward, 40)
        motor.motor_right_back(1, RB_forward, 40)
        motor.motor_left_front(1, LF_forward, 40)
        time.sleep(2)

        motor.motor_stop()
        time.sleep(1)




        # GIRO 180 GRADOS (reverso de un lado y avance del otro)
        print("Gira 180 grados...")
        motor.motor_left_front(1, LF_backward, 40)
        motor.motor_right_front(1, RF_forward, 40)
        motor.motor_left_back(1, LB_backward, 40)
        motor.motor_right_back(1, RB_forward, 40)
        time.sleep(2.5)

        motor.motor_stop()
        time.sleep(1)





        # SECUENCIA 2 - Llevar segundo carrito a estación 1
        print("Avanza hasta llegar al segundo carrito...")
        motor.motor_left_back(1, LB_forward, 40)
        motor.motor_right_front(1, RF_forward, 40)
        motor.motor_right_back(1, RB_forward, 40)
        motor.motor_left_front(1, LF_forward, 40)
        time.sleep(4)

        print("Frena...")
        motor.motor_stop()
        time.sleep(1)

        print("Gancho ACTIVADO (simulado)")
        time.sleep(1)

        print("Avanza con el carrito hasta estación 1...")
        motor.motor_left_back(1, LB_forward, 40)
        motor.motor_right_front(1, RF_forward, 40)
        motor.motor_right_back(1, RB_forward, 40)
        motor.motor_left_front(1, LF_forward, 40)
        time.sleep(4)

        print("Frena...")
        motor.motor_stop()
        time.sleep(1)

        print("Gancho DESACTIVADO (simulado)")
        time.sleep(1)

        print("Avanza un poco para separarse del carrito...")
        motor.motor_left_back(1, LB_forward, 40)
        motor.motor_right_front(1, RF_forward, 40)
        motor.motor_right_back(1, RB_forward, 40)
        motor.motor_left_front(1, LF_forward, 40)
        time.sleep(2)

        print("Deteniendo motores...")
        motor.motor_stop()

    except KeyboardInterrupt:
        motor.motor_stop()    