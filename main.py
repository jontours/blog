#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

form = """
    <form method="post" action="/textHandler">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(kwarg)s</textarea>
      <br>
      <input type="submit">
    </form>"""

class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.out.write(form % {'kwarg':""})

class TextHandler(webapp2.RequestHandler):
    def post(self):
        text = self.request.get("text")
        text = rot13(text)

        self.response.out.write(form % {'kwarg':text})
def rot13(text):
    s = ""
    list = []
    indexIntoTable = 65
    lettersInAlphabet = 26
    for c in text:
        x = ord(c)
        if x > 64 and x < 91:
            x = indexIntoTable + (x + lettersInAlphabet/2 + indexIntoTable) % lettersInAlphabet
        elif x > 96 and x < 123:
            x = (indexIntoTable + 32 + 1) + (x + indexIntoTable + 32) % lettersInAlphabet
        list.append(chr(x))
    #for stuff in list:
    #    s = (s + chr(stuff) + 256) % 256
    for x in list:
        s += x
    return s

app = webapp2.WSGIApplication([('/', MainHandler),('/textHandler',TextHandler)],
                              debug=True)
