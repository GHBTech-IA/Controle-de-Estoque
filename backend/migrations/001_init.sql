-- Migração inicial: tabelas para o sistema de Controle de Estoque

-- Extensões úteis (habilite se disponível)
-- create extension if not exists pgcrypto;

-- Tabela usuarios
CREATE TABLE IF NOT EXISTS usuarios (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nome text NOT NULL,
  email text NOT NULL UNIQUE,
  senha_hash text,
  perfil text NOT NULL DEFAULT 'funcionario', -- funcionario|gestor|admin
  ativo boolean NOT NULL DEFAULT true,
  criado_em timestamptz NOT NULL DEFAULT now()
);

-- Tabela fornecedores
CREATE TABLE IF NOT EXISTS fornecedores (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nome text NOT NULL,
  cnpj_cpf text,
  contato text,
  endereco jsonb,
  criado_em timestamptz NOT NULL DEFAULT now()
);

-- Tabela produtos
CREATE TABLE IF NOT EXISTS produtos (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nome text NOT NULL,
  descricao text,
  categoria text,
  preco numeric(12,2) DEFAULT 0,
  quantidade integer DEFAULT 0,
  unidade text,
  codigo text,
  fornecedor_id uuid REFERENCES fornecedores(id) ON DELETE SET NULL,
  estoque_minimo integer DEFAULT 0,
  criado_em timestamptz NOT NULL DEFAULT now(),
  atualizado_em timestamptz NOT NULL DEFAULT now()
);

-- Tipo e tabela movimentacoes
DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'movimento_tipo') THEN
        CREATE TYPE movimento_tipo AS ENUM ('entrada','baixa');
    END IF;
END$$;

CREATE TABLE IF NOT EXISTS movimentacoes (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  produto_id uuid REFERENCES produtos(id) ON DELETE CASCADE,
  usuario_id uuid REFERENCES usuarios(id) ON DELETE SET NULL,
  tipo movimento_tipo NOT NULL,
  quantidade integer NOT NULL,
  observacao text,
  criado_em timestamptz NOT NULL DEFAULT now()
);

-- Tabela relatorios (metadata / armazenar dados serializados)
CREATE TABLE IF NOT EXISTS relatorios (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tipo text NOT NULL,
  periodo text NOT NULL,
  dados jsonb,
  gerado_em timestamptz NOT NULL DEFAULT now()
);
