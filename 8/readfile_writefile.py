with open('text_file.txt') as f:
    list_from_file = f.readlines()
    print('# cat text_file.txt:\n' + ''.join(list_from_file))

f2 = open("text_file_reverted.txt", "w")
f2.writelines(''.join(list_from_file)[::-1])
f2.close()

with open('text_file_reverted.txt') as fr:
    list_from_file_reverted = fr.readlines()
    print('# cat ext_file_reverted.txt:\n' + ''.join(list_from_file_reverted))






