
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
    tanya=input(f"{W}[{R}!{W}] Back To The Tools {biru}({W}y{abu}/{W}t{biru}) {R}:{G} ")
    if tanya == "y" or tanya == "Y":
        banner()
        inputt()
    if tanya == "t" or tanya == "T":
        printtik(f"{W}[{R}!{W}] Program Dihentikan {R}!!!")
        sys.exit()

def bitly():
    token='df26aab8b854cb95e39df6e4a2f51d7e77b90f5d'
    link = input(f"{W}[{biru}~{W}] Link {R}:{G} ")
    start = bitly_api.Connection(access_token = token)
    done = start.shorten(link)
    time.sleep(3)
    printtik(f"{W}[{G}✓{W}] 'message':'success-shortn'")
    printtik (f"""
{W}[{R}•{W}] Url {R}:{Y} {done['url']}
{W}[{Y}•{W}] Long Url {R}:{Y} {link}""")

def tinyurl():
    link = input(f"{W}[{biru}~{W}] Link {R}:{G} ")
    start = pyshorteners.Shortener().tinyurl.short(link)
    printtik(f"[✓] 'message':'success-shortn'")
    printtik (f"""
{W}[{R}•{W}] Url {R}:{Y} {start}
{W}[{Y}•{W}] Long Url {R}:{Y} {link}""")

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
    pil = input(f"{W}Pilih Menu Tools {R}:{G} ")
    if pil == "1":
        print (f"{W}[{Y}1{W}]{R}.{W} Short Ke {G}'{W}bitly{G}'\n{W}[{Y}2{W}]{R}. {W}Short Ke {G}'{W}tinyurl{G}'")
        pilih=input(f"{W}Pilih Menu Tools {R}:{G} ")
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
        print (f"{W}[{R}!{W}] Program Dihentikan {R}!!!")
        sys.exit()

banner()
inputt()
