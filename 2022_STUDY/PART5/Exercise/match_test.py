#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
def fun(subject):
    match subject:
        case 400:
            return 'bad request'
        case 404:
            return 'not found'
        case 418:
            return "I'm a teapot"
        case 401 | 402:
            return 'not allowed'
        case _:
            return 'Error!'


print(fun(401))
