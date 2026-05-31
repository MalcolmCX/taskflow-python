class Task:

    def __init__(self, id, titulo, status, prioridade="Média"):
        self.id = id
        self.titulo = titulo
        self.status = status
        self.prioridade = prioridade

    def __str__(self):
        return f"{self.id} - {self.titulo} - {self.status} - {self.prioridade}"