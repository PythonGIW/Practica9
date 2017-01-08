<!DOCTYPE html>
<html xml:lang="es">

<head>
  <title>Practica9</title>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <h1>AGGREGATION PIPELINE</h1>
      </div>
    </div>
    <!--
    ESTA TABLA DEBE RECIBIR LOS SIGUIENTES DATOS
        - nombres: Nombres de las columnas a mostrar
        - result: resultados obtenidos para mostrar en la tabla
        - claves: claves de acceso a los resulados r
        - num: numero de resultados
    -->
    <div id="site_content">
      	<div id="content">
          <table>
            <tr>
            %for nombre in nombres:
              <td><strong>{{nombre}}</strong></td>
            %end
            </tr>
          %for r in result:
            <tr>
              <td>{{r["_id"]["nombre"]}}</td>
              <td>{{r["num"]}}</td>
              <td>{{r["_id"]["precio"]}}</td>
            </tr>
          %end 
          </table>
          <h1> Numero de resultados: {{num}} </h1>
    	</div>
    </div>
</body>
</html>
