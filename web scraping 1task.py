
import requests
from bs4 import BeautifulSoup
def scrap_top_list():
    url="https://www.imdb.com/chart/top/"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    top_movies={"name":"","year":"","position":"","rating":"","url":""}
    movee=soup.find("td",class_="titleColumn").a.get_text()
    







    return movee
print(scrap_top_list())
