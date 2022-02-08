# die Variable "hashed" hat wie folgt auszusehen: b'$2b$04$mIYoOZrAQm3jr0DrrE8Mqe/mxSiR.Pe/wPfTuJUfMKHxay8O0CmpG'
# bei dem vorliegenden bcrypt-Hash ist das Passwort 3101
# Script erstellt durch Linder 06.10.2020
# Happy Bruteforcing :)

import bcrypt

for num in range(0, 9999):
    passwd = "{:04n}".format(num)
    hashed = b'$2b$04$BG.SqGC/iKQJi4m.RP9raOFmg77uWGDKxofswbo1R30243qFpckii'
    if bcrypt.checkpw(passwd.encode('UTF-8'), hashed):
        print("PIN-Code:",passwd,"\n\nViel Erfolg beim Sichern")
