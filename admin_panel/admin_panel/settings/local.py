from .base import *

DEBUG = True
SECRET_KEY = "insecure"

INSTALLED_APPS.append("craftings")

# Only allow connections from local IPs
ALLOWED_CIDR_NETS = [
    "10.0.0.0/8",
    "172.16.0.0/12",
    "192.168.0.0/16",
]
