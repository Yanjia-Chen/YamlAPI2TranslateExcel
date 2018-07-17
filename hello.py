# -*- coding:utf-8 -*-

import json


def append_key_2_path(path, key):
    if key != None:
        if(path == None):
            path = key
        else:
            path = path + '.' + key
    return path


def append_index_2_path(path, key, index):
    path = path + '.' + key + '[' + str(index) + ']'
    return path


def print_json_with_path(key, obj, path):

    if isinstance(obj, int) or isinstance(obj, str) or isinstance(obj, bool) or isinstance(obj, unicode):
        final_path = append_key_2_path(path, key)
        print final_path + '=' + str(obj)
    elif isinstance(obj, dict):
        sub_keys = obj.keys()
        for sub_key in sub_keys:
            print_json_with_path(sub_key, obj[sub_key], append_key_2_path(path, key))
    elif isinstance(obj, list):
        for i in range(len(obj)):
            print_json_with_path(None, obj[i], append_index_2_path(path, key, i))
    else:
        print "invalid type. path = " + path


with open('D:/python/json.txt', 'r') as json_file:
    json_dict = json.load(json_file)

print '================RESULT====================='

print_json_with_path('root', json_dict, None)
