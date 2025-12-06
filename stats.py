def get_book_test(file_path):
    with open(file_path) as f:
     file= f.read()
    # print(file)
     return file

def wordcount(text):
    arr=text.split()
    return len(arr)


def meat(text):
    char=list(text.lower())
    dict={}
    for ch in char:
        if(ch in dict):
            dict[ch]+=1
        else:
            dict[ch]=1
    return dict

    
def sortit(dick):
    list_of_dicks=[]
    for dics in dick:
        list_of_dicks.append({"char":dics,"nums":dick[dics]})
    list_of_dicks.sort(reverse=True, key=sort_on)
    return list_of_dicks


def sort_on(items):
    return items["nums"]

