csvtojson
==========

This tool is to convert a csv file into new line delimited json format.
A data type auto-detection is implemented so that the schema and/or data type of a column will be auto-detected.
The supported data types are string, numbers (float and integer), and boolean.

Install
----------
pip install csvtojson

Usage
----------

```python
# auto-detect schema
from csvtojson import csvtojson
c2j = csvtojson('./file.csv',
                leadingrow=True)

# print the rows in json format
for row in c2j.convert():
    print row

# write into a file
with open('./output.json', 'wb') as f:
    c2j.write(f)
```
