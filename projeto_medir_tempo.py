import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        tempo_execucao = time.time() - inicio
        print(f"A função '{func.__name__}'executou em {tempo_execucao:.4f} segundos.")
        return resultado
    return wrapper

@medir_tempo
def medir_tempo(n):
   time.sleep(n)
print (medir_tempo(2))