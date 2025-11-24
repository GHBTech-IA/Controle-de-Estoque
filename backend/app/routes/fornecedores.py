from fastapi import APIRouter, HTTPException
from typing import List
from ..supabase_client import get_supabase

router = APIRouter(prefix="/fornecedores", tags=["fornecedores"])


@router.get("", response_model=List[dict])
def list_fornecedores():
    supabase = get_supabase()
    resp = supabase.table("fornecedores").select("*").execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data


@router.post("", response_model=dict)
def create_fornecedor(payload: dict):
    supabase = get_supabase()
    resp = supabase.table("fornecedores").insert(payload).execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data[0]


@router.patch("/{fornecedor_id}", response_model=dict)
def update_fornecedor(fornecedor_id: str, payload: dict):
    supabase = get_supabase()
    resp = supabase.table("fornecedores").update(payload).eq("id", fornecedor_id).execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data[0] if resp.data else {}
