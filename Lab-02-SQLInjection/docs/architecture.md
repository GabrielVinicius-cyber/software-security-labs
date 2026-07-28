# Arquitetura — Lab-02-SQLInjection

## Visão geral / Overview

🇧🇷 **PT-BR:** Laboratório prático para aprender os fundamentos de uma
falha em uma aplicação Flask vulnerável a SQL Injection, como identificar
e corrigir esse tipo de erro em construções de sistemas reais. Também
aprendemos a utilizar a ferramenta sqlmap na prática.

🇺🇸 **EN:** Practical lab to learn the fundamentals of a SQL Injection
flaw in a vulnerable Flask application, how to identify and fix this
type of error in real system builds. We also learn to use the sqlmap
tool in practice.

## Decisões técnicas / Technical decisions

### Por que estudar SQL Injection? / Why study SQL Injection?

🇧🇷 **PT-BR:** Para obter uma boa base de conhecimento sobre onde e como
evitar esse tipo de falha em qualquer aplicação que formos construir no
futuro — é uma das vulnerabilidades mais comuns e mais exploradas em
aplicações web reais.

🇺🇸 **EN:** To build a solid knowledge base on where and how to prevent
this type of flaw in any application we build in the future — it's one
of the most common and most exploited vulnerabilities in real-world web
applications.

### Por que reaproveitar a estrutura do Lab-01? / Why reuse the Lab-01 structure?

🇧🇷 **PT-BR:** Para manter consistência entre os laboratórios do
portfólio, reduzir tempo de setup, e permitir comparar diretamente a
evolução do código entre um lab e outro.

🇺🇸 **EN:** To keep consistency across the portfolio's labs, reduce setup
time, and allow direct comparison of code evolution between one lab and
another.

### Por que duas pastas separadas (vulnerable/fixed)? / Why two separate folders?

🇧🇷 **PT-BR:** Para organização do laboratório, permitindo realizar todos
os testes de exploração possíveis antes da correção, e ficando como
exemplo lado a lado de como um código não deve ser construído e como
deve ser.

🇺🇸 **EN:** For lab organization, allowing all possible exploitation
tests before the fix, and serving as a side-by-side example of how code
should not be built versus how it should be.

### Por que SQLite? / Why SQLite?

🇧🇷 **PT-BR:** Porque é um banco de dados leve e simples, nativo do
Python (sem necessidade de instalar servidor externo), ideal para
prototipagem e aprendizado — não é recomendado para produção em
aplicações de médio/grande porte, mas é perfeito para o escopo deste
laboratório.

🇺🇸 **EN:** Because it's a lightweight, simple database, native to Python
(no need to install an external server), ideal for prototyping and
learning — not recommended for production in medium/large applications,
but perfect for the scope of this lab.

## Limitações atuais / Current limitations

🇧🇷 **PT-BR:** Por enquanto não há ataques nem demonstrações implementadas
— nem da estrutura do banco, nem das técnicas de exploração.

🇺🇸 **EN:** At this stage, no attacks or demonstrations have been
implemented yet — neither the database structure nor the exploitation
techniques.
