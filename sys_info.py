import socket
from pyautogui import size
from sys import platform as name
import platform
import psutil
windows = """
                 ..----..__
               /_______/   ~~----~~/|
             /'   /' /---  /'~~' /'/|
           /..----./__   /~~~~~/|  ||
          |  .----._  ~~----~~|/' |/|
          | |      | |~~----. |/| | |
          | |      | |      | |/' | |
          | |.----.| |      | |  /'/|
          | |      | |~~----| |/' | |
          | |      | |      | | |/|/'
          | |.----.| |      | | '/'
          |_..----..__~~----' |/'
                        ~~----~~'



"""
apple = """
        /)
   .-"".L,""-.
  ;       :.  :
  (       :)  )
   :         ;
    "..-"-.."
"""
linux = """
              a8888b.
             d888888b.
             8P"YP"Y88
             8|o||o|88
             8'    .88
             8`   ' Y8.
            d/ :)  `8b.
          .dP   .     Y8b.
         d8:'   "   `::88b.
        d8"           `Y88b
       :8P     '       :888
        8a.    :      _a88P
      ._/"Yaa_ :    .| 88P|
 jgs  \    YP"      `| 8P  `.
 a:f  /     \._____.d|    .'
      `--..__)888888P`._.'
"""
# resolution
width , height = size()
# hostname
hostname = socket.gethostname()
# ip_address
ip_address = socket.gethostbyname(hostname)
# system version
os_info = platform.platform()
# memory
ram = psutil.virtual_memory().total
# ram in GigaBytes
ram = ram*0.000000001 
# architecture
architect = platform.architecture()
processor =  platform.processor()

if name == 'win32':
    print(windows)
if name == 'darwin':
    print(apple)
if name == 'linux' or name == 'linux2':
    print(linux)      
    
print(f'Hostname - {hostname}')
print(f'IP Address - {ip_address}')
print(f'OS Info -  {os_info}')
print(f'Ram - {ram} GB')
print(f'Architecture - {architect}')
print(f'Processor - {processor}')
print(f'Width - {width}')
print(f'Height - {height}')
      