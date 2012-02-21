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

csv2plist.py
============

#### ABOUT
Creates a plist array from a list of records in a CSV (using the first column only). Will soon allow for creating of dictionaries - but that's not implemented yet.

#### USAGE

Usage is simple, just invoke from the command line:

``python csv2plist.py csvfile [output plist file] [type]``

output plist file is optional, if unused it'll create a plist in the same directory as the CSV
type is going to be used for 'array' or 'dict'. At the moment it always defaults to 'array' so you can completely ignore this parameter.

#### EXAMPLES

``python csv2plist.py mycsv.csv``
outputs: mycsv.plist in the same directory as mycsv.csv

``python csv2plist.py mycsv.csv myplist.plist``
outputs: myplist.plist in the same directory as mycsv.csv

