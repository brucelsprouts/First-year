def main ():
    my_list = [1,2,3,4,5]
    delimiter = "~"
    print(f"Seperated string: {seperate(my_list,delimiter)}")

def seperate(list, delimiter):
    string = ''
    str_list = [str(i) for i in list]
    for i in range(0,len(str_list)):
        string = string + str_list[i]
        if i != len(str_list)-1:
            string = string + delimiter
    return string

main()