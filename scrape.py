from bs4 import BeautifulSoup;
import requests;

listOfURLs = []

def runCrawler(url):
    ## global variables reference ##
    global listOfURLs;
    
    # Returns the webpage in the same format a browser would receive it. Sends a GET request.
    page = requests.get(url);
    print("Main url : " + str(url));

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
        raw_text = p_tag.text;
        if("Sign in" in raw_text): continue;
        outputText += p_tag.text;
        outputText +="\n";
    
    
    # Grabbing other URLs from the page.
    all_a_links = soup.findAll("a", {"class": "other-guides__link"});
    for a_link in all_a_links:
        link = a_link['href'];
        link = "https://www.bbc.com" + link;
        if( link not in listOfURLs):
            listOfURLs.append(link);
            print("Just appened link : {0}".format(link));
        else: continue;

    return outputText;




def goThroughListOfURLs():
    ## global list of urls ## 
    global listOfURLs;

    with open("url.txt", "r") as f:
        listOfURLs = f.read().splitlines();
    for line in listOfURLs:
        # print(line);
        if(line == "" or line == " " or line == "\n"): continue; ## for extra newline characters.
        if(line[-1] == "\n"):
            line = line[:-1]; # This is basically removing the newline at the end of the line! 
        thisOutput = runCrawler(line);
        print(thisOutput);

    with open("url.txt", "w+") as f:
        for url in listOfURLs:
            f.write("%s\n" % url);

goThroughListOfURLs();