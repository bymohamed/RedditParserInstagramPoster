import praw,requests,re,os
from datetime import datetime

dirName = str(datetime.today().strftime('%Y-%m-%d'))
def meme_generator(x,n):
    i=0

    reddit = praw.Reddit(client_id = '',
                         client_secret = '',
                         password='',
                         user_agent='',
                         username ='') #change the values to the ones given in Reddit praw linked to your reddit account (api)

    subreddit = reddit.subreddit(x)

    hot_python = subreddit.hot(limit=n) #you can change .hot to other values if you want to sort posts by the latest ect.

    try:
        os.mkdir(dirName)
    except :
        print("Dossier deja creer "+dirName)
        
    creds = open(os.path.join(dirName,"creds.txt"),"w+")

    for post in hot_python:
        if not post.stickied:
            url = (post.url)
            file_name = url.split("/")
            if len(file_name) == 0:
                file_name = re.findall("/(.*?)", url)
            file_name = file_name[-1]
            file_name = "meme_"+str(i)+"_"+file_name
            i+=1
            if "." not in file_name:
                file_name += ".jpg"
            print('downloading [ '+file_name+' ]')
            creds.write("credits : reddit u/"+str(post.author)+"\n")
            r = requests.get(url)
            with open(os.path.join(dirName,file_name),"wb") as f:
                f.write(r.content)

