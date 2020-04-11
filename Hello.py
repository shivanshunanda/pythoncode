##traditional print command
print( "Hello Shivanshu");
## assigning non data types variables
age = 29 ;
name = "Shivanshu" ; 
balance = 89.90; 
## printing the varaiables
print(age);
print(name);
print(balance);

##lets see the mathematical operators 
num1= 15;
num2 = 3; 
## since variabels are not typed ,we need to cast explicity with str() function
print(str(num1+num2) + "should be 18");
print(str(num1-num2) + "should be 12");
print(str(num1* num2) + "should be 45");
print(str(num1/num2) + "should be 5");
print(str((num1+num2)/num2 )+ "should be 6");
print(str((num1+num2)//num2) + "should be 6");
print(str((num1+num2)/num2) + "should be 6");

## relational 
print(num1>num2);
print(num1<num2);
print(num1== num2);
print(num1<=num2);
print(num1>=num2);
print(num1!=num2);

#Logical operator

val1 = True; 
val2 = False;

print(val1 and val2);
print(val1 or val2);
print(not val1);

#bitwise operator
print (num1&num2);
print(num1|num2);
print(num1>>2);
print(num1<<2);
print(num1^num2);

##Special Operators : its CASE specific

one = "Shivanshu last name Nanda";
two = "Shivanshu last name Nanda";
three = "SHIVANSHU LAST NAME NANDA";

print ( one is two);
print(one is three);

print ("take a break");

print(one is not three);
print( one is not two ) ; 

print(name  in one ) ; 
print (name not in  three);
 

