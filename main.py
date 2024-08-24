import os
import json
import random
import shutil
import time
import sys
import NamaBerwarna
import displaywarna
import cpm as cpm
from colr import color
import shutil
import os
import datetime
import subprocess
import os
import json
import shutil
import sys
from rich.console import Console
from rich.table import Table
import cpm
import json
import httpx
import random as rdm  

def create_instant_clan(data):
    uri = "https://us-central1-cp-multiplayer.cloudfunctions.net/GetClanData    " # Sesuaikan dengan endpoint yang benar
    header = {
        "Host": "us-central1-cp-multiplayer.cloudfunctions.net",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImFlYzU4NjcwNGNhOTZiZDcwMzZiMmYwZDI4MGY5NDlmM2E5NzZkMzgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY3AtbXVsdGlwbGF5ZXIiLCJhdWQiOiJjcC1tdWx0aXBsYXllciIsImF1dGhfdGltZSI6MTcwODUzODU0NywidXNlcl9pZCI6ImluVHVKYktpNHNSamdndmR2QWZkdWFYSmx1eTIiLCJzdWIiOiJpblR1SmJLaTRzUmpnZ3ZkdkFmZHVhWEpsdXkyIiwiaWF0IjoxNzA4NTM4NTQ3LCJleHAiOjE3MDg1NDIxNDcsImVtYWlsIjoiYWt1bmJhaGFuZGVsbGFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiYWt1bmJhaGFuZGVsbGFAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.iu5J4x_69FcsBGu3lwHrK5wUhHfDP_4CzUoyKjP8jRw5ewc_w3KR8wNxFEsbDYoa8VtBWYgmbxD19e2AKxrVTkoHmfL2avzPgfra86jin-UZUhJvJvphk2_rcEkusgTa2bD82Aw3Uiox8tvhcWYd3YK0RZsr1q6b1j1dgIOrl8WPJMfnQMnOiwnzRBP2BsU9Phxbou3oxhPmaKGTLiIC4VAuLoaiKXdL0Jw6UVyODMcD64nxzroiyo0nDfqYEzXWx5KsEIdaRBgLtUwfDAEdEq4bwoRxIO0C8VWh_F0gjYQYxRd7VY1iUw5QMzfG4nLrP0xjYLgz1qNMXPYaoec86Q",
        "firebase-instance-id-token": "c9K2xb4pRFSc3sOl6sQd6W:APA91bHS_3BJP1SEZHTCg_vnlLJb8uot_sZvZOVpXj0d7PyYE_-ROFP5261MGSKak_CWmFbidOg7yTBDW6YD0CYLuDM94_8F0FZlB8uQ66ohcuuv9hzqGZwRTYT2ZgKRlQ9JwdfRGNG4",
        "content-type": "application/json; charset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": "okhttp/3.12.13"
    }
    req = httpx.post(uri, json=data, headers=header)
    if req.status_code == 200:
        ress = req.json()
        print("New clan added successfully!")
        return True, ress
    else:
        print("Failed to add new clan.")
        return False, None






# Ensure to define your 'c' and 'cpm' functions and 'datacar' variable before calling alisreq function




def duplicate_cars_folder(source_folder):
    # Membuat nama folder baru dengan tanggal otomatis
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    new_folder_name = f'newcars_{current_date}'

    # Membuat path lengkap untuk folder baru
    new_folder_path = os.path.join('player', new_folder_name)

    # Mengecek apakah folder baru sudah ada, jika ya, tambahkan indeks unik
    index = 1
    while os.path.exists(new_folder_path):
        new_folder_name = f'newcars_{current_date}_{index}'
        new_folder_path = os.path.join('player', new_folder_name)
        index += 1

    # Menggandakan folder sumber ke folder baru
    shutil.copytree(source_folder, new_folder_path)

    print(f"Folder '{source_folder}' telah digandakan ke '{new_folder_path}'")

# Contoh penggunaan fungsi




def upload_to_github(folder_name, github_repo_url):
    # Dapatkan tanggal saat ini dalam format YYYY-MM-DD
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Buat nama folder berdasarkan tanggal
    new_folder_name = os.path.join(folder_name, current_date)

    # Membuat folder baru
    os.mkdir(new_folder_name)

    # Salin isi folder ke folder baru
    shutil.copytree(folder_name, new_folder_name)

    # Inisialisasi Git di dalam folder baru
    os.chdir(new_folder_name)
    subprocess.call(['git', 'init'])

    # Tambahkan semua perubahan ke Git
    subprocess.call(['git', 'add', '.'])

    # Lakukan commit dengan pesan sesuai tanggal
    commit_message = f'Update on {current_date}'
    subprocess.call(['git', 'commit', '-m', commit_message])

    # Tambahkan remote repository GitHub
    subprocess.call(['git', 'remote', 'add', 'origin', github_repo_url])

    # Push perubahan ke GitHub
    subprocess.call(['git', 'push', '-u', 'origin', 'master'])

