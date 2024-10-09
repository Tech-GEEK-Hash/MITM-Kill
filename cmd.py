import os
import subprocess
import ctypes
import time
import sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
adm=is_admin()
if is_admin():
    j=1
    lst=[]
    lst1=[]
    MAC=0
    while j>0:
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call('powershell.exe [Set-ExecutionPolicy Unrestricted]', creationflags=CREATE_NO_WINDOW)
        time.sleep(15)
        x=subprocess.Popen(['powershell.exe',r"C:\Users\Moon\AppData\Local\Programs\Python\Python310\arp.ps1"], shell=False)
        time.sleep(20)
        net=open("Network.txt")
        data = net.read()
        for i in data:
            if i.isdigit() or i.isalpha():
                lst.append(i)
        net.close()
        for m in range(3):
            z=subprocess.Popen(['powershell.exe',r"C:\Users\Moon\AppData\Local\Programs\Python\Python310\arp1.ps1"], shell=False)
            time.sleep(15)
            net1=open("NewNetwork.txt")
            data1 = net1.read()
            for k in data1:
                if k.isdigit() or k.isalpha():
                    lst1.append(k)       
            net1.close()
            if lst1!=lst:
                print("Alert, MITM has been implemented on your network")
                print("Terminating network connections and performing necessary steps")
                subprocess.Popen(['powershell.exe',"ipconfig /flushdns"])
                time.sleep(10)
                subprocess.Popen(['powershell.exe',r'netsh interface set interface name="Wi-Fi" admin=DISABLED'])
                os.system('cmd /k "netsh interface set interface name="Ethernet" admin=DISABLED"')
                time.sleep(10)
                subprocess.Popen(['powershell.exe',r'netsh interface set interface name="Wi-Fi" admin=ENABLED'])
                subprocess.Popen(['powershell.exe',r'netsh interface set interface name="Ethernet" admin=ENABLED'])
                time.sleep(5)
                os.remove("NewNetwork.txt")
                time.sleep(5)
                lst1.clear()
            elif lst1==lst:
                from getmac import get_mac_address as gma
		def generate_random_mac():
			mac = [random.randint(0x00, 0xFF) for _ in range(6)]
			mac[0] = mac[0] & 0xFE
			return ''.join(f'{byte:02X}' for byte in mac)
		random_mac = generate_random_mac()
                r=gma()
                T=subprocess.Popen(['powershell.exe',r"C:\Users\Moon\AppData\Local\Programs\Python\Python310\arpa.ps1"], shell=False)
                time.sleep(20)
                netR=open("Networkarp.txt")
                dataR = netR.read()
                if r in dataR:
                    MAC=count(r)
                netR.close()
                print("Number of copies of your MAC address",MAC)
                if MAC>0:
                    print("Alert MITM may have been implemented on your network")
                    subprocess.Popen(['powershell.exe',"ipconfig /flushdns"])
                    time.sleep(10)
                    subprocess.Popen(['powershell.exe',r'netsh interface set interface name="Wi-Fi" admin=DISABLED'])
                    os.system('cmd /k "netsh interface set interface name="Ethernet" admin=DISABLED"')
                    time.sleep(10)
                    subprocess.Popen(['powershell.exe', "reg add “HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0001” /v NetworkAddress /d {random_mac} /f"])
                    subprocess.Popen(['powershell.exe',r'netsh interface set interface name="Wi-Fi" admin=ENABLED'])
                    subprocess.Popen(['powershell.exe',r'netsh interface set interface name="Ethernet" admin=ENABLED'])
                    time.sleep(5)
                    os.remove("NewNetwork.txt")
                    time.sleep(5)
                    lst1.clear()
                    r=''
                    MAC=0
                elif MAC==0:
                    print("All OK")
                    time.sleep(5)
                    time.sleep(5)
                    os.remove("NewNetwork.txt")
                    lst1.clear()
                    time.sleep(20)
                    r=''
                    MAC=0
        lst.clear()
        lst1.clear()
        r=''
        MAC=0
        os.remove("Network.txt")
else:
    print("Re run the program with admin rights")
