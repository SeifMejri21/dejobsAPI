import json
import sys


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


def sql_to_dict(sql_data, labels, type=1):
    """
    :param sql_data:
    :param labels:
    :param type: type 2 : [{'a': a, 'b':a}, ....], type 1 : {'a': [...], 'b':[...]}
    :return:
    """
    if type == 2:
        list_of_dict = []
        for s in sql_data:
            assert len(s) == len(labels)
            dicti = {}
            for el, l in zip(s, labels):
                dicti[l] = el
            list_of_dict.append(dicti)
    else:
        list_of_dict = {}
        for l in labels:
            list_of_dict[l] = []
        for s in sql_data:
            assert len(s) == len(labels)
            for el, l in zip(s, labels):
                list_of_dict[l].append(el)
    return list_of_dict


def set_env():
    if sys.platform == 'win32':
        env = 'local'
    else:
        env = 'prod'
    return env
