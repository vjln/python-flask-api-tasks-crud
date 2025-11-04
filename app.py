from flask import Flask, request, jsonify
from models.task import Task
from uuid import uuid4

app = Flask(__name__)
tasks = []


@app.route("/tasks", methods=["POST"])
def create_task():
    # cria uma nova task dentro do array
    data = request.get_json()  # recupera o que cliente enviou e já armazenamos em data

    new_task = Task(
        id=str(uuid4()),  # gera um id único
        title=data.get("title"),
        description=data.get("description"),
        done=data.get("done", False),
    )

    tasks.append(new_task)  # adiciona a nova task convertida em dicionário
    print(data)
    return jsonify(({"message": "Task created successfully"})), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]  # Converte cada task em dicionário
    output = {"tasks": task_list, "total_tasks": len(task_list)}

    print(output)
    return jsonify(output), 200


@app.route(
    "/tasks/<task_id>", methods=["GET"]
)  # Rota para obter uma task específica pelo ID
def get_task(task_id):
    for task in tasks:
        if task.id == task_id:
            return jsonify(task.to_dict()), 200
    return jsonify({"message": "Task not found"}), 404


@app.route(
    "/tasks/<task_id>", methods=["PATCH"]
)  # Rota para atualizr uma task específica pelo ID
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task.id == task_id:
            task.title = data.get("title", task.title)
            task.description = data.get("description", task.description)
            task.done = data.get("done", task.done)
            return jsonify({"message": "Task updated successfully"}), 200
    return jsonify({"message": "Task not found"}), 404


@app.route(
    "/tasks/<task_id>", methods=["PUT"]
)  # Rota para donar uma task específica pelo ID
def done_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return jsonify({"message": "Task marked as done"}), 200
    return jsonify({"message": "Task not found"}), 404


@app.route(
    "/tasks/<task_id>", methods=["DELETE"]
)  # Rota para deletar uma task específica pelo ID
def delete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"message": "Task not found"}), 404


# Apenas se o script for executado diretamente, subo com o debug=true, boas práticas.
if __name__ == "__main__":
    app.run(debug=True)
