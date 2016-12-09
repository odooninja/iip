

from odoo import api, fields, models, tools, _


class ProductLabel(models.Model):
    _inherit = ['product.template']
    product_image_ids = fields.One2many('product.image', 'product_tmpl_id', string='Images')
    date_production = fields.Date('Date of Production', index=True, required=True, translate=True)
    s_no = fields.Char('Serial Number')
    product_digressive_pricing_ids=fields.One2many('product.digressive.pricing','template_ids')



class ProductImage(models.Model):

    _inherit = ['product.image']
    name=fields.Char('name')
    available = fields.Boolean('Available')
    product_tmpl_id = fields.Many2one('product.template', 'Related Product', copy=True)

class product_digressive_pricing(models.Model):
    _name='product.digressive.pricing'


    quantity=fields.Float('Quantity')
    amount=fields.Float('Amount')
    template_ids=fields.Many2one('product.template')
