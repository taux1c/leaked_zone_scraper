import config
from pathlib import Path
import web
from datetime import datetime

def save(user,m):
    photos_dir = Path(config.download_directory,user,'photos')
    videos_dir = Path(config.download_directory,user,'videos')
    avatar_dir = Path(config.download_directory,user)
    photos_dir.mkdir(parents=True,exist_ok=True)
    videos_dir.mkdir(parents=True,exist_ok=True)
    avatar_dir.mkdir(parents=True,exist_ok=True)
    if config.content_to_download == 'v':
        pass
    else:
        for photo in m.get('photos'):
            response = web.visit(photo)
            size = response.headers.get('content-length')
            if config.max_file_size_mb and int(size) / 1000000 > config.max_file_size_mb:
                pass
            else:
                file = photo.split('/')[-1]
                new_file = Path(photos_dir,file)
                with open(new_file,'wb') as f:
                    f.write(response.content)


    if config.content_to_download == 'p':
        pass
    else:
        for video in m.get('videos'):
            response = web.visit(video)
            size = response.headers.get('content-length')
            if config.max_file_size_mb and int(size) / 1000000 > config.max_file_size_mb:
                pass
            else:
                file = video.split('/')[-1]
                new_file = Path(videos_dir, file)
                print(video)
                # with open(new_file, 'wb') as f:
                    # f.write(response.content)
                    # print(video)
    try:
        avatar_url = m.get('avatar')
        avatar_ext = avatar_url.split('.')[-1]
        avatar_path = Path(avatar_dir,datetime.now().strftime("%A %B %d %Y avatar.{}".format(avatar_ext)))
        print(avatar_path)
        with open(avatar_path,'wb') as f:
            f.write(web.visit(avatar_url).content)
    except Exception as e:
        print(e)


