bytesTotales = int(input("Introduce el número de bytes: "))


gb = bytesTotales // 10**9
mb = (bytesTotales % 10**9) // 10**6
kb = (bytesTotales % 10**6) // 10**3
b = bytesTotales % 10**3

print(bytesTotales," en sistema decimal (SI): ",gb,"GB,",mb,"mb,",kb,"kb,",b,"bytes.")

# Sistema binario (IEC)
gib = bytesTotales // 2**30
mib = (bytesTotales % 2**30) // 2**20
kib = (bytesTotales % 2**20) // 2**10
bBin = bytesTotales % 2**10
print(bytesTotales," en sistema decimal (IEC): ",gib,"gib,",mib,"mib,",kib,"kib,",bBin,"bytes.")
