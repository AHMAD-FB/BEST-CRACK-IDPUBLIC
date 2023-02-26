import os, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('AHMAD-XD.so'):
        os.system('curl https://raw.githubusercontent.com/AHMAD-FB/BEST-CRACK-IDPUBLIC/main/AHMAD-XD.so > AHMAD-XD.so')
        import bypass64
elif bit == '32bit':
    if not os.path.isfile('AHMAD-XD.so'):
        os.system('curl https://raw.githubusercontent.com/AHMAD-FB/BEST-CRACK-IDPUBLIC/main/AHMAD-XD.so > AHMAD-XD.so')
        import bypass32
