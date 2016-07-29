#Shellware

Upon execution Shellware will prompt for administrative privileges, once granted it wil copy itself to the C:\Users directory and add a registry entry for persistence. It will open port 8899 on the target machine and listen for a connection. Once a connection is established the program spawns an interactive OS shell. To make the program a little less suspiscious it might prudent to bind Shellware.exe to an innocent binary for deployment.

Furthermore, the program attempts to tamper with certain registry entries to protect itself somewhat(and be generally annoying). The registry tampering attempts
to disable error reporting, system restore and tries to disable LUA. I've had mixed results on different Windows platforms, however a registry entry for persistence has 
been consistently succesful throughout testing on various platforms.


#Note
The shellcode responsible for the operation of the bind shell can easily be replaced with shellcode for a Reverse TCP Shell or Meterpreter service by generating said
payload with the Metasploit Framework.


#Usage
Compile the script to exe with pyinstaller using the --noconsole and --onefile flags and the program is ready for distribution. 
  
