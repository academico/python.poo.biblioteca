
<details> <summary>Version 1.1.0</summary>

- **Issue #1**: substituição SQLite3 para SQLAlchemy Core
  
  | Antes (`sqlite3` puro) | Agora (SQLAlchemy Core) |
  |------------------------|-------------------------|
  | SQL escrito como string | SQL estruturado via Core |
  | `CREATE TABLE` manual | `Table` + `metadata.create_all` |
  | Rows acessados como dict | Rows acessados como atributos |
  | Difícil trocar de banco | Troca com 1 linha |
  | Mais código repetitivo | Código mais curto e explícito |
  | Menor suporte a tooling | Melhor tipagem e autocompletar |
   


  ✅ O que você ganhou com essa migração

  ✔ **Domínio 100% preservado**  
  Nada mudou nas classes de domínio. Elas continuam puras, sem dependências de banco de dados ou framework.

  ✔ **Repositórios mais expressivos e seguros**  
  O uso do SQLAlchemy Core substitui SQL em string por construções tipadas (`select`, `insert`, `Table`), reduzindo erros e melhorando a legibilidade do código.

  ✔ **Fim do SQL “stringly typed”**  
  Adeus strings SQL espalhadas pelo código. O schema agora é centralizado e reutilizável.

  ✔ **Criação automática de tabelas**  
  Com `metadata.create_all`, o schema é criado de forma declarativa, consistente e fácil de manter.

  ✔ **Facilidade extrema para trocar de banco**  
  Trocar SQLite em memória por SQLite em arquivo ou outro banco relacional exige apenas mudar a URL do engine.

  ✔ **Arquitetura Clean mantida**  
  O SQLAlchemy Core permanece totalmente restrito à camada de infraestrutura, sem contaminar domínio ou serviços.

  ✔ **Escalabilidade futura**  
  O projeto fica pronto para evoluir para múltiplos repositórios, transações mais complexas ou até ORM, sem reescrever regras de negócio.

</details>