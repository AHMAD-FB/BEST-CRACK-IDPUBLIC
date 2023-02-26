import os, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('AHMAD-XD'):
        os.system('curl https://raw.githubusercontent.com/AHMAD-FB/BEST-CRACK-IDPUBLIC/main/AHMAD-XD > AHMAD-XD')
        import bypass64
elif bit == '32bit':
    if not os.path.isfile('AHMAD-XD'):
        os.system('curl https://raw.githubusercontent.com/AHMAD-FB/BEST-CRACK-IDPUBLIC/main/AHMAD-XD > AHMAD-XD')
        import bypass32
