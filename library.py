import csv # import csv untuk membaca dan menuliskan kedalam file csv
import os # import os untuk membersikan screen pada terminal
from pathlib import Path # menggunakan fungsi pathlib dari modul Path
from datetime import datetime as tanggal # menggunakan fungsi datetime dari modul datetime

### DATA ADMIN ### 

def adminCsv(arg1): # mendefinisikan function adminCsv dengan parameter arg1
    # membuka file csv dan menggunakan mode write (tulis) untuk menulis pada file csv
    with open('admin.csv', 'w', newline='') as f:
        # membuat header pada file csv
        header = csv.DictWriter(f, fieldnames=arg1,  delimiter=',')
        header.writeheader()

def daftar(): # mendefinisikan function daftar
    os.system('cls') # menghapus tampilan layar sebelumnya pada terminal
    print("=" * 30) # menampilkan “=” sebanyak 30 kali
    print("======== DAFTAR AKUN ========") # menampilkan DAFTAR AKUN
    print("=" * 30) # menampilkan “=” sebanyak 30 kali

    with open('admin.csv', 'a', newline='') as file:
        # menulis data pada file csv
        data_admin = csv.writer(file)
        username = input("Masukkan Nama: ") # admin menginput nama
        password = input("Masukkan Kata Sandi: ") # admin menginput kata sandi

        data_admin.writerow([username, password])
        file.close()
        login()

def masuk(): # mendefinisikan function masuk
    os.system('cls') # menghapus tampilan layar sebelumnya pada terminal
    print("=" * 30) # menampilkan “=” sebanyak 30 kali
    print("=========== MASUK ============") # menampilkan MASUK
    print("=" * 30) # menampilkan “=” sebanyak 30 kali

    username = input("Masukkan Nama: ")
    password = input("Masukkan Kata Sandi: ")

    data = [] 
    with open("admin.csv", 'r') as file: # membuka file dalam file CSV dengan mode read 
        # membaca data pada file csv 
        csvreader = csv.reader(file)
        for row in csvreader: # menginterasikan baris yang ada pada csvreader
            data.append(row)
    index = 0
    for i in range(len(data) - 1):
        index += 1
        if (data[index][0] == username) and (data[index][1] == password):
            mainMenu()
    login()

### DATA BUKU ### 

def bukuCsv(arg2): # mendefiniskan function bukuCsv dengan parameter arg2
    #Membuka file csv dan menggunakan mode write (tulis) untuk menulis pada file csv
    with open('buku.csv', 'w', newline='') as f:
        # membuat header pada file csv
        header = csv.DictWriter(f, fieldnames=arg2,  delimiter=',')
        header.writeheader()

def tambahBuku(): # mendefinisikan function tambahBuku
    os.system('cls') # menghapus tampilan layar sebelumnya pada terminal
    print('=' * 60) # menampilkan “=” sebanyak 60 kali
    print('=' * 21, 'TAMBAH DATA BUKU', '=' * 21) # menampilkan “=” sebanyak 21 kali dan TAMBAH DATA BUKU
    print('=' * 60) # menampilkan “=” sebanyak 60 kali

    with open('buku.csv', 'a', newline='') as file: # membuka file csv dan menambahkan data menggunakan mode append
        # menulis data buku pada file csv
        data_buku = csv.writer(file)
        judul = input('Masukkan judul buku: ') # admin menginput judul buku
        penulis = input('Masukkan penulis buku: ') # admin menginput penulis buku
        genre = input('Masukkan genre buku: ') # admin menginput genre buku
        #judul, penulis, dan genre yang telah dimasukkan akan ditambahkan secara otomatis pada file csv 
        data_buku.writerow([judul, penulis, genre])
        file.close()
        menuBuku()

