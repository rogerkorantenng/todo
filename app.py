from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data to store tasks
tasks_15_sep = [
    {'id': 1, 'title': 'Attend TeamAlfy Interview', 'completed': True},
    {'id': 2, 'title': 'Buy waakye after the interview', 'completed': False},
]

# Instantaite the main 
@app.route('/')
def index():
    return render_template('index.html', tasks_15_sep=tasks_15_sep)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = {
        'id': len(tasks_15_sep) + 1,
        'title': request.form['title'],
        'completed': False
    }
    tasks_15_sep.append(new_task)
    return redirect(url_for('index'))


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks_15_sep
    tasks_15_sep = [t for t in tasks_15_sep if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