# Contoh penggunaan:
folder_name = 'player/cars'
github_repo_url = 'https://github.com/MakerDell/VVIP22/repo.git'







def loading():
    animation = ["[\x1b[1;91m\x1b[0m]","[\x1b[1;92m\x1b[0m]", "[\x1b[1;93m\x1b[0m]", "[\x1b[1;94m\x1b[0m]", "[\x1b[1;95m\x1b[0m]", "[\x1b[1;96m\x1b[0m]", "[\x1b[1;97m\x1b[0m]", "[\x1b[1;98m\x1b[0m]", "[\x1b[1;99m\x1b[0m]", "[\x1b[1;910m\x1b[0m]"]
    for i in range(1):
        sys.stdout.write(f"\r Harap tunggu sebentar  " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")


def c(colr, tex):
    try:
        w = {
            "RED": [255, 5, 0],
            "GREEN": [5, 255, 0],
            "CYAN": [5, 255, 255]
            
        }
        return color(tex,
                     fore=(w[colr.upper()][0],
                           w[colr.upper()][1],
                           w[colr.upper()][2]),
                     back=(0, 5, 0))
    except:
        return tex


def tes():
    pass


# while True:
#     tes()
#     input()
# exit()


def cariid(urutan):
    with open('nomer_car.json', 'r', encoding='utf-8') as openfile:
        data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["urutan"] == urutan:
            return mydatacar["id"]


def cariurutan(cariid):
    with open('nomer_car.json', 'r', encoding='utf-8') as openfile:
        data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["id"] == cariid:
            return mydatacar["urutan"] 


def cekdatalivery(carid):
    path = "cpm/cars/livery/"
    dir_list = os.listdir(path)
    dir_list = sorted(dir_list, key=len, reverse=False)
    if str(carid) in dir_list:
        return True
    else:
        return False


def savewscar(carid, data):
    datacarname = str(carid)
    itrliverydata = 1
    while True:
        print(datacarname)
        if cekdatalivery(datacarname) == False:
            break
        else:
            datacarname = f"{carid}_"+str(itrliverydata)
            itrliverydata += 1

        time.sleep(0.2)
    print(f"bisa di save {datacarname}")
    dataforsave = {
        "data": data["thisCarData"]
    }
    dataforsave["data"]["Vynils"] = data["thisCarVynils"]
    print(dataforsave)
    with open(f'cpm/cars/livery/{datacarname}', 'w', encoding='utf-8') as f:
        json.dump(dataforsave, f, ensure_ascii=False, indent=4)
    return datacarname
if __name__ == "__main__":
    vip = True
   ## if input("topix?") == "y":
     ##   vip = True
    disp = ""
    while True:
        print(disp)
        menus = """



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━༻🇮🇩༺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓

88888             8         .d88b 888b. 8b   d8    d88b 
  8   .d8b. .d8b. 8 d88b    8P    8  .8 8YbmdP8    " dP  - Tools VIP
  8   8' .8 8' .8 8 `Yb.    8b    8wwP' 8  "  8     dP  DELLSTORECPM
  8   `Y8P' `Y8P' 8 Y88P    `Y88P 8     8     8    d888 
                                                        

┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━༻🇮🇩༺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛



<[=• MENU LOGIN =•]>
1. EDIT AKUN
2. Create Account   
3. testing bug account
Input nomor NB: x untuk exit dan save!!: """
        inp = input(menus)
        if inp == "x" or inp == "X":
            cpm.HandleDeviceLogout4()
            break
        elif inp == "0":
            pass
        elif inp == "1":
            print(c("cyan", "=================== verifyPassword"))
            while True:
                teslogin = cpm.verifyPassword(
                    input("email : "), input("password : "))
                if teslogin != None:
                    break
            print(c("cyan", "=================== Login Checking"))
            cpm.chekss()
            cpm.CheckDeviceId4()
            cpm.HandleDeviceLogin4()
            print(c("cyan", "=================== GetAccountInfo"))
            cpm.getAccountInfo()
            print(c("cyan", "=================== GetPlayerRecords"))
            vrs = cpm.GetPlayerRecords()
            print(c("cyan", "=================== TestGetAllCars"))
            shutil.rmtree('player/cars')
            os.mkdir('player/cars')          
            cpm.TestGetAllCars()
            source_folder = 'player/cars'
            duplicate_cars_folder(source_folder)
           # Dapatkan tanggal saat ini dalam format YYYY-MM-DD
            print(c("cyan", "=================== Savedataversion")) 
            #cpm.GetClan2()
            #cpm.GetClanData4()
            print(c("red", "==========[ INFO AKUN]==========="))
            try:
                print(f' >> Nickname : {displaywarna.disp(vrs["PlayerStorage"]["Name"])}')
            except:
                print(f' >> Nickname : {vrs["PlayerStorage"]["Name"]}')
            try:
                print(f' >> ID       : {vrs["PlayerStorage"]["LocalID"]}')
                print(f' >> Coin     : {vrs["WalletData"]["Coins"]}')
                print(f' >> Money    : {vrs["WalletData"]["Money"]}')
                print(f' >> Slots    : {vrs["PlayerStorage"]["Other"]["Slots"]}')
                
            except:
                print("Data sebagian belum ada")
            print(c("red", "=============================="))
            menusedit = """Enter Melihat Info Akun
========<Menu>========         
1. Manual Edit Save
2. Suntik Money
"""
            while True:
                inp = input(menusedit)
                if inp == "x" or inp == "X":
                    cpm.HandleDeviceLogout4()
                    break
                elif inp == "":
                    print(c("cyan", "=================== Mendapatkan Informasi Akun"))
                    vrs = cpm.GetPlayerRecords()
                    
                    with open('player/data.json', 'r', encoding='utf-8') as openfile:
                        data = json.load(openfile)

                    print(c("cyan", "==========[ INFO AKUN ]==========="))
                    try:
                        print(f' >> Nickname : {displaywarna.disp(vrs["PlayerStorage"]["Name"])}')
                    except:
                        print(f' >> Nickname : {vrs["PlayerStorage"]["Name"]}')
                    try:
                        print(f' >> ID       : {vrs["PlayerStorage"]["LocalID"]}')
                        print(f' >> Coin       : {vrs["WalletData"]["Coins"]}')
                        print(f' >> Money    : {vrs["WalletData"]["Money"]}')
                        print(f' >> Slots    : {vrs["PlayerStorage"]["Other"]["Slots"]}')
                    except:
                        print("Data sebagian belum ada")
                    print(c("cyan", "=============================="))
                elif inp == "1":
                    with open('player/data.json', 'r', encoding='utf-8') as openfile:
                        data = json.load(openfile)
                    with open('player/carhash.json', 'r', encoding='utf-8') as openfile:
                        datacar = json.load(openfile)

                    if cpm.SavePlayerRecords7(data) and cpm.SaveCars(data):
                        disp = "Sukses"
                    else:
                        disp = "Gagal"  
                
                elif inp == "2":
                    print(c("cyan", "=================== GetPlayerRecords"))
                    vrs = cpm.GetPlayerRecords()
                    with open('player/data.json', 'r', encoding='utf-8') as openfile:
                        data = json.load(openfile)
                    data["data"]["WalletData"]["Money"] = input("Money : ")
                    if cpm.SavePlayerRecords7(data) and cpm.defsavewallet(data)==True:
                        disp = "Sukses"
                    else:   
                        disp = "Gagal"                                 
                                                                                    
        elif inp == "2":
            print("Create Account")
            if cpm.signupNewUser(input(" Email : "), input(" Password : ")):
                with open('data_basic.json', 'r') as openfile:
                    data = json.load(openfile)
                data["data"]["PlayerStorage"]["localID"] = "DL" + \
                    str(random.randint(111111, 999999))
                print(c("red", "=============================="))
                try:
                    print(f' >> Nickname : {displaywarna.disp(data["data"]["PlayerStorage"]["Name"])}')
                except:
                    print(f' >> Nickname : {data["data"]["PlayerStorage"]["Name"]}')
                try:
                    print(f' >> ID       : {data["data"]["PlayerStorage"]["LocalID"]}')
                    print(f' >> Coin       : {data["data"]["WalletData"]["Coins"]}')
                    print(f' >> Money    : {data["data"]["WalletData"]["Money"]}')
                except:
                    print("Data sebagian belum ada")
                print(c("red", "=============================="))
                if cpm.SavePlayerRecords7(data):
                    disp = "Sukses"
                    print(c("cyan", "=================== GetPlayerRecords"))


                    path = "unlock/cars/"
                    dir_list = os.listdir(path)
                    dir_list = sorted(dir_list, key=len, reverse=False)
                    for idcar in dir_list:
                        sys.stdout.write(f"  >> Inject Car id [{idcar}]    \r")
                        sys.stdout.flush()
                        with open(f'unlock/cars/{idcar}', 'r', encoding='utf-8') as openfile:
                            datacar = json.load(openfile)
                        if cpm.SaveCars(datacar):
                            disp = "Sukses"
                        else:
                            disp = "Gagal"      
                else:
                    disp = "Email sudah terdaftar"
            # Bagian ini untuk membuat akun tanpa full unlock
            # Misalnya, hanya membuat akun tanpa melakukan tindakan lain
            pass

        else:
            print("Wrong...!")
