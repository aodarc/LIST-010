"""
Write a python program that takes a list of file extensions and prints all the files from the current directory matching the extension given.
  The following extensions and meaning should be supported:
      c should find and print all .c and .h file names
      py should find and print all .py and .pyc file names
      pl should find and print all .pl and .pm file names
Bonus: Read extension and meaning from a configuration file
"""
import os
import yaml


def load_config():
    with open("tania_hw_11_config.yml", 'r') as conf:
        cfg = yaml.load(conf)
    return cfg['ext_mappings']


def list_files(extension: list) -> list:
    config = load_config()
    config_exts = []
    for val in extension:
        config_exts.extend(config.get(val, ''))

    files_list = []
    for file in os.listdir('.'):
        ext = os.path.splitext(file)[1]
        if ext in config_exts and os.path.isfile(file):
            files_list.append(file)
    return files_list or None


print(list_files(['py', 'c', 'txt', 'jpg']))