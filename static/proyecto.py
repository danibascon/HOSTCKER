from sys import argv
import bottle
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post, default_app, response, get, post
import os
import json
import requests
import commands

#


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
  if int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2]) != 0:
    var = 'Ese usuario ya esta registrado'
    return template('register.tpl', variable = var)
  else:
    insert = "insert into usuarios values ('"+user+"','"+passwd+"','"+nombre+"','"+apellido+"','"+email+"');"
    commands.getoutput("mysql -u dani -pdani proyecto -e "+'"'+insert+'"')
    if int(commands.getoutput("mysql -u dani -pdani proyecto -e 'select count(usuario) from usuarios where usuario = "+'"'+user+'";'+"'").split("\n")[2]) == 0:
      var = "Ha ocurrido un problema a la hora de registar el usuario '"+user+"'"
      return template('register.tpl', variable = var)
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