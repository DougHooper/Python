# declare two values
a = 5
b = 10

"""
    single alternative decisions

        if statements
        
        '''
            VB:
            If condition Then
                statement(s)


        '''
        

     dual alterantives

        if / else statemetns
        
    
    multiple alternatives

        if / else if statements

        '''
            VB:
            if condition Then
                statement(s)
            ElseIf condition Then
                statement(s)
            Else    
                statement(s)
            End If
        '''

        '''
            Python:
            if condition: 
                    statement(s)
            elseif condition:
                statement(s)
            else:
                statement(s)
        '''

    Relational operators in Python: 

    > greater than
    < less than
    >= greater than or equal to 
    <= less than or equal to
    == is equal to (do not confuse with single =)
    ! not (changes tru/false)
    != is not equal to 
    and - logical and
    or - logical or
    
"""
# if statement
if a > b:
        print(f"{a} is greater than {b}")

#if / else statement
if a == b:
        print(f"{a} is equal to be")
else:
        print(f"{a} is not equal to {b}")

#if else if statement
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{a} is equal to {b}")
else: 
        print(f"{a} is equal to{b}")

#if with !=
if a != b:
    print(f"{a} is not equal to {b}")

flag = True

if not flag:
    print("Something")
