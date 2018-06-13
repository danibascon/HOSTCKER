from sys import argv
import bottle
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post, default_app, response, get, post
import os
import json
import requests
import commands

#def docker_start_usuario(user,puerto, var):
#  commands.getoutput("docker run -d -p " + str(puerto) + ":80 --name " + user +" --link mysql:mysql -v proftpd:/var/www/html -e SERVER_NAME='" + user + "' -e VAR='" + var + "' -e DOCUMENTROOT='" + user + "' danibascon/apache2-usuario:7")
 
def docker_start_usuario(user,puerto):
  commands.getoutput("docker run -d -p " + str(puerto) + ":80 --name " + user +" --link mysql:mysql -v proftpd:/var/www/html -e SERVER_NAME='" + user + "' -e DOCUMENTROOT='" + user + "' danibascon/apache2-usuario:7")
 
  return

def docker_stop_servidor():
  commands.getoutput("docker stop servidor servidor_apache mysql phpmyadmin; docker rm servidor servidor_apache mysql phpmyadmin")

  return

def docker_start_mysql(usuario,contra):
  if usuario =="":
    commands.getoutput("docker  run  --name  mysql  -e  DB_REMOTE_ROOT_NAME==root -e DB_REMOTE_ROOT_PASS=root  -e MYSQL_ROOT_HOST=0.0.0.0 -d  -v  mysql:/var/lib/mysql  danibascon/mysql-ubuntu:1")
 
  else:
    commands.getoutput("docker  run  --name  mysql  -e  DB_REMOTE_ROOT_NAME==root -e DB_REMOTE_ROOT_PASS=root  -e DB_USER=" + usuario + "  -e  DB_NAME=" + usuario + "  -e  DB_PASS=" + contra + "  -e MYSQL_ROOT_HOST=0.0.0.0 -d  -v  mysql:/var/lib/mysql  danibascon/mysql-ubuntu:1")

  commands.getoutput("docker run -d -p 82:80 --name phpmyadmin --link mysql:mysql danibascon/phpmyadmin7-ubuntu:2")
  return

def docker_start_servidor():
  usuario =""
  contra=""
  num=int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios;'").split("\n")[2])
  variables = commands.getoutput("mysql -u dani -pdani proyecto -e 'select usuario,contra,puerto from usuarios'").split("\n")[2:]
  

  if num!=0:
#    var=""
    for i in range(len(variables)):
#      docker_start_usuario(variables[i].split("\t")[0],variables[i].split("\t")[2],var)
      docker_start_usuario(variables[i].split("\t")[0],variables[i].split("\t")[2])

      #ip_cliente=commands.getoutput("docker exec -it "+variables[i].split("\t")[0]+" ip a | grep global | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'")
#      commands.getoutput("echo '"+ip_cliente+"' dit.hostcker-"+variables[i].split("\t")[0]+".org' >> /etc/hosts")
      usuario = usuario + variables[i].split("\t")[0] + ";"
      contra = contra + variables[i].split("\t")[1] + ";"

    commands.getoutput("docker run -d --name servidor -e USER='" + usuario[:-1] + "' -e PASS='" + contra[:-1] + "' -v proftpd:/var/www/html danibascon/proftpd")

  else:
    commands.getoutput("docker run -d --name servidor -e USER='" + usuario + "' -e PASS='" + contra + "' -v proftpd:/var/www/html danibascon/proftpd")


 
  commands.getoutput("docker run -d -p 21:21 -p 22:22 -p 81:80 --name servidor_apache --link servidor:servidor danibascon/apache2:1")
  return

def docker_stop_usuario(user):
  commands.getoutput("docker stop " + user + ";docker rm " + user)

  return  

docker_start_mysql(usuario ="",contra="")         
docker_start_servidor()

#ip_servidor_apache=commands.getoutput("docker exec -it servidor_apache ip a | grep global | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'")
#ip_phpmyadmin=commands.getoutput("docker exec -it phpmyadmin ip a | grep global | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'")
#ip_host =commands.getoutput("ip a | grep wlp2s0 | grep global | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'| head -n 1")
#hosts="127.0.0.1\tlocalhost\n127.0.1.1\tmsi"

