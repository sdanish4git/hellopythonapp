# Copyright (c) 2015 Pepijn Oomen <oomen@piprograms.com>
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "Hello Python World edited!\r\n", 200, { 'Content-Type': 'text/plain' }

@application.route('/test')
def showForm():
    self.response.headers["Content-Type"] = "text/html"
    self.response.write("""
          <html>
            <head><title>Enter your name...</title></head>
            <body>
              <form action="/welcome" method="post">
                <input type="text" name="my_name"><br>
                <input type="submit" value="Sign In">
              </form>
            </body>
            </html>""")
            
@application.route('/welcome')
def display():
    username = self.request.get("my_name")
    welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(username)
    self.response.headers["Content-Type"] = "text/html"
    self.response.write(welcome_string)

if __name__ == '__main__':
    application.run(debug = True)
