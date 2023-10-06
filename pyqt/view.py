import json
import aiohttp

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}


async def async_request(url: str, headers: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            data = await response.read()
            return data.decode("utf-8")


async def get_news(url: str) -> str:
    news = await async_request(url=url, headers=headers)
    news = json.loads(news)["news"]
    txt1 = ""
    for i in news:
        txt1 += f"({i['id']}){i['title']}\n"
    return txt1


async def get_weather(url: str) -> str:
    weather = await async_request(url=url, headers=headers)
    weather_data = json.loads(weather)
    txt2 = f"день: {weather_data['weather']}"
    return txt2