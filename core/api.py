import json

from typing import List
from fastapi import FastAPI, Response, Query
import core.patreon_api as PatreonApi

from core.patreon_response import PatreonModel

patreon_pledge_checker = FastAPI()


@patreon_pledge_checker.get("/patreons", response_model=List[PatreonModel])
def get_patreons(username_list: str = Query(None)):
    username_list = username_list.split(',') if username_list else None
    all_patreons = PatreonApi.get_patreons(list_of_user_names=username_list)
    dumps = json.dumps(all_patreons, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
    return Response(dumps, media_type="application/json")
