from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="alglege",
    password="",
    database="tasks_bd"
)
cursor = db.cursor()

# Création de la table si elle n'existe pas
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255),
    status BOOLEAN
)
""")

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    total_tasks = len(tasks)
    return render_template('index.html', tasks=tasks, total_tasks=total_tasks)

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

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    cursor.execute("UPDATE tasks SET status = TRUE WHERE id = %s", (task_id,))
    db.commit()
    return redirect('/')

@app.route('/incomplete/<int:task_id>')
def incomplete_task(task_id):
    cursor.execute("UPDATE tasks SET status = FALSE WHERE id = %s", (task_id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
