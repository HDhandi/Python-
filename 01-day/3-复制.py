file_name = input('请输入要复制的文件名称')
old_dile = open(file_name,'r')
content = old_dile.read()

position = file_name.rfind('.')
file_name[0:postion:]
file_name[position:]

new_file = open(file_name+'复制'+'1.txt','w')
new_file.wrien(contert)


old_file.close()
ner_file.close()
