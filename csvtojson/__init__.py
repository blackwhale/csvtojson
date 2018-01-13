from csvtojson import csvtojson

def load(filename, **kargs):
    data = csvtojson(filename, **kargs)
    return data.convert()
