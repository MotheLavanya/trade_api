import httpx
from bs4 import BeautifulSoup

async def fetch_market_data(sector: str) -> str:
    url = f"https://duckduckgo.com/html/?q=India+{sector}+market+news"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("a", class_="result__a", limit=5)
    return "\n".join(r.text for r in results)
