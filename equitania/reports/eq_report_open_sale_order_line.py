# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from openerp.osv import osv
from openerp import api
from openerp.report import report_sxw

class eq_report_open_sale_order_line(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context):
        super(eq_report_open_sale_order_line, self).__init__(cr, uid, name, context=context)
        
        self.localcontext.update({
            'get_qty':self.get_qty,
            'get_price': self.get_price,
            'get_standard_price': self.get_standard_price,
            'get_records': self._get_records,
            'get_translated_productname': self.get_translated_productname,
            'get_product_no': self.get_product_no
        })
        
    
    def get_qty(self, object, language):
        return self.pool.get("eq_report_helper").get_qty(self.cr, self.uid, object, language, 'Sale Quantity Report')
           
    
    def get_price(self, object, language, currency_id):                
        return self.pool.get("eq_report_helper").get_price(self.cr, self.uid, object, language, 'Sale Price Report', currency_id)
    
    
    def get_standard_price(self, object, language, currency_id):
        return self.pool.get("eq_report_helper").get_standard_price(self.cr, self.uid, object, language, currency_id)


    def _get_records(self):
        """
            Get all records created by wizard and show them as lines in table
            @return: An array with all created records from eq_product_sales_data table
        """

        result = []
        table = self.pool.get('eq_buffer_order_line_list')
        ids = table.search(self.cr, self.uid, [('create_uid','=',self.uid),('write_uid','=',self.uid)])
        for id in ids:
            result.append(table.browse(self.cr, self.uid, id))

        return result

    def get_translated_productname(self,obj):
        tmpl_id = obj.product_tmpl_id.id
        ir_translation_id = self.pool.get('ir.translation').search(self.cr, self.uid, [('res_id', '=', tmpl_id), ('name', '=', 'product.template,name')])
        if ir_translation_id:
            id_to_select = None
            if len(ir_translation_id) > 1:
                id_to_select = ir_translation_id[0]             # wir haben hier mehrere Positionen zurückbekommen und wollen kein Singletonfehler haben..also...es wird die erste Position geladen
            else:
                id_to_select = ir_translation_id

            #ir_translation_obj = self.pool.get('ir.translation').browse(self.cr,self.uid,ir_translation_id)
            ir_translation_obj = self.pool.get('ir.translation').browse(self.cr, self.uid, id_to_select)
            result = ir_translation_obj.value
        else:
            product_id = self.pool.get('product.template').search(self.cr, self.uid,[('id', '=', tmpl_id)])
            product_obj = self.pool.get('product.template').browse(self.cr,self.uid,product_id)
            result = product_obj.name
        return result

    def get_product_no(self,obj):
        if len(obj) > 0 :
            result = '[' + obj.default_code + ']'
        return result
          
    
class report_lunchorder(osv.AbstractModel):
    
    _name = 'report.equitania.report_open_sale_order_line'
    _inherit = 'report.abstract_report'
    _template = 'equitania.report_open_sale_order_line'
    _wrapped_report_class = eq_report_open_sale_order_line