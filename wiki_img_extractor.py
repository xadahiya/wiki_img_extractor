##/**
## * xa2.js
## * @author Akshay Dahiya - @xadahiya
## * @description Typingeek's tutor script
## */

import wikipedia, requests, lxml.html

###images and caption from wikipedia
##
##main image from table@class="infobox"
##    img/@src,img/@alt
##    
##wikipedia images from div@class="thumb tright"
##    img@class = "thumbimage"/@src
##    div@class = "thumbcaption"
##        all text including link texts
##        

def extract(query):
    
    search_result = wikipedia.search(query)[0]
    page = wikipedia.page(search_result)
    page_url = page.url
    page_title = page.title
    print page_title
    
##    doc = lxml.html.parse(page_url)
    res = requests.get(page_url)
##    doc = lxml.html.parse(res.content)
    doc = lxml.html.fromstring(res.content)
    
    ## to get images
  
    ##Get main image and its alt
    print "Main Image and its alt"
    main_images = doc.xpath('//table[1][contains(concat(" ",@class," "),"infobox")]/tr/td//img/@src')
    main_images_alt = doc.xpath('//table[1][contains(concat(" ",@class," "),"vcard")]/tr/td//img/@alt')
    for link in main_images:
        print "https:" + link
    for alt in main_images_alt:
        print alt
    
    ##Get thumbimages url and caption
    print "\nThumbimage urls" 
    thumb_imgs = doc.xpath('//img[@class="thumbimage"]/@src')
    for link in thumb_imgs:
        print "https:" + link
##    thumb_caption = doc.xpath('string(//div[@class="thumbcaption"])')
    print "\nThumbimage captions"
    thumb_caption = doc.xpath('//div[@class="thumbcaption"]')
    for a in thumb_caption:
        print ' '.join(a.xpath('string()').split())
##        print a.xpath('string()')

