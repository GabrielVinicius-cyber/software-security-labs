# Changelog — Lab-03-CommandInjection

Todas as mudanças relevantes deste laboratório são documentadas neste arquivo.

## [0.1.0] - 2026-08-04

### Added
- Estrutura inicial de pastas do projeto.
- README, roadmap e architecture bilíngues.
- Aplicação vulnerável a Command Injection (`src/vulnerable/app.py`).
- Exploração manual documentada via curl: injeção no campo `host`
  usando os separadores `;`, `&&` e `|`.
- Prova de impacto: escrita arbitrária de arquivo no sistema.
- Interceptação manual com Burp Suite Community (captura da requisição
  HTTP, edição manual do payload, envio da requisição alterada).
- Aplicação corrigida usando `subprocess.run()` com lista de argumentos
  (`src/fixed/app.py`).
- Validação da correção: manual (reteste dos payloads de injeção) e
  automatizada (5 testes de regressão com pytest).
- Testes de regressão automatizados (`tests/test_command_injection_fixed.py`):
  - `test_ping_legitimo_funciona`
  - `test_ping_sem_host_retorna_erro`
  - `test_injecao_semicolon_nao_executa_comando`
  - `test_injecao_and_nao_executa_comando`
  - `test_injecao_pipe_nao_executa_comando`

### Security
- **[CWE-78] Command Injection** identificada na rota `/ping` da versão
  vulnerável, corrigida na versão `fixed` via execução segura de
  subprocessos (lista de argumentos, sem passar pelo shell).
