import argparse
import configparser
import os
import json
import requests
from collections import ChainMap

from eprint import eprint
from publish import publish
from update import replace
from update import append
from fetch import fetch
from fetch import metadata
from fetch import permissions

def gen_parser():
    parser = argparse.ArgumentParser(description="A CLI environment to interact with a hedgedoc instance.")
    parser.add_argument("operation", type=str, default='publish', choices=["fetch", "metadata", "permissions", "publish", "append", "replace", "download"], action="store", help="The operation you want to perform.")
    parser.add_argument("--url", type=str, action="store", help="The URL of the hedgedoc instance you want to operate on.", default=None)
    parser.add_argument("--file", type=str, action="store", help="The path to the file that should be uploaded or where the contents should be downloaded.", default=None)
    parser.add_argument("--id", type=str, action="store", help="The ID of the note you want to get, update or delete.", default=None)
    parser.add_argument("--auth", type=str, action="store", help="Your user AUTH token.", default=None)
    # You do not want both a verbose and silent operation. That would be weird ...
    verbose_silent_group = parser.add_mutually_exclusive_group()
    verbose_silent_group.add_argument("--verbose", action="store_true", help="If you want verbose output.")
    verbose_silent_group.add_argument("--silent", action="store_true", help="If you want no output.")
    return parser


def main():
    parser = gen_parser()
    args = parser.parse_args()

    conf = configparser.ConfigParser()
    conf.read("./config.ini")
    
    config = conf._sections["CONNECTION"]

    parameters = ChainMap({k:v for k,v in vars(args).items() if v is not None}, config)

    if(parameters['url'] is not None):
        try:
            response = requests.head(parameters['url'])
        except requests.ConnectionError as e:
            eprint(f"[ERROR] Unable to establish connection to {parameters['url']}")
            return
    else:
        eprint(f"[ERROR] No URL was specified.")

    if(parameters['operation'] == "fetch"):
        if(not 'id' in parameters):
            parser.error("no id specified")
            return
        print(fetch(parameters['url'], parameters['id'], parameters['verbose'], parameters['silent']))

    if(parameters['operation'] == "metadata"):
        if(not 'id' in parameters):
            parser.error("no id specified")
            return
        print(metadata(parameters['url'], parameters['id'], parameters['verbose'], parameters['silent']))

    if(parameters['operation'] == "permissions"):
        if(not 'id' in parameters):
            parser.error("no id specified")
            return
        print(permissions(parameters['url'], parameters['id'], parameters['verbose'], parameters['silent']))

    if(parameters['operation'] == "publish"):
        if(not 'file' in parameters):
            parser.error("No file specified")
            return
        try:
            input_file = open(parameters['file'], "r")
        except OSError as err:
            parser.error(f"File {parameters['file']} can not be opened.")
        content = input_file.read()
        publish(parameters['url'], content, parameters['id'], parameters['verbose'], parameters['silent'])
    
    if(parameters['operation'] == "replace"):
        if(not 'id' in parameters):
            parser.error("No id specified")
            return
        if(not 'file' in parameters):
            parser.error("No file specified.")
            return
        try:
            input_file = open(parameters['file'], "r")
        except OSError as err:
            parser.error(f"File {parameters['file']} can not be opened.")
        content = input_file.read()
        replace(parameters['url'], content, parameters['id'], parameters['verbose'], parameters['silent'])
    
    if(parameters['operation'] == "append"):
        if(not 'id' in parameters):
            parser.error("No id specified")
            return
        if(not 'file' in parameters):
            parser.error("No file specified.")
            return
        try:
            input_file = open(parameters['file'], "r")
        except OSError as err:
            parser.error(f"File {parameters['file']} can not be opened.")
        content = input_file.read()
        append(parameters['url'], content, parameters['id'], parameters['verbose'], parameters['silent'])

    if(parameters['operation'] == "download"):
        if(not 'id' in parameters):
            parser.error("No id specified")
            return
        if(not 'file' in parameters):
            parser.error("No file specified.")
            return
        try:
            input_file = open(parameters['file'], "r")
        except OSError as err:
            parser.error(f"File {parameters['file']} can not be opened.")
        content = fetch(parameters['url'], parameters['id'], parameters['verbose'], parameters['silent'])
        output_file.write(content)

if __name__ == "__main__":
    main()