import os
from dotenv import load_dotenv
from Instagram import Instagram

load_dotenv()
xuyna = Instagram()

xuyna.login(os.getenv('IG_USERNAME'), os.getenv('IG_PASSWORD'))
xuyna.go_to_profile('azad_sahveledov')
xuyna.send_message('salam')