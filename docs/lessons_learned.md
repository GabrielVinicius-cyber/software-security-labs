## 🇧🇷 PATH conflitante entre pytest global e pytest do venv

Mesmo com o venv ativo (prompt mostrando `(venv)`), o comando `pytest`
sozinho pode executar uma instalação global (`/usr/bin/pytest`) em vez
da instalação isolada do projeto, se houver conflito na ordem do PATH.

**Solução:** usar `python3 -m pytest` em vez de `pytest` diretamente —
isso garante que o interpretador correto (do venv) seja usado.

## 🇺🇸 PATH conflict between global pytest and venv pytest

Even with the venv active (prompt showing `(venv)`), running `pytest`
alone may execute a global installation (`/usr/bin/pytest`) instead of
the project's isolated one, if there's a PATH ordering conflict.

**Fix:** use `python3 -m pytest` instead of `pytest` directly — this
guarantees the correct (venv) interpreter is used.
