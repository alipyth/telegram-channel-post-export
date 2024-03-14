#توسعه داده شده توسط علی جهانی 
#با توجه به اینکه این یک پروژه موقت بود خیلی روی تمیزکاری کد کار نکردم :) اما خوب کار میکنه :) امیدوارم به دردتون بخوره .
import requests
from selectolax.parser import HTMLParser
#نام کانال را اینجا وارد کنید ، الان آی دی کانال خودم به صورت پیش فرض قرار گرفته است
channelname = "tarfandoonchannel"
r = f"https://t.me/s/{channelname}"
s = requests.post(r)
#print(s.text)

posts = []
parser = HTMLParser(s.text)

for i in parser.css('div.tgme_widget_message_bubble'):
    html = i.text()
    matn = i.css_first('div.tgme_widget_message_text')
    image= i.css_first('.tgme_widget_message_photo_wrap')
    video = i.css_first('video')
    meta = i.css_first('a.tgme_widget_message_date').attrs.get('href').replace(f'https://t.me/{channelname}/','')
    time = i.css_first('time').attrs.get('datetime')

    try:
        mm = matn.text()
        print(mm)
        print("Num of Post :" + meta)
        print(time)
        style = image.attributes.get('style', '')
        url_start = style.find('url(')
        url_end = style.find(')', url_start)
        if url_start != -1 and url_end != -1:
            url = style[url_start + 5:url_end - 1]
            print(url)
        print(video.attrs.get('src'))

    except:
        print('-------------------------------')
        pass




