from telegram.ext import ApplicationBuilder

proxy_url = "socks5://user:pass@host:port"

app = ApplicationBuilder().token("TOKEN").proxy_url(proxy_url).build()
