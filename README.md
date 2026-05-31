# TaskFlow Python

## Descrição do Projeto

O TaskFlow Python é um sistema simples de gerenciamento de tarefas desenvolvido para aplicar conceitos de Engenharia de Software, Metodologias Ágeis e Controle de Qualidade.

O sistema permite criar, listar, atualizar e remover tarefas, auxiliando equipes no acompanhamento de atividades e prioridades.

## Objetivo

Desenvolver um sistema básico de gerenciamento de tarefas utilizando Python, GitHub, GitHub Actions e práticas ágeis de desenvolvimento.

## Escopo Inicial

O projeto foi desenvolvido com as seguintes funcionalidades:

* Cadastro de tarefas
* Listagem de tarefas
* Busca de tarefas
* Atualização de status
* Remoção de tarefas

## Metodologia Ágil Utilizada

Foi utilizada a metodologia Kanban para organizar as atividades do projeto.

As tarefas foram distribuídas nas colunas:

* To Do
* In Progress
* Done

O gerenciamento foi realizado utilizando GitHub Projects.

## Mudança de Escopo

Durante o desenvolvimento foi identificada a necessidade de priorizar tarefas críticas.

Por esse motivo foi adicionada a funcionalidade de prioridade das tarefas, permitindo classificar atividades como:

* Alta
* Média
* Baixa

Essa melhoria auxilia na organização do fluxo de trabalho e na tomada de decisão da equipe.

## Estrutura do Projeto

taskflow-python/

├── .github/workflows/
├── src/
│ ├── task.py
│ └── task_manager.py
├── test_task_manager.py
├── requirements.txt
└── README.md

## Testes Automatizados

Os testes foram implementados utilizando PyTest.

Cenários testados:

* Adicionar tarefa
* Remover tarefa
* Atualizar status

## Integração Contínua

O projeto utiliza GitHub Actions para executar automaticamente os testes a cada atualização enviada ao repositório.

## GitHub Actions

Workflow configurado para executar os testes automaticamente a cada push e pull request.

## Como Executar

Instalar dependências:

pip install -r requirements.txt

Executar testes:

python -m pytest

## Tecnologias Utilizadas

* Python 3.13
* PyTest
* Git
* GitHub
* GitHub Actions
* Kanban
=======
* Kanban

