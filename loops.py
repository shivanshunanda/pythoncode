##While loops 
mylist=["hello", "hi", "how", "are"];

while mylist:
 print(mylist.pop());
 
i =0
while   i<5 : i = i+1 ; print(i);

##control statements; 
#continue: It returns the control to the beginning of the loop
#break : It brings control out of the loop

breakvar = 9 

continuevar = 7;

k =0 
while k<78 :
 print ( k); 
 k= k+1; 
 if(k==continuevar):
  print("in the condition of continue");
  continue;
 if(k==breakvar):
  print("loop is going to break as reached break condition")
  break;
 print("double of the  k is " + str(2*k));
 

#pass : We use pass statement to write empty loops. 

while k<78: 
 k = k+1 ; 
 pass; 
print("value of K is " + str(k));

#while loop with else 

while k<100 :
 k= k+1;
 if(k<90):
  pass;
 print ("k should be 89  " +str(89)); 
else :                    # else block will be executed as there is no break statement
 print("K is equal to 100  " + str(k));
 
 
while k<105 :
 k= k+1; 
 if(k==102):
  break; 
else :   # else block will not be executed as there is no break statement
 print("else block of while");

print("end of while loop concept")


#FOR Loop
mylist = ["new" , "list" , "as" , "pop", "function", "delted" , "elements"];
for element in mylist:
  print(element);
  
myStr = "SHIVANSHU";

for mychar in myStr :
  print(mychar);

mytuple = ( "tuple1" , 23, "hero" , [67, 89 ,  80]);

for mix in mytuple:
 print(mix);
 
myset = set([ 2, 4 , 6, 8 , 10 , 10]);

for num in myset:
 print(num);


mydict = {1:"one", 2:"two"}

for count in mydict:
 print( "%d %s "%(count, mydict[count]));

#continue, break , pass and for-else work same as while 

"""range :  allows user to generate a series of numbers within a given range.
1) start: integer starting from which the sequence of integers is to be returned
2) stop: integer before which the sequence of integers is to be returned.
3) step: integer value which determines the increment between each integer in the sequence
 range(start, stop , step)
 ******
 The step value must not be zero. If a step is zero python raises a ValueError exception.
 ****** 
"""

for num in range(9):
 print (num , end =" ");
 
print() ;

for even in range(2 , 18 , 2):
 print(even, end= " ");
print();
# Python range() function doesn’t support the float numbers.
"""
for fai in range(3.5):
 print(fail ,end =" ");
"""

"""A sequence of numbers is returned by the range() function as it’s object that can be accessed by its index value. 
Both positive and negative indexing is supported by its object"""

nums = range(10); 

print(nums[4]);

print(nums[-1]);
