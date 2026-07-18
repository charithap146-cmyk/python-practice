#defining the sets
n1={1,3,5,7,9}
n2={9,5,6,8}
wd1={"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}
wd2={"Mon","Tue","Wed"}
#intersection of n1 and n2
intersection=n1&n2
print("intersection of n1 and n2:",intersection)
#difference of n1 and n2(n1-n2)
difference_n1_n2=n1-n2
print("difference of n1 and n2(n1-n2):",difference_n1_n2)
#difference of n2 and n1(n2-n1)
difference_n2_n1=n2-n1
print("difference of n2 and n1(n2-n1):",difference_n2_n1)
#symmetric_difference between n1 and n2
symmetric_difference=n1^n2
print("symmetric difference between n1 and n2:",symmetric_difference)
#checking if wd1 is a superset of wd2
is_superset=wd1.issuperset(wd2)
print("is wd1 a superset of wd2?",is_superset)
#checking if wd2 is a subset of wd1
is_subset=wd2.issubset(wd1)
print("is wd2 a subset of wd1?",is_subset)

