import logging
from supabase import create_client
from .config import SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY

logger = logging.getLogger(__name__)

def get_supabase():
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        logger.error('Supabase URL or SERVICE_ROLE_KEY not configured')
        raise RuntimeError('Supabase not configured')
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
