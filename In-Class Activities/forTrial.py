

print("Hello")

#will begin at 0 and will print 1000 times
for n in range(10):
    print("{0}".format(n), "Howdy")
print("End of the first for loop.\n++++++++++++++++++++")

#keep doing this until something happens
while n <= 10:
    print("{0}".format(n), "Howdy")
    n = n+1
    print ("End of the second for loop")
    print("{0}".format(n), "Value of n")

#erica - 0, hannah - 1, john - 2
list_of_names = ["Erica", "Hannah", "John", "MJ"]
print(list_of_names[0])

find_name = "MJ"
#as long as there is a name in list_of_names print the name
for name in list_of_names:
    #see if name is included
    if find_name.lower() == find_name.lower():
        print("found at" + "{0}".format(n), "location", format(name))
    print("found")

