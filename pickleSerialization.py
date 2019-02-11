import jsonpickle


########################################################################
class Car(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.wheels = 4
        self.doors = 5

    # ----------------------------------------------------------------------
    def drive(self):
        """"""
        print("Driving the speed limit");


if __name__ == "__main__":
    my_car = Car()
    serialized = jsonpickle.encode(my_car)
    print(serialized);

    my_car_obj = jsonpickle.decode(serialized)
    print(my_car_obj.drive());

    # JS JSON STRINGIFY PARSER
    # test_variable = {"key": "value", "array": ["item1", "item2"]}
    # JSON.parse(test_variable);
    # JSON.stringify(test_variable);



json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

import json
parsed_json = json.loads(json_string)

print(parsed_json['first_name'])

d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}

print(json.dumps(d) + "\n")



print("Marshal: ");


data = {12:'twelve', 'feep':list('ciao'), 1.23:4+5j, (1,2,3):u'wer'}

import marshal
bytes = marshal.dumps(data)

redata = marshal.loads(bytes)

print("Redata : " + str(redata))
print("Bytes : " + str(bytes))