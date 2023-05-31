#faktorial genap

def faktorialgenap(jumlah, awal):
    #base case
    if jumlah == 0:
        return 1
    else:
        #rekursif case
        return faktorialgenap(jumlah -1, awal +2) * (awal+2)

#print (faktorialgenap(5,0)) => 2*4*6*8*10
print (faktorialgenap(5,0))