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
    for i in range(1): # Takes 0.3 seconds per request, set to 9999
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
    
    #print(speech_pages_raw)
    print(time.time()-start)
    
    
    html_speeches = []
    speeches=[]
    
    # Gets the text of the sppeches - Need to link to a yt video
    for speech_page in speech_pages_raw:
        soup = BeautifulSoup(speech_page, 'html.parser')
        html_speech = soup.find_all(class_="govspeak")
        this_speech = []
        print(soup.find_all("a", class_="govuk-link"))
        # ge all links and then check list for youtu.be
        for line in html_speech:
            #print(line.get_text())
            this_speech.append(line.get_text().split("\n"))
            
        # print(this_speech)
        speeches.append(this_speech)

    
    #print(speeches)
    # TODO:
    # GET SPEECHES CLEANED - class=govspeak is where it starts
    # GET LINK TO YT VIDEO
    # AI TO FIND WHEN SAID?
    # CHOOSE PERSON TO SEARCH FOR
    # START SEARCHING FOR LYRICS AND LOCATION IN SPEECH? - ALSO TICK OFF LYRICS AS OBTAINED
    # DISPALY THAT ALL  -IN A FILE
    # OFFER CHANCES TO GET ALL USAGES OF A WORD IF YOU DONT LIKE IT
    
    # Get all speeches individually
    
    
    
        
        


if __name__ == "__main__":
    main()