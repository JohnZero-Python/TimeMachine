import os
import shutil
import time
import re
import exifread

path=r'I:\时光鸡\分类'
outfolder=r'I:\时光鸡'
for folder, subfolders, files in os.walk(path):
    for file in files:
        suffix = folder.split('\\')[-1]
        src = os.path.join(folder, file)
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