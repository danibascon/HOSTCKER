%include('header.tpl')
	<center>
	<h1>BIENVENIDOS A HOSTCKER</h1>
	<h2>
	<form action="/login" method="post">
		<label>Usuario</label>
		<input type="text" name="user" required/>
		<br>
		<label>Contraseña</label>
		<input type="password" name="passwd" required/>
		<br>
		<input type="submit" value="Enviar">
	</form>
	<h3>{{variable}}</h3>
	</h2>
	<h2><a href="/register">¿No estás registrado?</a></h2>
	<h1><a href="baja">Darte de baja</a></h1>
	</center>
%include('footer.tpl')