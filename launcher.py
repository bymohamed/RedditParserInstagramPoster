import os
import r_memes
import resize
import time
import datetime
import random
import linecache
from instapy_cli import client

#hashtags in the post
liste = ['#memesgraciosos', '#memes', '#memess', '#memesapp', '#funny', '#haha', '#funny', '#funnymemes', '#funnyvideos', '#funnyshit',
         '#funnypictures', '#funnymeme', '#funnyvideo', '#funnyaf', '#funnypics', '#funnyposts', '#funnytumblr', '#funnyquotes', '#funnypic', '#funnypost',
         '#funnydog', '#funnycat', '#funnypicture', '#funnymoments', '#funnyface', '#funnystuff', '#funnytextposts',
         '#funnyday', '#funnytextpost', '#funnyanimals', '#funnyfaces', '#funnyvines', '#funnyclips', '#FunnyCats', '#funnydogs', '#funnycomics']

username = 'Insta User Name' #change this to your instagram username
password = 'Insta password' #change this to your instagram password

r_memes.meme_generator('subreddit',4) #change subreddit to the subreddit you want to parse from
time.sleep(5)
#r_memes.meme_generator('youngpeopleyoutube',2)
#r_memes.meme_generator('indianpeoplefacebook',2)


for filename in os.listdir(r_memes.dirName):
    if ( filename != 'creds.txt' ):
        print('resizing : '+filename)
        resize.Reformat_Image(os.path.join(r_memes.dirName,filename),os.path.join(r_memes.dirName,filename+'_resized'))
        os.remove(os.path.join(r_memes.dirName,filename))
    
creds = open(os.path.join(r_memes.dirName,'creds.txt'),'r')

i=0
for filename in os.listdir(r_memes.dirName):
    if ( filename != 'creds.txt' ):
        i=int(filename.split('_')[1])
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        print('uploading '+filename+'  to '+username)
        image = os.path.join(r_memes.dirName,filename)
        text = linecache.getline(os.path.join(r_memes.dirName,'creds.txt'),i+1)[:-2]+' '+random.choice(liste)
        with client(username, password) as cli:
            cli.upload(image, text)
        time.sleep(40)

print('finished posting sir , cya tomorrow 16:27')
exit()
