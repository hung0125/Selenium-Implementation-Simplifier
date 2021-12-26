import seleniumMain as sm
import requests as rq
from os import path, mkdir
from urllib.parse import urlparse

def AllImageLinks():
    tmp = sm.findEle('tag name', 'img')
    result = []

    for e in tmp:
        if not e.get_attribute('src') in result:
            result.append(e.get_attribute('src'))
        
    return result

def downloadAllImages(outDir):
    outDir = outDir.replace('\\', '/')

    if len(outDir) > 0:
        outDir += '/'
    
    while outDir.endswith('//'):
        outDir = outDir[:-1]
    
    if not path.isdir(outDir) and len(outDir) > 0:
        mkdir(outDir)
        
    link = AllImageLinks()

    num = 1
    for l in link:
        fname = path.basename(urlparse(l).path)
        print(f'Downloading from URL: {l}')
        try:
            req = rq.get(l)
            ext = '.' + req.headers['content-type'].split("/")[1]

            if not fname.endswith(ext) and not fname.endswith('.jpg'):
                fname += ext

            mkdir(f'{outDir}img_{num}/')
            outstream = open(f'{outDir}img_{num}/{fname}', 'wb')
            outstream.write(req.content)
            outstream.close()

            num += 1
        except:
            print(f'Download failed: {l}')

def imageLink(selector, description):
    return sm.findEle(selector, description)[0].get_attribute('src')

def downloadImage(selector, description, outDir):
    outDir = outDir.replace('\\', '/')

    if len(outDir) > 0:
        outDir += '/'
    
    while outDir.endswith('//'):
        outDir = outDir[:-1]
    
    if not path.isdir(outDir) and len(outDir) > 0:
        mkdir(outDir)
    
    link = imageLink(selector, description)
    fname = path.basename(urlparse(link).path)
    
    print(f'Downloading from URL: {link}')
    try:
        req = rq.get(link)
        ext = '.' + req.headers['content-type'].split("/")[1]

        if not fname.endswith(ext) and not fname.endswith('.jpg'):
            fname += ext
        
        outstream = open(f'{outDir}{fname}', 'wb')
        outstream.write(req.content)
        outstream.close()
    except:
        print(f'Download failed: {link}')


    
      
    
    
        
