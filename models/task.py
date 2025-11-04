class Task:
    def __init__(self, id, title, description, done=False):
        self.id = id
        self.title = title
        self.description = description
        self.done = done

    def to_dict(self):  # Converte o objeto Task em um dicionário
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
        }
