import os
from tileTiff import tileTiff

for i in os.listdir('compressed/'):
	tileTiff('compressed/'+i)
