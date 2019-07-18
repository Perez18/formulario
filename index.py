from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='172.18.96.30'
app.config['MYSQL_USER']='azul_medio'
app.config['MYSQL_PASSWORD']='azul'
app.config['MYSQL_DB']='orac'
mysql=MySQL(app)

@app.route('/')
def formulario():
   return render_template("practica.html")

@app.route('/add', methods=["POST"])
def add():
  if request.methods == 'POST':
     usuario= request.form['nombre']
     email=request.form['email']
     mensaje=request.form['mensaje']
     cur=mysql.connection.cursor()
     cur.execute( INSERT INTO MONITOREO_WEB()VALUES (%s,%s,%s ),(nombre,email,mensaje) )

if __name__ == "__main__":
    app.run(debug=True)