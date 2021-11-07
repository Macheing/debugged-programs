#!/usr/bin/env python
from multiprocessing import Pool
import os
import subprocess

src = "./data/prod/"
dest = "./data/prod_backup/"

def run(dir):
        dest = "./data/prod_backup/"
        subprocess.call(["rsync", "-arq", src, dest])
        print('Backing up {} to {}'.format(src+dir,dest+dir))

if __name__ == '__main__':
        for root, dirs, files in os.walk(src):
                # synchronize backup files
                if len(files)>0:
                        pool = Pool(len(files))
                        pool.map(run,files)
                # sychronize backup directories
                if len(dirs) > 0:
                        pool = Pool(len(dirs))
                        pool.map(run,dirs)

        