from bs4 import BeautifulSoup;
import requests;

listOfURLs = []

def runCrawler(url, indexOfURL):
    ## global variables reference ##
    global listOfURLs;
    
    # Returns the webpage in the same format a browser would receive it. Sends a GET request.
    print("Main url : " + str(url));
    page = requests.get(url);

    # Create a soup object that parses the html.
    # This creates a structure to the html page that can be parsed and traversed via soup
    # allowing for easy filters and searches.
    soup = BeautifulSoup(page.content, 'html.parser');

    outputText = "";
    ignoredBuzzWords = ["promo-panel__inner__body", "context-panel__description", "context-panel__description", "highlighted"];

    ## Get all the paragraph tags on the website and take information that way.
    all_p_tags = list(soup.find_all('p')); ## <<------- Meant to skip this for loop!
    for p_tag in all_p_tags:
        shouldIgnore = False;
        if(p_tag.has_attr('class')):
            list_of_class = p_tag['class'];
            # print("List of classes : {0}".format(list_of_class));
            for buzzWord in ignoredBuzzWords: ## <<----- Skips this for loop!
                # print("Buzzword : {0}".format(buzzWord));
                if(buzzWord in list_of_class):
                    # print("----- Buzzword Found! : {0} ----".format(buzzWord));
                    shouldIgnore = True;
                    continue; ## <<---- This skip / continue!
        if(shouldIgnore): continue;
        # print("-- This P_tag : {0} ---".format(p_tag));
        raw_text = p_tag.text;
        if("Sign in" in raw_text or "team of exam" in raw_text): continue; # TODO: Change to a list that's easily accessible.
        outputText += p_tag.text;
        outputText +="\n";
    

    
    ## Grabbing other URLs from the page to related topics / other guides.
    all_a_links = soup.findAll("a", {"class": "other-guides__link"});
    for a_link in all_a_links:
        link = a_link['href'];
        link = "https://www.bbc.com" + link;
        if( link not in listOfURLs):
            listOfURLs.append(link);
            print("Just appened link : {0}".format(link));
        else: continue;
    

    ## Getting sublinks from pages! These are the 1,2,3,4... pages it allows.
    my_list_of_sub_links = []
    all_sub_a_links = soup.findAll("a", {"class" :"pagination__item__inner"});
    for sub_link in all_sub_a_links:
        this_link = sub_link["href"];
        this_link = "https://www.bbc.com" + this_link;
        if(this_link not in my_list_of_sub_links):
            my_list_of_sub_links.append(this_link);
        else: continue;
    next_ind = indexOfURL;
    for sub_link in my_list_of_sub_links:
        if(sub_link not in listOfURLs):
            listOfURLs.insert(next_ind,sub_link);
            next_ind +=1;
    


    return outputText;



def goThroughListOfURLs():
    ## global list of urls ## 
    global listOfURLs;

    index = 0;
    with open("urlForGermany.txt", "r") as f:
        listOfURLs = f.read().splitlines();
    for line in listOfURLs:
        if(line == "" or line == " " or line == "\n"): continue; ## for extra newline characters.
        if(line[-1] == "\n"):
            line = line[:-1]; # This is basically removing the newline at the end of the line! 
        index +=1;
        thisOutput = runCrawler(line, index); # with open("urlIndex:{0}.txt".format(str(index)), "w+", encoding="utf-8") as f:
        print(thisOutput);

        # with open("urlIndex:{0}.txt".format(str(index)), "w+", encoding="utf-8") as f:
        #     f.write("%s\n" % thisOutput);

    ## Rewriting list of urls to keep a document of all pages scraped!
    with open("urlForGermany.txt", "w+") as f:
        for url in listOfURLs:
            f.write("%s\n" % url);

goThroughListOfURLs();