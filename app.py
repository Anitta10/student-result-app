from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'admin123'  # for session management

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT UNIQUE,
            subject1 INTEGER,
            subject2 INTEGER,
            subject3 INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Initialize at start

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['admin'] = True
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('admin'):
        return redirect('/')
    conn = sqlite3.connect('database.db')
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template('dashboard.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        s1 = request.form['subject1']
        s2 = request.form['subject2']
        s3 = request.form['subject3']
        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO students (name, roll, subject1, subject2, subject3) VALUES (?, ?, ?, ?, ?)",
                     (name, roll, s1, s2, s3))
        conn.commit()
        conn.close()
        return redirect('/dashboard')
    return render_template('add_student.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    student = None
    if request.method == 'POST':
        roll = request.form['roll']
        conn = sqlite3.connect('database.db')
        student = conn.execute("SELECT * FROM students WHERE roll=?", (roll,)).fetchone()
        conn.close()
    return render_template('search.html', student=student)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
      print(f"Editing student ID: {student_id}") 
      if not session.get('admin'):
         return redirect('/')
    
      conn = sqlite3.connect('database.db')
    
      if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        s1 = request.form['subject1']
        s2 = request.form['subject2']
        s3 = request.form['subject3']
        
        conn.execute("UPDATE students SET name=?, roll=?, subject1=?, subject2=?, subject3=? WHERE id=?",
                     (name, roll, s1, s2, s3, student_id))
        conn.commit()
        conn.close()
        return redirect('/dashboard')
    
      student = conn.execute("SELECT * FROM students WHERE id=?", (student_id,)).fetchone()
      conn.close()
      return render_template('edit_student.html', student=student)

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    if not session.get('admin'):
        return redirect('/')
    
    conn = sqlite3.connect('database.db')
    conn.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    return redirect('/dashboard')
