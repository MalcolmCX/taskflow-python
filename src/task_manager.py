from src.task import Task


class TaskManager:

    def __init__(self):
        self.tasks = []

    def adicionar_tarefa(self, tarefa):
        self.tasks.append(tarefa)

    def listar_tarefas(self):
        return self.tasks

    def buscar_tarefa(self, id):

        for tarefa in self.tasks:

            if tarefa.id == id:
                return tarefa

        return None

    def atualizar_status(self, id, novo_status):

        tarefa = self.buscar_tarefa(id)

        if tarefa:
            tarefa.status = novo_status
            return True

        return False

    def remover_tarefa(self, id):

        tarefa = self.buscar_tarefa(id)

        if tarefa:
            self.tasks.remove(tarefa)
            return True

        return False