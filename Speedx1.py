
try:
    import os,sys,time,requests,json,re
    import pyshorteners
    import colorama
    import bitly_api
    from colorama import Fore,init,Back
except ModuleNotFoundError:
     os.system("bash requirements.sh")

Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

#def checkping():
    #os.system("python speedx1.py")

def printtik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)

def tanya():
    tanya=input(f"[!] Back To The Tools {biru}(y{abu}/t{biru}) : ")
    if tanya == "y" or tanya == "Y":
        banner()
        inputt()
    if tanya == "t" or tanya == "T":
        printtik(f"[!] Program Dihentikan !!!")
        sys.exit()

def bitly():
    BITLY_ACCESS_TOKEN = "74e40eae5737852ee2bba8ece28adb3b452208c4"
    link = input(f"{biru}[~] Link : ")
    b = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
    response = b.shorten('http://google.com/')
    time.sleep(3)
    printtik(f"[✓] 'message':'success-shortn'")
    printtik (f"""
   [•] Url : {done['url']}
   [•] Long Url : {link}""")

def tinyurl():
    link = input(f"{biru}[~] Link : ")
    start = pyshorteners.Shortener().tinyurl.short(link)
    printtik(f"[✓] 'message':'success-shortn'")
    printtik (f"""
   [•] Url : {start}
   [•] Long Url : {link}""")

def banner():
    os.system("clear")
    print ("""
\033[1;96m╔═╗\033[1;97m┬ ┬┌─┐┬─┐┌┬┐  \033[1;96m╦  \033[1;97m┬┌┐┌┬┌─  \033[1;97m{\033[1;93m•\033[1;97m} Creator \033[1;93m:\033[1;97m DEMONX
\033[1;96m╚═╗\033[1;97m├─┤│ │├┬┘ │   \033[1;96m║  \033[1;97m││││├┴┐  \033[1;97m{\033[1;93m•\033[1;97m} Githubb \033[1;93m:\033[1;92m github.com/THEMOON555
\033[1;96m╚═╝\033[1;97m┴ ┴└─┘┴└─ ┴   \033[1;96m╩═╝\033[1;97m┴┘└┘┴ ┴  \033[1;97m{\033[1;93m•\033[1;97m} Thx For All Member \033[1;95mCyber Hunter Team
""")

def inputt():
    print (f"""\033[1;97m1.\033[1;92mShort-Link
\033[1;97m2.\033[1;97mReport Bug
\033[1;97m3.\033[1;97mExit
""")
    pil = input(f"Pilih Menu Tools:")
    if pil == "1":
        print (f"[1]. Short Ke 'bitly'\n[2]. Short Ke 'tinyurl'")
        pilih=input(f"Pilih Menu Tools : ")
        if pilih == "1":
            bitly()
            tanya()
        if pilih == "2":
            tinyurl()
            tanya()
    if pil == "2":
        os.system("xdg-open https://www.instagram.com/ammarexecuted")
        tanya()
    if pil == "3":
        print (f"[!] Program discontinued  !!!")
        sys.exit()

banner()
inputt()
