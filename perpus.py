import os

os.system("cls")

def men():
    print("""MENU\n
    1.Tambah   Barang 
    2.Hapus    Barang
    3.Lihat    Barang
    4.Pembelian
    5.Pemasukan dan Penjualan
    6.Keluar
    """)
def clear():
    os.system("cls")
    print("\n")
data_bar=[]
def barang(data_bar):
    print("Tambah   Barang\n")
    tampung=[]
    a=int(input("Jumlah barang: "))
    tampung.append(a)
    b=input("Nama barang  : ")
    tampung.append(b)
    c=int(input("Harga barang : "))
    tampung.append(c)
    data_bar.append(tampung)
    return data_bar
def hapus(data_bar):
    if len(data_bar)==0:
        print("tidak ada barang")
    else:
        print("Hapus Barang\n")
        a=int(input("ketik no barang yang akan dihapus: "))
        print("\n\t{} berhasil dihapus".format(data_bar[a-1][1]))
        data_bar.pop(a-1)
def lihat(a):
    print("| No |  Stok  |     Nama     | Harga |\n"+"="*38)
    for i in range(len(a)):
        print("| %-2s | %-6s | %-12s | %-5s |"%(i+1,a[i][0],a[i][1],a[i][2])) 

def menu2():
    clear()
    lihat(data_bar)
    print("\n")
    hapus(data_bar)

pemasu=[]
def masuk():
    print("Pemasukan dan Penjualan\n")
    print("| No | Pemasukan |    Barang    | Banyak |\n"+"="*42)
    for i in range(len(pemasu)):           
        print("| %-2s | %-9s | %-12s | %-6s |"%(i+1,pemasu[i][0],pemasu[i][1],pemasu[i][2]))                

bar=""
ban=0
def beli(bar,ban):
    clear()
    lihat(data_bar)
    print("\nPembelian\n")
    bar=input("nama barang    : ")
    ban=int(input("banyak barang  : "))
    return bar, ban
sisa=0
def sis(sisa):
    i.pop(0)
    i.insert(0, jum)
    masu=[]
    masu.append(tot)
    masu.append(bar)
    masu.append(ban)
    pemasu.append(masu)
    print("harga total    :",tot)
    uan=int(input("\nuang anda      : "))
    sisa=uan-tot
    return sisa
while 1:
    clear()
    men()
    menu=int(input("\nmasukan menu(angka): "))
    if menu==1:
        while 1:
            clear()
            data_bar=barang(data_bar)
            b=input("\ntambah lagi? (y/n): ").lower()
            if b=="y":
                continue
            else:
                break            
    elif menu==2:
        while 1:
            menu2()
            if len(data_bar)!=0:
                b=input("\nhapus barang lagi? (y/n): ").lower()
                if b=="y":
                    continue
                else:
                    break
            else:
                b=input("\ntekan enter untuk kembali ke menu : ").lower()
                if b=="":
                    break
                else:
                    break
    elif menu==3:
        while 1:
            clear()
            print("lihat barang\n")
            lihat(data_bar)
            b=input("\ntekan enter untuk kembali ke menu : ").lower()
            if b=="":
                break
            else:
                break
    elif menu==4:
        batas=True
        bar,ban=beli(bar,ban)
        while batas:
            a=False
            for i in data_bar:
                if bar in i:
                    a=True
                    break
                else:
                    a=False
            if a==True:
                tot=i[2]*ban
                jum=i[0]-ban
                if jum>0:
                    sisa=sis(sisa)
                    if sisa>=0:
                        print("uang kembalian :",sisa)
                        b=input("\ntekan enter untuk kembali ke menu : ")
                        if b=="":
                            batas=False
                            break
                        else:
                            batas=False
                            break
                    else:
                        print("maaf, uang anda tidak cukup\n")
                        b=input("\ntekan enter untuk kembali ke menu : ")
                        if b=="":
                            batas=False
                            break
                        else:
                            batas=False
                            break
            else:
                print("\nmaaf, kami tidak punya barang tersebut\n")
                b=input("tekan enter untuk kembali ke menu : ")
                if b=="":
                    batas=False
                    break
                else:
                    batas=False
                    break  
    elif menu==5:
        while 1:
            clear()
            masuk()
            b=input("\ntekan enter unutk kembali ke menu : ").lower()
            if b=="":
                break
            else:
                break
    else:
        break