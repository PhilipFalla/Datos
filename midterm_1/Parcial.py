from Stack import Stack
#from time import time
#from memory_profiler import profile

class Parcial:
    
    def __init__(self, size):
        self.n = size

    def poblar(self, m):
        
        size = self.n*m

        s = Stack(size)  # Stack de tamaño n
        for _ in range(size):
            s.push("A")
        return s

        """start_time = time()
        s1 = Stack(n)  # Stack de tamaño n
        for _ in range(n):
            s1.push("A")
        end_time = time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")"""