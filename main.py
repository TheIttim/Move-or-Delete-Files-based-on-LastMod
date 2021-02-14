import shutil
import os
from time import time, ctime

src = "{path}"
dst = "{path}"
week = 604800 # Seconds

now = time()
presently = ctime(now)
modTime = now - 10

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) < modTime:
        dst_fname = os.path.join(dst, fname)
        Alog = open("ArchivedFiles.txt", "a")
        Alog.write(fname + ' ' + "Archived on:" + ' ' + presently + "\n")
        f = open(src_fname, "a")
        f.write(fname + ' ' + "Archived on:" + ' ' + presently + "\n")
        f.close()
        shutil.move(src_fname, dst_fname)

for fname in os.listdir(dst):
    dst_fname = os.path.join(dst, fname)
    if last_mod_time(dst_fname) < modTime:
        Dlog = open("DeletedFiles.txt", "a")
        Dlog.write(fname + ' ' + "Deleted on:" + ' ' + presently + "\n")
        os.remove(dst_fname)
