import time
import os, sys

try:
    import googlesearch, colorama
except ImportError:
    os.system('python3 -m pip install googlesearch-python')
    os.system('pip install colorama')

from googlesearch import search
from colorama import Fore, Back, Style

s = Style
f = Fore
r = f.RED
g = f.GREEN
y = f.YELLOW
b = f.BLUE
c = f.CYAN
line = f'{y}|                               |'
line2 = f'{y}================================='


def banner():
    print(f"""{y}{s.BRIGHT}   
|                               |
|===============================|
|-------------------------------|
~~~~~[+]{r}By: Anikin Luke{y}[+]~~~~~~
            {c}DORKER{y}       
|-------------------------------|
|===============================|
|                               |
|                               |""")


os.system('clear')
log = ("")
banner()
def dorks():
    try:
        dork = input(f"{y}|{g}  [!]Enter a Dork:{y} ")
        amount = input(f"{y}|{g}  [!]Enter Amount Value:{y} ")
        log = input(f"{y}|{g}  [!]Output file name:{y} ")
        print(line)
        print(line2)
        def logger(user):
            file = open((log) + ".txt", "a")
            file.write(str(user))
            file.write("\n")
            file.close()

        requ = 0
        flag = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            flag = flag + 1
            print(f"{c}",results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            user = results

            logger(user)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print(f"\n{r}[x] User Interruption Detected..!")
            time.sleep(0.5)
            sys.exit(1)

    print(f"\n{g}[✅️] Complete!!")
    sys.exit()



dorks()
