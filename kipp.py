from colorama import Fore, Style
from time import sleep
from os import system
import threading
from sms import SendSms  # SendSms modülünün doğru şekilde yüklendiğinden emin olun

# Örnek SendSms sınıfı (gerçek sınıfınızı buraya ekleyin)
class SendSms:
    def __init__(self, phone, mail):
        self.phone = phone
        self.mail = mail
        self.adet = 0

    def servis1(self):
        print(f"SMS gönderiliyor: {self.phone} - Servis 1")
        self.adet += 1

    def servis2(self):
        print(f"SMS gönderiliyor: {self.phone} - Servis 2")
        self.adet += 1

# Mevcut servislerin listesini al
servisler_sms = [
    attr for attr in dir(SendSms)
    if callable(getattr(SendSms, attr)) and not attr.startswith('__')
]

while True:
    system("cls||clear")
    print(f"""
{Fore.LIGHTCYAN_EX}
 ██╗░░██╗██╗██████╗░██████╗░
 ██║░██╔╝██║██╔══██╗██╔══██╗
 █████═╝░██║██████╔╝██████╔╝
 ██╔═██╗░██║██╔═══╝░██╔═══╝░
 ██║░╚██╗██║██║░░░░░██║░░░░░
 ╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝░░░░░
    
    Sms: {len(servisler_sms)}           {Style.RESET_ALL}by {Fore.LIGHTRED_EX}@Kipp1337
    """)

    try:
        menu = input(f"{Fore.LIGHTMAGENTA_EX} 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n{Fore.LIGHTYELLOW_EX} Seçim: ")
        if not menu:
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(f"{Fore.LIGHTYELLOW_EX}Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): {Fore.LIGHTGREEN_EX}", end="")
        tel_no = input()
        tel_liste = []
        if not tel_no:
            system("cls||clear")
            print(f"{Fore.LIGHTYELLOW_EX}Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: {Fore.LIGHTGREEN_EX}", end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    tel_liste = [i.strip() for i in f.readlines() if len(i.strip()) == 10]
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(f"{Fore.LIGHTRED_EX}Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
            except Exception as e:
                system("cls||clear")
                print(f"{Fore.LIGHTRED_EX}Dosya okuma hatası: {e}")
                sleep(3)
                continue
        else:
            try:
                if not tel_no.isdigit() or len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"
            except ValueError:
                system("cls||clear")
                print(f"{Fore.LIGHTRED_EX}Hatalı telefon numarası. Tekrar deneyiniz.")
                sleep(3)
                continue

        system("cls||clear")
        try:
            print(f"{Fore.LIGHTYELLOW_EX}Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): {Fore.LIGHTGREEN_EX}", end="")
            mail = input()
            if mail and ("@" not in mail or ".com" not in mail):
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(f"{Fore.LIGHTYELLOW_EX}Kaç adet SMS göndermek istiyorsun {sonsuz}: {Fore.LIGHTGREEN_EX}", end="")
            kere = input()
            kere = int(kere) if kere else None
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(f"{Fore.LIGHTYELLOW_EX}Kaç saniye aralıkla göndermek istiyorsun: {Fore.LIGHTGREEN_EX}", end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        for tel in tel_liste:
            sms = SendSms(tel, mail)
            if kere is None:
                while True:
                    for servis in servisler_sms:
                        getattr(sms, servis)()
                        sleep(aralik)
            else:
                while sms.adet < kere:
                    for servis in servisler_sms:
                        if sms.adet >= kere:
                            break
                        getattr(sms, servis)()
                        sleep(aralik)

        print(f"{Fore.LIGHTRED_EX}\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 2:
        system("cls||clear")
        print(f"{Fore.LIGHTYELLOW_EX}Telefon numarasını başında '+90' olmadan yazınız: {Fore.LIGHTGREEN_EX}", end="")
        tel_no = input()
        try:
            if not tel_no.isdigit() or len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Hatalı telefon numarası. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(f"{Fore.LIGHTYELLOW_EX}Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): {Fore.LIGHTGREEN_EX}", end="")
            mail = input()
            if mail and ("@" not in mail or ".com" not in mail):
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()

        def Turbo():
            while not dur.is_set():
                threads = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    threads.append(t)
                    t.start()
                for t in threads:
                    t.join()

        try:
            turbo_thread = threading.Thread(target=Turbo, daemon=True)
            turbo_thread.start()
            input(f"{Fore.LIGHTRED_EX}Durdurmak için 'enter' tuşuna basınız..")
            dur.set()
            turbo_thread.join(timeout=1.0)
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}Turbo mod durduruldu. Menüye dönülüyor..")
            sleep(2)
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)

    elif menu == 3:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}Çıkış yapılıyor...")
        break
