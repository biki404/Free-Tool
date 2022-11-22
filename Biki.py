import os, sys
try:
    __import__("cream").menu()
except Exception as e:
    exit(str(e))

