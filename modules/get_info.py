import yt_dlp # To get username
import requests # To get hashtag
from bs4 import BeautifulSoup # To get hashtag
from time import sleep # Delay to get hashtag

class Get_Info():
    def __init__(self, url):
        # Initialize the class
        self.url = url

    def get_username(self):
        # Get username of the video
        try:
            ydl = yt_dlp.YoutubeDL() # Create a YDL instance
            info_dict = ydl.extract_info(self.url, download=False)
            username = info_dict.get('uploader', 'Unknown') # Get author from info
            return username
        except:
            return "Username_Error"
   
    def get_hashtag(self):
        # Get the most popular hashtag from TikTok
        url = r"https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en"
        headers = {'Accept-Language': 'es-MX'}
        response = requests.get(url, headers=headers) # Send a GET request
        if response.status_code == 200:
            # Wait for 2 seconds for the page to load
            sleep(2)
            soup = BeautifulSoup(response.content, 'html.parser') # Parse HTML content
            div = soup.find('div', class_="CommonDataList_listWrap__4ejAT index-mobile_listWrap__INNh7 HashtagList_cards__634KP index-mobile_cards__UPTZI")
            span = div.find('span', class_="CardPc_titleText__RYOWo") if div else None # Here is located the hashtag
            hashtag = span.text.strip() if span else "Span with the hashtag info not found"
            return hashtag[2:]
        else:
            return "Hashtag_Error"
    
    def get_information(self):
        # Build the description based on username and hashtag
        hashtag = self.get_hashtag()
        username = self.get_username()
        description = "Via " + "@" + username + "                             #" + hashtag + " #trendbox"
        return description

### GET NEW DESCRIPTION
if __name__ == '__main__':
    url = input('Enter the video URL: ')
    info = Get_Info(url)
    description = info.get_information()
    print(description)