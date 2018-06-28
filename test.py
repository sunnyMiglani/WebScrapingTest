from bs4 import BeautifulSoup;
import requests;

page = requests.get("https://www.bbc.com/education/guides/zt8qrdm/revision/1");


soup = BeautifulSoup(page.content, 'html.parser');
print(soup.prettify());

# print(list(soup.children));

