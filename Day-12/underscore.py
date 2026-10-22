# main.py
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from utils import *

# #from utils import *


public_var = "Accessible"
_internal_var = "Hidden from wildcard"


print(public_var)    # Works fine!
print(_internal_var) # ❌ Raises NameError: name '_internal_var' is not defined


