# Arquitetura — Lab-03-CommandInjection

## Visão geral / Overview

🇧🇷 **PT-BR:** Laboratório prático para estudar Command Injection — como
a falha surge na aplicação, como explorá-la e como corrigi-la usando as
ferramentas certas para cada etapa.

🇺🇸 **EN:** Practical lab to study Command Injection — how the flaw
arises in the application, how to exploit it, and how to fix it using
the right tools for each stage.

## Decisões técnicas / Technical decisions

### Por que Command Injection? / Why Command Injection?

🇧🇷 **PT-BR:** Para aprender a identificar e corrigir uma das falhas mais
exploradas em aplicações web reais, reforçando a segurança de sistemas
que formos construir no futuro. Também traz o benefício de praticar o
uso do terminal manualmente e da ferramenta Burp Suite.

🇺🇸 **EN:** To learn how to identify and fix one of the most commonly
exploited flaws in real-world web applications, reinforcing the security
of systems we build in the future. It also brings the benefit of
practicing manual terminal usage and the Burp Suite tool.

### Por que usar os.system() na versão vulnerável? / Why use os.system() in the vulnerable version?

🇧🇷 **PT-BR:** Porque `os.system()` envia a string inteira do comando
para o shell do sistema interpretar. Como a entrada do usuário é colada
dentro dessa string, caracteres especiais de shell (`;`, `&&`, `|`) são
interpretados como comandos separados, permitindo a injeção — o mesmo
princípio da concatenação SQL, mas no contexto do sistema operacional.

🇺🇸 **EN:** Because `os.system()` sends the entire command string to the
system shell for interpretation. Since user input is pasted inside that
string, special shell characters (`;`, `&&`, `|`) are interpreted as
separate commands, enabling injection — the same principle as SQL
concatenation, but in the operating system context.

### Por que subprocess.run() com lista resolve o problema? / Why does subprocess.run() with a list solve the problem?

🇧🇷 **PT-BR:** Porque `subprocess.run()`, ao receber uma **lista de
argumentos** (em vez de uma string), executa o programa diretamente, sem
passar pelo shell. A entrada do usuário é tratada como um único
argumento literal, nunca como comando — caracteres especiais perdem
qualquer significado especial.

🇺🇸 **EN:** Because `subprocess.run()`, when given a **list of
arguments** (instead of a string), executes the program directly,
without going through the shell. User input is treated as a single
literal argument, never as a command — special characters lose any
special meaning.

## Limitações atuais / Current limitations

🇧🇷 **PT-BR:** Laboratório simples, sem estrutura ou aplicação complexa,
o que limita a possibilidade de explorar ataques de Command Injection
mais avançados.

🇺🇸 **EN:** Simple lab, without complex structure or application, which
limits the possibility of exploring more advanced Command Injection
attacks.

