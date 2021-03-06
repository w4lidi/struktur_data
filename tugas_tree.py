def binary_tree(x):
    return [x,[],[]]
def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1 :
        root.insert(1, [new_branch, t,[]])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
            root.insert(2, [new_branch, t,[]])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def get_root_val(root):
    return root(0)
def set_root_val(root, new_val):
    root[0] = new_val
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]


x = binary_tree('cuaca')
print(x)
insert_left(x, "hujan")
insert_right(x, "kecerahan")
l = get_left_child(x)
set_root_val(l, 'hujan')
insert_right(x, "angin")
insert_left(x, "lembab")
print("isi dari cabang bagian kiri = ",l)
r = get_right_child(x)
print("isi dari cabang bagian kanan : ",r)
print(x)