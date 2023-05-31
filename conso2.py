#konversi ip address

def binary_to_dex (biner, pangkat = 0):
    #base case
    if biner == "0":
        return 0
    elif biner == "1":
        return pow(2,pangkat)
    else:
        last_digit = int(biner[-1])
        if last_digit == 0:
            return binary_to_dex(biner[:-1], pangkat +1)
        else:
            return binary_to_dex(biner[:-1], pangkat + 1) + pow(last_digit*2, pangkat)
        
def bagi_biner(biner):
    #pecah jadi 4 biji
    pecahan = biner.split(".")
    for i in range (len(pecahan)):
        pecahan[i] = binary_to_dex(pecahan[i])
    hasil = (f"{pecahan[0]}.{pecahan[1]}.{pecahan[2]}.{pecahan[3]}")
    return hasil
    

print(bagi_biner("1001.1001.1001.1111"))
