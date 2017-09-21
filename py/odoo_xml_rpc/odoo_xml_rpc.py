#!/usr/bin/env python2
import xmlrpclib

#db = 'jod'
#user = 'admin'
#password = 'admin'
#uid = xmlrpclib.ServerProxy('http://localhost:8071/xmlrpc/2/common').authenticate(db, user, password, {})
#odoo = xmlrpclib.ServerProxy('http://localhost:8071/xmlrpc/2/object')

db = 'viki2'
user = 'annaduraidm@hotmail.com'
password = '15031989'
uid = xmlrpclib.ServerProxy('https://viki2.odoo.com/xmlrpc/2/common').authenticate(db, user, password, {})
odoo = xmlrpclib.ServerProxy('https://viki2.odoo.com/xmlrpc/2/object')

#installed_modules = odoo.execute_kw(db, uid, password, 'sale.order', 'search_read',[[('state', '=', 'done')], ['name']], {'context':{'lang': 'fr_FR'}})
values = odoo.execute_kw(db, uid, password, 'res.partner', 'search_read',[[('id', '=', 13)], ['name','lang']],)
for value in values:
	print value['name']
	print values
	value['name']="xml_rpc_test"
	value.update({'name':"xml_rpc_test"})
	print "values--  ", value
	print value['name']

rights = odoo.execute_kw(db, uid, password,'res.partner', 'check_access_rights',['read'], {'raise_exception': False})
print "Rights ?",rights

no_cust = odoo.execute_kw(db, uid, password,'res.partner', 'search',[[['is_company', '=', False], ['customer', '=', True]]])
print " number of partners   -- ", no_cust

offset_cust = odoo.execute_kw(db, uid, password,'res.partner', 'search',[[['is_company', '=', False], ['customer', '=', True]]],{'offset': 10, 'limit': 5})
print "offset_example",offset_cust

count_rec = odoo.execute_kw(db, uid, password,'res.partner', 'search_count',[[['is_company', '=', False], ['customer', '=', True]]])
print "count_rec", count_rec

listing_rec_field = odoo.execute_kw(db, uid, password, 'res.partner', 'fields_get',[], {'attributes': ['string', 'type']})
print "\n Listing Record Field", listing_rec_field

search_read = odoo.execute_kw(db, uid, password,'res.partner', 'search_read',[[['is_company', '=', False], ['customer', '=', True]]],{'fields': ['name', 'country_id'], 'limit': 5})
print "\n search_read", search_read

#create_partner = odoo.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "XMLRPCnewpartner",}])
#print "\n create_partner created", create_partner

update_rec = odoo.execute_kw(db, uid, password, 'res.partner', 'write', [[15], {'mobile': "23421342"}])
print "\n update_partner created", update_rec

updated_rec_idname = odoo.execute_kw(db, uid, password, 'res.partner', 'name_get', [[15]])
print "\n updated_rec_idname", updated_rec_idname


#my_partner_id = 13
#my_tag_id = 1  # or use a search to find the correct one
#try:
#    many2many_id = odoo.execute_kw(db, uid, password, 'res.partner', 'write',[[my_partner_id], {'source_id': 2,'title':3,'parent_id':1,'agents':(6,0,[154,156]),'agent':False}])
#except :
#    print "\n Invalid field or value"
#else:
#    print "many2many_id  ",many2many_id

# for delete rec
#models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
# check if the deleted record is still in the database
#models.execute_kw(db, uid, password,'res.partner', 'search', [[['id', '=', id]]])