to_addr = ["9176833080apu@gmail.com", "ghosh.santanu30@gmail.com"]
string_1 = "9176833080apu@gmail.com, ghosh.santanu30@gmail.com"

print (",".join(to_addr))  # This will add (,) in between list elements, but this method will
                        # work in a list of string elements

#print ('"' + (",".join(to_addr))+" " + '"')  # This will append append double quote at the begining and end of string

a =  '"' + (", ".join(to_addr))+ '"'     #  '"' + (",".join(to_addr))+ '"'

print(a)

print(type(",".join(to_addr)))

print(to_addr==string_1)

print(([string_1]))

