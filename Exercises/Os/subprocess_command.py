# subprocess is much better way to execute system commands

import subprocess

subprocess.call('date')  # This is not storing anything to a variable. It will directly disply the output to termianal

subprocess.call('ping google.com')  # This is not storing anything to a variable. It will directly disply the output to termianal
