List_Of_Given_Numbers = []

Input = input()

String_Given_List = Input [ 1 : -1 ]
List = String_Given_List.split( "," )

for i in List:
    List_Of_Given_Numbers.append ( int ( i ) )
extval, final_answer = [], "" 
l = len ( str ( max ( List_Of_Given_Numbers ))) + 1
for i in List_Of_Given_Numbers :
    temp = str ( i ) * l  
    extval.append (( temp [ : l : ] , i ))  
    extval.sort ( reverse = True )  
for i in extval:  
    final_answer += str ( i [ 1 ] )


    
print(final_answer)
