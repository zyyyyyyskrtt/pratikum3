Max = 0

while True:
    N = int(input("Masukkan bilangan (0 untuk berhenti): "))
    
    if N == 0:
        print(f"Bilangan terbesar adalah: {Max}")
        break
    
    
    if N > Max:
        Max = N
