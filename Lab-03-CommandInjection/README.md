# Lab-03 — CommandInjection

---

## 🇧🇷 Objetivo
Construir uma aplicação Flask com uma versão vulnerável a Command
Injection e outra corrigida. Faremos a exploração manual usando curl e,
como extra, vamos usar o Burp Suite Community para interceptação e
análise da aplicação.

## 🇺🇸 Objective
Build a Flask application with a version vulnerable to Command
Injection and another one fixed. We'll perform manual exploitation
using curl and, as an extra, use Burp Suite Community for interception
and analysis of the application.

---

## 🇧🇷 Tecnologias
- Python 3.x + Flask
- `subprocess` (nativo do Python)
- Burp Suite Community
- pytest

## 🇺🇸 Technologies
- Python 3.x + Flask
- `subprocess` (native to Python)
- Burp Suite Community
- pytest

---

## 🇧🇷 Status
✅ Laboratório concluído — estrutura completa. Laboratório para estudos
práticos de Command Injection, com versão vulnerável e corrigida. Pode
ser testado tanto manualmente (curl) quanto com Burp Suite Community.

## 🇺🇸 Status
✅ Lab completed — full structure. Practical study lab for Command
Injection, with vulnerable and fixed versions. Can be tested both
manually (curl) and with Burp Suite Community.

---

## 🇧🇷 Como executar

1. Ative o ambiente virtual e instale as dependências:
```bash
   source venv/bin/activate
   pip install -r requirements.txt
```

2. Rode a versão **vulnerável** (porta 5003):
```bash
   python3 src/vulnerable/app.py
```

3. Ou rode a versão **corrigida** (porta 5004), em outro terminal:
```bash
   python3 src/fixed/app.py
```

4. Teste um ping legítimo:
```bash
   curl -G "http://127.0.0.1:5003/ping" --data-urlencode "host=127.0.0.1"
```

5. Teste a exploração (só funciona na porta 5003, vulnerável):
```bash
   curl -G "http://127.0.0.1:5003/ping" --data-urlencode "host=127.0.0.1;whoami"
```

6. Rode os testes automatizados:
```bash
   python3 -m pytest tests/ -v
```

## 🇺🇸 How to Run

1. Activate the virtual environment and install dependencies:
```bash
   source venv/bin/activate
   pip install -r requirements.txt
```

2. Run the **vulnerable** version (port 5003):
```bash
   python3 src/vulnerable/app.py
```

3. Or run the **fixed** version (port 5004), in another terminal:
```bash
   python3 src/fixed/app.py
```

4. Test a legitimate ping:
```bash
   curl -G "http://127.0.0.1:5003/ping" --data-urlencode "host=127.0.0.1"
```

5. Test the exploit (only works on port 5003, vulnerable):
```bash
   curl -G "http://127.0.0.1:5003/ping" --data-urlencode "host=127.0.0.1;whoami"
```

6. Run the automated tests:
```bash
   python3 -m pytest tests/ -v
```

---

## 🇧🇷 Vulnerabilidade estudada
- Command Injection (CWE-78 / OWASP A03:2021 – Injection)

## 🇺🇸 Vulnerability studied
- Command Injection (CWE-78 / OWASP A03:2021 – Injection)
