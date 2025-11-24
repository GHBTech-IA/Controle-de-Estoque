Migrações SQL para Supabase

Arquivo principal:
- `001_init.sql` — cria tabelas `usuarios`, `fornecedores`, `produtos`, `movimentacoes`, `relatorios` e o tipo `movimento_tipo`.

Como aplicar (duas opções):

1) Executar no Supabase SQL Editor (mais simples):
   - Acesse o painel do seu projeto Supabase → SQL Editor → New Query
   - Cole o conteúdo de `001_init.sql` e execute (Run)

2) Usando a CLI do Supabase (local):
   - Instale a CLI: https://supabase.com/docs/guides/cli
   - Faça login `supabase login` e selecione o projeto
   - Execute: `supabase db remote set "postgresql://<db_user>:<db_pass>@<host>:5432/postgres"` (se aplicável)
   - Ou simplesmente cole o SQL no editor do painel de SQL.

Observações de permissões:
- Para rodar DDL via API/programaticamente é necessário usar credenciais com privilégios (service_role).
- Nunca exponha `SUPABASE_SERVICE_ROLE_KEY` no frontend.
