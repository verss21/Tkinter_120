import tkinter as tk
# mengimpor library tkinter dan membuat alias tk
from tkinter import messagebox
# mengimpor modul messagebox dari tkinter

def hasil_prediksi():
    try: 
        for entry in entries:
            nilai = int(entry.get()) #mengambil nilai input dari setiap Entry dan konversi menjadi integer
            if not (0 <= nilai <= 100):  #memastikan nilai 0-100
                raise ValueError("Nilai harus antara 0 dan 100.") #jika menginput nilai - atau lebih dari 100 maka muncul valueError
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") #untuk mengatur judul utama aplikasi
root.geometry("500x600") # untuk mengatur ukuran 
root.configure(bg="White") # untuk warna background

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold"))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)
#untuk mengatur font dan tata letak judul

entries = [] #untuk menyimpan semua widget Entry

for i in range(10): # mengulang sebanyak 10x untuk input mata kuliah
    mata_kuliah_label = tk.Label(root, text=f"Nilai Mata Kuliah {i + 1}:", bg="White") #untuk mengatur sebuah label tkinter yang berfungsi untuk menampilkan teks pada jendela aplikasi dan mengatur teks yang akan ditampilkan pada label
    mata_kuliah_label.grid(row=i + 1, column=0, sticky="e", padx=10, pady=5) #untuk menempatkan widget pada jendela menggunakan layout berbasis grid.

    input_value = tk.Entry(root) #untuk mengisi input dari pengguna
    input_value.grid(row=i + 1, column=1, padx=10, pady=5)

    entries.append(input_value) #untuk menambahkan input entry ke dalam list entries

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)
#membuat tombol hasil prediksi

hasil_label = tk.Label(root, text="", font=("Arial", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)
#memunculkan output hasil prediksi dibawah tombol hasil prediksi

root.mainloop()
#untuk memanggil program
