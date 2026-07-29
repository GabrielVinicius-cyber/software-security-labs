# Changelog — Lab-02-SQLInjection

Todas as mudanças relevantes deste laboratório são documentadas neste arquivo.

## [0.1.0] - 2026-07-29

### Added
- Estrutura inicial de pastas do projeto.
- README, roadmap e architecture bilíngues.
- Script de inicialização do banco SQLite (`scripts/init_db.py`).
- Aplicação vulnerável a SQL Injection (`src/vulnerable/app.py`).
- Exploração manual documentada: bypass via `OR '1'='1'` e via
  comentário SQL (`--`).
- Confirmação automatizada da vulnerabilidade com sqlmap
  (boolean-based blind e time-based blind).
- Aplicação corrigida usando prepared statements (`src/fixed/app.py`).
- Validação da correção: manual (payloads de ataque) e automatizada
  (sqlmap, sessão limpa).
- Testes de regressão automatizados (`tests/test_sqli_fixed.py`) —
  4 testes cobrindo login válido, login inválido e os dois bypasses
  de SQL Injection.

### Security
- **[CWE-89] SQL Injection** identificada na rota `/login` da versão
  vulnerável, corrigida na versão `fixed` via parameterized queries.
