# Experimenting with datatypes
integer = 90 
floating = 67.54
complex = 90 + 56j; 

print(str(type(integer))  + 'should be int');
print(str(type(floating)) + 'should be float');
print(str(type (complex)) + 'shoud be complex');


#Types of String
name = 'Shivanshu';
decs = "I'm  going to have coffee";
mood = '''let's have some experiment''';

print(type(name));
print(type(decs));
print(type(mood));

print(name);
print(decs);
print(mood);

print(name[4]);
"""del name[3];
TypeError: 'str' object doesn't support item deletion, String is immutable 
"""

""" Index   are two ways 
 0 1 2 3 4 5 6 7 8
 S H I V A N S H U
-9-8-7-6-5-4-3-2-1
"""
extr =name[4];
etrO = name[-5];
print(extr is etrO);

##Slicing of  Strings  using slice object 
shiv = slice(4);  #creates a slice object to substring the string slice(stopping_index)
shiva = slice(-4);
print(name[shiv]);
print(name[shiva]);
#slice(start, stop)
ansh = slice(4,8);
print(name[ansh]);

#Slice(start, stop, increment)
txt = slice(0,9,1) ; 
print(name[txt]);
duplicate = name[txt];
print(duplicate is name);

#String[start: end : increment/step] also used as shortcut for slice 

print(name[0:4] + " should be Shiv");

print(name[4:9] + "  Should be Anshu");

print(name[-1:-9:-2] +" Should be usai");

print(name[:5] + " should be shiva");

#reversal of string
print(name[::-1]);



#LIST Datatpe 

mylist = [] ; 

print(mylist) ; 
print (type(mylist)); 

#append, insert, extend in list 

mylist.append("Shiv"); #appends the element at the end of the list 
mylist.insert(0,"Lord") ;  # insert the lement at specified index
mylist.extend(["addition" , "to" , 1 , "list"]);


print(mylist);
""" List will be indexed same as string 
  0        1         2        3    4    5
['Lord', 'Shiv', 'addition', 'to', 1, 'list']
  -6     -5         -4       -3   -2    -1 

"""

#  printing the element  using index 

print(mylist[2] + " is same as " + mylist[-4]);


print(str(mylist[4]) + " is same as " + str(mylist[-2]));

#print the length

print( len(mylist));

#remove , pop element from the list 
mylist.pop(); #deletes the last from the list 

print(mylist);

mylist.remove(1);  #deletes the specific

print(mylist);


"""
Tuple is an ordered collection of Python objects much like a list.
The important difference between a list and a tuple is that tuples are immutable.
""" 
mytuple =("hi","hello", "how"); 
print(mytuple);
print (type(mytuple));
tuple2 =("are" ,"you");
tuple3 =(mytuple , tuple2);
print(tuple3);

#update & delete wil not work with tuple as its immutable
"""
mytuple[-1]= "let";
del mutuple[0];
"""

#Boolean
mytrue =True; 
myfalse = False; 
print(type(mytrue));

#SET 
"""
Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.
Sets can be created by using the built-in set() function with an iterable object or a sequence by 
placing the sequence inside curly braces {}, separated by ‘comma’
"""

set1 = set() ;

setOfStrings = set("hellohowareyou");

setOfList = set(["Shiva" , "Anshu", "Shiva"]);

print( "***********************SET***********");
print(set1);
print(setOfStrings);
print(setOfList);

mixedSet = set() ; 
#Update & Add in SET 

mixedSet.add(34);
#mixedSet.update( True);  boolean object is not iterable
mixedSet.add(True)
mixedSet.add("String");
#mixedSet.add(["list", "of", "list"]);  -- unhashable type 

mixedSet.update(["list", "of", "list"]); 
mixedSet.add((67, 78, "tuple"));
mixedSet.update(setOfList);
#mixedSet.add(setOfStrings); -- unhashable Type

"""  All of Python's immutable built-in objects are hashable & since list is not immutable cant be added.
 Add will be used for built in , non iterable  and  immutable and hashable elements like , int , boolean , String , tuple.
 List and Sets cant be added.()
Update will be used for two or more elements, should be iterable String, tuple , list and Sets
"""
mixedSet.update("My" , "hero", "my" , "dad" );


print(mixedSet);

#Accessing Set 

for i in mixedSet:
 print(i , end= " ");
print("\n");
for j in setOfStrings:
  print(j, end = " ");
print("\n");
# Clear, pop , remove and discard 
"""
Elements can be removed from the Set by using built-in remove() function but a KeyError arises if element doesn’t exist in the set.
To remove elements from a set without KeyError, use discard(), if the element doesn’t exist in the set, it remains unchanged.
To remove all the elements from the set, clear() function is used.
Pop()  removes only the last element of the set. I
If the set is unordered then there’s no such way to determine which element is popped by using the pop() function.
"""

mixedSet.remove(True)
#mixedSet.remove("Hello");   KeyError: 'Hello' as String is not present
mixedSet.discard("Hello"); 

print(mixedSet);

mixedSet.pop();
print("After Popping the last element ")
print(mixedSet);

mixedSet.clear();
print("After clear medthod")
print(mixedSet);


"""
Dictionary can be considered as a map. Dictionary holds key:value pair
"""

myDict = {}; #creating an empty dictionary 

myDict = {1:"hello", 2:"Hi", 3:"How" , "last": "last"};

print(myDict);
myDict["list"] =[3, 5 , 7]; 
myDict["tuple"]=("tuple1", "tuple2", " tuple3");

print(myDict);

myDict["set"]= setOfStrings;

print(myDict);

# Print the values using key & get 

print(myDict["tuple"]); # using the key name 

print(myDict.get("list")); # using get method 

"""pop()Removes and returns an element from a dictionary having the given key.
popitem()Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
"""

myDict.pop("list");

print(myDict);

myDict.popitem();
print(myDict);