def editBuku(): # mendefinisikan function editBuku
    tampilBuku() # memanggil tampilBuku untuk menampilkan data buku
    print('—' * 75) # menampilkan '—' sebanyak 75 kali

    data = []
    with open("buku.csv", 'r') as file: # membuka file csv dengan mode read 
        # membaca data buku pada file csv
        csvreader = csv.reader(file)
        for row in csvreader: # menginterasikan kolom yang ada pada csvreader
            data.append(row)

    edit = int(input("Pilih nomor data buku yang ingin diubah: ")) # admin memilih nomor buku yang ingin diubah
    if edit > len(data) - 1: # jika edit lebih besar dari panjang data
        editBuku() # kembali ke inputan edit

    judul = input('Masukkan judul buku: ') # admin menginput judul buku yang akan diubah
    penulis = input('Masukkan penulis buku: ') # admin menginput penulis buku yang ingin diubah
    genre = input('Masukkan genre buku: ') # admin menginput genre buku yang akan diubah
 
    index = 0
    for i in range(len(data)): # menginterasikan seluruh data yang ada pada jangkauan data
        if i == edit: # jika format data sesuai dengan edit
            data[index][0] = judul
            data[index][1] = penulis
            data[index][2] = genre
        index += 1

    head = data.pop(0)
    with open("buku.csv", "w", newline="") as file: # membuka dan menulis file csv dengan mode write
        header = csv.DictWriter(file, fieldnames=head)
        # menggunakan .writeheader() untuk mengembalikan nilai yang dikembalikan menggunakan .writerow() dengan perulangan for dalam data. 
        # sehingga data yang sudah diperbarui akan ditulis ke dalam file csv dan mengganti data yang diinginkan.
        header.writeheader()
        for i in data:  
            header.writerow({'Judul Buku': i[0], 'Penulis': i[1], 'Genre': i[2]})
    menuBuku()

def hapusBuku(): # mendefinisikan function hapusBuku
    tampilBuku() # memanggil tampilBuku untuk menampilkan data buku
    print('—' * 75) # menampilkan '—' sebanyak 75 kali

    data = []
    with open("buku.csv", 'r') as file: #membuka file csv dengan mode read 
        # membaca data buku pada file csv
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)

    hapus = int(input("Pilih nomor data buku yang ingin dihapus: ")) # admin memilih nomor data buku dalam bentuk integer
    if hapus > len(data) - 1: # jika inputan lebih besar dari jumlah data
        hapusBuku() # maka kembali ke inputan hapus 

    index = 0
    for i in range(len(data)): # menginterasikan seluruh data yang ada pada jangkauan data
        if i == hapus: # jika nomor yang dimasukkan ada pada data, maka
            # menghapus data buku sesuai nomor yang dimasukkan
            data.remove(data[index])
        index += 1
    
    head = data.pop(0)
    with open("buku.csv", "w", newline="") as file: # membuka dan menulis pada file csv dengan mode write
        header = csv.DictWriter(file, fieldnames=head)
        # menggunakan .writeheader() untuk mengembalikan nilai yang dikembalikan menggunakan .writerow() dengan perulangan for dalam data. 
        # sehingga data yang sudah diperbarui akan ditulis ke dalam file SCV dan menghapus data yang diinginkan.
        header.writeheader() 
        for i in data:
            header.writerow({'Judul Buku': i[0], 'Penulis': i[1], 'Genre': i[2]})
    menuBuku()

def tampilBuku(): # mendefinisikan function tampilBuku
    os.system('cls')

    data = []
    with open("buku.csv", 'r') as file: #membuka file csv dengan mode read 
        # membaca data buku pada file csv
        csvreader = csv.reader(file)
        for row in csvreader: # menginterasikan kolom yang ada pada csvreader
            data.append(row)

    header = data.pop(0)
    header.insert(0, 'No')
    nomor = 1

    print('=' * 75)  #menampilkan "=" sebanyak 75 kali
    print('=' * 32, 'DATA BUKU', '=' * 32) # menampilkan "=" sebanyak 35 kali dan DATA BUKU
    print('=' * 75) # menampilkan "=" sebanyak 75 kali
    print(f"{header[0]}\t {header[1]}\t\t\t {header[2]}\t {header[3]}") # menampilkan header sesuai dengan index-nya
    print('—' * 75) # menampilkan "=" sebanyak 75 kali

    for i in data: # menginterasikan data dalam jangkauan data
        print(f"{nomor}\t {i[0]}\t\t {i[1]}\t {i[2]}") # menampilkan data sesuai row atau index
        nomor += 1
    file.close()

