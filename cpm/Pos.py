import httpx
import json
import random as rdm

Vhost = "us-central1-cpm-2-7cea1.cloudfunctions.net"
Vheader = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer2",
    "X-Android-Cert": "004A4780B060C9F35B7C9868D1D50379B79940DF",
    "Accept-Language": "in-ID, en-US",
    "X-Client-Version": "Android/Fallback/X23000000/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:891105416504:android:37d689c257df3c37b19dcd",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "X-Firebase-AppCheck": "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ==",
    "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
# for cekdata in ["data"]:
#     if cekdata not in Vdata:
#         Vdata[cekdata]=input(f"{cekdata} : ")
Vdata = {}
Vdata["idToken"] = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ0MjY5YTE3MzBlNTA3MTllNmIxNjA2ZTQyYzNhYjMyYjEyODA0NDkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY3BtLTItN2NlYTEiLCJhdWQiOiJjcG0tMi03Y2VhMSIsImF1dGhfdGltZSI6MTcyNDI3NjI1MCwidXNlcl9pZCI6IlQ2Qmg1T3RyRnZib3hsUFVLWktCZXI1YW9pQTMiLCJzdWIiOiJUNkJoNU90ckZ2Ym94bFBVS1pLQmVyNWFvaUEzIiwiaWF0IjoxNzI0Mjc2MjUwLCJleHAiOjE3MjQyNzk4NTAsImVtYWlsIjoibW9ubmV5ZGxAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1vbm5leWRsQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.swnTJSQI6WUlT8JJoFmrhzwzcFkMYzdmzrUhXXLP-qljhHQjfcaSfF9FzATCiPUzCPv7Q4NSiVg9Vnah_vTY_7zywfay-_Vpah0pjjUPz6GX5kG6j4Yqrkb4Z9ufkqGr_vS2NNJkYyIujPyVyyLhMVUR6PtdrNE9v7vfNI6ELcFoaC2eAdpNkQ_pzLa8s3hc9nGbUbOy4SQZHbUTIUuQS0IZQuZF-95g2cfNtLdJCJM0gHyTU0W-AH03BnL3N6mYz1vnwjAtRyCqmiX-6j_N6AN-UG-S4trXLzr1J5r-71OzOSdC5usquJt8XHMAh-tRPRL8F8Tj1rT94CwHKQ_3nA"
Vdata["key"] = "AIzaSyCQDz9rgjgmvmFkvVfmvr2-7fT4tfrzRRQ"
Vdata["firebase-instance-id-token"] = "d1ytc_nPQiOD4AB5s0TnFl:APA91bElhqsg2d4BkWlbwoaRLSuZF9uFsE0pYvoCyUwaXrF98_g1ZAT6_-UUZrBO1qjUB-EAEZScy9I8N3Hj-Gz0Ah1cTNp1SaPe7BhxZnS0MXQJ2wYyUw0brRrqPsG_i9fLq1r8Dj5a"
Vdata["data"] = "8D39D2AFCB86255981A067D0DEF6C3290F55E620"
Vdata["check"] = "A8543B13CDA4B7679237AD7180A2113C75D2F39D"
Vdata["CheckDeviceId4"] = "1bc9933bad5c19d1c734e0b8b04a3bbd","10"
Vdata["datalogin"] = "1bc9933bad5c19d1c734e0b8b04a3bbd"


def verifyPassword(email, password):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={Vdata['key']}"
    data = {"email": email, "password": password, "returnSecureToken": True, "clientType":"CLIENT_TYPE_ANDROID"}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"verifyPassword : {len(ress)}")
        Vdata["idToken"] = ress["idToken"]
        # print(Vdata["idToken"])
        return True


def getAccountInfo():
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key={Vdata['key']}"
    data = {"idToken": Vdata["idToken"]}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"getAccountInfo : {len(ress)}")


def GetPlayerRecords():
    uri = f"https://{Vhost}/GetPlayerRecords4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    data = {"data": Vdata["data"]}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        with open('player/data.json', 'w', encoding='utf-8') as f:
            json.dump({"data": resss}, f, ensure_ascii=False, indent=4)
        print(f"Data Player : {len(resss)}")
        return resss
    


# Example usage
wallet_data = "{\"Money\":49995000}"
result = defsavewallet(wallet_data)
print(result)

def SavePlayerRecords7(dataakun):
    uri = f"https://{Vhost}/SavePlayerRecords4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    pipit = json.dumps(dataakun["data"])
    data = {"data": pipit}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    # print(req.status_code)
    # print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"Save Account Info {ress}")
        resss = json.loads(ress["result"])
        if resss == 1:
            return True
        return True
    return False

