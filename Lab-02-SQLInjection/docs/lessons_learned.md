# Lições Aprendidas — Lab-02-SQLInjection

## 🇧🇷 Vulnerabilidade: SQL Injection na rota de login

### O que é
A rota `/login` monta a query SQL concatenando diretamente a entrada do
usuário (username e password) usando f-string, sem nenhum tipo de
tratamento ou escape:

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

### Exploração 1 — Bypass com OR
**Payload:** `username = admin' OR '1'='1` | `password = qualquercoisa`

Query resultante:
```sql
SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = 'qualquercoisa'
```

Como `AND` tem precedência maior que `OR` em SQL, a query é avaliada como
`username = 'admin' OR ('1'='1' AND password = '...')`. Como o username
`admin` é válido, essa condição sozinha (ligada por `OR`) já é suficiente
para autenticar, ignorando completamente a senha.

**Resultado:** Login bypassado como `admin`, sem saber a senha real.
Evidência: `logs/exploit_or_bypass.log`

### Exploração 2 — Bypass com comentário SQL
**Payload:** `username = admin'--` | `password = qualquercoisa`

Query resultante:
```sql
SELECT * FROM users WHERE username = 'admin'--' AND password = 'qualquercoisa'
```

O `--` é um comentário SQL — tudo após ele na mesma linha é ignorado pelo
banco. A checagem de senha inteira desaparece da query executada:
```sql
SELECT * FROM users WHERE username = 'admin'
```

**Resultado:** Login bypassado como `admin`, checagem de senha eliminada
por completo. Evidência: `logs/exploit_comment_bypass.log`

### Impacto
Um atacante que sabe (ou adivinha) apenas o **username** de uma conta
consegue autenticar-se sem conhecer a senha, comprometendo totalmente o
controle de acesso da aplicação.

### Causa raiz
Concatenação direta de entrada do usuário na construção de comandos SQL,
sem uso de parâmetros/prepared statements.

---

## 🇺🇸 Vulnerability: SQL Injection in the login route

### What it is
The `/login` route builds the SQL query by directly concatenating user
input (username and password) using an f-string, with no sanitization
or escaping:

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

### Exploit 1 — OR-based bypass
**Payload:** `username = admin' OR '1'='1` | `password = anything`

Resulting query:
```sql
SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = 'anything'
```

Since `AND` has higher precedence than `OR` in SQL, the query evaluates
as `username = 'admin' OR ('1'='1' AND password = '...')`. Since the
username `admin` is valid, that condition alone (joined by `OR`) is
enough to authenticate, completely bypassing the password check.

**Result:** Login bypassed as `admin`, without knowing the real password.
Evidence: `logs/exploit_or_bypass.log`

### Exploit 2 — Comment-based bypass
**Payload:** `username = admin'--` | `password = anything`

Resulting query:
```sql
SELECT * FROM users WHERE username = 'admin'--' AND password = 'anything'
```

`--` is a SQL comment — everything after it on the same line is ignored
by the database. The entire password check disappears from the executed
query:
```sql
SELECT * FROM users WHERE username = 'admin'
```

**Result:** Login bypassed as `admin`, password check completely
eliminated. Evidence: `logs/exploit_comment_bypass.log`

### Impact
An attacker who knows (or guesses) only a valid **username** can
authenticate without knowing the password, fully compromising the
application's access control.

### Root cause
Direct concatenation of user input into SQL command construction,
without using parameters/prepared statements.
