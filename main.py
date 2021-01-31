
import numpy as np
print(np.__version__)

from replit import db
db["key"] = "value"
value = db["key"]
del db["key"]
