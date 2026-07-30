# Roadmap — Lab-03-commandInjection

## Missão 1 — Criar estrutura do projeto

## Missão 2 — Documentação inicial (README, roadmap, architecture) 

## Missão 3 — Construir a aplicação vulnerável
Aplicacao com a rota /ping  em `src/vulnerable/`,que recebe um endereço IP ou domínio
devolvendo o resultado na resposta. Aqui propositalmente vamos dar liberdade ao usuario 
ter controle no campo {host} intencionalmente

## Missão 4 — Explorar manualmente
commandinjection nos parametros host na linguagem shell via input malicioso, direto no navegador/curl.

## Missão 5 — Explorar com Burp Suite (extra)
Interceptar a requisição de ataque com o Burp Suite Community, para
visualizar e manipular a exploração através da interface da ferramenta.

## Missão 6 — Documentar o ataque
Escrever `docs/lessons_learned.md` com a explicação técnica da falha
e evidências em `images/`.

## Missão 7 — Construir a versão corrigida
Mesma aplicação, em `src/fixed/`, usando `subprocess.run()` com lista
de argumentos, em vez de string concatenada — isso evita que o shell
interprete caracteres especiais do input do usuário.

## Missão 8 — Validar a correção
Tentar o mesmo ataque na versão corrigida (deve falhar) e documentar
por quê.

## Missão 9 — Fechar CHANGELOG + revisão geral

