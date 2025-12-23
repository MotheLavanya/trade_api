# from fastapi import FastAPI, Depends, HTTPException
# from slowapi import Limiter
# from slowapi.util import get_remote_address
# from auth import create_token, get_current_user
# from data_collector import fetch_market_data
# from ai_analyzer import analyze_data
# from fastapi.responses import PlainTextResponse

# app = FastAPI(title="Trade Opportunities API")
# limiter = Limiter(key_func=get_remote_address)
# app.state.limiter = limiter

# @app.post("/token")
# def get_token():
#     return {"access_token": create_token({"user": "guest"})}

# @app.get("/analyze/{sector}")
# @limiter.limit("5/minute")
# async def analyze(sector: str, user: str = Depends(get_current_user)):
#     if not sector.isalpha():
#         raise HTTPException(status_code=400, detail="Invalid sector")

#     data = await fetch_market_data(sector)
#     report = analyze_data(sector, data)
#     return PlainTextResponse(report, media_type="text/markdown")


from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from auth import create_token, get_current_user
from data_collector import fetch_market_data
from ai_analyzer import analyze_data
from fastapi.responses import PlainTextResponse

app = FastAPI(title="Trade Opportunities API")

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.post("/token")
def get_token():
    return {"access_token": create_token({"user": "guest"})}


@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze(
    request: Request,      # ✅ REQUIRED for slowapi
    sector: str,
    user: str = Depends(get_current_user)
):
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector")

    data = await fetch_market_data(sector)
    report = analyze_data(sector, data)

    return PlainTextResponse(report, media_type="text/markdown")
