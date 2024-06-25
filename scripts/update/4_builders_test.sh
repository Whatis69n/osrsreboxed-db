#!/bin/bash
: '
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Run the builders.

Copyright (c) 2021, PH01L

###############################################################################
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
###############################################################################
'
odb=$(cd ../..; pwd)

export PYTHONPATH="$(dirname "$(dirname "$(pwd)")")"

cd $odb
py -m venv venv
source venv/bin/activate

echo -e ">>> Testing item database builder"
cd $odb/builders/items/
py builder.py --test=True

echo -e ">>> Testing monster database builder"
cd $odb/builders/monsters/
py builder.py --test=True
