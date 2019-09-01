from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from fuzzywuzzy import fuzz
import webbrowser
import subprocess
import random
import os

Linked = 'https://duckduckgo.com/?q='
lookup_dict = {"rt": "retweet", "dm": "direct message", "awsm": "awesome", "luv": "love", "adorbs": "adorable",
               "booty": "butt", "broke": "poor", "busted": "caught", "chick": "girl", "aaf": "as a friend",
               "aabf": "as a best friend", "asaik": "as soon as I know", "rip": "rest in peace", "bb": "baby",
               "da9": "the family", "diss": "disrespecting", "delish": "delicious", "fam": "family", "kudos": "respect",
               "pos": "parents over shoulder", "pir": "parents in room", "props": "respect", "smh": "shaking my head",
               "smol": "small", "yhf": "you have failed", "zup": "what's up?", "zonked": "tired", "yt": "youtube",
               "YT": "youtube", "faq": "questions", "re": "reply", "acc": "account", "sign": "signature", "u": "you",
               "idk": "I don't know", "f2f": "face to face", "twite": "twitter", "fb": "facebook", "insta": "instagram",
               "stats": "statistics"}


# Opens Web pages
class Webapp:
    @staticmethod
    def youtube():
        webbrowser.open('https://www.youtube.com')

    @staticmethod
    def twitter():
        webbrowser.open('https://www.twitter.com')

    @staticmethod
    def instagram():
        webbrowser.open('https://www.instagram.com')

    @staticmethod
    def google():
        webbrowser.open('https://www.google.com')

    @staticmethod
    def facebook():
        webbrowser.open('https://www.facebook.com')

    @staticmethod
    def spotify():
        webbrowser.open('https://www.spotify.com')

    @staticmethod
    def apple():
        webbrowser.open('https://www.apple.com')

    @staticmethod
    def samsung():
        webbrowser.open('https://www.samsung.com')

    @staticmethod
    def maps():
        webbrowser.open('https://maps.google.com')

    @staticmethod
    def mail():
        webbrowser.open('mailto:crafterbenben@gmail.com')

    @staticmethod
    def translation():
        webbrowser.open('https://translate.google.com')

    @staticmethod
    def weather():
        webbrowser.open('https://darksky.net')

    @staticmethod
    def netflix():
        webbrowser.open('https://www.netflix.com')

    @staticmethod
    def news():
        webbrowser.open('https://news.google.com')

    @staticmethod
    def amazon():
        webbrowser.open('https://www.amazon.com')

    @staticmethod
    def pinterest():
        webbrowser.open('https://www.pinterest.com')

    @staticmethod
    def website():
        webbrowser.open('https://benben377.wixsite.com/home')

    @staticmethod
    def grabify():
        webbrowser.open('https://grabify.link')

    @staticmethod
    def baidu():
        webbrowser.open('https://baidu.com')

    @staticmethod
    def wikipedia():
        webbrowser.open('https://wikipedia.org')

    @staticmethod
    def tencent():
        webbrowser.open('https://qq.com')

    @staticmethod
    def taobao():
        webbrowser.open('https://taobao.com')

    @staticmethod
    def tmall():
        webbrowser.open('https://tmall.com')

    @staticmethod
    def sohu():
        webbrowser.open('https://sohu.com')

    @staticmethod
    def yahoo():
        webbrowser.open('https://yahoo.com')

    @staticmethod
    def jingdong():
        webbrowser.open('https://jd.com')

    @staticmethod
    def windows():
        webbrowser.open('https://live.com')

    @staticmethod
    def vk():
        webbrowser.open('https://vk.com')

    @staticmethod
    def weibo():
        webbrowser.open('https://weibo.com')

    @staticmethod
    def reddit():
        webbrowser.open('https://reddit.com')

    @staticmethod
    def sinacorp():
        webbrowser.open('https://sina.com.cn')

    @staticmethod
    def yandex():
        webbrowser.open('https://yandex.ru')

    @staticmethod
    def haosou():
        webbrowser.open('https://360.cn')

    @staticmethod
    def blogspot():
        webbrowser.open('https://blogspot.com')

    @staticmethod
    def pornhub():
        webbrowser.open('https://pornhub.com')

    @staticmethod
    def twitch():
        webbrowser.open('https://twitch.tv')

    @staticmethod
    def linkedin():
        webbrowser.open('https://linkedin.com')

    @staticmethod
    def csdn():
        webbrowser.open('https://csdn.net')

    @staticmethod
    def aliexpress():
        webbrowser.open('https://aliexpress.com')

    @staticmethod
    def alipay():
        webbrowser.open('https://alipay.com')

    @staticmethod
    def microsoft():
        webbrowser.open('https://microsoft.com')

    @staticmethod
    def ebay():
        webbrowser.open('https://ebay.com')

    @staticmethod
    def bing():
        webbrowser.open('https://bing.com')

    @staticmethod
    def imdb():
        webbrowser.open('https://imdb.com')

    @staticmethod
    def naver():
        webbrowser.open('https://Naver.com')

    @staticmethod
    def github():
        webbrowser.open('https://github.com')

    @staticmethod
    def stackoverflow():
        webbrowser.open('https://stackoverflow.com')

    @staticmethod
    def whatsapp():
        webbrowser.open('https://whatsapp.com')

    @staticmethod
    def odnoklassniki():
        webbrowser.open('https://ok.ru')

    @staticmethod
    def quora():
        webbrowser.open('https://quora.com')

    @staticmethod
    def sogou():
        webbrowser.open('https://sogou.com')

    @staticmethod
    def accuweather():
        webbrowser.open('https://accuweather.com')

    @staticmethod
    def ampproject():
        webbrowser.open('https://ampproject.org')

    @staticmethod
    def bitly():
        webbrowser.open('https://bitly.com')

    @staticmethod
    def shenma():
        webbrowser.open('https://sm.cn')

    @staticmethod
    def minecraft():
        webbrowser.open('https://minecraft.net')

    @staticmethod
    def raetia():
        webbrowser.open('https://www.iteraetia.it')

    @staticmethod
    def stol():
        webbrowser.open('https://www.stol.it')

    @staticmethod
    def deejay():
        webbrowser.open('https://www.deejay.it')

    @staticmethod
    def tabacco():
        webbrowser.open('https://www.gustotabacco.it')

    @staticmethod
    def zombie():
        webbrowser.open('https://the-zombie-hunter.blogspot.com')

    @staticmethod
    def infinity():
        webbrowser.open('https://www.xfinity.com')

    @staticmethod
    def chan4():
        webbrowser.open('https://www.4chan.org')

    @staticmethod
    def wikihow():
        webbrowser.open('https://m.wikihow.com')

    @staticmethod
    def fandom():
        webbrowser.open('https://community.fandom.com')

    @staticmethod
    def slitherio():
        webbrowser.open('http://slither.io')

    @staticmethod
    def agario():
        webbrowser.open('https://agar.io')

    @staticmethod
    def happywheels():
        webbrowser.open('https://happywheels8.com')

    @staticmethod
    def pottermore():
        webbrowser.open('https://www.pottermore.com')

    @staticmethod
    def webtoon():
        webbrowser.open('https://www.webtoons.com')

    @staticmethod
    def steam():
        webbrowser.open('https://store.steampowered.com')

    @staticmethod
    def origin():
        webbrowser.open('https://www.origin.com')

    @staticmethod
    def deviantart():
        webbrowser.open('https://www.deviantart.com')

    @staticmethod
    def ao3():
        webbrowser.open('https://archiveofourown.org')

    @staticmethod
    def wattpad():
        webbrowser.open('https://www.wattpad.com')


