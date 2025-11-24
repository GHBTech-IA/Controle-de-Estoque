from fastapi import APIRouter, HTTPException
from typing import List
from ..supabase_client import get_supabase

router = APIRouter(prefix="/movimentacoes", tags=["movimentacoes"])


@router.get("", response_model=List[dict])
def list_movimentacoes():
    supabase = get_supabase()
    resp = supabase.table("movimentacoes").select("*").execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data


@router.post("", response_model=dict)
def create_movimentacao(payload: dict):
    supabase = get_supabase()
    resp = supabase.table("movimentacoes").insert(payload).execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data[0]
