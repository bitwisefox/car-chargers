# car-chargers
Create a database of car charges from register file

- chargers.db

## Notes
- I had to modify two lines around 2200 where there were two carriage returns in the middle of the lines.
- Charge speeds are in three groups
  - less than 7kW - Slow
  - 7-22kW - Fast
  - greater than 22kW - Rapid
- There are 7 connector types
  - Type 2 Mennekes (IEC62196)
  - CCS Type 2 Combo (IEC62196)
  - JEVS G105 (CHAdeMO) DC
  - 3-pin Type G (BS1363)
  - Type 1 SAEJ1772 (IEC 62196)
  - Type 3 Scame (IEC62196)
  - Type 2 Tesla (IEC62196) DC

## Linux
I used the sqlite3 and csv modules built into python. No need to install additonal modules.

https://docs.python.org/3/library/csv.html

https://docs.python.org/3/library/sqlite3.html

## Windows Setup
### Install python
https://www.python.org/downloads/windows/
### Install the mysql connector driver

From command prompt
`C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector-python`
