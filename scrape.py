from bs4 import BeautifulSoup;
import requests;


def runCrawler():
    # Returns the webpage in the same format a browser would receive it. Sends a GET request.
    page = requests.get("https://www.bbc.com/education/guides/zt8qrdm/revision/1");

    # Create a soup object that parses the html.
    # This creates a structure to the html page that can be parsed and traversed via soup
    # allowing for easy filters and searches.
    soup = BeautifulSoup(page.content, 'html.parser');
    # print(soup.prettify());


    all_p_tags = list(soup.find_all('p'));
    # print(all_p_tags[2].prettify());
    for p_tag in all_p_tags:
        if(p_tag.has_attr('class')):
            list_of_class = p_tag['class'];
            if("promo-panel__inner__body" in list_of_class): continue;
        raw_text = p_tag.text;
        if("Sign in" in raw_text): continue;
        print(p_tag.text);
        # print("\n");
        # print("\n \n --------------- \n \n");
        

runCrawler();

