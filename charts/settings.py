import os

# load a bunch of environment
DEBUG = os.getenv('DEBUG', '').lower() in ['true', '1', 'yes']

NONCE_SECRET = os.getenv('NONCE_SECRET')
REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

SERVICE_NAME = os.getenv('SERVICE_NAME') or 'Charts'
SERVICE_URL = os.getenv('SERVICE_URL') or 'http://localhost:5000'
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL') or 'team@example.com'
API_ROOT = os.getenv('API_ROOT') or '//localhost:5000'
FORMS_API = os.getenv('FORMS_API') or '//formspree.io' # for collecting feedback on the landing page
ASSEMBLY_URL = os.getenv('ASSEMBLY_URL') or 'http://assembly.com'
