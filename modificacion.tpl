%include('header.tpl')
	<center>
	<h1>Modificación de usuarios</h1>
	<h3>{{variable}}</h3>
	<h2>
	<form action="/modificacion" method="post">
		<label>Usuario</label>
		<input type="text" name="nombre" required/>
		<br>
		<label>Correo Electrónico Antiguo</label>
		<input type="text" name="email" required/>
		<br>
		<label>Correo Electrónico Nuevo</label>
		<input type="text" name="email" required/>
		<br>
		<label>Contraseña Antigua</label>
		<input type="password" name="passwd" required/>
		<br>
		<label>Contraseña Nueva</label>
		<input type="password" name="passwd" required/>
		<br>
		<label>Repita la Contraseña Nueva</label>
		<input type="password" name="passwd" required/>
		<br>				
		<input type="submit" value="Enviar">
	</form>
	</h2>
	</center>
	<br>
	<p><a href="/">Volver Inicio</a></p>
%include('footer.tpl')