def SetUserRating1(isidata):
    uri = f"https://{Vhost}/SetUserRating4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; charset=utf-8",  # Typo: 'chatset' should be 'charset'
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    data = {'data': json.dumps(isidata)}
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=100)

    if req.status_code == 200:
        ress = json.loads(req.text)
        print(ress)  # Menambahkan perintah print untuk mencetak respons JSON
        return True
    return False
def SaveWalletData4(isidata):
    uri = f"https://{Vhost}/SaveWalletData4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; charset=utf-8",  # Typo: 'chatset' should be 'charset'
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    data = {'data': json.dumps(isidata)}
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=100)

    if req.status_code == 200:
        ress = json.loads(req.text)
        print(ress)  # Menambahkan perintah print untuk mencetak respons JSON
        return True
    return False
def SetUserRating1(isidata):
    uri = f"https://{Vhost}/SetUserRating4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; charset=utf-8",  # Typo: 'chatset' should be 'charset'
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    data = {'data': json.dumps(isidata)}
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=100)

    if req.status_code == 200:
        ress = json.loads(req.text)
        print(ress)  # Menambahkan perintah print untuk mencetak respons JSON
        return True
    return False




def SaveCars(data):
    uri = f"https://{Vhost}/SaveCar4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    # pipit=json.dumps(data["data"])
    # data=json.dumps(data)
    data = json.dumps({"data": json.dumps(data["data"])})
    req = httpx.post(uri, data=data, headers=heder)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        # print(resss)
        return True
    print(req.status_code)
    print(req.text)
    return False


def TestGetAllCars():
    uri = f"https://{Vhost}/GetAllCars4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    data = {"data": Vdata["data"]}
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=1000)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        urutan = ""
        for itr in range(len(resss)):
            urutan += str(resss[itr]["CarID"])+","
            with open(f'player/cars/{resss[itr]["CarID"]}', 'w', encoding='utf-8') as f:
                json.dump({"data": resss[itr]}, f,
                          ensure_ascii=False, indent=4)
        print(urutan)
        print(f"Data : {len(resss)}")


# World Sale
def GetCarListWorldSale2(wsvalue):
    # print("Get Car List WorldSale2")
    uri = f"https://{Vhost}/GetCarListWorldSale2"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    data = json.dumps({"data": {
                      "@type": "type.googleapis.com/google.protobuf.Int64Value", "value": wsvalue}})
    req = httpx.post(uri, data=data, headers=heder, timeout=10)
    # print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        return ress["result"]


def TestGetOneCarFromWorldSale(ownerAccountID, carid, wsvalue):
    print("Get Car From WorldSale")
    uri = f"https://{Vhost}/TestGetOneCarFromWorldSale"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111, 999999)})"
    }
    data = json.dumps(
        {"data": [str(ownerAccountID), str(carid), str(wsvalue)]})
    print(data)
    req = httpx.post(uri, data=data, headers=heder, timeout=10)
    print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        return ress["result"]


def signupNewUser(email, password):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key={Vdata['key']}"
    data = {"email": email, "password": password}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"signupNewUser : {len(ress)}")
        Vdata["idToken"] = ress["idToken"]
        return True
    print(req.text)
    return False

def chekss():
    uri = f"https://{Vhost}/Check4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": Vdata["check"]}     
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=1000)
    if req.status_code == 200:
        ress = json.loads(req.text)       
        print(f"Check Account : {len(ress)}")
        return True
        return True
    return False
def HandleDeviceLogin4():
    uri = f"https://{Vhost}/HandleDeviceLogin4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": Vdata["datalogin"]}     
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=1000)
    if req.status_code == 200:
        ress = json.loads(req.text)       
        print(f"Check Login : {len(ress)}")
        return True
        return True
    return False

def HandleDeviceLogout4():
    uri = f"https://{Vhost}/HandleDeviceLogout4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": Vdata["datalogin"]}     
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=1000)
    if req.status_code == 200:
        ress = json.loads(req.text)       
        print(f"Check Logout : {len(ress)}")
        return True
        return True
    return False

def CheckDeviceId4():
    uri = f"https://{Vhost}/CheckDeviceId4"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": Vdata["CheckDeviceId4"]}     
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=1000)
    if req.status_code == 200:
        ress = json.loads(req.text)       
        print(f"CheckDeviceId : {len(ress)}")
        return True
        return True
    return False
