import os
import platform
import subprocess
import re

os.system('cls')

#Operating System
print('Operating System:')
os.system('systeminfo | findstr /C:"OS Name" /C:"OS Version"')
print('')

#Motherboard type/brand
print('Motherboard type/brand:')
os.system('wmic baseboard get product,Manufacturer,version,serialnumber')
print('')

#CPU
print('CPU:')
os.system('wmic cpu get name')
print('')

#RAM
print('RAM:')
os.system('wmic memorychip get capacity')
print('')

#Storage
print('Storage:')
os.system('wmic logicaldisk get size,freespace,caption')
print('')

#GPU
print('GPU:')
os.system('wmic path win32_VideoController get caption')
print('')

#Other Things
print('Other Things:')
os.system('wmic nic get name')
print('')

input('Press enter to exit')
