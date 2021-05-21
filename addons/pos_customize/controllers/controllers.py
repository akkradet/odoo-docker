# -*- coding: utf-8 -*-
# from odoo import http


# class PosCustomize(http.Controller):
#     @http.route('/pos_customize/pos_customize/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_customize/pos_customize/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_customize.listing', {
#             'root': '/pos_customize/pos_customize',
#             'objects': http.request.env['pos_customize.pos_customize'].search([]),
#         })

#     @http.route('/pos_customize/pos_customize/objects/<model("pos_customize.pos_customize"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_customize.object', {
#             'object': obj
#         })
