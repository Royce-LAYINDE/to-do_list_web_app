from flask import Flask, render_template, request, redirect
import mysql.connector

# AI-Vision  – Axé sur la reconnaissance faciale et la surveillance intelligente.

app = Flask(__name__)

# Configure MySQL Database Connection
db = mysql.connector.connect(
 host="localhost",
 user="alglege",
 database="tasks_bd"
 pass_word  = ""
)
cursor = db.cursor()

# Create the database table if it does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255), status BOOLEAN)")

@app.route('/')
def index():
 cursor.execute("SELECT * FROM tasks")
 tasks = cursor.fetchall()
 return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
 task = request.form['task']
 cursor.execute("INSERT INTO tasks (task, status) VALUES (%s, %s)", (task, False))
 db.commit()
 return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
 cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
 db.commit()
 return redirect('/')

if __name__ == '__main__':
 app.run(debug=True)