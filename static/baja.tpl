%include('header.tpl')
	<center>
	<h1>Eliminación de usuarios</h1>
	<h3>{{variable}}</h3>
	<h2>
	<form action="/darbaja" method="post">
		<label>Usuario</label>
		<input type="text" name="user" required/>
		<br>
		<label>Contraseña</label>
		<input type="password" name="passwd" required/>
		<br>
		<input type="submit" value="Enviar">
	</form>
	</h2>
	</center>
	<br>
	<p><a href="/">Volver Inicio</a></p>
%include('footer.tpl')