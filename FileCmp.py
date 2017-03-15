import os
import filecmp

def check_dir(directory):
    sizelist=dict()
    multi_files=[]


    for filename in os.listdir(directory):          #Access all files in the directory
        f=open(directory+'/'+filename)              #Open file
        size=os.path.getsize(directory+'/'+filename) #get size of the file

        try:
            sizelist[size].append(filename)             #Appending files to sizelist based on the size as index
        except:
            sizelist.setdefault(size,[]).append(filename)
        else:
            if size not in multi_files:
                multi_files.insert(size,size)           #Making list of all sizes

    final_ans=dict()
    for file_size in multi_files:
        list_of_files=sizelist[file_size]
        same_files=compare(list_of_files,file_size)      #passing each list of files based on the size of file to compare
        if len(same_files[file_size]):
            final_ans.setdefault(file_size,same_files[file_size])   #inserting the matched files into final_ans dictionary
    ans_files=final_ans.values()
    #group=[]
    #for i in range(0,len(ans_files)):                   #Merging all the matched files into a list (available during first commit)
    #    group+=ans_files[i]

    matches=dict()
    matches.setdefault("Matches",ans_files)
    return matches                                      #Returns the array of matched files


def compare(list_of_files,file_size):               #Compare function takes list of files as input along with the size in order to categorize
    answer=dict()
    for file in range(0, len(list_of_files)-1):
        match=0
        for next_file in range(file+1,len(list_of_files)-file):
            answer.setdefault(file_size, [])
            if filecmp.cmp(directory+"/"+list_of_files[file],directory+"/"+list_of_files[next_file])==True:         #Comparing files
                answer[file_size].append(list_of_files[next_file])
                match+=1
        if match>0:
            if list_of_files[file] not in answer[file_size]:
                answer[file_size].append(list_of_files[file])
    return answer


directory = raw_input("Input Example: /Users/VamshidharReddy/PycharmProjects/FileCmp/files")
print check_dir(directory)