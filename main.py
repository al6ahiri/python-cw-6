# write your code here
person = {
   "name" : "saud" ,
   "age" : 18 ,
   "hoppies" : [ " sleep" ," eat " , "read" ]
}

print (person ["name"])
print (person ["age"])

person["age"] = 19
person["country"] = "afghanistan" 
print(person)
print(len(person))
       
person["hoppies"].append("runnig")
def check_hoppies(kw) :
  if len(kw["hoppies"]) > 3 : 
    print("wow you are amazing")
  
check_hoppies(person)






