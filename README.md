# Notitas
  Este trabajo fue creado para el taller de Diseño y Desarollo de soluciones.(Enso Guidotti)
  
 Este proyecto fue creado por :
 <a href="https://github.com/pinguin-frosch">Gabriel Barrientos</a>,
 <a href="https://github.com/Thekawaiicokie">Charlotte Rodriguez</a>
  

<div align="center">
    <img src="https://i.pinimg.com/originals/d8/4f/b4/d84fb4493c74c8a9eb3ada6ba064b0e5.gif">
</div>

 Notitas es un proyecto que nacio en base a la idea de que cuando uno tiene un auto y quiere registrar los registros que tiene o cuando le toca su proxima
 fecha de mantenimiento como usuario es  bastante incomodo escribir datos registrados  en una libreta ya sea porque se podrian  perder, romper o 
 olvidar es por ello que para solucionar esta problematica lo mejor es  simplificar todo estos servicios y solucionandolo desarollando 
 un sistema que se encargara de   dejar registro de todos los servicios mecanicos que se llevan a cabo es decir cada vez que un usuario se 
 registra podra registrar su vehiculo para asi poder dejar los registros de la ultima fecha en la que realizo sus mantenciones y miro su kilometraje
 para asi siempre llevar un registro de el mantenimiento que lleva echo asociado a su vehiculo 
 y su cuenta
<h1 align="center">🍙 Usuarios</h1>
<div align="center">
    <img src="https://i.pinimg.com/originals/e6/00/03/e60003cf7977f349cdc4df9f0039ad9a.gif">

</div>


## Registro
  Como funciona el proceso del registro de los usuarios es sumamente intuitivo un usuario debera simplemente registrarse y completar todo el formulario
  de una manera correcta es decir escribiendo todo el formato en que se deberia y cumpliedo todos los fomularios incluso en el formato que se deberia
  ya que el formulario tiene restricciones y si no las completa correctamente no se podra registrar hasta que las complete. Todo estos servicios iran 
  conectados a una base de datos la cual estara gestionada mediante linode para asi despues poder posteriormente inciar sesión y dejar los datos 
  registados dentro de la base de datos
  
## Inicio de sesión
   El inicio de sesión se realiza mediante un proceso de validacion de los datos sera validadndo si el usuario existe y si los datos que esta ingresado
   para inciar sesión son validos o no. Si estos son validos podra ingresar sesión y de lo contrario no se podra iniciar sesión y para recuperar su cuenta
   debera hablar con un administrador.
 
 ## Eliminacion de la cuenta❌
   ⚠️La eliminacion de la cuenta y la vista de esta paguina  solo se podra visualizar una vez iniciada la sesión.Para poder eliminar la cuenta debe iniciar sesión y validar 
   que quiere eliminarla.

<h1 align="center">Vehiculos🚙</h1>
<div align="center">
    <img src="https://i.pinimg.com/originals/59/8b/b3/598bb3a9a24a4747a492b7d82c4baecb.gif">
</div>


## Registro de vehiculo
  Como funciona el proceso del registro del vehiculo funciona mediante una lista que lleva consigo a un monton de modelos en los cuales el usuario
  debera seleccionar la marca y el modelo si el usuario selecciono un modelo correspondiente a la marca lo podra registrar y de lo contrario debera validarlo
  nuevamente hasta cumplir con el requisito solicitado es decir que la marca y el modelo registrado concida ya que sino no podra registrarse.
  <img src="https://i.pinimg.com/originals/e1/f0/53/e1f053aa268dcb381ffbc1c82c927e0d.gif"  width="10px" height="10px"> Se debe tener en condideracion que si
  el usuario no inicia sesión no podra entrar a esta vista asi que le redireccionara a la apguina de inicio

## Actualizacion♻️
   La actualizacion del vehiculo solo se podra realizar una vez el usuario haya inciado se sesión al precionar el boton para actualizarlo se le redireccionara
   a una vista en la cual se le mostrar un formulario en que se muestra una lista con los datos a los cuales podra actualizar esta lista tendra en consideracion 
   los siguientes atributos:Año, Modelo y  Nombre.
 
