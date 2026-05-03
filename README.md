# Arquitetura Clean em Python (CLI Oriented)

Este projeto é um **exemplo prático de aplicação da Clean Architecture / DDD Lite em Python**, estruturado em **múltiplos projetos (packages)** e executado via **linha de comando**, sem dependência de framework web.

A proposta é demonstrar como organizar corretamente **domínio, aplicação e infraestrutura**, mantendo baixo acoplamento, alta coesão e facilidade de evolução.

---

## ✅ O que essa arquitetura te dá

✔ **Execução por linha de comando**  
✔ **Camadas totalmente desacopladas**  
✔ **Fácil troca de persistência**  
✔ **Alta testabilidade**  
✔ **Escalável para API no futuro**  
✔ **100% alinhada com Clean Architecture**  
✔ **Reutilização de regras de negócio**

---

## 🎯 Objetivo do projeto

- Demonstrar uma arquitetura profissional em Python
- Aplicar princípios de Clean Architecture e SOLID
- Separar claramente responsabilidades
- Servir como base para sistemas CLI, APIs ou jobs batch

---

## 🧱 Visão geral da arquitetura

A solução é dividida em três projetos Python independentes:

```
app  ──▶ appl ──▶ core
```

- **core**: regras de negócio e contratos
- **appl**: casos de uso e serviços
- **app**: infraestrutura e ponto de entrada da aplicação

As dependências sempre apontam para dentro, respeitando a regra da Clean Architecture.

---

## 📁 Estrutura de diretórios

```
src/
├── app/
│   ├── pyproject.toml
│   └── app/
│       ├── main.py
│       └── infra/
│           └── repositories/
│               └── in_memory_user_repository.py
│
├── appl/
│   ├── pyproject.toml
│   └── appl/
│       ├── dto/
│       │   └── create_user_dto.py
│       └── services/
│           └── user_service.py
│
└── core/
    ├── pyproject.toml
    └── core/
        ├── domain/
        │   └── user.py
        └── repositories/
            └── user_repository.py
```

---

## 🧠 Responsabilidade das camadas

### Core (Domínio)

- Entidades e regras de negócio
- Validações e comportamento
- Interfaces de repositório
- Nenhuma dependência técnica

---

### Appl (Camada de Aplicação)

- Casos de uso
- Serviços de aplicação
- Orquestração do domínio
- Usa DTOs para entrada de dados

---

### App (Infraestrutura e Execução)

- Implementações concretas (ex.: repositórios)
- Ponto de entrada CLI (`main.py`)
- Dependências técnicas

---

## ▶️ Como executar o projeto

### Instalação em modo desenvolvimento

```bash
pip install -e src/core
pip install -e src/appl
pip install -e src/app
```

### Execução

```bash
python src/app/app/main.py
```

---

## 🔄 Troca de persistência

A persistência atual é em memória. Para alterá-la:

1. Crie uma nova classe que implemente a interface do repositório
2. Injete a implementação desejada no `main.py`

Nenhuma modificação é necessária no domínio ou nos serviços.

---

## 🧪 Testes

Essa arquitetura facilita:

- Testes unitários do domínio
- Mock de repositórios
- Testes isolados sem banco de dados

---

## 🚀 Evolução futura

- API REST (FastAPI / Django)
- Interface gráfica
- Workers e filas
- Microserviços

As regras de negócio permanecem intactas.

---

## 📚 Princípios aplicados

- Clean Architecture
- SOLID
- Inversão de Dependência
- Separação de Responsabilidades
- DDD (Lite)

---

## 📝 Licença

Uso livre para fins educacionais e profissionais.
