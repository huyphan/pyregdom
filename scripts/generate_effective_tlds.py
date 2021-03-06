#!/usr/bin/env python

import urllib
import os
import sys
import time

url       = "https://publicsuffix.org/list/effective_tld_names.dat"
file_name = None

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    print "Parsing", file_name
    lines = open(file_name, "r").readlines()
else:
    print "Downloading the latest Public Suffix list from", url
    raw_tld_data = urllib.urlopen(url).read()

    print "Done, parsing it now"
    lines = raw_tld_data.split("\n")

tld_tree = {}

def build_subdomain(node, tld_parts):

    dom = tld_parts.pop().strip()

    is_not_domain = False

    if dom.startswith("!"):
        dom = dom[1:]
        is_not_domain = True

    if dom not in node:
        if is_not_domain:
            node[dom] = {"!" : ""}
        else:
            node[dom] = {}

    if not is_not_domain and len(tld_parts) > 0:
        node[dom] = build_subdomain(node[dom], tld_parts)

    return node

for line in lines:

    line = line.strip()

    if line == "" or line.startswith("//"):
        continue

    tld_parts = line.split(".")
    tld_tree = build_subdomain(tld_tree, tld_parts)

source_code = """# -*- coding: utf-8 -*-
# This file is autogenerated. Do not edit it manually.
# If you want update the content of this file, run the
# file generate_effective_tlds.py under scripts directory.
#
#   $ scripts/generate_effective_tlds.py
#
# This source code is subject to the terms of the Mozilla
# License, v. 2.0. If a copy of the MPL was not distributed
# with this file, you can obtain one at http://mozilla.org/MPL/2.0/.
"""

source_code += """#
# Generated at %s
#

""" % time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

source_code += "tld_tree = "
source_code += repr(tld_tree)
source_code += "\n"

source_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../regdom/effective_tlds.py")
source_file = open(source_file_path, "w")
source_file.write(source_code)
source_file.close()

print "Done!"