# Roadmap — Lab-02-SQLInjection

## Missão 1 — Criar estrutura do projeto ✅

## Missão 2 — Documentação inicial (README, roadmap, architecture) 🚧
Em andamento.

## Missão 3 — Construir a aplicação vulnerável
Formulário de login em `src/vulnerable/`, usando SQLite, com query
SQL montada por concatenação de string (falha proposital).

## Missão 4 — Explorar manualmente
Bypass de login via input malicioso, direto no navegador/curl.

## Missão 5 — Explorar com sqlmap
Automatizar a exploração e comparar com o resultado manual.

## Missão 6 — Documentar o ataque
Escrever `docs/lessons_learned.md` com a explicação técnica da falha
e evidências em `images/`.

## Missão 7 — Construir a versão corrigida
Mesma aplicação, em `src/fixed/`, usando *prepared statements*.

## Missão 8 — Validar a correção
Tentar o mesmo ataque na versão corrigida (deve falhar) e documentar
por quê.

## Missão 9 — Fechar CHANGELOG + revisão geral
