# Buat lah output dari menggunakan bahasa pemprograman python dengan : 
# 1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19 = ….
total = 0

for i in range(1,20,2):
    print(end="+ ")
    print(i, end=" ")
    total += i
print(" = ", total )