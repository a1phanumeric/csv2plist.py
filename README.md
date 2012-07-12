csv2plist.py
============

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

### ABOUT
Creates a plist array from a list of records in a CSV OR a plist dictionary from a multi-column CSV

### USAGE

Usage is simple, just invoke from the command line:

``python csv2plist.py csvfile [output plist file] [type]``

output plist file is optional, if unused it'll create a plist in the same directory as the CSV
type can be 'array' or 'dict' (default is 'array').

If you're creating a dictionary, the first row in the CSV will be used as the keys.

### EXAMPLES

``python csv2plist.py mycsv.csv``
outputs: mycsv.plist in the same directory as mycsv.csv

``python csv2plist.py mycsv.csv myplist.plist``
outputs: myplist.plist in the same directory as mycsv.csv

``python csv2plist.py mycsv.csv myplist.plist dict``
outputs: myplist.plist in the same directory as mycsv.csv but this time creates a dictionary.

