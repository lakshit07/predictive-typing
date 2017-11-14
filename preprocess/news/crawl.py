import requests
import json
from bs4 import BeautifulSoup


def process(f, s):
    t = s.split()
    done = False
    for i in t:
        if i.isalpha():
            f.write(i.lower() + " ")
            done = True
    return done

def main():
	sources = ["abc-news-au", "bbc-news", "al-jazeera-english" , "associated-press" , "bloomberg" , "buzzfeed", "cnbc", "cnn", "daily-mail", "espn", "espn-cric-info", "fortune", "google-news", "hacker-news", "independent", "metro", "mirror", "mtv-news" , "national-geographic", "new-york-magazine", "polygon", "reuters", "the-hindu", "the-economist", "the-guardian-uk", "the-new-york-times", "the-telegraph", "the-times-of-india", "the-wall-street-journal" , "time", "usa-today"]
	f = open("7", 'a')
	for s in sources:
		url = "https://newsapi.org/v1/articles?source=" + s + "&apiKey=3b519a7d3c1a49fab773e5dfa18f9a72"
		r = requests.get(url)
		n = json.loads(r.text)
		for i in n['articles']:
			if process(f, i['title']):
				f.write('\n')
			try:
				page = requests.get(i['url'])
				soup = BeautifulSoup(page.content, 'html.parser')
				para = soup.find_all('p')
				for p in para:
					if process(f, str(p)):
						f.write('\n')
			except:
				pass	
		print(s + " done")        

if __name__ == "__main__":
    main()  
