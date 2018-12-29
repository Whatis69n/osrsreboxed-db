# osrsbox-db: Item Database API Tools

This folder hosts the code used to interact with the item database. This code is tested and works pretty well for a short and simple implementation. 

## API Classes

#### AllItems.py

- Purpose: Class to handle and store all items in the database
- This script takes one command line argument:
    - `-i ..\docs\items_complete.json`: This file should be taken from the docs directory
    - `-i ..\docs\items-json`: This directory should be taken from the docs directory
- Requirements:
    - Python 3

#### ItemDefinition.py

- Purpose: Class to handle a single item

#### ItemBonuses.py

- Purpose: Class to handle a single item bonuses

#### ItemEquipment.py

- Purpose: Class to handle a single item equipment metadata

## API Tools

Any tool in this folder that is identifiable as it starts with a lowercase letter `c_`. This stands for _caller_ and should help identify the actual tools available and tell them apart from the API classes. The following tools are currently available:

- `c_PrintItemNames.py`: Print the names of every item in the database
- `c_DetermineNewItems.py`: Part of the database update workflow. Put new `items_itemscraper.json` in the same dir, and compare to current database contents to determine new, removed and changed items
- `c_GenerateItemsCompleteFile.py`: Part of the database update workflow. Creates a single `items_complete.json` file after `items-json` is updated
- `c_GenerateItemSlotFiles.py`: Part of the database update workflow. Creates JSON files for different equipment slots