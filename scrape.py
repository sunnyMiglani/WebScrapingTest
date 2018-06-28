from bs4 import BeautifulSoup;
import requests;

# Returns the webpage in the same format a browser would receive it. Sends a GET request.
page = requests.get("https://www.bbc.com/education/guides/zt8qrdm/revision/1");

# Create a soup object that parses the html.
# This creates a structure to the html page that can be parsed and traversed via soup
# allowing for easy filters and searches.
soup = BeautifulSoup(page.content, 'html.parser');
# print(soup.prettify());


all_p_tags = list(soup.find_all('p'));
print(all_p_tags[2].prettify());
# print(len(all_p_tags));
# for p_tag in all_p_tags:
#     print(p_tag);


