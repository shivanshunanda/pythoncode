#Lets play with  input output 
 
name = input("Enter  our name ") ; 
age  = input("Enter your AGE ") ; 

print(name); 
print (type(name));

print(age);
print(type(age));
#$ input always read the daat as String
nextyear = int(age)+1;
print(type(nextyear));
print (str(nextyear) + " will be ur age next year");

#sep='' is just short form of seperator
print ("Shivanhu" , "Nanda", sep='_');
print('A' , 'B' ,'C', sep= '@');
#end ='' will end the string with args pass in end
print( 'Test' , end = "#");
print('Python');

print("Happy Coding!")
  
