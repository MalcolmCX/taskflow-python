from src.task import Task
from src.task_manager import TaskManager


def test_adicionar_tarefa():

    manager = TaskManager()

    tarefa = Task(
        1,
        "Criar Login",
        "To Do"
    )

    manager.adicionar_tarefa(tarefa)

    assert len(manager.listar_tarefas()) == 1


def test_remover_tarefa():

    manager = TaskManager()

    tarefa = Task(
        1,
        "Criar Login",
        "To Do"
    )

    manager.adicionar_tarefa(tarefa)

    resultado = manager.remover_tarefa(1)

    assert resultado is True


def test_atualizar_status():

    manager = TaskManager()

    tarefa = Task(
        1,
        "Criar Login",
        "To Do"
    )

    manager.adicionar_tarefa(tarefa)

    manager.atualizar_status(
        1,
        "Done"
    )

    assert tarefa.status == "Done"