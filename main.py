file = open('data.txt', 'r')
file_content = file.read()

file.close()
print(file_content)

user_name = input("enter username: ")
file_write = open('data.txt', 'w')
file_write.write(user_name)
file_write.close()

file = open('data.txt', 'r')
file_content = file.read()

file.close()
print(file_content)
