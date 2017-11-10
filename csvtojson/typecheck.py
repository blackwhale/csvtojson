def typecheck(data):
    if data == '':
        return 'none'

    checks = [check_bool,
              check_int,
              check_float]

    for check in checks:
        t = check(data)
        if t:
            return t
    return 'string'


def check_float(data):
    try:
        fdata = float(data)
    except:
        return None
    if data == str(fdata):
        return 'float'
    return None


def check_int(data):
    try:
        idata = int(data)
    except:
        return None
    if data == str(idata):
        return 'integer'
    return None


def check_bool(data):
    if data.lower() in ['true', 'false']:
        return 'boolean'
    return None
