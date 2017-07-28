# -*- coding: utf-8 -*-

import os
from odoo import models, fields, api, _



class testcase(models.Model):
    def meth(self):
        rec=self.env['sale.order']
        for i in rec:
            print i.name
            return i.name
a= testcase()
print a
print a.meth()
print getattr(a,'meth')