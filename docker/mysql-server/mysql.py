from sys import argv
import crypt
import commands

for i in range(len(argv[1].split(";"))):
	commands.getoutput("echo 'CREATE DATABASE IF NOT EXISTS "+argv[1].split(";")[i]+";' >> $tfile")
	commands.getoutput("echo 'GRANT ALL ON "+argv[1].split(";")[i]+".* to '"+argv[1].split(";")[i]+"'@'%' IDENTIFIED BY '"+argv[2].split(";")[i]+"';' >> $tfile")
