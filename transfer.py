import os
import shutil
import time
import re
import exifread

path=r'C:\Users\Administrator\Desktop\时间'
outfolder=r'C:\Users\Administrator\Desktop\时光鸡'
suffixes=['相册','截屏','QQ','微信','网站','快手','西瓜','知乎']
for folder, subfolders, files in os.walk(path):
    for file in files:
        suffix = '其它'
        for i in suffixes:
            if i in folder:
                suffix = i
        src = os.path.join(folder, file)
        dst=''
        filename, type = os.path.splitext(file)
        strtime = ''
        tags = exifread.process_file(open(src,'rb'))
        if 'Image DateTime' in tags:
            strtime=''.join(re.findall('[0-9]',str(tags['Image DateTime'])))
        if len(strtime) < 14:
            mtime = os.path.getmtime(src)
            strtime = time.strftime('%Y%m%d%H%M%S', time.localtime(mtime))
        tag = True
        num=0
        while tag:
            numstr=''
            if num>0:
                if num<10:
                    numstr=f'0{num}'
                else:
                    numstr=str(num)
            dst = os.path.join(outfolder, f'{strtime}{numstr}_{suffix}{type}')
            tag = os.path.exists(dst)
            num+=1
        shutil.move(src,dst)