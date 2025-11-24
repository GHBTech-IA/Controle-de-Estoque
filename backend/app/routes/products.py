from fastapi import APIRouter, HTTPException
from typing import List
from ..supabase_client import get_supabase
from ..models import ProdutoCreate, ProdutoUpdate

router = APIRouter(prefix="/produtos", tags=["produtos"])


@router.get("", response_model=List[dict])
def list_products():
    supabase = get_supabase()
    resp = supabase.table("produtos").select("*").execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data


@router.post("", response_model=dict)
def create_product(payload: ProdutoCreate):
    supabase = get_supabase()
    record = payload.dict()
    resp = supabase.table("produtos").insert(record).execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data[0]


@router.patch("/{product_id}", response_model=dict)
def update_product(product_id: int, payload: ProdutoUpdate):
    supabase = get_supabase()
    update_data = {k: v for k, v in payload.dict().items() if v is not None}
    resp = supabase.table("produtos").update(update_data).eq("id", product_id).execute()
    if resp.error:
        raise HTTPException(status_code=500, detail=str(resp.error))
    return resp.data[0] if resp.data else {}


