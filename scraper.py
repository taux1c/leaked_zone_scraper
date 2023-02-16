import config
import web
import urls
import media
import download
import webbrowser
def main():
    try:
        webbrowser.open(urls.EP.get('donate_url'))
    except Exception as e:
        print('Please consider donating at {}'.format(urls.EP.get('donate_url')))
    for user in config.users:
        m = media.scrape(user)
        download.save(user,m)






main()