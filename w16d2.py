from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

class Task:
    def __init__(self, title, description, completed=False):
        self.id = str(id)
        self.title = title
        self.description = description
        self.completed = completed

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(title=data.get('title'), description=data.get('description'))
    tasks.append(new_task)
    return jsonify({'message': 'Task created', 'task_id': new_task.id}), 201


@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return jsonify({'id': task.id, 'title': task.title, 'description': task.description,
                        'completed': task.completed})
    return jsonify({'message': 'Task not found'}), 404


@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({'message': 'Task deleted'})


if __name__ == '__main__':
    app.run(debug=True)