import os, sys
try:
    __import__("libbiki").menu()
except Exception as e:
    exit(str(e))
