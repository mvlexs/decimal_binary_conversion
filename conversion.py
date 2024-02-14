def start():
    print("Hello, to convert a decimal number into a binary one or vice versa please enter the number you want to convert.")


def check_for():
    try:
        number_to_convert = input("Enter a decimal or binary number: ")
        identifier = ""
        try:
            number_to_convert = int(number_to_convert, 2)
            identifier = "binary"
        except ValueError:
            try:
                number_to_convert = int(number_to_convert, 10)
                identifier = "decimal"
            except ValueError:
                print("Neither decimal nor integer.")
    except TypeError:
        ("Unknown input.")
    finally:
        converter(number_to_convert, identifier)

    
    #TODO check if given input is either dec or bin and proceed/throw error

def converter(number_to_convert, identifier):
    converted_to = ""
    if identifier == "decimal":
        number_to_convert = bin(number_to_convert)
        number_to_convert = number_to_convert.replace('0b','')
        converted_to = "binary"
    elif identifier == "binary":
        number_to_convert = int(number_to_convert)
        number_to_convert = str(number_to_convert)
        converted_to = "decimal"
    else:
        print("An unknown error occured.")
    print("Your " + identifier + " number converted into a " + converted_to + " is: " + number_to_convert + "!")