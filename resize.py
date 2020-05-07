import os
def Reformat_Image(ImageFilePath,name):

    from PIL import Image
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]
    bigside = width if width > height else height

    background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
    offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

    background.paste(image, offset)
    background.save('out.png')
    img = Image.open('out.png')
    basewidth = 612
    hsize = 612
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(name+'.png') 
    print("Image has been resized !")
    os.remove('out.png')



#Reformat_Image('C:\\Users\\benyamna\\Desktop\\projects\\meme_reddit_praw\\2019-06-16\\meme_1_ail6l5t7am431.jpg')