# Opens Applications
class Winapp:
    @staticmethod
    def calculator():
        os.startfile('C:/Windows/System32/calc.exe')

    @staticmethod
    def notepad():
        os.startfile('C:/Windows/System32/notepad.exe')

    @staticmethod
    def music():
        os.startfile('C:/Program Files (x86)/Windows Media Player/wmplayer.exe')

    @staticmethod
    def paint():
        os.startfile('C:/Windows/System32/mspaint.exe')

    @staticmethod
    def cmd():
        os.startfile('C:/Windows/System32/cmd.exe')

    @staticmethod
    def filesearch():
        os.startfile('C:/Windows/explorer.exe')

    @staticmethod
    def shutdown():
        os.popen('shutdown -s -t 30 -c “Computer shutdown in 30 seconds.”').read()

    @staticmethod
    def restart():
        os.popen('shutdown -r')

    @staticmethod
    def logout():
        os.popen('shutdown -l')

    @staticmethod
    def chrome():
        os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

    @staticmethod
    def firefox():
        os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

    @staticmethod
    def word():
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk')

    @staticmethod
    def excel():
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk')

    @staticmethod
    def mccraft():
        os.startfile('C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher')

    @staticmethod
    def noteplus():
        os.startfile('C:\\Program Files\\Notepad++\\notepad++')


