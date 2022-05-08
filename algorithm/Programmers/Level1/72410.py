def solution(new_id: str):
    # 1
    new_id = new_id.lower()
    # 2
    id_len = len(new_id)
    tmp = []
    for i in range(id_len):
        if new_id[i] in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            tmp.append(new_id[i])
    new_id = ''.join(tmp)
    # 3
    while new_id.count('..'):
        new_id = new_id.replace('..', '.')
    # 4
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5, 7
    if not new_id:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
