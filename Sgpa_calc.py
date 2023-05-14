print("\t\tWelcome")
print("\nGive the following details to calculate your sgpa")
theory=[]
sub=[]
lab=[]
crd_t=[]
lab_s=[]
gd_ptr=[]
crd_l=[]
gd_ptr_l=[]
n=int(input("\n\nEnter number of theory subjects: "))
for i in range(n):
    ms=[]
    ss=input(f"\nEnter the name of the theory subject {i+1}: ")
    sub.append(ss)
    ms.append(ss)
    cr=int(input(f"Enter the credits of the {sub[i]}: "))
    crd_t.append(cr)
    ms.append(cr)
    ms.append(int(input(f"Enter the average mid sem marks of the {sub[i]} (out of 20): ")))
    ms.append(int(input(f"Enter the quiz assignment and prof marks combined of the {sub[i]} (out of 20): ")))
    ms.append(int(input(f"Enter the expected end sem marks of the {sub[i]} (out of 50): ")))
    theory.append(ms)

m=int(input("\n\nEnter how many labs you had this semester: "))
for i in range(m):
    lab_marks=[]
    ls=input(f"\nEnter the name of the lab {i+1}: ")
    lab_s.append(ls)
    lab_marks.append(ls)
    cd=int(input(F"Enter the credits of the {lab_s[i]} lab: "))
    crd_l.append(cd)
    lab_marks.append(cd)
    lab_marks.append(int(input(f"Enter the expected viva marks of {lab_s[i]} (out of 60): ")))
    lab_marks.append(int(input(f"Enter the expected sbmp marks of {lab_s[i]} (out of 20): ")))
    lab_marks.append(int(input(f"Enter the expected lab file marks of {lab_s[i]} (out of 20): ")))
    lab.append(lab_marks)
print(theory)
print(lab)

for i in range(n):
    crd=theory[i][1]
    tm=theory[i][2]+theory[i][3]+theory[i][4]
    if(tm>90):
        pt=10
    elif(tm>80 and tm<=90):
        pt=9
    elif(tm>70 and tm<=80):
        pt=8
    elif(tm>60 and tm<=70):
        pt=7
    elif(tm>50 and tm<=60):
        pt=6
    elif(tm>40 and tm<=50):
        pt=5
    elif(tm>30 and tm<=40):
        pt=4
    ptr = pt*crd
    gd_ptr.append(ptr)
    

for i in range(m):
    crd=lab[i][1]
    tm=lab[i][2]+lab[i][3]+lab[i][4]
    if(tm>90):
        pt=10
    elif(tm>80 and tm<=90):
        pt=9
    elif(tm>70 and tm<=80):
        pt=8
    elif(tm>60 and tm<=70):
        pt=7
    elif(tm>50 and tm<=60):
        pt=6
    elif(tm>40 and tm<=50):
        pt=5
    elif(tm>30 and tm<=40):
        pt=4
    ptr = pt*crd
    gd_ptr_l.append(ptr)
    



final_crd= sum(crd_l) + sum(crd_t)
p=sum(gd_ptr) + sum(gd_ptr_l)
cgpa=p/final_crd
print(cgpa)
print("Your sgpa will be in between ", cgpa-0.2, " and ", cgpa+0.2)
