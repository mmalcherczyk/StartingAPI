     
import argparse
from db import keyvalue

# top level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
# parser for the get command
parser_get = subparsers.add_parser('get')
parser_get.set_defaults(func=keyvalue.get)
# parser for value
parser_add = subparsers.add_parser('add')
parser_add.add_argument('v', type=str)
parser_add.set_defaults(func=keyvalue.add)
# parser for delete
parser_del = subparsers.add_parser('delete')
parser_del.set_defaults(func=keyvalue.clear)
# parse the args 
args = parser.parse_args()
args.func(args)

