# Como subir este projeto para o GitHub (scripts + geração de chave)

1) Pré-requisitos
- Git instalado
- GitHub CLI (`gh`) instalado: https://cli.github.com/

2) Autenticar o `gh`
- Execute:

```bash
gh auth login
```

Siga o assistente (recomendado: autenticação via web). Após autenticar, `gh` poderá criar repositórios em seu nome.

3) Usar os scripts fornecidos
- PowerShell (Windows):

```powershell
cd C:\Projetos\Controle-de-Estoque
.\scripts\create_github_repo.ps1 -RepoName MeuRepoNome -Visibility public
```

- Bash (Linux/macOS / WSL):

```bash
cd /c/Projetos/Controle-de-Estoque
./scripts/create_github_repo.sh MeuRepoNome public
```

Os scripts inicializam git (se necessário), fazem commit inicial e usam `gh repo create` para criar o repositório remoto e empurrar o código.

4) Gerar uma chave SSH (opção segura para pushes sem senha)

- Gerar chave (ed25519 recomendado):

```bash
ssh-keygen -t ed25519 -C "seu_email@exemplo.com"
# Pressione Enter para aceitar o local padrão e opcionalmente defina uma passphrase
```

- Adicionar ao ssh-agent:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

- Copiar a chave pública e adicionar ao GitHub: (web) cole o conteúdo de `~/.ssh/id_ed25519.pub` em Settings → SSH and GPG keys → New SSH key
  ou (gh) executar:

```bash
gh ssh-key add ~/.ssh/id_ed25519.pub -t "Minha chave de desenvolvimento"
```

Após isso, você pode clonar usando SSH (`git@github.com:usuario/repo.git`) e fazer `git push` sem precisar inserir token.

5) Usar token pessoal (PAT) — alternativa
- No GitHub: Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token
- Habilite scopes: `repo` (full control of private repositories) e `workflow` (se usar CI)
- Salve o token com segurança e configure `gh auth login --with-token` ou use no CI como Secret.

6) Recomendação para execuções automáticas (migrations, deploy)
- Configure CI (GitHub Actions) com Secrets (`DATABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`) e crie workflow para rodar migrações e deploy (segue modelo se precisar).


