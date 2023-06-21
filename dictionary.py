phone_number=(input("Phone: "))
output=""
digits_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
for number in phone_number:
   output+= digits_mapping.get(number,"!")+" "
print(output)


# customer={
#     "name":"Amal Shalabi",
#     "age":30,
#     "is_verified":True
# }
# customer["name"]="amal sh"
# customer["birthdate"]="Jan 1 1980"
# print(customer["birthdate"])