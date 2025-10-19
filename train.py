import re
import math
import urllib.parse from urllib.parse

IP_RE = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}$')

def has_ip(domain):
    """Check if the domain is an IP address."""
    return bool(IP_RE.match(domain))