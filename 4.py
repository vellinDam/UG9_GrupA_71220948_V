print("=============CAFE================")
print("=========Masukkan Jumlah Pesanan =============")
capucino = int(input("Cappucino        DISKON 50%      Rp 25.000   :"))
Vanilla = int(input("Vanilla Latte     DISKON 65%      Rp 22.000   :"))
americano = int(input("Americano       DISKON 35%      Rp 30.000   :"))
Brewed = int(input("Brewed Coffee      DISKON 40%      Rp 20.000   :"))
cap = (25000*capucino)*0.5
van = (22000*Vanilla)*0.65
ame = (30000*americano)*0.35
bre = (20000*Brewed)*0.4
print ("===================TOTAL====================")
print ("Total Cappucino : ",cap)
print ("Total Vanilla Latte : ",van)
print ("Total Americano : ",ame)
print ("Total Brewed Coffee : ",bre)