print("Hello World")


# dictionary of 2 letter ISO 3166 country codes
# and their country names
country_codes = {
    "AF": "Afghanistan",
    "AX": "Aland Islands",
    "AL": "Albania",
    "DZ": "Algeria"
}

# print the country code and country name
for code, name in country_codes.items():
    print(f"The country code for {name} is {code}")

# validate a phone number
def validate_phone_number(number):
    if len(number) != 12:
        return False
    for i in range(0, 3):
        if not number[i].isdecimal():
            return False
    if number[3] != '-':
        return False
    for i in range(4, 7):
        if not number[i].isdecimal():
            return False
    if number[7] != '-':
        return False
    for i in range(8, 12):
        if not number[i].isdecimal():
            return False
    return True

print(validate_phone_number("010-1234-5678"))
print(validate_phone_number("010-123-5678"))


s_name = "I'm a random string"
# remove whitespace from a string
s_name = s_name.replace(" ", "")
print(s_name)