def dataBuku(): # mendefinisikan function dataBuku
    tampilBuku() # memanggil tampilBuku untuk menampilkan data buku
    print('—' * 75) # menampilkan "=" sebanyak 75 kali
    input("Tekan enter untuk kembali ke menu") # admin bisa menekan enter untuk kembali pada menu buku
    os.system('cls') # menghapus tampilan layar sebelumnya secara otomatis pada terminal
    menuBuku() # kembali ke menuBuku

### DATA PEMINJAMAN ###

def peminjamanCsv(arg3): # mendefiniskan function peminjamanCsv dengan parameter arg3
    # membuka file csv dan menggunakan mode write (tulis) untuk menulis pada file csv
    with open('peminjaman.csv', 'w', newline='') as f: 
        # membuat header pada file csv
        header = csv.DictWriter(f, fieldnames=arg3,  delimiter=',')
        header.writeheader()

def tambahPeminjaman(): # mendefinisikan function tambahPeminjam
    os.system('cls') # menghapus tampilan layar sebelumnya pada terminal 
    print('=' * 60) # menampilkan '=' sebanyak 60 kali
    print('=' * 18, 'TAMBAH DATA PEMINJAMAN', '=' * 18) # menampilkan TAMBAH DATA PEMINJAMAN dan (=) sebanyak 18 kali
    print('=' * 60) # menampilkan '=' sebanyak 60 kali

    # membuka file csv dan menambahkan data ke dalam file CSV secara otomatis menggunakan mode append (tambah)
    with open('peminjaman.csv', 'a', newline='') as file:
        # menulis data peminjaman pada file csv
        data_pinjam = csv.writer(file)
        nama = input('Masukkan nama peminjam: ')
        nim = input('Masukkan NIM peminjam: ')

        # mengambil dan menampilkan data pada file buku.csv untuk diambil bagian Judul buku
        buku = []
        f = open('buku.csv', 'r') # membuka file csv dengan mode read
        reader = csv.reader(f)
        for row in reader:
            buku.append(row)

        header = buku.pop(0)
        header.insert(0, 'No')
        nomor = 1

        print('=' * 40) # menampilkan '=' sebanyak 40 kali
        print('=' * 14, 'DATA BUKU', '=' * 15) # menampilkan DATA BUKU dan "=" sebanyak 14 dan 15 kali
        print('=' * 40) # menampilkan '=' sebanyak 50 kali
        print(f'{header[0]}\t {header[1]}') # menampilkan data buku dengan mengambil row 0 sebagai nomor dan 1 sebagai judul buku
        print('—' * 40)

        for i in buku: # menginterasikan data dalam jangkauan buku
            print(f"{nomor}\t {i[0]}") # menampilkan row judul buku
            nomor += 1
        print('—' * 40)

        inputbuku = input('Masukkan nomor buku: ') # admin menginput judul buku yang ingin dipinjam

        if inputbuku == '': # jika inputan kosong, maka
            print("Mohon maaf, isi dengan benar") # tampil alert dan kembali ke menu
            input('tekan enter untuk kembali ke menu ')
            menuPeminjaman()

        elif int(inputbuku) > len(buku): # jika inputan melebihi jumlah data, maka
            print("Mohon maaf, data buku tidak ada") # tampil alert dan kembali ke menu
            input('tekan enter untuk kembali ke menu ')
            menuPeminjaman()

        else:
        # menentukan tanggal sesuai hari (ini)
            tgl = tanggal.now() # menampilkan tanggal saat pengguna meminjam buku secara otomatis
            tgl_pinjam = (str(tgl.day) + '/' + str(tgl.month) + '/' + str(tgl.year)) # format penulisan tanggal yang disimpan dalam variabel tgl_pinjam
            tgl_balik = tgl.day + 14 # rumus pengembalian buku dimulai saat pengguna menginputkan data dan dikembalikan paling lama 14 hari
            tgl_kembali = (str(tgl_balik) +'/' + str(tgl.month) + '/' + str(tgl.year)) # format penulisan tanggal pengembalian buku yang disimpan dalam variabel tgl_kembali

            # nama, nim, buku, data, tgl_pinjam, tgl_kembali akan ditambahkan secara otomatis pada file csv 
            data_pinjam.writerow([nama, nim, buku[int(inputbuku) - 1][0], tgl_pinjam, tgl_kembali])
            file.close()
            menuPeminjaman()

