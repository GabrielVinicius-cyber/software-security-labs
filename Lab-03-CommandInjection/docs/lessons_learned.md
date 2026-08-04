# Lições Aprendidas — Lab-03-CommandInjection

## 🇧🇷 Sobre o impacto real de Command Injection

Antes mesmo de implementar a aplicação, vale registrar uma reflexão
importante sobre por que essa vulnerabilidade é considerada crítica.

### Impacto ligado a privilégio
Um comando injetado herda exatamente as permissões do processo que
executa a aplicação. Se a aplicação roda como usuário comum, o dano é
limitado ao que esse usuário pode fazer. Se roda como root (nunca deve
rodar assim), o atacante ganha controle total da máquina. Isso ilustra
o **Princípio do Menor Privilégio**: nunca executar uma aplicação com
mais permissão do que ela realmente precisa.

### Command Injection como ponto de entrada de uma cadeia de ataque
Uma única falha de Command Injection pode ser o primeiro passo de um
ataque muito mais amplo, seguindo fases conhecidas (referência: MITRE
ATT&CK):

1. **Reconhecimento** — descobrir a falha existe
2. **Exploração inicial** — executar comandos básicos (`whoami`, `id`)
3. **Persistência** — garantir acesso permanente (ex: chave SSH própria,
   usuário novo, tarefa agendada) mesmo que a falha original seja
   corrigida depois
4. **Escalação de privilégio** — buscar outra falha para virar root
5. **Movimento lateral** — alcançar outras máquinas da mesma rede
6. **Exfiltração/impacto final** — roubo de dados, ransomware, ou acesso
   silencioso mantido por longos períodos

### Conclusão
Uma única linha de código sem tratamento de entrada pode ser a causa
raiz de um comprometimento completo de infraestrutura. Isso reforça por
que secure coding não é opcional — e por que defesa em profundidade
(múltiplas camadas de proteção, não só o código) é essencial mesmo
quando o código está correto.

## 🇺🇸 On the real impact of Command Injection

Even before implementing the application, it's worth recording an
important reflection on why this vulnerability is considered critical.

### Impact tied to privilege
An injected command inherits exactly the permissions of the process
running the application. If the application runs as a regular user,
the damage is limited to what that user can do. If it runs as root (it
never should), the attacker gains full control of the machine. This
illustrates the **Principle of Least Privilege**: never run an
application with more permission than it actually needs.

### Command Injection as an entry point for an attack chain
A single Command Injection flaw can be the first step of a much larger
attack, following known phases (reference: MITRE ATT&CK):

1. **Reconnaissance** — discover the flaw exists
2. **Initial exploitation** — run basic commands (`whoami`, `id`)
3. **Persistence** — secure permanent access (e.g. own SSH key, new
   user, scheduled task) even if the original flaw is fixed later
4. **Privilege escalation** — look for another flaw to become root
5. **Lateral movement** — reach other machines on the same network
6. **Exfiltration/final impact** — data theft, ransomware, or silent
   access maintained for long periods

### Conclusion
A single line of code without input handling can be the root cause of
a complete infrastructure compromise. This reinforces why secure coding
is not optional — and why defense in depth (multiple layers of
protection, not just the code) is essential even when the code itself
is correct.

---

## 🇧🇷 Prova de impacto — escrita arbitrária de arquivo

Além de executar comandos de leitura (`whoami`, `id`, `uname -a`), foi
demonstrado que a falha permite **escrita arbitrária no sistema de
arquivos**, com conteúdo controlado pelo atacante:

```bash
curl -G "http://127.0.0.1:5003/ping" --data-urlencode "host=127.0.0.1; echo 'conteúdo malicioso' > /home/kali/arquivo.txt"
```

Isso comprova que o impacto de Command Injection vai além de
reconhecimento (coleta de informação) — inclui manipulação real do
sistema, o que poderia ser usado, em um cenário real, para persistência
(ex: modificar arquivos de configuração, agendar tarefas via `cron`,
adicionar chaves SSH).

**Nota de responsabilidade:** o arquivo de prova foi criado e removido
imediatamente após a validação, dentro de ambiente isolado e controlado.
Nenhuma técnica de persistência real foi implementada — o objetivo foi
apenas demonstrar a capacidade de escrita, suficiente para documentar
o impacto da vulnerabilidade.

## 🇺🇸 Proof of impact — arbitrary file write

Beyond executing read commands (`whoami`, `id`, `uname -a`), it was
demonstrated that the flaw allows **arbitrary file system writes**, with
attacker-controlled content:

```bash
curl -G "http://127.0.0.1:5003/ping" --data-urlencode "host=127.0.0.1; echo 'malicious content' > /home/kali/file.txt"
```

This proves that Command Injection's impact goes beyond reconnaissance
(information gathering) — it includes real system manipulation, which
could be used, in a real scenario, for persistence (e.g. modifying
configuration files, scheduling tasks via `cron`, adding SSH keys).

**Responsibility note:** the proof file was created and immediately
removed after validation, within an isolated and controlled
environment. No real persistence technique was implemented — the goal
was only to demonstrate write capability, sufficient to document the
vulnerability's impact.

---

## 🇧🇷 Interceptação com Burp Suite (extra)

Como exercício adicional, a exploração foi repetida usando o Burp Suite
Community como proxy interceptador, configurando o `curl` para rotear
a requisição através dele (`curl -x http://127.0.0.1:8080 ...`).

Isso permitiu editar manualmente a requisição HTTP antes do envio,
diretamente na interface do Burp — incluindo o payload de injeção na
query string.

### Lição técnica: URL Encoding
Ao editar a requisição manualmente, foi necessário codificar espaços
como `%20` (URL encoding), já que a primeira linha de uma requisição
HTTP (`MÉTODO CAMINHO VERSÃO`) não aceita espaços não codificados sem
quebrar a sintaxe. O Flask/Werkzeug decodifica isso automaticamente ao
processar a requisição, entregando o valor já com espaços normais para
a aplicação.

## 🇺🇸 Interception with Burp Suite (extra)

As an additional exercise, the exploitation was repeated using Burp
Suite Community as an intercepting proxy, configuring `curl` to route
the request through it (`curl -x http://127.0.0.1:8080 ...`).

This allowed manually editing the HTTP request before sending it,
directly in the Burp interface — including the injection payload in
the query string.

### Technical lesson: URL Encoding
When manually editing the request, spaces had to be encoded as `%20`
(URL encoding), since the HTTP request line (`METHOD PATH VERSION`)
doesn't accept unencoded spaces without breaking the syntax. Flask/
Werkzeug automatically decodes this when processing the request,
delivering the value with normal spaces to the application.
