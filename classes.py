@startuml

class Cinema {
    - nome: string
    - endereco: string
    - salas: list<Sala>
}

class Sala {
    - numero: int
    - capacidade: int
}

class Sessao {
    - filme: string
    - horario: datetime
    - sala: Sala
    - preco: float
    - ingressos_vendidos: int
    + comprar_ingresso(): Ingresso
}

class Ingresso {
    - sessao: Sessao
    - preco: float
}

class Cliente {
    - nome: string
    - idade: int
    - email: string
}

Cinema *-- "salas" Sala
Sala *-- Sessao
Sessao *-- Ingresso
Cliente *-- Ingresso

@enduml
