#!/usr/bin/python3
""" class User that inherits from BaseModel"""

import models


class User(models.base_model.BaseModel):
    '''defining user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
