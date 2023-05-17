import os
from pathlib import Path

print(os.getenv('OPENAI_API_KEY'))
maindir = Path(os.getcwd()).parent
print(maindir)
