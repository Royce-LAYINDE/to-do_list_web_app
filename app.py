from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Chemin vers la base de données SQLite
db_path = os.path.join(os.path.dirname(__file__), 'tasks.db')

# Création de la base de données et de la table si elles n'existent pas
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status BOOLEAN NOT NULL DEFAULT 0
    )
    """)
    conn.commit()

# Route principale
@app.route('/')
def index():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
       # Séparer les tâches en deux groupes
        tasks_non_validees = [task for task in tasks if task[2] == 0]
        tasks_validees = [task for task in tasks if task[2] == 1]
        completed_tasks = len(tasks_validees)
        total_tasks = len(tasks)
    return render_template('index.html', 
                           tasks_non_validees=tasks_non_validees, 
                           tasks_validees=tasks_validees, 
                           completed_tasks = completed_tasks,
                           total_tasks=total_tasks)

# Ajouter une tâche
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, False))
        conn.commit()
    return redirect('/')

# Supprimer une tâche
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    return redirect('/')

# Marquer une tâche comme complétée
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = 1 WHERE id = ?", (task_id,))
        conn.commit()
    return redirect('/')

# Marquer une tâche comme incomplète
@app.route('/incomplete/<int:task_id>')
def incomplete_task(task_id):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = 0 WHERE id = ?", (task_id,))
        conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
