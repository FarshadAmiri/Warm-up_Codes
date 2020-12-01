import os
def list_folders(path):
    folders = []
    for name in os.listdir(path):
        folders.append(name)
        print(folders)
    return folders 

subfolder_dir = str(input("Enter the folder's directory:  "))
#'C:/Users/famir/Desktop/یادگیری ماشین - فرادرس - Copy'
L = list_folders(subfolder_dir)


def modify_faradars():
    for i in L:
        dir1 = str('%s/%s' % (subfolder_dir,i))
        L1 = list_folders(dir1)
        dir2 = str('%s/%s' % (dir1,L1[0]))
        L2 = list_folders(dir2)
        if 'Courses List.url' in L2:
            os.remove('%s/Courses List.url' %dir2 )
        if 'FaraDars.org.url' in L2:
            os.remove('%s/FaraDars.org.url' %dir2 )
        if 'Free Courses.url' in L2:
            os.remove('%s/Free Courses.url' %dir2 )
        if 'License.pdf' in L2:
            os.remove('%s/License.pdf' %dir2 )
        if 'Recent Courses.url' in L2:
            os.remove('%s/Recent Courses.url' %dir2 )
        if 'Videos' in L2:
            dir3 = str('%s/Videos' % dir2)
            L3 = list_folders(dir3)
            if len(L3) > 1:
                c = 1
                for j in L3:
                    os.rename('%s/%s' %(dir3,L3[c-1]),'%s/%s_%i.wmv' %(dir1,i, c))
                    c += 1
            else:
                os.rename('%s/%s' %(dir3,L3[0]),'%s/%s.wmv' %(dir1,i))
        L2_2 = list_folders(dir2)
        c2=1
        for k in L2_2:
            os.rename('%s/%s' %(dir2,L2_2[c2-1]),'%s/%s' %(dir1,L2_2[c2-1]))
            c2 += 1
        L1_2 = list_folders (dir1)
        if L1[0] in L1_2:
            os.removedirs('%s/%s' %(dir1,L1[0]))
        if 'Videos' in L1_2:
            os.removedirs('%s/Videos' %dir1)

            
            
modify_faradars()