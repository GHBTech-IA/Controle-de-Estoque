# Sistema Login/Cadastro (CustomTkinter + SQLite)

Pequeno exemplo em Python usando `customtkinter` para UI e `sqlite3` para persistência.

Requisitos
- Python 3.10+
- Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar

```bash
python main.py
```

Arquivos principais
- `main.py` - inicializa o banco e executa a aplicação
- `ui.py` - interface (login / cadastro)
- `db.py` - camada simples de acesso ao SQLite
- `utils.py` - hashing/validação de senhas (PBKDF2)

Backend proposto:
- `backend/` - esqueleto FastAPI que usa Supabase como banco (endpoints iniciais em `backend/app/routes`)


Observações
- Senhas não são armazenadas em texto claro; usam `hashlib.pbkdf2_hmac` com salt.
- Recomenda-se instalar `customtkinter` atualizado antes de executar.