#commands.getoutput("echo '"+hosts+"' > /etc/hosts")
#commands.getoutput("echo '"+ip_host+" dit.hostcker.org' >> /etc/hosts")
#commands.getoutput("echo '"+ip_servidor_apache+" dit.hostcker-ftp.org' >> /etc/hosts")
#commands.getoutput("echo '"+ip_phpmyadmin+" dit.hostcker-phpmyadmin.org' >> /etc/hosts")

@route('/', method = "get")
def inicio():
	return template('inicio.tpl',variable='')    


@route('/login', method = "post")
def login():
  user = request.forms.get('user')
  passwd = request.forms.get('passwd')
  num = int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2])

  if num == 0:
    var = 'El usuario no existe'
  else:
    if passwd != commands.getoutput("mysql -u dani -pdani proyecto -e 'select contra from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2]:
      var = 'La clave no es correcta'
    else:
      return template('correcto.tpl', variable = user)

  return template('inicio.tpl', variable = var)





@route('/register', method = "get")
def register():
  return template('register.tpl', variable = '')


@route('/registro',method = "post")
def registro():
  user = request.forms.get('user')
  passwd = request.forms.get('passwd')
  nombre = request.forms.get('nombre')
  apellido = request.forms.get('apellido')
  email = request.forms.get('email')
#  wordpress = request.forms.get('wordpress')
#  mail="Bienvenidos a HOSTCKER, "+nombre+" "+apellido+"\n\nusuario: "+user+"\ncontra: "+passwd+"\ndominio: dit."+user+".org"


  if int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios;'").split("\n")[2]) == 0:
    puerto = 83
  else:
    puerto = int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select puerto from usuarios order by puerto desc;'").split("\n")[2]) + 1

  if int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2]) != 0:
    var = 'Ese usuario ya esta registrado'
    return template('register.tpl', variable = var)
  else:
    insert = "insert into usuarios values ('"+user+"','"+passwd+"','"+nombre+"','"+apellido+"','"+email+"','"+str(puerto)+"');"
    commands.getoutput("mysql -u dani -pdani proyecto -e "+'"'+insert+'"')
    
    if int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2]) == 0:
      var = "Ha ocurrido un problema a la hora de registar el usuario '"+user+"'"
      return template('register.tpl', variable = var)

    else:
      docker_stop_servidor()
      docker_start_mysql(user,passwd)
      ip_cliente=commands.getoutput("docker exec -it "+user+" ip a | grep global | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'")
      #commands.getoutput("echo '"+ip_cliente+"' dit.hostcker-"+user+".org' >> /etc/hosts")
      docker_start_servidor()
#      docker_start_usuario(user,puerto,wordpress)
      docker_start_usuario(user,puerto)
#      commands.getoutput("echo '"+mail+"'| sudo sendmail  -s 'HOSTCKER' "+email)
      return template('registrado.tpl', variable = user)


@route('/baja', method = 'get')
def baja():
  return template('baja.tpl', variable = '')


@route('/darbaja', method = 'post')
def darbaja():
  user = request.forms.get('user')
  passwd = request.forms.get('passwd')
  email = request.forms.get('email')
  if int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2]) == 1:
    delete = "delete from usuarios where usuario = '"+user+"'"
    commands.getoutput("mysql -u dani -pdani proyecto -e "+'"'+delete+'"')
    var="El usuario '"+user+"' ha sido eliminado satisfactoriamente"
    docker_stop_usuario(user)
    return template('bajacuenta.tpl', variable=var)

    if int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2]) == 1:
      var = "Ha ocurrido un problema a la hora de dar baja al usuario '"+user+"'"
  else:
    var = 'Ese usuario no existe'
  return template('baja.tpl', variable=var)



@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='static')

run(host='0.0.0.0',port=argv[1])





# consulta=$(mariadb -u root -e "select Level, JobStatus, 
#  RealEndTime from bacula.Job where RealEndTime in 
#  (select max(RealEndTime) from bacula.Job group by Name) 
#  and Name='$host' group by Name;") 