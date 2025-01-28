import threading
import time

flag = [False, False] 
turn = 0               

# Região crítica: 
def secao_critica(process_id):
    print(f"Processo {process_id} está na região crítica.")
    time.sleep(1) 


# Região não crítica:
def secao_nao_critica(process_id):
    print(f"Processo {process_id} está na região NÃO crítica.")
    time.sleep(1)  


# Processo 0:
def process_0():
    global turn
    while True:
        flag[0] = True 
        turn = 1       

        while flag[1] and turn == 1: # 
            pass 

        # Região crítica:
        secao_critica(0)

        flag[0] = False 

        # Região não crítica:
        secao_nao_critica(0)

# Processo 1:
def process_1():
    global turn
    while True:
        flag[1] = True 
        turn = 0       

        while flag[0] and turn == 0:
            pass 

        # Região crítica:
        secao_critica(1)

        flag[1] = False

        # Região não crítica:
        secao_nao_critica(1)


if __name__ == "__main__":
    t0 = threading.Thread(target=process_0)
    t1 = threading.Thread(target=process_1)

    t0.start()
    t1.start()

    t0.join()
    t1.join()
