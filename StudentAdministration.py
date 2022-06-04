import csv
def w_csv(i_list):
    with open('st_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
           writer.writerow(["Name","Age","Mob_num","E-mail"])
        writer.writerow(i_list)
if __name__=='__main__':
    condition=True
    student_num=1
    
    while(condition):
        st_info=input("Enter the information of the Student#{} in this format(Name age Mob_num E-Mail):".format(student_num))
       
        st_list=st_info.split(' ')
       
        print("\n The Entered Information is-\nName:{}\nAge:{}\nMob_num:{}\nE-Mail:{}"
              .format(st_list[0],st_list[1],st_list[2],st_list[3]))
        check=input("Is the Entered Information is correct?(yes/no):")
        if check=="yes":
            w_csv(st_list)
        
            m_info=input("Enter (yes/no) to enter some more Students information:")
            if m_info=="yes":
               condition=True
               student_num=student_num+1
            elif m_info=="no":
                condition=False
            elif check=="no":
                 print("\n Please re-enter the values:")
    
