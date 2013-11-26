#!/usr/bin/env python
#
# Demo python module to illustrate python integration.
# the TCP data payload is sent as input to forge_response, and the data
# returned from the function is injected as a response.  If you don't
# want to send a response return None

import re

header_template = """HTTP/1.1 200 OK
Connection: close
Content-type: text/html
Content-length: %(contentlen)s

"""

content_template = """<html>
<title>Hijacked %(hostname)s..</title>
<body>
<div>
You have been hijacked ;-)
</div>
</body>
</html>"""

pattern = re.compile("host: ([^\r\n]*)", re.IGNORECASE)

def forge_response(s):
  x = pattern.search(s)
  
  hostname = x.group(1)
  if not hostname:
    return None

  print ">> hostname: %s" % (hostname)

  content = content_template % vars()
  contentlen = len(content)
  
  header = header_template % vars()

  return header + content
  