def editPeminjaman(): # mendefinisikan function editPeminjaman
    tampilPeminjaman() # memanggil tampilanPeminjaman
    print("—" * 120)

    data = []
    with open("peminjaman.csv", 'r') as file: # membuka file dalam file csv dengan mode read 
        # membaca data buku pada file csv
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)

    edit = int(input("Pilih nomor : ")) # admin memilih nomor data peminjaman yang ingin diedit
    if edit > len(data) - 1:
        editPeminjaman()

    nama = input('Masukkan nama baru : ') # admin menginput nama baru
    nim = input('Masukkan NIM peminjam: ') # admin menginput NIM peminjam

    # mengambil dan menampilkan data pada file buku.csv untuk diambil bagian Judul buku
    buku = []
    f = open('buku.csv', 'r') # membuka file csv dengan mode read
    reader = csv.reader(f)
    for row in reader:
        buku.append(row)

    header = buku.pop(0)
    header.insert(0, 'No')
    nomor = 1

    print('=' * 40) # menampilkan = sebanyak 40 kali
    print('=' * 14, 'DATA BUKU', '=' * 15) # menampilkan DATA BUKU dan "=" sebanyak 14 dan 15 kali
    print('=' * 40) # menampilkan = sebanyak 40 kali
    print(f'{header[0]}\t {header[1]}') # menampilkan data buku dengan mengambil row 0 sebagai nomor dan 1 sebagai judul buku
    print('—' * 40)

    for i in buku: # menginterasikan data dalam jangkauan buku
        print(f"{nomor}\t {i[0]}") # menampilkan row judul buku
        nomor += 1
    print('—' * 40) #menampilkan '—' sebanyak 40 kali

    inputbuku = input('Masukkan nomor buku: ') # admin menginput judul buku

    if inputbuku == '': # jika inputan kosong, maka
        print("Mohon maaf, isi dengan benar") # tampil alert dan kembali ke menu
        input('tekan enter untuk kembali ke menu ')
        menuPeminjaman()

    elif int(inputbuku) > len(buku): # jika inputan melebihi jumlah data, maka
        print("Mohon maaf, data buku tidak ada") # tampil alert dan kembali ke menu
        input('tekan enter untuk kembali ke menu ') 
        menuPeminjaman()

    else:
        # menentukan tanggal sesuai hari (ini)
        tgl = tanggal.now() # menampilkan tanggal saat pengguna meminjam buku secara otomatis
        tgl_pinjam = (str(tgl.day) + '/' + str(tgl.month) + '/' + str(tgl.year)) # format penulisan tanggal yang disimpan dalam variabel tgl_pinjam
        hr_ini = tgl.day 
        tgl_balik = hr_ini + 14  # rumus pengembalian buku dimulai saat pengguna menginputkan data dan dikembalikan paling lama 14 hari
        tgl_kembali = (str(tgl_balik)+'/'+str(tgl.month)+'/'+str(tgl.year)) # format penulisan tanggal pengembalian buku  yang disimpan dalam variabel tgl_kembali

        index = 0
        for i in range(len(data)): # menginterasikan data dalam jangkauan data
            if i == edit: # jika format data sesuai dengan edit
                data[index][0] = nama
                data[index][1] = nim
                data[index][2] = buku[int(inputbuku) - 1][0] # mengambil data pada buku indeks 0 untuk diambil judul buku 
                data[index][3] = tgl_pinjam
                data[index][4] = tgl_kembali
            index += 1
        head = data.pop(0)

        # membuka file csv dan menggunakan mode write (tulis) untuk menulis pada file csv
        with open("peminjaman.csv", "w", newline="") as file:
            header = csv.DictWriter(file, fieldnames=head)
            # menggunakan .writeheader() untuk mengembalikan nilai yang dikembalikan menggunakan .writerow() dengan perulangan for dalam data. 
            # sehingga data yang sudah diperbarui akan ditulis ke dalam file CSV dan mengganti data yang diinginkan.
            header.writeheader()
            for i in data:
                header.writerow({'Nama peminjam': i[0], 'NIM': i[1], 'Judul buku': i[2], 'Tanggal pinjam': i[3], 'Tanggal harus kembali': i[4]})
        menuPeminjaman() # setelah selesai maka kembali ke menu peminjaman

