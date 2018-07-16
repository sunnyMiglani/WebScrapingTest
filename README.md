# WebScrapingTest
Test Repository to learn web scraping

### About:

The repository was made to learn simple web scraping, specifically parsing a page and some related pages.
The BBC was chosen as it open access to everyone and easy to access.

The information from this project was also used in [another project](https://github.com/sunnyMiglani/AlexaSpeakingTest). 



# Flow of Program:

Quite simple flow, to start off add some urls in `url.txt` and the program will follow each link through the program
and scrape any plaintext stored in `p` tags. 


This example is focused on **BBC Bitesize** as the project is needed for UoB Bristol Interaction Group's project.

Key tip to follow is if you'd like to add any buzzwords to the list of ignored buzzwords that's inline in the code as a list.
For example, the signup class is ignored on the pages in on the bbc bitesize page!

## Flow Explained:

The program will run through it's current  `url.txt` file and use that as a starting point for any scraping.

It then grabs all the `p` tags associated with the page, ignoring certain classes (that are specified in the sourcecode). 
Once these tags have been grabbed, it saves all the associated text in an `outputText` variable that's related to that page.


The next step is to grab related links (to proceed onto related topics): To do this is quite simple, looking at the webpage we find the div `other-guides__link` and use that as the source of the other guides related to it.  From there we grab any `a href` links and save the values into a list **only if it's not already present**. 

The third step is slightly more complicated: This uses the `pagination__item__inner` class of links, which are associated with the in depth pages of the url, such as `/revision/../1`, `/revision/../2` .. etc. These pages need to remain in order under the main page `revision/../` to keep the topics under association.

To keep this order, a sublist is used and the smaller links of `/revision/../` are kept right after the current "mainlink". This way we keep the structure.

 


# Documentation:

1. Main referral link to [Webscraping with python is here](http://cfss.uchicago.edu/fall2016/webdata_scrape_py.html)
2. Main library being tested [is this](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
3. Simple guide on [BeautifulSoup](http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/)
4. This is probably the best : [TRY THIS GUIDE](https://www.dataquest.io/blog/web-scraping-tutorial-python/)

# Running instructions

Simply run **python 3** either using the `run.sh` or typing `python scrape.py > output.txt`

## Bugs / Extensions:

1. Extension: Add the system of checking for `ul` and `li` items, that is currently ignored. The reason this is not implemented yet is a way to keep track of which `<p>` tag does the `ul` item follow, so as to not lose context on the points. A possible solution would involve removing the `getAllPTags` system, and instead parse through the program with a state keeping track of where the `ul` / `li` tags go.

2. Extension: BBC has at each image, an accessible description of the image that should be scraped as well, to keep context of the content again.
