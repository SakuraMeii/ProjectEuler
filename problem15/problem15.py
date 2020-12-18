import scipy.special

def Lattice(row,col):
    if row == 0 or col == 0:
        return(1)
    return Lattice(row-1, col) + Lattice(row, col-1)
def main():
    #print(Lattice(20,20))
    print(scipy.special.comb(40,20))

if __name__ == '__main__':
    main()
