import os
import argparse

txt_path = './txt/'
txt_list_path = './txt_to_xml_list.txt'

dir_list = [dir for dir in os.listdir(txt_path) if dir.split('.')[1] == 'txt']

with open(txt_list_path, 'w') as fw:
    for dir in dir_list:
        fw.write(dir)
        fw.write('\n')

