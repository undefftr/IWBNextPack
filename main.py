# IWBPack - A tool to config your IWB in class automaticly
# Copyright (C) 2024 unDefFtr

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, see
# <https://www.gnu.org/licenses/>.

import os
import yaml

def init():
    print('''IWBPack Snapshot 24w42a
Copyright (C) 2024 unDefFtr
This prgram comes with ABSOLUTELY NO WARRANTY, for details, check our GitHub pages.
This is a free software, and you are welcome to redistribute it under certain conditions.''')
    print()

    print("Initializing...")
    if os.path.exists("configs/list.yaml") == False:
        print("Software list not found!")
        print("Please add config file first.")
        print("If you need help, check https://iwbpack.undefined.ac.cn for documentation.")
        os.system("pause")
        exit()
    
    with open("configs/list.yaml", "r") as file:
        softwareList = yaml.safe_load(file)


if __name__ == '__main__':
    init()