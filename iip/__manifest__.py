{
    'name': 'label',
    'version': '1.2',
    'category': 'Sales',
    'depends': ['sale','report','product','purchase','mrp','website_sale'],
    'description': """
This is the base module for managing products and pricelists in Odoo.
========================================================================

# Products support variants, different pricing methods, vendors information,
# make to stock/order, different units of measure, packaging and properties.
#
# Pricelists support:
# -------------------
#     * Multiple-level of discount (by product, category, quantities)
#     * Compute price based on different criteria:
#         * Other pricelist
#         * Cost price
#         * List price
#         * Vendor price

Pricelists preferences by product and/or partners.

Print product labels with barcode.
    """,
    'data': [
        'data/product_data.xml',
        'data/price_data.xml',
        'view/product_label.xml',
        'report/report.xml',
        'report/product_label_report.xml',
    ],
    # 'demo': [
    #     'data/product_demo.xml',
    #     'data/product_image_demo.xml',
    # ],
    'installable': True,
    'auto_install': False,
}
