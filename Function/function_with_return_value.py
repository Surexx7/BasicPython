def add (a,b):
    sum=a+b
    return sum

output= add(4,5)
print(output)

#converting name in title cas

def format_name(f_name,l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    print(f"{formatted_f_name} {formatted_l_name}")

format_name("suresh", "SHAHI")

#with return value
def format_name(f_name,l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return (f"{formatted_f_name} {formatted_l_name}")

print(format_name("suresh", "SHAHI"))