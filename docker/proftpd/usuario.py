from sys import argv
import crypt
import commands

for i in range(len(argv[1].split(";"))):
	contra = crypt.crypt(argv[2].split(";")[i],"salt")
	commands.getoutput("if [ ! -d /var/www/html/" + argv[1].split(";")[i] + " ] ;then mkdir /var/www/html/" + argv[1].split(";")[i] + " ;fi")
	commands.getoutput("useradd " + argv[1].split(";")[i] + " -p " + contra + "  -d /var/www/html/" + argv[1].split(";")[i] + " -s /bin/bash")
	commands.getoutput("chown " + argv[1].split(";")[i] + ":" + argv[1].split(";")[i] + " /var/www/html/"+ argv[1].split(";")[i])
