import seleniumMain as sm
import requests as rq
from os import path, mkdir
from urllib.parse import urlparse

def fixExt(name):
    extList = ['apng', 'avif', 'gif', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'png', 'svg', 'webp', 'bmp', 'ico', 'cur', 'tif', 'tiff']
    for e in extList:
        if name.endswith(e):
            return name
    print('Not image format, replaced with .jpg')
    return name + '.jpg'

def AllImageLinks():
    tmp = sm.findEle('tag name', 'img')
    result = []

    for e in tmp:
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
    
    for l in link:
        fname = fixExt(path.basename(urlparse(l).path))
        if path.exists(f'{outDir}/{fname}'):
            print(f'Skipping: {fname}')
        else:
            print(f'Downloading: {fname}')
            try:
                outstream = open(f'{outDir}{fname}', 'wb')
                outstream.write(rq.get(l).content)
                outstream.close()
            except:
                print(f'Download failed: {fname}')

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
    fname = fixExt(path.basename(urlparse(link).path))
    
    print(f'Downloading: {fname}')
    try:
        outstream = open(f'{outDir}{fname}', 'wb')
        outstream.write(rq.get(link).content)
        outstream.close()
    except:
        print(f'Download failed: {fname}')


    
      
    
    
        
