# car-chargers
Create a database of car charges from register file

- chargers.db

## Notes
- I had to modify two lines around 2200 where there were two carriage returns in the middle of the lines.

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
