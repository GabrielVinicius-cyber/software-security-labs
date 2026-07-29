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

---

## 🇧🇷 Confirmação automatizada com sqlmap

Usamos o `sqlmap` para validar de forma automatizada a vulnerabilidade
já confirmada manualmente. A ferramenta identificou duas técnicas de
exploração adicionais:

- **Boolean-based blind**: permite inferir dados observando diferenças
  na resposta (verdadeiro/falso), sem necessidade de ver o retorno
  direto dos dados.
- **Time-based blind**: técnica mais avançada, que injeta uma operação
  pesada no banco (`RANDOMBLOB`) para forçar atraso na resposta quando
  uma condição é verdadeira — permite extrair dados byte a byte mesmo
  em aplicações que não mostram diferença visível na tela.

Comando usado:
```bash
sqlmap -u "http://127.0.0.1:5001/login" --data="username=admin&password=teste" -p username --batch --ignore-code=401
```

**Observação importante:** foi necessário usar `--ignore-code=401`,
porque nossa aplicação retorna HTTP 401 em login inválido, o que o
sqlmap interpreta por padrão como uma barreira de autenticação HTTP,
não como resposta normal da aplicação.

Evidência completa: `logs/sqlmap_scan.log`

## 🇺🇸 Automated confirmation with sqlmap

We used `sqlmap` to automatically validate the vulnerability already
confirmed manually. The tool identified two additional exploitation
techniques:

- **Boolean-based blind**: allows inferring data by observing
  differences in the response (true/false), without needing to see the
  data returned directly.
- **Time-based blind**: a more advanced technique that injects a heavy
  database operation (`RANDOMBLOB`) to force a delay in the response
  when a condition is true — allows extracting data byte by byte even
  in applications that show no visible difference on screen.

Command used:
```bash
sqlmap -u "http://127.0.0.1:5001/login" --data="username=admin&password=teste" -p username --batch --ignore-code=401
```

**Important note:** `--ignore-code=401` was required, because our
application returns HTTP 401 on invalid login, which sqlmap interprets
by default as an HTTP authentication barrier, not a normal application
response.

Full evidence: `logs/sqlmap_scan.log`

---

## 🇧🇷 Correção aplicada

A vulnerabilidade foi corrigida em `src/fixed/app.py`, substituindo a
concatenação de string por **prepared statements** (parameterized
queries):

```python
# Antes (vulnerável)
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

# Depois (corrigido)
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

### Por que a correção funciona
Com `?` como placeholder, o driver do SQLite trata a entrada do usuário
como **dado literal**, nunca como parte executável do comando SQL. A
etapa de "montar a query" e a etapa de "inserir os valores" ficam
completamente separadas — não existe mais concatenação de string
alguma, então não há como o atacante alterar a estrutura da query.

### Validação da correção
- **Manual:** os dois payloads que bypassavam o login (`' OR '1'='1` e
  `'--`) retornam corretamente HTTP 401 (login negado) na versão
  corrigida.
- **Automatizada (sqlmap):** com sessão limpa (`--flush-session`), o
  sqlmap não identificou nenhum parâmetro injetável.
  Evidência: `logs/sqlmap_fixed_validation.log`

## 🇺🇸 Applied fix

The vulnerability was fixed in `src/fixed/app.py`, replacing string
concatenation with **prepared statements** (parameterized queries):

```python
# Before (vulnerable)
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

# After (fixed)
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

### Why the fix works
With `?` as a placeholder, the SQLite driver treats user input as
**literal data**, never as executable SQL. The "build the query" step
and the "insert the values" step are completely separated — there's no
string concatenation at all anymore, so there's no way for an attacker
to alter the query's structure.

### Fix validation
- **Manual:** both payloads that bypassed login (`' OR '1'='1` and
  `'--`) now correctly return HTTP 401 (login denied) on the fixed
  version.
- **Automated (sqlmap):** with a clean session (`--flush-session`),
  sqlmap identified no injectable parameters.
  Evidence: `logs/sqlmap_fixed_validation.log`
