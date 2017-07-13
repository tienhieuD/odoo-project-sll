# -*- coding: utf-8 -*-
from odoo import models, fields, api

class xlhkhshnkt(models.Model):
    '''Xếp loại hạnh kiểm học sinh hòa nhập, khuyết tật'''
    _name = 'solienlac.bc.xlhkhshnkt'
    khoi = fields.Many2one(
        string="Khối",
        comodel_name="solienlac.khoi",
    )
    tongsohs = fields.Integer()
    tot_sl = fields.Integer()
    # tot_pt = fields.Float(compute='_compute_tot_pt', store=True)
    # kha_sl = fields.Integer(compute='_compute_kha_sl', store=True)
    # kha_pt = fields.Float(compute='_compute_kha_pt', store=True)
    # tb_sl = fields.Integer(compute='_compute_tb_sl', store=True)
    # tb_pt = fields.Float(compute='_compute_tb_pt', store=True)
    # y_sl = fields.Integer(compute='_compute_y_sl', store=True)
    # y_pt = fields.Float(compute='_compute_y_pt', store=True)
    @api.multi
    @api.onchange('khoi')
    def _compute_model(self):
        # Tổng số học sinh khuyết tật
        self.tongsohs = self.env['solienlac.hocsinh'].search_count(
            [
                ('lop.khoi.id','=',self.khoi.id),
                ('khuyettat','!=','value1')
            ]
        )
        # Số lượng tốt
        self.tot_sl = self.env['solienlac.hocsinh'].search_count(
            [
                ('lop.khoi.id','=',self.khoi.id),
                '&', ('khuyettat','!=','value1'),
                ('hanhkiem.xeploai','=','tot'),
            ]
        )

