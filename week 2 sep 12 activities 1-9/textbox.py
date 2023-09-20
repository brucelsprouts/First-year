#Activity 7: Textbox
text = input("Input your text: ")

width = len(text)
width = int(width)

print('**' + '*'*(width) + '**')
print('* ' + ' '*(width) + ' *')

print('* ' + text + ' *')

print('* ' + ' '*(width) + ' *')
print('**' + '*'*(width) + '**')