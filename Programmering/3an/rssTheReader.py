from ftplib import FTP

ftp = FTP(host="127.0.0.1", user="root", passwd="Henkekung123")

filetosend = "feed.py"

file = open(filetosend, "rb")

ftp.storbinary("STOR " + filetosend, file)

ftp.quit()
file.close()

'''
# Hämta en fil
filetoget = "makefile"

file = open(filetoget, "wb")

ftp.cwd("//nånmapp")
ftp.retrbinary("RETR " + filetoget, file.write)

ftp.quit()
file.close()
'''

'''
ftp.dir()

"""ftp.cwd("//nån mapp")"""

print("nMappen nån mapp")
ftp.dir()

ftp.quit()
'''