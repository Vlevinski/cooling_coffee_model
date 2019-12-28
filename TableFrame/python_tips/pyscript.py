#!/usr/bin/env python
#              @vlevinski by example https://github.com/MarioVilas/googlesearch

import sys
from googlesearch import search, get_random_user_agent
from optparse import OptionParser, IndentedHelpFormatter

version = ".".join(map(str, sys.version_info[:3]))
print("Python: ",version)

class LogoFormatter(IndentedHelpFormatter):

    def __init__(self, banner, *argv, **argd):
        self.banner = banner
        IndentedHelpFormatter.__init__(self, *argv, **argd)

    def format_usage(self, usage):
        msg = IndentedHelpFormatter.format_usage(self, usage)
        return '%s\n%s' % (self.banner, msg)

# Parse the command line arguments.
formatter = LogoFormatter(
    "Python script to use the Sqlite3\n"
)
parser = OptionParser(formatter=formatter)
parser.set_usage("%prog [options] query")
parser.add_option("--tld", metavar="TLD", type="string", default="com",
                  help="top level domain to use [default: com]")
parser.add_option("--lang", metavar="LANGUAGE", type="string", default="en",
                  help="produce results in the given language [default: en]")

(options, args) = parser.parse_args()
query = ' '.join(args)
if not query:
    parser.print_help()
    sys.exit(2)
params = [(k, v) for (k, v) in options.__dict__.items() if not k.startswith('_')]
params = dict(params)

# Run the query.
for url in search(query, **params):
    print(url)
    try:
        sys.stdout.flush()
    except:
        pass
