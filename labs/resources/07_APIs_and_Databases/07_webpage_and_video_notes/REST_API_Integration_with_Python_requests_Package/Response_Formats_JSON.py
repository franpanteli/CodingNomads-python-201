"""Response formats: JSON
    -> types of data format
        -> JSON, HTML or XML formats
        -> HTML <- how information is returned to a user
        -> JSON / XAML <- when we request extra information

    -> JSON
        -> JSON <- JAVASCRIPT OBJECT NOTATION
        -> a data interchange format
        -> this is based on a subset of JS
        -> this is language independent
        -> IT IS AN INTERCHANGE LANGUAGE

        -> example:
            {
                "first_name" : "Joseph",
                "last_name" : "Gemarsten",
                "email" : "jo@demo.com"
            }

        -> it is built on a collection of name-value pairs
            -> this is mostly shown as an array / list in other languages
            -> IT IS INTERCHANGEABLE WITH OTHER LANGUAGES
            -> objects {}
            -> KEY: VALUE
            -> a value can be a string in double quotes, and the structures can be nested
            -> a string is like a c or java string
                -> hexidecimal formats aren't used

        -> JSON maps to the user class in Java:
            public class User {
                String first_name;
                String last_name;
                String email;
            }

        -> or to the class in Python:
            class User:
                def __init__(first_name, last_name, email):
                    self.first_name = first_name
                    self.last_name = last_name
                    self.email = email

        -> example
                {
                    "users" :
                    [
                        {
                            "first_name" : "Joseph",
                            "last_name" : "Gemarsten",
                            "email" : "jo@demo.com"
                        },
                        {
                            "first_name" : "Daniel",
                            "last_name" : "Gemarsten",
                            "email" : "dan@demo.com"
                        },
                        {
                            "first_name" : "Lillian",
                            "last_name" : "Gemarsten",
                            "email" : "lilly@demo.com"
                        }
                    ]
                }

                -> this is a collection of User objects
                -> square brackets are for collections / an array

        -> this maps to the following JS class
            public class JsonExample {
                // User being the class created just above
                User[] users;
            }

        -> JSON CAN STORE INFORMATION THAT CAN BE MAPPED DIRECTLY TO A CLASS
        -> this is a collection of key-value pairs that can map to or from different coding languages
        -> PYTHON HAS A JSON PACKAGE
        -> it's a data interchange language
        -> the library has marshal and pickle modlues
        -> YOU IMPORT THE json module into Python
        -> it has a json.dumps() method
        -> this can be used to do string io
            -> from io import StringIO
            -> and then a json.dump
            -> io.getvalue()
        -> decoding JSON
            -> json.loads()
            -> you can also specialise JSON object decoding
                -> defining a function speficially for decoding JSON objects, for instance, by converting them into dicitonaries
                -> the json.loads method is used in this example:
                    import json
                    def as_complex(dct):
                        if '__complex__' in dct:
                            return complex(dct['real'], dct['imag'])
                        return dct

                    json.loads('{"__complex__": true, "real": 1, "imag": 2}',
                        object_hook=as_complex)

                    import decimal
                    json.loads('1.1', parse_float=decimal.Decimal)
            -> you can then use json.tool from the shell to validate and pretty-print
                -> echo in Bash
                -> JSON is a subset of YAML 1.2
            -> json.dump
                -> IT ALWAYS PRODUCES STR OUTPUT
                -> using a positive integer of indents will indent that many elements on the level
                -> json encoder can otherwise be used
                -> json is not a framed protocol
            -> json.dumps
                -> the arguments of this are the same as with json.dump
                -> THE OUTPUT IS A STRING
            -> json.load()
                -> object hook can be used to call elements in a form other than a dicitonary
                    -> this can be used for custom decoders, e.g for collections
                    -> this will remember the order of insertion
                -> infinity NaN can be used to raised an exception if numbers are encountered
                -> there are different deocoder errors which can be raised
            -> json.loads()
                -> the arguments are the same as in json.load()
            -> encoders and decoders
                -> .JSONDecoder()
                    -> this performs translations
                    -> if a dictionary is used, then other elements can be used instead of this
                    -> some inputs, e.g collections, remember the order which the input was entered in
                        -> this is what the decoder can rely on
                        -> this can also be used for other datatypes
                        -> the string of every JSON
            -> raw_code(s)
                -> to decode a JSON object
                -> this may have too much data at the end
            -> .JSONEncoder()
                -> this can take many different datatypes in its arguments
                -> this method can take many different arguments
                -> a TypeError is raised if the datatype of the argument is not specified
            -> encode()
                -> return a JSON string representation of a Python data structure
            -> iterencode()
                -> encode the given object, and yield each string representation as avaliable
            -> exceptions
                -> infinite and NaN values are acceptable in JS, but not JSON
            -> character encodings
                -> UTF-8, 16 or 32 has to be used
"""