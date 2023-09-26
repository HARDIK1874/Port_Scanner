print("---------------------------------------------------------------------\n")
print("""@@@@@@@   @@@ @@@  @@@@@@@   @@@@@@@                                  
@@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@                                  
@@!  @@@  @@! !@@  @@!  @@@    @@!                                    
!@!  @!@  !@! @!!  !@!  @!@    !@!                                    
@!@@!@!    !@!@!   @!@!!@!     @!!                                    
!!@!!!      @!!!   !!@!@!      !!!                                    
!!:         !!:    !!: :!!     !!:                                    
:!:         :!:    :!:  !:!    :!:                                    
 ::          ::    ::   :::     ::                                    
 :           :      :   : :     :                                     
                                                                      
                                                                      
 @@@@@@    @@@@@@@   @@@@@@   @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  
!@@       !@@       @@!  @@@  @@!@!@@@  @@!@!@@@  @@!       @@!  @@@  
!@!       !@!       !@!  @!@  !@!!@!@!  !@!!@!@!  !@!       !@!  @!@  
!!@@!!    !@!       @!@!@!@!  @!@ !!@!  @!@ !!@!  @!!!:!    @!@!!@!   
 !!@!!!   !!!       !!!@!!!!  !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
     !:!  :!!       !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!: :!!   
    !:!   :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:       :!:  !:!  
:::: ::    ::: :::  ::   :::   ::   ::   ::   ::   :: ::::  ::   :::  
:: : :     :: :: :   :   : :  ::    :   ::    :   : :: ::    :   : :""")

print("\n---------------------------------------------------------------------\n")
print("                    Port Scanner Developed by SIST                     \n")


import threading
import socket

target = str(input("Enter target: "))
#ip = socket.gethostbyname(target)
flag = int(input("Enter 0 for specific port scan or 1 for scanning all ports:"))

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)# 

    try:
        con = s.connect((target,port))

        print('Port :',port,"is open.")

        con.close()
    except: 
        pass
r = 1 
if flag ==1:
    for x in range(1,65535): 

        t = threading.Thread(target=portscan,kwargs={'port':r}) 

        r += 1     
        t.start()
if flag ==0:
    print("Note:Port number should be seperated with a comma\n")
    ports = str(input("Enter ports to scan:"))
    portu = ports.split(",")
    for port in portu:
        port = int(port)
        portscan(port)