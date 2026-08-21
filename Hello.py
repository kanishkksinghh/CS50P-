#ask user for their name
name =  input("What's your name?") # input function


#remove the extra whitespace
name = name.strip()

#it captialize the all text
name = name.capitalize()

#Say hello to the user 
#print("Hello",name)  #print funtion
print(f"Hello, {name}")
