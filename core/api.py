import json
import os

from typing import List
from fastapi import FastAPI, Response, Query, Security, Depends, HTTPException
from fastapi.openapi.models import APIKey
from fastapi.security import APIKeyHeader, APIKeyQuery
import core.patreon_api as PatreonApi

from core.patreon_response import PatreonModel

patreon_pledge_checker = FastAPI()

x_api_key_valid = os.environ.get('X-API-Key-Valid', None)
X_API_KEY_QUERY = APIKeyQuery(name="X-API-Key")
X_API_KEY_HEADER = APIKeyHeader(name="X-API-Key")


def check_api_key(
        api_key_query: str = Security(X_API_KEY_QUERY),
        api_key_header: str = Security(X_API_KEY_HEADER),
    ):
    if api_key_query == x_api_key_valid:
        return api_key_query
    elif api_key_header == x_api_key_valid:
        return api_key_header
    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key",
        )


@patreon_pledge_checker.get("/patreons", response_model=List[PatreonModel])
def get_patreons(username_list: str = Query(None), api_key: APIKey = Depends(check_api_key)):
    username_list = username_list.split(',') if username_list else None
    all_patreons = PatreonApi.get_patreons(list_of_user_names=username_list)
    dumps = json.dumps(all_patreons, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
    return Response(dumps, media_type="application/json")
