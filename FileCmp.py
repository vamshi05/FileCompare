import os
import filecmp

def check_dir(directory):
    sizelist=dict()
    multi_files=[]


    for filename in os.listdir(directory):
        f=open(directory+'/'+filename)
        size=os.path.getsize(directory+'/'+filename)

        try:
            sizelist[size].append(filename)
        except:
            sizelist.setdefault(size,[]).append(filename)
        else:
            if size not in multi_files:
                multi_files.insert(size,size)

    final_ans=dict()
    for file_size in multi_files:
        list_of_files=sizelist[file_size]
        same_files=compare(list_of_files,file_size)
        if len(same_files[file_size]):
            final_ans.setdefault(file_size,same_files[file_size])
    ans_files=final_ans.values()
    group=[]
    for i in range(0,len(ans_files)):
        group+=ans_files[i]
    matches=dict()
    matches.setdefault("Matches",group)
    return matches


def compare(list_of_files,file_size):
    answer=dict()
    for file in range(0, len(list_of_files)-1):
        match=0
        for next_file in range(file+1,len(list_of_files)-file):
            answer.setdefault(file_size, [])
            if filecmp.cmp(directory+"/"+list_of_files[file],directory+"/"+list_of_files[next_file])==True:
                answer[file_size].append(list_of_files[next_file])
                match+=1
        if match>0:
            if list_of_files[file] not in answer[file_size]:
                answer[file_size].append(list_of_files[file])
    return answer



directory = raw_input("Example: /Users/VamshidharReddy/PycharmProjects/FileCmp/files")
print check_dir(directory)