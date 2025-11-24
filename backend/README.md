# Backend (FastAPI) — Skeleton

Este diretório contém um esqueleto de backend em FastAPI que usa o Supabase como armazenamento.

Instalação (no ambiente virtual):

```powershell
python -m pip install -r backend\requirements.txt
```

Executar em desenvolvimento:

```powershell
setx $(Get-Content ..\.env | ForEach-Object { $_ })
C:\Projetos\Teste-01\.venv-1\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
```

Endpoints iniciais:
- `GET /health` — verificação
- `GET /produtos` — lista produtos (lê do Supabase)
- `POST /produtos` — cria produto (insere no Supabase)

Nota: não exponha `SUPABASE_SERVICE_ROLE_KEY` no frontend; backend deve usar a service role para ações administrativas.
