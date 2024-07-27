import pandas as pd

url = 'https://en.wikipedia.org/wiki/World_population'
tables = pd.read_html(url)
