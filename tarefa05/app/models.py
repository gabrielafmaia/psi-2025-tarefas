from django.db import models

class Tarefa(models.Model):
    CONCLUIDO = "Concluído"
    EM_ANDAMENTO = "Em andamento"
    PENDENTE =  "Pendente"

    status_tarefa = [
        (CONCLUIDO, "Concluído"), (EM_ANDAMENTO, "Em andamento"), (PENDENTE, "Pendente")
    ]
    nome = models.CharField("Nome", max_length = 100)
    status = models.CharField("Status", choices = status_tarefa, default=PENDENTE)
    prazo = models.DateField("Prazo")

    def __str__(self):
        return self.nome