import time
import board
import digitalio

# Configurar los 4 pines como salida digital
coil_A_1 = digitalio.DigitalInOut(board.GP7)
coil_A_2 = digitalio.DigitalInOut(board.GP8)
coil_B_1 = digitalio.DigitalInOut(board.GP9)
coil_B_2 = digitalio.DigitalInOut(board.GP10)

coil_A_1.direction = digitalio.Direction.OUTPUT
coil_A_2.direction = digitalio.Direction.OUTPUT
coil_B_1.direction = digitalio.Direction.OUTPUT
coil_B_2.direction = digitalio.Direction.OUTPUT

# Secuencia de pasos para 28BYJ-48 (un paso = una activación)
# Esta es una secuencia de 4 pasos (half-stepping también es posible, pero usamos full-step aquí)
step_sequence = [
    [1, 0, 0, 1],  # paso 1
    [1, 0, 0, 0],  # paso 2
    [1, 1, 0, 0],  # paso 3
    [0, 1, 0, 0],  # paso 4
    [0, 1, 1, 0],  # paso 5
    [0, 0, 1, 0],  # paso 6
    [0, 0, 1, 1],  # paso 7
    [0, 0, 0, 1],  # paso 8
]

# Función para activar las bobinas según la secuencia
def set_step(w1, w2, w3, w4):
    coil_A_1.value = w1
    coil_A_2.value = w2
    coil_B_1.value = w3
    coil_B_2.value = w4

# Función para girar el motor N pasos
def step_motor(steps, delay=0.01, direction=1):
    for i in range(steps):
        # El índice depende de la dirección
        index = (i * direction) % len(step_sequence)
        step = step_sequence[index]
        set_step(*step)
        time.sleep(delay)

# Programa principal
try:
    print("Girando sentido horario")
    step_motor(512, delay=0.005, direction=1)  # 512 pasos ≈ 360° con 28BYJ-48

    time.sleep(1)

    print("Girando sentido antihorario")
    step_motor(512, delay=0.005, direction=-1)

    print("Listo.")

    # Apagar las bobinas (opcional pero recomendado)
    set_step(0, 0, 0, 0)

except KeyboardInterrupt:
    print("Interrumpido por usuario")
    set_step(0, 0, 0, 0)
