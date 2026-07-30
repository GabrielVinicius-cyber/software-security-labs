# Lab-02 — SQL Injection

---

## 🇧🇷 Objetivo
Construir uma aplicação Flask com um formulário de login intencionalmente
vulnerável a SQL Injection, explorar essa falha manualmente e com
ferramentas automatizadas, corrigi-la com *prepared statements*, e
documentar todo o processo tecnicamente.

## 🇺🇸 Objective
Build a Flask application with a login form intentionally vulnerable to
SQL Injection, exploit this flaw both manually and with automated tools,
fix it using *prepared statements*, and technically document the entire
process.

---

## 🇧🇷 Tecnologias
- Python 3.x + Flask
- SQLite (`sqlite3`, nativo do Python)
- sqlmap
- pytest

## 🇺🇸 Technologies
- Python 3.x + Flask
- SQLite (`sqlite3`, native to Python)
- sqlmap
- pytest

---
## 🇧🇷 Status
✅ Laboratório completo — aplicação vulnerável, versão corrigida, testes
automatizados e documentação da exploração, tudo implementado e validado.
Para entender a falha e a correção em detalhes, veja `docs/lessons_learned.md`.

## 🇺🇸 Status
✅ Complete lab — vulnerable application, fixed version, automated tests,
and exploitation documentation, all implemented and validated. For a
detailed explanation of the flaw and the fix, see `docs/lessons_learned.md`.

---

## 🇧🇷 Como executar

1. Ative o ambiente virtual e instale as dependências:
```bash
   source venv/bin/activate
   pip install -r requirements.txt
```

2. Inicialize o banco de dados com usuários de teste:
```bash
   python3 scripts/init_db.py
```

3. Rode a versão **vulnerável** (porta 5001):
```bash
   python3 src/vulnerable/app.py
```

4. Ou rode a versão **corrigida** (porta 5002), em outro terminal:
```bash
   python3 src/fixed/app.py
```

5. Teste um login legítimo:
```bash
   curl -X POST http://127.0.0.1:5001/login -d "username=admin&password=admin123"
```

6. Teste a exploração (só funciona na porta 5001, vulnerável):
```bash
   curl -X POST http://127.0.0.1:5001/login -d "username=admin'--&password=qualquercoisa"
```

7. Rode os testes automatizados:
```bash
   python3 -m pytest tests/ -v
```

## 🇺🇸 How to Run

1. Activate the virtual environment and install dependencies:
```bash
   source venv/bin/activate
   pip install -r requirements.txt
```

2. Initialize the database with test users:
```bash
   python3 scripts/init_db.py
```

3. Run the **vulnerable** version (port 5001):
```bash
   python3 src/vulnerable/app.py
```

4. Or run the **fixed** version (port 5002), in another terminal:
```bash
   python3 src/fixed/app.py
```

5. Test a legitimate login:
```bash
   curl -X POST http://127.0.0.1:5001/login -d "username=admin&password=admin123"
```

6. Test the exploit (only works on port 5001, vulnerable):
```bash
   curl -X POST http://127.0.0.1:5001/login -d "username=admin'--&password=qualquercoisa"
```

7. Run the automated tests:
```bash
   python3 -m pytest tests/ -v
```
---

## 🇧🇷 Vulnerabilidades estudadas
- **SQL Injection** (CWE-89 / OWASP A03:2021 – Injection)

## 🇺🇸 Vulnerabilities studied
- **SQL Injection** (CWE-89 / OWASP A03:2021 – Injection)

---

## 🇧🇷 Referências
- OWASP SQL Injection: https://owasp.org/www-community/attacks/SQL_Injection
- CWE-89: https://cwe.mitre.org/data/definitions/89.html

## 🇺🇸 References
- OWASP SQL Injection: https://owasp.org/www-community/attacks/SQL_Injection
- CWE-89: https://cwe.mitre.org/data/definitions/89.html