def hapusPeminjaman(): # mendefinisikan function hapusPeminjaman
    tampilPeminjaman() # memanggil tampilPeminjaman
    print("—" * 120) # menampilkan "—" sebanyak 120 kali

    data = []
    with open("peminjaman.csv", 'r') as file: # membuka file peminjaman.csv dengan mode read
        # membaca data peminjaman pada file csv
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)

    hapus = int(input("Pilih nomor: ")) # admin memilih nomor yang akan dihapus
    if hapus > len(data) - 1:
        hapusPeminjaman()
    
    index = 0
    for i in range(len(data)): # menginterasikan jumlah data dalam jangkauan data
        if i == hapus: 
            data.remove(data[index])
        index += 1
    
    head = data.pop(0)
    with open("peminjaman.csv", "w", newline="") as file:
        header = csv.DictWriter(file, fieldnames=head)
        # menggunakan .writeheader() untuk mengembalikan nilai yang dikembalikan menggunakan .writerow() dengan perulangan for dalam data. 
        # sehingga data yang sudah diperbarui akan ditulis ke dalam file CSV dan menghapus data yang diinginkan.
        header.writeheader()
        for i in data:
            header.writerow({'Nama peminjam': i[0], 'NIM': i[1], 'Judul buku': i[2], 'Tanggal pinjam': i[3], 'Tanggal harus kembali': i[4]})
    menuPeminjaman()

def tampilPeminjaman(): # mendefinisikan function tampilPeminjaman
    os.system('cls')

    data = []
    with open("peminjaman.csv", 'r') as file: 
        # membaca data peminjaman pada file csv
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)

    header = data.pop(0)
    header.insert(0, 'No')
    nomor = 1

    print('=' * 120)
    print('=' * 49, 'DATA PEMINJAMAN BUKU', '=' * 49) #menampilkan DATA PEMINJAMAN BUKU dan (=) sebanyak 49 kali
    print('=' * 120)
    print(f"{header[0]}\t {header[1]}\t\t {header[2]}\t\t\t {header[3]}\t\t {header[4]}\t {header[5]}")
    print('—' * 120)

    for i in data: # menginterasikan data dalam jangkauan data
        print(f"{nomor}\t {i[0]}\t\t {i[1]}\t\t {i[2]}\t {i[3]}\t {i[4]}") # menampilkan data 
        nomor += 1
    file.close()

def dataPeminjaman(): # mendefinisikan fungsi dataPeminjaman
    tampilPeminjaman() # memanggil tampilPeminjaman 
    print('—'*120) # menampilkan '—' sebanyak 120 kali
    input("Tekan enter untuk kembali ke menu") # admin bisa menekan enter agar kembali ke menu utama
    os.system('cls') # tampilan layar sebelumnnya akan otomatis terhapus
    menuPeminjaman() # kembali ke menuPinjamanan

### MENU ###

def mainMenu(): # mendefinisikan fungsi mainMenu
    os.system('cls') # menghapus tampilan layar sebelumnya secara otomatis pada terminal
    print("=" * 30)
    print("========= MENU UTAMA =========") # menampilkan ========= MENU UTAMA =========
    print("=" * 30)
    print('[1] Data Buku \n[2] Data Peminjaman \n[3] Keluar') # menampilkan urutan menu Data Buku, Data Peminjaman, Keluar
    print("=" * 30)

    pilihan = int(input("Pilih menu: ")) # admin memilih menu dalam bentuk integer atau angka
    if pilihan == 1: # jika menu sama dengan 1
        menuBuku() # maka menjalankan function menuBuku
    elif pilihan == 2: # jika menu sama dengan 2
        menuPeminjaman() # maka menjalankan function menuPeminjaman
    elif pilihan == 3: # jika menu sama dengan 3
        os.system('cls') # menghapus tampilan layar sebelumnya secara otomatis pada terminal
        login() # kembai ke menu login
    else:
        mainMenu() # kembali ke pilihan / input ulang

