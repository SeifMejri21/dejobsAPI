import json


def read_json(file_name, local=False, custom_path=''):
    """
    :param finle_name: filename
    :return: data
    """
    if custom_path:
        base = custom_path
    else:
        if local:
            base = 'C:/Users/Administrator/Desktop/'
        else:
            base = 'database/'
    try:
        f = open(base + file_name + '.json')
        data = json.load(f)
        f.close()
    except Exception as e:
        print(e)
        data = []

    return data


def save_json(data, name, local=False, custom_path=''):
    if custom_path:
        base = custom_path
    else:
        if local:
            base = 'C:/Users/Administrator/Desktop/'
        else:
            base = 'database/'
    jsonString = json.dumps(data)
    jsonFile = open(base + name + '.json', "w")
    jsonFile.write(jsonString)
    jsonFile.close()


def chunkify(big_list, chunk_size):
    chunks = [big_list[x:x + chunk_size] for x in range(0, len(big_list), chunk_size)]
    return chunks