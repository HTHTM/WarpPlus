import requests, json, datetime, random, string, time, os, sys

os.system('title WARP-PLUS-CLOUDFLARE By HTHTM')

os.system('cls')

print('[+] ABOUT SCRIPT:')

print('[-] With this script, you can getting unlimited GB on Warp+.')

print('--------')

print('[+] THIS SCRIPT CODDED BY ALI. PUBLIC BY HTHTM')

print('[-] SUPPORT: @HTHTM_BOT')

print('[-] CHANNEL TELEGRAM: @HTHTM')

print('--------')

referrer = input('[#] Enter the WARP+ ID:')

def genString(stringLength):

    try:

        letters = string.ascii_letters + string.digits

        return ''.join(random.choice(letters) for i in range(stringLength))

    except Exception as error:

        print(error)

def digitString(stringLength):

    try:

        digit = string.digits

        return ''.join(random.choice(digit) for i in range(stringLength))

    except Exception as error:

        print(error)

url = f"http://api.cloudflareclient.com/v0a{digitString(3)}/reg"

def run():

    try:

        install_id = genString(11)

        body = {'key':'{}='.format(genString(42)),  'install_id':install_id, 

         'fcm_token':'{}:APA91b{}'.format(install_id, genString(134)), 

         'referrer':referrer, 

         'warp_enabled':False, 

         'tos':datetime.datetime.now().isoformat()[:-3] + '+07:00', 

         'type':'Android', 

         'locale':'zh-CN'}

        bodyString = json.dumps(body)

        headers = {'Content-Type':'application/json; charset=UTF-8',  'Host':'api.cloudflareclient.com', 

         'Connection':'Keep-Alive', 

         'Accept-Encoding':'gzip', 

         'User-Agent':'okhttp/3.12.1'}

        r = requests.post(url, data=bodyString, headers=headers)

        return r

    except Exception as error:

        print(error)

g = 1

b = 0

while True:

    result = run()

    if result.status_code == 200:

        os.system('cls')

        print('')

        print('                  WARP-PLUS-CLOUDFLARE (script)' + ' By HTHTM')

        print('')

        animation = ['[■□□□□□□□□□] 10%', '[■■□□□□□□□□] 20%', '[■■■□□□□□□□] 30%', '[■■■■□□□□□□] 40%', '[■■■■■□□□□□] 50%', '[■■■■■■□□□□] 60%', '[■■■■■■■□□□] 70%', '[■■■■■■■■□□] 80%', '[■■■■■■■■■□] 90%', '[■■■■■■■■■■] 100%']

        for i in range(len(animation)):

            time.sleep(0.5)

            sys.stdout.write('\r[+] Preparing... ' + animation[(i % len(animation))])

            sys.stdout.flush()

        print(f"\n[-] WORK ON ID: {referrer}")

        print(f"[:)] {g} GB has been successfully added to your account.")

        print(f"[#] Total: {g} Good {b} Bad")

        g = g + 1

        print('[*] After 20 seconds, a new request will be sent.')

        time.sleep(20)

    else:

        os.system('cls')

        print('')

        print('                  WARP-PLUS-CLOUDFLARE (script)' + ' By HTHTM')

        print('')

        print('[:(] Error when connecting to server.')

        print(f"[#] Total: {g} Good {b} Bad")

        b = b + 1