def menuBuku(): # mendefinisikan fungsi menuBuku
    os.system('cls') # menghapus tampilan layar sebelumnya secara otomatis pada terminal
    print("=" * 30)
    print("======= MENU DATA BUKU =======") # menampilkan ==== MENU DATA BUKU  ====
    print("=" * 30)
    print('[1] Data buku \n[2] Tambah data buku \n[3] Ubah data buku \n[4] Hapus data buku \n[5] Kembali ke menu utama')
      # menampilkan urutan menu Data buku, Tambah data buku, Ubah data buku, Hapus data buku, Kembali ke menu utama
    print("=" * 30)

    menu = int(input("Pilih menu: ")) # admin memilih menu dalam bentuk integer atau angka
    if menu == 1:  # jika menu sama dengan 1
        dataBuku() # maka menjalankan function dataBuku
    elif menu == 2:  # jika menu sama dengan 2
        # menuliskan data di file csv 
        if not(Path('buku.csv').is_file()):
            bukuCsv(["Judul Buku", "Penulis", "Genre"])
        tambahBuku()
    elif menu == 3:  # jika menu sama dengan 3
        editBuku() # maka menjalankan function editBuku
    elif menu == 4:  # jika menu sama dengan 4
        hapusBuku() # maka menjalankan function hapusBuku
    elif menu == 5:  # jika menu sama dengan 5
        mainMenu() # maka menjalankan function mainMenu
    else:
        menuBuku() # kembali ke pilihan / input ulang

def menuPeminjaman():# mendefenisikan fungsi menuPeminjaman
    os.system('cls') # menghapus tampilan layar sebelumnya secara otomatis pada terminal
    print("=" * 30)
    print("==== MENU DATA PEMINJAMAN ====") # menampilkan ==== MENU DATA PEMINJAMAN ====
    print("=" * 30)
    print('[1] Tampil data \n[2] Tambah data \n[3] Ubah data \n[4] Hapus data \n[5] Kembali ke menu utama')
    # menampilkan menu Tampil data, Tambah data, Ubah data, Hapus data, Kembali ke menu utama
    print('=' * 30)

    menu = int(input("Pilih menu: ")) # admin memilih menu dalam bentuk integer
    if menu == 1:  # jika menu sama dengan 1
        dataPeminjaman() # maka menjalankan function dataPeminjaman
    elif menu == 2: #jika menu sama dengan 2
        # menuliskan data di file csv 
        if not(Path('peminjaman.csv').is_file()):
            peminjamanCsv(["Nama peminjam", "NIM", "Judul buku", "Tanggal pinjam", "Tanggal harus kembali"])
        tambahPeminjaman()
    elif menu == 3: # jika menu sama dengan 3
        editPeminjaman()  # maka menjalankan function editPeminjam
    elif menu == 4: # jika menu sama dengan 4
        hapusPeminjaman() # maka menjalankan function hapusPeminjam
    elif menu == 5: # jika menu sama dengan 5
        mainMenu()  # maka menjalankan function mainMenu
    else: #jika false
        menuPeminjaman() # kembali ke pilihan / input ulang

def login(): # mendefinisikan function login
    os.system('cls') # menghapus tampilan layar sebelumnya secara otomatis pada terminal
    print("=" * 30)
    print("== LOGIN ADMIN PERPUSTAKAAN ==") # menampilkan == LOGIN ADMIN PERPUSTAKAAN ==
    print("=" * 30)
    print('[1] Daftar \n[2] Masuk \n[3] Keluar Aplikasi') # menampilkan urutan menu Daftar, Masuk,dan Keluar Aplikasi. /n berfungsi untuk mengenter data
    print('=' * 30)
    pilihan = int(input('Pilih menu: ')) # admin memilih menu dalam bentuk integer
    if pilihan == 1: # jika pilihan sama dengan 1
        # menuliskan data di file csv 
        if not(Path('admin.csv').is_file()): 
            adminCsv(["Nama", "Kata sandi"])
        daftar()
    elif pilihan == 2:  # jika pilihan sama dengan 2
        masuk() # menjalankan fungi masuk, maka akan masuk ke dalam program
    elif pilihan == 3:  # jika pilihan sama dengan 3
        os.system('cls') # maka tampilan layar akan terhapus
        exit() # keluar dari program
    else:
        login() # kembali ke pilihan / input ulang

# eksekusi kode
if __name__ == "__main__":
    login()