def close_window(tkinterlvl):
    tkinterlvl.destroy()


def hotspot():
    bestlevel = Toplevel()
    bestlevel.title("Hotspot instructions")
    label0 = Label(bestlevel, text="How to create Hotspot\n", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Label(bestlevel, text="Enter the following command to enable Wi-Fi Hotspot:\n"
                                   "\"netsh wlan set hostednetwork mode=allow ssid=Hotspotname key=password\"\n",
                   font=("arial", 10, "bold"))
    label1.pack()

    label2 = Label(bestlevel, text="Then, to start Hotspot, enter:\n\"netsh wlan start hostednetwork\"\n",
                   font=("arial", 10, "bold"))
    label2.pack()

    label3 = Label(bestlevel, text="As well as to stop hotspot, enter:\n\"netsh wlan stop hostednetwork\"\n",
                   font=("arial", 10, "bold"))
    label3.pack()

    execute = Button(bestlevel, text="Open CMD", command=lambda: Winapp.cmd(), font=("arial", 10, "bold"))
    execute.pack()


def statistics():
    biglevel = Toplevel()
    biglevel.title("Computer statistics")
    label0 = Label(biglevel, text="Output:\n", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Text(biglevel)
    label1.pack(expand=True)

    o = subprocess.check_output('netstat -n', shell=True)
    for i in o.splitlines():
        label1.insert(END, i)
        label1.insert(END, '\n')


def driverlist():
    highlevel = Toplevel()
    highlevel.title("List of drivers")
    label0 = Label(highlevel, text="Output:\n", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Text(highlevel)
    label1.pack(expand=True)

    o = subprocess.check_output('driverquery', shell=True)
    for i in o.splitlines():
        label1.insert(END, i)
        label1.insert(END, '\n')


def gotit():
    nextlevel = Toplevel()
    nextlevel.title("Output")
    label0 = Label(nextlevel, text="Output:", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Text(nextlevel)
    label1.pack(expand=True, fill="y", side=LEFT)

    label2 = Text(nextlevel)
    label2.pack(expand=True, fill="y", side=RIGHT)

    label3 = Text(nextlevel)
    label3.pack(expand=True, side=BOTTOM)

    label4 = Text(nextlevel)
    label4.pack(expand=True, side=LEFT)

    n = getting.get()

    o = subprocess.check_output('ipconfig', shell=True)
    for i in o.splitlines():
        label1.insert(END, i)
        label1.insert(END, '\n')

    p = subprocess.check_output('ping ' + n, shell=True)
    for i in p.splitlines():
        label2.insert(END, i)
        label2.insert(END, '\n')

    o = subprocess.check_output('nslookup ' + n, shell=True)
    for i in o.splitlines():
        label3.insert(END, i)
        label3.insert(END, '\n')

    o = subprocess.check_output('tracert ' + n, shell=True)
    for i in o.splitlines():
        label4.insert(END, i)
        label4.insert(END, '\n')


def ping():
    global getting
    newlevel = Toplevel()
    newlevel.title("Pingin the IP")
    label0 = Label(newlevel, text="Enter IP or Host", font=("arial", 10, "bold"), fg="green")
    label0.pack()
    getting = Entry(newlevel)
    getting.pack()
    confr = Button(newlevel, text="CONFIRM", command=lambda: gotit(), font=("arial", 10, "bold"))
    confr.pack()


def arp():
    arplevel = Toplevel()
    arplevel.title("Arp connections")
    label0 = Label(arplevel, text="Output:\n", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Text(arplevel)
    label1.pack(expand=True)

    o = subprocess.check_output('arp -a', shell=True)
    for i in o.splitlines():
        label1.insert(END, i)
        label1.insert(END, '\n')


def route():
    routelevel = Toplevel()
    routelevel.title("Prints the route")
    label0 = Label(routelevel, text="Output:\n", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Text(routelevel)
    label1.pack(expand=True)

    o = subprocess.check_output('route print', shell=True)
    for i in o.splitlines():
        label1.insert(END, i)
        label1.insert(END, '\n')


def netuser():
    netlevel = Toplevel()
    netlevel.title("Netuser commands")
    label0 = Label(netlevel, text="Output:\n", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Text(netlevel)
    label1.pack(expand=True)

    o = subprocess.check_output('net user', shell=True)
    for i in o.splitlines():
        label1.insert(END, i)
        label1.insert(END, '\n')


def tasklist():
    tasklevel = Toplevel()
    tasklevel.title("Task manager")
    label0 = Label(tasklevel, text="Output:\n", font=("arial", 15, "bold"), fg="red")
    label0.pack()

    label1 = Text(tasklevel)
    label1.pack(expand=True)

    o = subprocess.check_output('tasklist', shell=True)
    for i in o.splitlines():
        label1.insert(END, i)
        label1.insert(END, '\n')


def logfiles():
    date = str(datetime.now())
    f = open('log.txt', 'a')
    f.write("Log opened at " + date + "\n")
    f.close()
    os.startfile('log.txt')


def helper():
    toplevel = Toplevel()
    toplevel.title("Helping hand")
    label01 = Label(toplevel, text="")
    label01.pack()
    label0 = Label(toplevel, text="Information", font=("arial", 15, "bold"), height=0, width=100, fg="red")
    label0.pack()
    label1 = Label(toplevel, text="This is a simple Windows assistant programmed by Benjamin.\n"
                                  "I tested it on Windows with standard download location\n"
                                  "It may not work with other settings, I'm working on it.", height=0, width=100,
                   font=("arial", 10, "bold"))
    label1.pack()
    label00 = Label(toplevel, text="")
    label00.pack()
    label2 = Label(toplevel, text="Help", font=("arial", 15, "bold"), height=0, width=100, fg="green")
    label2.pack()
    label3 = Label(toplevel, text="For suggestions or other questions, just mail me\n"
                                  "You can type \"Mail Ben\" into the Assistant,\n"
                                  "or copy it from here: crafterbenben@gmail.com", height=0, width=100,
                   font=("arial", 10, "bold"))
    label3.pack()
    label000 = Label(toplevel, text="")
    label000.pack()
    label4 = Label(toplevel, text="Apps and websites", font=("arial", 15, "bold"), height=0, width=100, fg="blue")
    label4.pack()
    label5 = Label(toplevel, text="For a list of all implemented apps and Websites,\n"
                                  "just type \"List\" into the assistant", height=0, width=100,
                   font=("arial", 10, "bold"))
    label5.pack()
    label6 = Label(toplevel, text="")
    label6.pack()


def listing():
    listlevel = Toplevel()
    listlevel.title("Full list")
    label0 = Label(listlevel, text="These are all the saved Apps and Websites", font=("arial", 15, "bold"))
    label0.pack()
    label05 = Label(listlevel, text="")
    label05.pack()
    labela = Text(listlevel)
    labela.pack(side=LEFT)
    labelb = Text(listlevel)
    labelb.pack(side=RIGHT)

    c = dir(Webapp)[26:]
    d = dir(Winapp)[26:]

    for i in c:
        labela.insert(END, i)
        labela.insert(END, '\n')

    for j in d:
        labelb.insert(END, j)
        labelb.insert(END, '\n')


def randomizer():
    c = dir(Webapp)[26:]
    a = random.choice(c)
    eval('Webapp.' + a + '()')


def diceroll():
    dicelevel = Toplevel()
    dicelevel.title("Roll the dice!")
    label0 = Label(dicelevel, text="Let's roll the dice!", font=("arial", 15, "bold"))
    label0.pack()
    label05 = Label(dicelevel, text="")
    label05.pack()
    label1 = Label(dicelevel, text="Result:", font=("arial", 10, "bold"))
    label1.pack()
    label2 = Label(dicelevel, text="", font=("arial", 10, "bold"), fg="green")
    label2.pack()
    label3 = Label(dicelevel, text="")
    label3.pack()

    minimum = 0
    maximum = 100

    a = random.randint(minimum, maximum)
    label2.config(text=a)

    btn = Button(dicelevel, text="Again?", font=("arial", 10, "bold"),
                 command=lambda: [close_window(dicelevel), diceroll()])
    btn.pack()


def guessing():
    global numberguessing
    numberguessing = random.randint(0, 100)

    def guessing1():
        t = int(entern.get())
        print(t)
        guesses = 0
        if t < numberguessing:
            guesses += 1
            outcome.config(text="guess is low (" + str(t) + ")")
            entern.delete(0, 'end')
        elif t > numberguessing:
            guesses += 1
            outcome.config(text="guess is high (" + str(t) + ")")
            entern.delete(0, 'end')
        elif t == numberguessing:
            messagebox.showinfo("Success", "You did it! Congratulations\n"
                                           "The number was: " + str(numberguessing))
            guesslevel.destroy()

    guesslevel = Toplevel()
    guesslevel.title("Can you guess it?")
    label0 = Label(guesslevel, text="Guess the secret number!", font=("arial", 15, "bold"))
    label0.pack()
    label05 = Label(guesslevel, text="")
    label05.pack()
    label1 = Label(guesslevel, text="Enter your guess\n(Number from 1 to 100)", font=("arial", 10, "bold"))
    label1.pack()
    entern = Entry(guesslevel)
    entern.pack()
    btn = Button(guesslevel, text="Guess it", font=("arial", 10, "bold"), command=guessing1)
    btn.pack()
    label2 = Label(guesslevel, text="")
    label2.pack()
    label3 = Label(guesslevel, text="Output:", font=("arial", 10, "bold"))
    label3.pack()
    outcome = Label(guesslevel, text="", font=("arial", 10, "bold"), fg="red")
    outcome.pack()


def credition():
    creditlevel = Toplevel()
    creditlevel.title("Credits")
    label0 = Label(creditlevel, text="CREDITS", font=("arial", 15, "bold"), fg="green")
    label0.pack()
    label05 = Label(creditlevel, text="")
    label05.pack()
    label1 = Label(creditlevel, text="this asiistant has been created for fun purpose only. Don't take anything to "
                                     "serious, except this.\nIf something doesn't work, please report it immediately.\n"
                                     "The assistant has been created by Benjamin Demetz, better known as Benben377.\n"
                                     "It has been created with much support from many other people.\n"
                                     "I especially want to thank Valentina Schöpf, Nina Demetz, 1L1C1M and Kia for "
                                     "their great support.\n But if you are reading this, a big thanks to you too for "
                                     "downloading and using my assistant.\n"
                                     "Goodbye,\nBenjamin", font=("arial", 10, "bold"))
    label1.pack()
    label2 = Label(creditlevel, text="")
    label2.pack()


def eightball():
    def execution():
        answers = random.randint(1, 8)
        if answers == 1:
            label2.config(text="It is certain")

        elif answers == 2:
            label2.config(text="Outlook good")

        elif answers == 3:
            label2.config(text="You may rely on it")

        elif answers == 4:
            label2.config(text="Ask again later")

        elif answers == 5:
            label2.config(text="Concentrate and ask again")

        elif answers == 6:
            label2.config(text="Reply hazy, try again")

        elif answers == 7:
            label2.config(text="My reply is no")

        elif answers == 8:
            label2.config(text="My sources say no")

    eightlevel = Toplevel()
    eightlevel.title("8Ball answers")
    label0 = Label(eightlevel, text="Ask a \"Yes\" or \"No\" question", font=("arial", 10, "bold"), fg="steelblue")
    label0.pack()
    entering = Entry(eightlevel)
    entering.pack()
    label1 = Label(eightlevel, text="")
    label1.pack()
    label2 = Label(eightlevel, text="", font=("arial", 10, "bold"), fg="green")
    label2.pack()
    btn = Button(eightlevel, text="Ask the assistant", command=execution, font=("arial", 10, "bold"), fg="red")
    btn.pack()
    label3 = Label(eightlevel, text="")
    label3.pack()


# Checks for the input of the User
def checker():
    global x
    web = Webapp
    app = Winapp
    y = collector.get()
    stoppwords = set(stopwords.words('english'))
    words = word_tokenize(y)
    wordsfiltered = []
    for w in words:
        if w not in stoppwords:
            wordsfiltered.append(w)
    a = " ".join(wordsfiltered)
    words = a.split()
    new_words = []
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        new_words.append(word)
        x = " ".join(new_words)
    f = open('log.txt', 'a')
    f.write(x + '\n')
    print(y)
    print(a)
    if fuzz.token_sort_ratio(x, "Youtube") >= 90:
        web.youtube()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Twitter") >= 90:
        web.twitter()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Instagram") >= 90:
        web.instagram()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Google") >= 90:
        web.google()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Facebook") >= 90:
        web.facebook()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Spotify") >= 90:
        web.spotify()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Apple") >= 90:
        web.apple()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Samsung") >= 90:
        web.samsung()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Maps") >= 90:
        web.maps()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Calculator") >= 90:
        app.calculator()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Notepad") >= 90:
        app.notepad()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Music") >= 90:
        app.music()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Paint") >= 90:
        app.paint()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Cmd") >= 90:
        app.cmd()
        collector.delete('0', 'end')
    elif x in ["Mail Ben", "Mail ben", "mail ben", "mail Ben", "Mail", "mail"]:
        web.mail()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Translation") >= 90:
        web.translation()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Help") >= 90:
        helper()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Weather") >= 90:
        web.weather()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Netflix") >= 90:
        web.netflix()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "News") >= 90:
        web.news()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Amazon") >= 90:
        web.amazon()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Pinterest") >= 90:
        web.pinterest()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Search file") >= 90:
        app.filesearch()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Ping") >= 90:
        ping()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Shutdown") >= 90:
        app.shutdown()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Trettel") >= 90:
        web.grabify()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Restart") >= 90:
        app.restart()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Log out") >= 90:
        app.logout()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Statistics") >= 90:
        statistics()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Driver list") >= 90:
        driverlist()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Hotspot") >= 90:
        hotspot()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Baidu") >= 90:
        web.baidu()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Wikipedia") >= 90:
        web.wikipedia()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Tencent") >= 90:
        web.tencent()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Taobao") >= 90:
        web.taobao()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Tmall") >= 90:
        web.tmall()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Sohu") >= 90:
        web.sohu()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Yahoo") >= 90:
        web.yahoo()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Jingdong") >= 90:
        web.jingdong()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Windows") >= 90:
        web.windows()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Vk") >= 90:
        web.vk()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Weibo") >= 90:
        web.weibo()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Reddit") >= 90:
        web.reddit()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Sinacorp") >= 90:
        web.sinacorp()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Yandex") >= 90:
        web.yandex()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Haosou") >= 90:
        web.haosou()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Blogspot") >= 90:
        web.blogspot()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Pornhub") >= 90:
        web.pornhub()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Twitch") >= 90:
        web.twitch()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Linkedin") >= 90:
        web.linkedin()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Csdn") >= 90:
        web.csdn()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Ali Express") >= 90:
        web.aliexpress()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Ali Pay") >= 90:
        web.alipay()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Microsoft") >= 90:
        web.microsoft()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Ebay") >= 90:
        web.ebay()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Bing") >= 90:
        web.bing()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Imdb") >= 90:
        web.imdb()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Naver") >= 90:
        web.naver()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Github") >= 90:
        web.github()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Stack Overflow") >= 90:
        web.stackoverflow()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Whatsapp") >= 90:
        web.whatsapp()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Odnoklassniki") >= 90:
        web.odnoklassniki()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Quora") >= 90:
        web.quora()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Sogou") >= 90:
        web.sogou()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Accuweather") >= 90:
        web.accuweather()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Amp Project") >= 90:
        web.ampproject()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Bitly") >= 90:
        web.bitly()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Shenma") >= 90:
        web.shenma()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Minecraftnet") >= 90:
        web.minecraft()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Raetia") >= 90:
        web.raetia()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Stol") >= 90:
        web.stol()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Deejay") >= 90:
        web.deejay()
        collector.delete('0', 'end')
    elif x in ["List", "list", "App", "app", "Apps", "apps", "Website", "website"]:
        listing()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Arp") >= 90:
        arp()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Route") >= 90:
        route()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Net User") >= 90:
        netuser()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Tasklist") >= 90:
        tasklist()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Log") >= 90:
        logfiles()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Tabacco") >= 90:
        web.tabacco()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Zombie") >= 90:
        web.zombie()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Infinity") >= 90:
        web.infinity()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Chan4") >= 90:
        web.chan4()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Wikihow") >= 90:
        web.wikihow()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Fandom") >= 90:
        web.fandom()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Slitherio") >= 90:
        web.slitherio()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Agario") >= 90:
        web.agario()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Happywheels") >= 90:
        web.happywheels()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Pottermore") >= 90:
        web.pottermore()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Webtoon") >= 90:
        web.webtoon()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Steam") >= 90:
        web.steam()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Origin") >= 90:
        web.origin()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Deviantart") >= 90:
        web.deviantart()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Ao3") >= 90:
        web.ao3()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Wattpad") >= 90:
        web.wattpad()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Chrome") >= 90:
        app.chrome()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Firefox") >= 90:
        app.firefox()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Word") >= 90:
        app.word()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Excel") >= 90:
        app.excel()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Minecraft") >= 90:
        app.mccraft()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Notepad++") >= 90:
        app.noteplus()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Random") >= 90:
        randomizer()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Roll") >= 90:
        diceroll()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "Guessing") >= 90:
        guessing()
        collector.delete('0', 'end')
    elif fuzz.token_sort_ratio(x, "8Ball") >= 90:
        eightball()
        collector.delete('0', 'end')
    elif '+' in x:
        a = x.split('+')[0]
        b = x.split('+')[1]
        c = float(a) + float(b)
        calclevel = Toplevel()
        calclevel.title("Result")
        result = Label(calclevel, text=c)
        result.pack()
        collector.delete('0', 'end')
    elif '-' in x:
        a = x.split('-')[0]
        b = x.split('-')[1]
        c = float(a) - float(b)
        calclevel = Toplevel()
        calclevel.title("Result")
        result = Label(calclevel, text=c)
        result.pack()
        collector.delete('0', 'end')
    elif '/' in x:
        a = x.split('/')[0]
        b = x.split('/')[1]
        c = float(a) / float(b)
        calclevel = Toplevel()
        calclevel.title("Result")
        result = Label(calclevel, text=c)
        result.pack()
        collector.delete('0', 'end')
    elif '*' in x:
        a = x.split('*')[0]
        b = x.split('*')[1]
        c = float(a) * float(b)
        calclevel = Toplevel()
        calclevel.title("Result")
        result = Label(calclevel, text=c)
        result.pack()
        collector.delete('0', 'end')
    else:
        webbrowser.open(Linked + x)
        collector.delete('0', 'end')


def confirm(event=None):
    checker()


# Tkinter Code
root = Tk()
root.title("Sociality")
root.geometry('200x200')
root.resizable(0, 0)
root.bind('<Return>', confirm)

# Labels
heading = Label(root, text="Sociality", font=("arial", 20, "bold"), fg="steelblue").pack()
space0 = Label(root, text="").pack()
info = Label(root, text="Name of the Website or App:",
             font=("arial", 10, "bold"), fg="green").pack()
collector = Entry(root)
collector.pack()
space = Label(root, text="").pack()
smallinfo = Label(root, text="Created by Benjamin Demetz", fg="deepskyblue").pack(side=BOTTOM)
# Button
Enter = Button(root, text="ENTER", font=("arial", 15, "bold"), fg="red", command=checker).pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=Winapp.filesearch)
filemenu.add_command(label="Open", command=Winapp.filesearch)
filemenu.add_command(label="Log", command=logfiles)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helper)
helpmenu.add_command(label="Full list", command=listing)
helpmenu.add_command(label="Credits", command=credition)
menubar.add_cascade(label="Help", menu=helpmenu)

gamesmenu = Menu(menubar, tearoff=0)
gamesmenu.add_command(label="Guessing", command=guessing)
gamesmenu.add_command(label="Roll the dice", command=diceroll)
gamesmenu.add_separator()
gamesmenu.add_command(label="Agar.io", command=Webapp.agario)
gamesmenu.add_command(label="Slither.io", command=Webapp.slitherio)
menubar.add_cascade(label="Games", menu=gamesmenu)

randommenu = Menu(menubar, tearoff=0)
randommenu.add_command(label="8Ball", command=eightball)
menubar.add_cascade(label="Random", menu=randommenu)

root.config(menu=menubar)
root.mainloop()

# Programmed by Benjamin Demetz (Benben377)
