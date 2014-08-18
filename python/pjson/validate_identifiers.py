#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

# Written by Alan Viars
import json, sys, datetime, re
from choices import STATES



def validate_identifier_list(l, enumeration_type):
    errors = []
    primary_count  = 0
    max_values = {
        'state'        : 2,
        'code'         : 2, 
        'issuer'       : 150, 
        'identifier'   : 20, 
        }
    for d in l:
    
        identifer_string = "%s %s %s issue by %s" % (d['identifier'],
                                            d['code'], d['state'],
                                            d['issuer'])

        
        for k in max_values.keys():
            if d.get(k):
                if max_values[k] < len(d.get(k)):
                    error = "%s : %s max allowable length %s." % (identifer_string, k, max_values[k])
                    errors.append(error)
    
    
        #check for required information
        if d.get('code') not in ("", "01", "02", "04","05", "06", "07", "08"):
            error = "%s : code  is not in ['', '01', '02', '04','05', '06', '07', '08']" % d.get('code')
            errors.append(error)
            
        #if state is provided then it should be valid.
        if d.get('state') and d.get('state') not in STATES:
            primary_count += 1
    
    return errors