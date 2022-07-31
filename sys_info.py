import socket
from sys import platform as name
from screeninfo import get_monitors
import platform
import psutil
uname = platform.uname()
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
# width , height = size()
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
release = uname.release
version = uname.version
machine = uname.machine
cpufreq = psutil.cpu_freq()
maxfreq = str(cpufreq.max) + "Mhz"
minfreq =  str(cpufreq.min) + "Mhz"
currentfreq = str(cpufreq.current) + "Mhz"
physical_cores = psutil.cpu_count(logical = False)
total_cores = psutil.cpu_count(logical = True)
if name == 'win32':
    print(windows)

if name == 'darwin':
    print(apple)
if name == 'linux' or name == 'linux2':
    print(linux)      
print("--" * 30)    
print(f'Hostname - {hostname}')
print(f'IP Address - {ip_address}')
print("--" * 30)
print(f'OS Info -  {os_info}')
print(f'Ram - {ram} GigaBytes')
print(f'Architecture - {architect}')
print(f'Processor - {processor}')
print(f'Release - {release}')
print(f'Version - {version}')
print(f'Machine - {machine}')
print("--" * 30)
print(f'Frequency - {cpufreq}')
print(f'Physical Cores - {physical_cores}')
print(f'Total Cores - {total_cores}')
print("--" * 30)
print("Monitors")
print()
for index,m in enumerate(get_monitors()):
    print(f'{index+1} - {m}')
      