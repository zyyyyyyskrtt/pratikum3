# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : Razy Al Farisi

Kelas : TI.24.A.5

NIM : 312410524

Mata Kuliah : Bahasa Pemograman


## Mencari bilangan terbesar dari bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## flowchart program
![foto](https://github.com/zyyyyyyskrtt/foto/blob/ee1b53329dcafc61841ee3c254d21e34d812df4a/Screenshot%202024-10-22%20200650.png)

## kode program python
```python
Max = 0

while True:
    N = int(input("Masukkan bilangan (0 untuk berhenti): "))
    
    if N == 0:
        print(f"Bilangan terbesar adalah: {Max}")
        break
    
    
    if N > Max:
        Max = N
```

## penjelasan kode program
`Max = 0`

Variabel `Max` diinisialisasi dengan nilai awal 0.
Variabel ini digunakan untuk menyimpan bilangan terbesar yang ditemukan selama proses input

`while True:`

Program memasuki loop tak terbatas dengan `while True.`
Ini berarti program akan terus meminta input bilangan sampai ditemukan kondisi keluar di dalam loop (yaitu, ketika pengguna memasukkan 0).

`N = int(input("Masukkan bilangan (0 untuk berhenti): "))`

Dalam setiap iterasi, pengguna diminta memasukkan sebuah bilangan.
Nilai input dikonversi menjadi tipe data integer dan disimpan dalam variabel `N`.

`if N == 0:`

Program memeriksa apakah bilangan yang dimasukkan adalah 0.
Jika benar (input = 0), program akan:

1. Mencetak bilangan terbesar yang ditemukan (nilai `Max`).
   
2. Keluar dari loop dengan menggunakan `break`.

`if N > Max:`

Jika bilangan yang baru dimasukkan lebih besar dari nilai `Max` saat ini, maka:

Nilai `Max` diperbarui menjadi bilangan tersebut.

## hasil eksekusi kode program
![foto](https://github.com/zyyyyyyskrtt/foto/blob/ee1b53329dcafc61841ee3c254d21e34d812df4a/Screenshot%202024-10-22%20192033.png)
