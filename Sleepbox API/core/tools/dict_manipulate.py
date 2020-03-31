def supress_temp(obj):
    attrs = vars(obj)
    keys = attrs.keys()
    temp = [attrs.pop(key) if key.startswith('_') else None for key in keys]
    del temp
    print(attrs)

    return attrs