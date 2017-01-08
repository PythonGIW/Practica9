# -*- coding: utf-8 -*-
 
##

# Autores: 
# Alberto Marquez Gomez
# Álvaro Asenjo Torrijo
# Juan Jose Montiel Cano
# declaramos que esta solución
# es fruto exclusivamente de nuestro trabajo personal. No hemos sido
# ayudados por ninguna otra persona ni hemos obtenido la solución de
# fuentes externas, y tampoco hemos compartido nuestra solución con
# nadie. Declaramos además que no hemos realizado de manera desho-
# nesta ninguna otra actividad que pueda mejorar nuestros resultados
# ni perjudicar los resultados de los demás.

## 


from bottle import get, run, template, error, static_file, request,response,redirect
from pymongo import MongoClient

mongoclient = MongoClient()
db = mongoclient['giw']


@get('/top_countries')
# http://localhost:8080/top_countries?n=3
def agg1():
	result = db.usuarios.aggregate( [
		{"$group": {"_id": "$pais","num": {"$sum":1}}},
 		{"$sort" : {"num":-1, "_id":-1}},
 		{"$limit" : int(request.query['n'])}
	])
    	return template('aggregationPipeline.tpl', result = result, claves= ["_id","num"], nombres = ["Pais", "Numero"], num = num)

@get('/products')
# http://localhost:8080/products?min=2.34
def agg2():
	result2 = db.pedidos.aggregate([
		{"$unwind":"$lineas"},
		# {"$project": {"precio": "$lineas.precio",
		# 				"cantidad": "$lineas.cantidad",
		# 				"nombre": "$lineas.nombre"}},
		{"$match" : {"lineas.precio":{"$gte":float(request.query['min'])}}},
		{"$group": {"_id": { "nombre": "$lineas.nombre", "precio": "$lineas.precio"},"num": {"$sum":"$lineas.cantidad"}}}
		#
	])
    	return template('aggregationPipelineProductos.tpl', result = result2, nombres = ["Nombre", "Numero", "Precio"], num = 10)

    
@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():
    r = db.usuarios.aggregate( [
		{"$group": {"_id": "$pais","num": {"$sum":1}, "max":{"$max":"$edad"}, "min":{"$min":"$edad"}}},
		{"$project": {"range":{"$subtract":["$max", "$min"]}, "pais": "$_id", "max":"$max", "min":"$min"}},
		{"$match" : {"range":{"$gte":int(request.query['min'])}}},
		{"$sort" : {"range":-1, "_id":-1}}
	])
		return template('aggregationPipeline.tpl', result = r, claves= ["_id","range"], nombres = ["Pais", "Rango de Edades"])

    
    
@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():
    pass
    
    
@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():
    pass
    
        
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)