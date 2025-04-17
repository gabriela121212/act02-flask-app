from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    getServidorTxt = requests.get("https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt")
    encabezado = any
    personas_fil = []
    txtPlano = any
    searchIds = ("3", "4", "5", "7")


    if getServidorTxt.status_code == 200:
        txtPlano=getServidorTxt.text
    else:
        txtPlano = ""
    
    lineas = txtPlano.strip().split("\n")
    encabezado = lineas[0].split("|") #aqui sacamos los encabezados
    datos = lineas[1:] #aqui nos devuelve todos los registros sin los encabezados le decimos coje todas las filas.
                       #empezando desde la fila 1 no la 0 que serian los encabezados.

    
    for linea in datos:
        campos = linea.split("|") #en cada linea como tenemos varios campos los separamos con | es decir id|nombre| etc.
        if campos[0].startswith(searchIds): #aqui buscamos desde el primer campo es decir id| todos los que comiensen con 3,4,5,7.
            personas_fil.append(campos) #con el append agregamos a la lista todos los que cumplen con la condicion.

    #modelamos la tabla y aplicamos css.
    tabla = """
    <style>
        table {
            border-collapse: collapse;
            width: 90%;
            margin: 30px auto;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        th, td {
            padding: 12px;
            text-align: center;
            transition: background-color 0.3s ease;
        }
        tr:hover td {
            background-color: #d1f0ff !important;
            color: #000;
        }
        th:nth-child(1), td:nth-child(1) { background-color: #F28B82; color: white; }
        th:nth-child(2), td:nth-child(2) { background-color: #FBBC04; color: white; }
        th:nth-child(3), td:nth-child(3) { background-color: #34A853; color: white; }
        th:nth-child(4), td:nth-child(4) { background-color: #4285F4; color: white; }
        th:nth-child(5), td:nth-child(5) { background-color: #A142F4; color: white; }
        h2{
            background-color:white;
        }
    </style>
    <table>
        <tr>
    """ + "".join([f"<th>{col}</th>" for col in encabezado]) + "</tr>"

    for persona in personas_fil:
        tabla += "<tr>" + "".join([f"<td>{dato}</td>" for dato in persona]) + "</tr>"

    tabla += "</table>"
    return tabla
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