## Eliminacion❌
   Esta vista solo retornara una vista con un mensaje con alerta que dice que si desea eliminar el vehiculo 
   si desea eliminar el automovil  le despliegara una alerta 
   <img src="https://i.pinimg.com/originals/e1/f0/53/e1f053aa268dcb381ffbc1c82c927e0d.gif"  width="10px" height="10px"> Se debe tener en condideracion que si
    el usuario no inicia sesión no podra entrar a esta vista asi que le redireccionara a la paguina de inicio

<h1 align="center">Mantenciones🔩</h1>
<div align="center">
    <img src="https://i.pinimg.com/originals/6d/8f/42/6d8f4254e8f50c2d45a81d9335a2906c.gif">
</div>


## Registro de Mantenciones
  Como funciona el proceso del registro de las manteciones es sumamente intuitivo un usuario debera simplemente iniciar secion y desde la paguina principal seleccionar
  el vehiculo al que desea realizarle una mantecion dentro del registro de la manteciones toma en consideracion los parametros de el tipo de mantencion
  (Que se relizara ej: Cambio de aceite, neumaticos etc) el tipo de mantencion selccionar un seleccionable para dejar registrado que mantencion
  se realizo y no cometer errores del registro esta estara relacionada al usuario y al vehiculo ademas en el registro de las manteciones del vehiculo
  se debera dejar registrado la fecha de la mantencion el costo y la descripcion de esta de manera manual si el usuario desea podra tambien escribir
  en la descripcion el valor de esta mantencion hya que asi se podra ver desde la vista en la parte de la descripcion. 
  <img src="https://i.pinimg.com/originals/e1/f0/53/e1f053aa268dcb381ffbc1c82c927e0d.gif" width="10px" height="10px"> Se debe tener en consideracion que solo 
  se podra vizualizar esta vista una vez el usuario haya iniciado sesión dentro de la paguina.

## Actualizacion♻️
   La actualizacion solo se pondra realizar si el usuario tiene una mantencion relacionada al vehiculo ya que si no hay no se podra visualizar a lo que queremos realizar una mantencion
   puesto a que nisiquiera tendriamos mantenciones.Si hay manteniciones aparecera un formulario igual al registro pero en estos el usuario debe tener en consideracion
   que debe agregar los nuevos datos a los que decea actualizar porque puede que se haya equivocado y mediante esta vista podra corregir los datos que coloco de manera erronea
   como quizas el tipo de mantencion o la descripcion la fecha o el valor
   <img src="https://i.pinimg.com/originals/e1/f0/53/e1f053aa268dcb381ffbc1c82c927e0d.gif" width="10px" height="10px">  Se debe tener en consideracion que solo 
  se podra vizualizar esta vista una vez el usuario haya iniciado sesión dentro de la paguina.

## Eliminacion❌
   Para eliminar la Mantencion solo debemos precionar que queremos eliminarla y confirmar que eso es lo que deseamos no nos pide ningun formulario de manera adicional.Sin embargo para llegar 
   a eliminar la mantencion exclusivamente  y no el vehiculo debemos tener en consideracion  que debemos entrar a la vista de mantenciones y no a la de vehiculos y no tratar de saltarnos ningun 
   paso para borrarla mas rapido ya que por un error asi podriamos eliminar el completo registro del vehiculo.
   <img src="https://i.pinimg.com/originals/e1/f0/53/e1f053aa268dcb381ffbc1c82c927e0d.gif"  width="10px" height="10px"> Se debe tener en condideracion que si
    el usuario no inicia sesión no podra entrar a esta vista asi que le redireccionara  a la paguina index y si se puede saltar rutas quizas porque el usuario las agrego a favoritos pero
    solo funcionaran si este inicio sesión es por ello que se pide que revisen bien las rutas en las cuales estan eliminando
    
<h1 align="center">Gracias por leer el README.md del proyecto</h1>
<div align="center">
    <img src="https://i.pinimg.com/originals/28/0a/05/280a05c05fa4cd05717a9256d661f425.gif">
</div>
