# Laboratório: Pull Request e Code Review

Projeto inicial para aula prática Pull Request e Code Review.

## Objetivo

Melhore a função `validar_email` em `usuarios.py`, protegendo a `main` contra mudanças não revisadas.
O validador inicial é intencionalmente incompleto. O objetivo da atividade não é implementar integralmente o RFC de e-mails.

## Regras de aceite

A função deve retornar `False` se a entrada não for `str`, tiver espaço, não tiver exatamente um `@`, tiver usuário vazio, ou tiver domínio sem pelo menos duas partes não vazias separadas por ponto. Uma entrada como `ana@empresa.com` deve retornar `True`.

## Execução dos testes

```bash
pytest tests/ -v
```

## Fluxo solicitado

1. Criar branch `feature/melhorar-validacao-email` a partir da main.
2. Implementar a melhoria, testar e registrar commit.
3. Publicar com `git push -u origin feature/melhorar-validacao-email`.
4. Abrir PR de `feature/...` para `main`, com descrição do que mudou e como testar.
5. Solicitar revisão de outro integrante da dupla.
6. Rever código, deixar ao menos um comentário técnico e pedir ajustes quando necessário.
7. Converter feedback em testes regressivos; corrigir o código; fazer commit e push na mesma branch.
8. Obter aprovação, realizar merge e atualizar a main local.

