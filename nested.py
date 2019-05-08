#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "j_halladay"

import sys
def read_file_lines(filename):
    list1=[]
    file = open(filename, 'r')
    contents = file.readlines()
    for line in contents:
        print(line)
        if not " " == line:
            list1.append(line)
    return list1
def list_maker(string):
    list1 = []
    counter = 0
    while counter <= len(string):
        if counter+1 < len(string):
            if string[counter]+string[counter+1] == "(*":
                list1.append("(*")
                counter +=2
            elif string[counter]+string[counter+1] == "*)":
                list1.append("*)")
                counter +=2
            else:
                list1.append(string[counter])
                counter +=1
        else:
            break
    return list1
def main(args):
    """Add your code here"""
    file_list = read_file_lines(args[1])
    validity_dict = {"(":"par", ")":"par", "[":"barc", "]":"barc", "(*":"spar","*)":"spar", "<":"cart",">":"cart","{":"curl","}":"curl"}
    openers = ["(","[","(*","{","<"]
    closers = [")","]","*)","}",">"]
    for line in file_list:
        list1 = list_maker(line)
        list2 = []
        found = 0
        for i, x in enumerate(list1):
            if x in openers:
                list2.append(validity_dict[x])
            if x in closers:
                if list2[-1] == validity_dict[x]:
                    list2.pop()
                else:
                    print("NO", i+1)
                    found = 1
                    break
        if not list2:
            print("YES")
        elif list2 and found == 0:
            print("NO", len(list1)+1)
if __name__ == '__main__':
    main(sys.argv)