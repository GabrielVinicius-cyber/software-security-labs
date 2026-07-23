# Lab-01 — Fundação / Foundation
### *Ambiente, Git e Estrutura de Projeto / Environment, Git & Project Structure*

---

## 🇧🇷 Objetivo
Estabelecer o ambiente de desenvolvimento, o fluxo de trabalho com Git e a estrutura de projeto que servirá como base para todos os laboratórios deste repositório.

## 🇺🇸 Objective
Establish the development environment, Git workflow, and project structure that will serve as the foundation for all laboratories in this repository.

---

## 🇧🇷 Tecnologias
- Python 3.x
- Flask *(será implementado na Missão 3)*
- Git

## 🇺🇸 Technologies
- Python 3.x
- Flask *(to be implemented in Mission 3)*
- Git

---

## 🇧🇷 Status
✅ Ambiente, estrutura e aplicação base concluídos.

## 🇺🇸 Status
✅ Environment, structure, and base application completed.

---
## 🇧🇷 Como executar

1. Clone o repositório e entre na pasta do Lab-01:
```bash
   cd Lab-01-Flask
```

2. Crie e ative um ambiente virtual:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Instale as dependências:
```bash
   pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz com o seguinte conteúdo:

```
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-aqui

```
5. Execute a aplicação:
```bash
   python run.py
```

6. Acesse no navegador ou via curl:
```bash
   curl http://127.0.0.1:5000/
   curl http://127.0.0.1:5000/status
```

## 🇺🇸 How to Run

1. Clone the repository and enter the Lab-01 folder:
```bash
   cd Lab-01-Flask
```

2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file in the root with the following content:
```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```
5. Run the application:
```bash
   python run.py
```

6. Access it via browser or curl:
```bash
   curl http://127.0.0.1:5000/
   curl http://127.0.0.1:5000/status
```

---

## 🇧🇷 Roadmap
Consulte `docs/roadmap.md`.

## 🇺🇸 Roadmap
See `docs/roadmap.md`.

---

## 🇧🇷 Vulnerabilidades estudadas
Nenhuma. Este é um laboratório estrutural, dedicado à preparação do ambiente e da organização do projeto.

## 🇺🇸 Studied Vulnerabilities
None. This is a foundational lab focused on environment setup and project organization.
