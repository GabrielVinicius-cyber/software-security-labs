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
