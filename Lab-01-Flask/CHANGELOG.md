# Changelog — Lab-01-Flask

Todas as mudanças relevantes deste laboratório são documentadas neste arquivo.

## [0.1.0] - 2026-07-24

### Added
- Estrutura inicial de pastas do projeto.
- Configuração de ambiente (Python, venv, Git).
- README bilíngue (PT-BR/EN) com objetivo, tecnologias e instruções de execução.
- Documentação de arquitetura (`docs/architecture.md`) bilíngue.
- Aplicação Flask estruturada com application factory pattern.
- Blueprint `main` com rotas `/` e `/status`.
- Configuração via variáveis de ambiente (`.env` + `python-dotenv`).
- Testes automatizados com pytest (`tests/conftest.py`, `tests/test_routes.py`).
- Script de setup automatizado (`scripts/setup.sh`).
- Registro de lições aprendidas (`docs/lessons_learned.md`).

### Fixed
- Conflito de PATH entre `pytest` global e `pytest` do ambiente virtual.
