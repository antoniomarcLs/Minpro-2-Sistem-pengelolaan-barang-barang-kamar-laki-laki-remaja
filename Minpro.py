from getpass import getpass
try:
        List_barang = {
                "Tas" : "Buku",
                "Meja" : "Pulpen",
                "Lemari" : "Baju"
        }

        def Pemilik():
                while True:
                        print("Berikut Perintah yang bisa anda gunakan")
                        List_Perintah = """
Masukkan barang                     = 1
Mengganti barang                    = 2
Membuang barang                     = 3
Logout                              = 4
                """
                        print(List_Perintah)
                        print("~")
                        i = 1
                        for (tempat,barang) in List_barang.items():
                                print(f"{i}. {tempat} = {barang}")
                                i += 1
                        print("~")
                        Perintah = int(input("Masukkan perintah berdasarkan angka: "))
                        print("~")
                        if Perintah == 1:
                                Tindakan = input("Letak barang yang baru: ")
                                print("~")
                                Tindakan1 = input("Barang yang ingin ditambahkan: ")
                                print("~")
                                List_barang.update({Tindakan : Tindakan1})
                                print(f"menambahkan {Tindakan1}")
                                print("~")
                        elif Perintah == 2:
                                Tindakan = input("Letak barang yang diganti: ")
                                print("~")
                                if Tindakan in List_barang:
                                        Tindakan_3 = input("nama barang untuk menggantikannya: ")
                                        print("~")
                                        List_barang[Tindakan] = Tindakan_3
                                        print(f"Barang pada {Tindakan} ditukar dengan {Tindakan_3}")
                                        print("~")
                                else :
                                        print("Letak tidak ditemukan")
                                        print("~")
                        elif Perintah == 3:
                                Tindakan = input("Dimana Letak barang yang ingin dibuang: ")
                                print("~")
                                if Tindakan in List_barang:
                                        del List_barang[Tindakan]
                                        print(f"{Tindakan} dan barang telah dibuang")
                                        print("~")
                                else:
                                        print("Letak tidak ditemukan")
                                        print("~")
                        elif Perintah == 4:
                                break
                        else:
                                print("Permintaan anda tidak kami pahami")
                                print("Barang tidak mengalami perubahan")
                                print("~")

        def Pengunjung():
                while True:
                        List_Perintah = """
Melihat daftar barang = 1
Logout                = 2
"""
                        print(List_Perintah)
                        print("~")
                        Perintah = int(input("apa yang ingin kamu lakukan? "))
                        print("~")
                        if Perintah == 1:
                                i = 1
                                for (tempat,barang) in List_barang.items():
                                        print(f"{i}. {tempat} = {barang}")
                                        i += 1
                                        print("~")
                        elif Perintah == 2:
                                break
                        else:
                                print("Permintaan anda tidak kami pahami")
                                print("Barang tidak mengalami perubahan")
                                print("~")

        while True:
                print("~" * 100)
                print("Write 'Stop' to stop looping")
                print("~")
                login = input("Username? ")
                print("~")
                if login == "Pemilik":
                        password = getpass("Password: ")
                        print("~")
                        if password == "123":
                                Pemilik()
                        else:
                                print("password salah")
                elif login == "Pengunjung":
                        password = getpass("Password: ")
                        if password == "456":
                                Pengunjung()
                        else:
                                print("password salah")
                                print("~")
                elif login == "Stop" :
                        break
                else:
                        print("Login gagal")
                        print("~")

        print("~" * 100)
except KeyboardInterrupt:
        print("error ctrl + C")
except ValueError:
        print("Input tidak sesuai")
except EOFError:
        print("Error terjadi karena menekan ctrl + D/Z")
except NameError:
        print("Terjadi kesalahan pada kode")