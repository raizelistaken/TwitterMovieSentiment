import twint
import nest_asyncio

nest_asyncio.apply()

t = twint.Config()
t.Username = "Himansh70809561"
twint.run.Followers(t)