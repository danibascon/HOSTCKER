%include('header.tpl')
	<center>
	<h3>{{variable}}</h3>
	<h2>
	<form action="/registro" method="post">
		<label>Nombre</label>
		<input type="text" name="nombre" min='4' max='20' required/>
		<br>
		<label>Apellidos</label>
		<input type="text" name="apellido" min='4' max='20' required/>
		<br>
		<label>Usuario</label>
		<input type="text" name="user" min='4' max='10' required/>
		<br>
		<label>Correo Electrónico</label>
		<input type="text" name="email" min='6' max='30' pattern="[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{1,5}" required/>
		<br>
		<label>Contraseña</label>
		<input type="password" name="passwd" min='4' max='10' required/>
		<form action="checkbox-form.php" method="post">
		<br>
		<label>Añadir wordpress como CMS</label>		
		<input type="checkbox" name="wordpress" value="1" />
		<br>
		<input type="submit" value="Enviar">
	</form>
	</h2>
	</center>
	<br>
	<p><a href="/">Volver Inicio</a></p>	
%include('footer.tpl')