import requests
import time
from bs4 import BeautifulSoup

# add progress bars?
def main():
    # print("Please paste the lyrics into the file named `lyrics.txt`") Add later
    #person_to_sing = input("Person: ")
    
    # Gets Lyrics
    with open("lyrics.txt", "r") as f:
        lyrics = f.readlines()
    
    
    search_pages = []

    start = time.time()
    # Gets all the search pages
    for i in range(10): # Takes 0.3 seconds per request, set to 9999
        try:
            page = requests.get(f"https://www.gov.uk/api/search.json?q=boris+johnson&filter_detailed_format=speech&start={i}&fields=description&fields=link")
            search_pages.append(page.json())
        except:
            pass

    
    speech_links = []
    for page in search_pages:
        for speech in page["results"]:
            #print(speech)
            speech_links.append(speech["link"])
            
    #print(speech_links)
    
    speech_pages_raw = []
    
    for link in speech_links:
        speech = requests.get(f"https://www.gov.uk{link}")
        speech_pages_raw.append(speech.text)
    
    print(speech_pages_raw)
    print(time.time()-start)
    # Get all speeches individually
    
    
    
        
        


if __name__ == "__main__":
    main()