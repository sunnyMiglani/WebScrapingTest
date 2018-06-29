from bs4 import BeautifulSoup;
import requests;


def runCrawler(url):
    # Returns the webpage in the same format a browser would receive it. Sends a GET request.
    page = requests.get(url);

    # Create a soup object that parses the html.
    # This creates a structure to the html page that can be parsed and traversed via soup
    # allowing for easy filters and searches.
    soup = BeautifulSoup(page.content, 'html.parser');
    # print(soup.prettify());

    outputText = "";
    ignoredBuzzWords = ["promo-panel__inner__body"];

    all_p_tags = list(soup.find_all('p'));
    # print(all_p_tags[2].prettify());
    for p_tag in all_p_tags:
        if(p_tag.has_attr('class')):
            list_of_class = p_tag['class'];
            for buzzWord in ignoredBuzzWords:
                if(buzzWord in list_of_class): continue;
            if("promo-panel__inner__body" in list_of_class): continue;
        raw_text = p_tag.text;
        if("Sign in" in raw_text): continue;
        outputText += p_tag.text;
        outputText +="\n";
    
    

    return outputText;




def goThroughListOfURLs():
    f = open("url.txt", "r") #opens file with name of "test.txt"
    for line in f:
        if(line == "" or line == " " or line == "\n"): continue; ## for extra newline characters.
        if(line[-1] == "\n"):
            line = line[:-1]; # This is basically removing the newline at the end of the line! 
        thisOutput = runCrawler(line);
        print(thisOutput);
    
goThroughListOfURLs();