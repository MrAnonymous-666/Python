customer = {
    "name" : "John Smith",
    "age" :  30,
    "is_verified" : True

}
print(customer["name"]) # OR
print(customer.get("name")) 
print(customer.get("birthdate", "Jan 1, 1990")) # Default value if key doesn't exist


# Exercise

phone = input ("Phone: ")
digits_mapping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
output = ""
for ch in phone :
    output += digits_mapping.get(ch, "!") + " "

# Emoji converter

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😀"
}
output = ""
for word in words:
    output += emojis.get(word, word ) + " "
print(output)