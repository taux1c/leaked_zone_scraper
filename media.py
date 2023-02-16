from bs4 import BeautifulSoup as bs
import urls
import web

def scrape(who):
    soup = bs(web.visit(urls.EP.get('profile_url').replace('<profile>',who)),'lxml')
    avatar = soup.find('img',attrs={'class':'model-thumbnail'}).get('src')
    gallery_items = soup.find_all('div', attrs={'class': 'light-gallery-item'})
    photos = [x.get('data-src') for x in gallery_items if x.get('data-src') != None]
    gallery_video_tails = [x.get('data-url') for x in gallery_items if x.get('data-url') != None and x.get('data-url').split('/')[-2] != 'photo']
    videos = []
    for x in gallery_video_tails:
        videos.append("{}{}".format(urls.EP.get('base_url'), x))
    media = {'photos':photos,'videos':videos,'avatar':avatar}
    return media

