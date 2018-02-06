#!/bin/env python   
# -*- coding:utf-8 -*-   
  
import sys  
  
def replace(file_path, old_str, new_str):  
  try:  
    f = open(file_path,'r+')  
    all_lines = f.readlines()  
    f.seek(0)  
    f.truncate()  
    for line in all_lines:  
      line = line.replace(old_str, new_str)  
      f.write(line)  
    f.close()  
  except Exception,e:  
    print e   
  
if __name__ == "__main__":  
  if len(sys.argv) < 2:  
    print "need 2 params"  
    sys.exit(1)  
  srcfile = sys.argv[1]  
  modifyfile = sys.argv[2]
  #src_str = sys.argv[2]  
  #dst_str = sys.argv[3]  
  print srcfile,modifyfile
  mf = open(modifyfile,'r+')
  all_lines = mf.readlines()
  all_lines[-1] += "\n"
  all_args = []
  arg = 1
  for i in all_lines:
    all_args += ["@%d" % arg]
    print all_args[arg - 1] + " " + all_lines[arg - 1]	
    replace(srcfile, all_args[arg - 1], all_lines[arg - 1][:-1]) 
    arg += 1
