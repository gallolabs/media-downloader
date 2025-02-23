#!/usr/bin/env python3

from qobuz_dl.core import QobuzDL
from json import dumps
import os
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
)

qobuz = QobuzDL(
	quality=int(os.environ['QUALITY']),
	embed_art=True,
	directory='.',
	folder_format='.'
)

print('get_tokens')
qobuz.get_tokens()

print('initialize_client')
qobuz.initialize_client(os.environ['EMAIL'], os.environ['PASSWORD'], qobuz.app_id, qobuz.secrets)

for url in sys.argv[1:]:
	print('Handling ' + url)
	qobuz.handle_url(url)
