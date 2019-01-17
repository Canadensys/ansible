#!/usr/bin/python
# Run dropboxd and get the url
from subprocess import Popen, PIPE
import re
process = Popen(["timeout", "5", "./.dropbox-dist/dropboxd"], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
error_sentence = 'Sorry we can\'t have access to dropboxd\the error is'+str(err)+'\n'
if err is None:
    s = "(This computer isn't linked to any Dropbox account...\\nPlease visit https:\/\/www.dropbox.com\/cli_link_nonce\?nonce=\w* to link this device.)"
    p = re.match(s, output)
    if p:
        print p.groups()[0]
    else:
        print error_sentence
else:
    print error_sentence
