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
import csvtojson as c2j
data = c2j.load('./file.csv')

# print the rows in json format
for item in data:
    print item
```
