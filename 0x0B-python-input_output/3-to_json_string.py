#!/usr/bin/python3
   """Defines a function 
      To convert a Python object to its JSON representation.
   """
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
