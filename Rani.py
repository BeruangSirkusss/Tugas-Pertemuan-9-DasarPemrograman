Buah_buahan = ["Apel", "Jeruk", "Mangga", "Pisang", "Anggur", "Durian"]
A = []

for i in Buah_buahan:
    if len(i) >= 5:
        A.append(i)
        
A.sort()

print(A)