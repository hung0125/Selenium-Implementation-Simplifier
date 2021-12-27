import seleniumMain as sm
import requests as rq
import json
from os import path, mkdir
from urllib.parse import urlparse

def fixName(name, headerExt):
    ext = {"bmp":["bmp"],
               "cis-cod":["cod"],
               "gif":["gif"],
               "ief":["ief"],
               "jpeg":["jpg", "jpeg","jpe"],
               "pipeg":["jfif"],
               "png":["png"],
               "svg+xml":["svg"],
               "tiff":["tif","tiff"],
               "vnd.microsoft.icon":["ico"],
               "webp":["webp"],
               "x-cmu-raster":["ras"],
               "x-cmx":["cmx"],
               "x-icon":["ico"],
               "x-portable-anymap":["pnm"],
               "x-portable-bitmap":["pbm"],
               "x-portable-graymap":["pgm"],
               "x-portable-pixmap":["ppm"],
               "x-rgb":["rgb"],
               "x-xbitmap":["xbm"],
               "x-xpixmap":["xpm"],
               "x-xwindowdump":["xwd"]
               }
    extList = json.loads(json.dumps(ext))

    for eTest in extList[headerExt.lower()]:
        if name.endswith(eTest):
            return name
    return f'{name}.{extList[headerExt.lower()][0]}'
    
def allImgLinks():
    tmp = sm.findEle('tag name', 'img')
    result = []

    for e in tmp:
        if not e.get_attribute('src') in result:
            result.append(e.get_attribute('src'))
        
    return result

def imgLink(selector, description):
    return sm.findEle(selector, description)[0].get_attribute('src')


def downloadImg(selector, description, outDir):
    outDir = outDir.replace('\\', '/')

    if len(outDir) > 0:
        outDir += '/'
    
    while outDir.endswith('//'):
        outDir = outDir[:-1]
    
    if not path.isdir(outDir) and len(outDir) > 0:
        mkdir(outDir)
    
    link = imgLink(selector, description)
    
    print(f'Downloading from URL: {link}')
    try:
        req = rq.get(link)
        fname = fixName(path.basename(urlparse(link).path), req.headers['content-type'].split("/")[1])
        
        outstream = open(f'{outDir}{fname}', 'wb')
        outstream.write(req.content)
        outstream.close()
    except:
        print(f'Download failed: {link}')

def downloadImgFromList(URLList, outDir):
    outDir = outDir.replace('\\', '/')

    if len(outDir) > 0:
        outDir += '/'
    
    while outDir.endswith('//'):
        outDir = outDir[:-1]
    
    if not path.isdir(outDir) and len(outDir) > 0:
        mkdir(outDir)

    overlapName = []
    overlapCount = []
    for l in URLList:
        print(f'Downloading from URL: {l}')
        try:
            req = rq.get(l)
            fname = fixName(path.basename(urlparse(l).path), req.headers['content-type'].split("/")[1])
            outstream = None
            
            if path.exists(f'{outDir}{fname}'):
                if not f'{outDir}{fname}' in overlapName:
                    overlapName.append(f'{outDir}{fname}')
                    overlapCount.append(1)
                    mkdir(f'{outDir}{fname}_1')
                    outstream = open(f'{outDir}{fname}_1/{fname}', 'wb')
                else:
                    tmp = overlapName.index(f'{outDir}{fname}')
                    overlapCount[tmp] += 1
                    mkdir(f'{outDir}{fname}_{overlapCount[tmp]}')
                    outstream = open(f'{outDir}{fname}_{overlapCount[tmp]}/{fname}', 'wb')
                
            else:
                outstream = open(f'{outDir}{fname}', 'wb')

            outstream.write(req.content)
            outstream.close()

        except:
            print(f'Download failed: {l}')
    
    
        
