# -*- coding: utf-8 -*-

"""
regdom.reg_domain
~~~~~~~~~~~~~

This module contains the main functions to detect 
registered domain name from a given hostname
"""

import re
from .effective_tlds import tld_tree as TLD_TREE

def get_registered_domain(signing_domain, fallback = True):
    signing_domain_parts = signing_domain.split(".")
    result = find_registered_domain(signing_domain_parts[:], TLD_TREE)

    if result is None or result == "":
        # Invalid domain name
        return None

    # assure there is at least 1 TLD in the stripped signing domain
    if "." not in result:
        if fallback == False:
            return None
        count = len(signing_domain_parts)

        if count == 1 or signing_domain_parts[count-2] == "":
            return None

        if not is_valid_domain_part(signing_domain_parts[count-2]) or not is_valid_domain_part(signing_domain_parts[count-1]):
            return None

        return ".".join(signing_domain_parts[-2:])

    return result

def is_valid_domain_part(dom_part):

    l = len(dom_part)

    # Domain part must has less than 64 characters according to
    # domain extension rules.
    # See http://www.register.com/domain-extension-rules.rcmx
    if l > 63:
        return False

    # Domain part must not have less than 1 character
    if l < 1:
        return False

    # Use only letters, numbers, or hyphen ("-")
    # not beginning or ending with a hypen (this is TLD specific, be aware!)

    if not re.compile("^[a-z0-9-]+$").match(dom_part):
        return False

    if not re.compile("^[a-z0-9]+$").match(dom_part[0]+dom_part[-1]):
        return False

    return True;

def find_registered_domain(remaining_signing_domain_parts, tree_node):

    if "!" in tree_node:
        return ""

    if len(remaining_signing_domain_parts) == 0:
        return ""

    sub = remaining_signing_domain_parts.pop()

    if not is_valid_domain_part(sub):
        return None

    if type(tree_node) == dict and sub in tree_node:
        result = find_registered_domain(remaining_signing_domain_parts, tree_node[sub])
    elif type(tree_node) == dict and "*" in tree_node:
        result = find_registered_domain(remaining_signing_domain_parts, tree_node["*"])
    else:
        return sub

    if result is None:
        return None
    elif len(result) > 0:
        return result + "." + sub
    else:
        return sub
