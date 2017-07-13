# -*- coding: utf-8 -*-
from odoo import models, fields, api

class xlhkhshnkt(models.Model):
    '''Xếp loại hạnh kiểm học sinh hòa nhập, khuyết tật'''
    _name = 'solienlac.baocao.xlhkhshnkt'
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
    )
    namhoc = fields.Char('Năm học')
    khoi = fields.Many2one(
        string="Khối",
        comodel_name="solienlac.khoi",
    )
    tongsohs = fields.Integer('Tổng số học sinh')
    tot_sl = fields.Integer('Số lượng HK Tốt')
    tot_pt = fields.Float('Phần trăm HK Tốt')
    kha_sl = fields.Integer('Số lượng HK Khá')
    kha_pt = fields.Float('Phần trăm HK Khá')
    tb_sl = fields.Integer('Số lượng HK Trung bình')
    tb_pt = fields.Float('Phần trăm HK Trung bình')
    y_sl = fields.Integer('Số lượng HK Yếu')
    y_pt = fields.Float('Phần trăm HK Yếu')

    @api.multi
    @api.onchange('khoi')
    def _compute_model(self):
        def laysoluong_hs(hanhkiem):
            return self.env['solienlac.hocsinh'].search_count(
                [
                    ('lop.khoi.id','=',self.khoi.id),
                    ('khuyettat','!=','value1'),
                    ('hanhkiem.xeploai','=', hanhkiem),
                    ('hanhkiem.hocky', '=', self.hocky),
                    ('hanhkiem.namhoc', '=', self.namhoc),
                ]
            )
        def layphantram_hs(x,y):
            try:
                return round(float(x)/float(y)*100, 2)
            except:
                return 0.0
        _tongsohs = self.env['solienlac.hocsinh'].search_count([
                ('lop.khoi.id','=',self.khoi.id),
                ('khuyettat','!=','value1'),
            ])
        _tot_sl = laysoluong_hs('tot')
        _kha_sl = laysoluong_hs('kha')
        _tb_sl  = laysoluong_hs('tb')
        _y_sl   = laysoluong_hs('yeu')
        _tot_pt = layphantram_hs(_tot_sl,_tongsohs)
        _kha_pt = layphantram_hs(_kha_sl,_tongsohs)
        _tb_pt = layphantram_hs(_tb_sl,_tongsohs)
        _y_pt = layphantram_hs(_y_sl,_tongsohs)

        self.tongsohs = _tongsohs
        self.tot_sl = _tot_sl
        self.tot_pt = _tot_pt
        self.kha_sl = _kha_sl
        self.kha_pt = _kha_pt
        self.tb_sl = _tb_sl
        self.tb_pt = _tb_pt
        self.y_sl = _y_sl
        self.y_pt = _y_pt

class xlhkhsdt(models.Model):
    '''Xếp loại hạnh kiểm học sinh dân tộc'''
    _name = 'solienlac.baocao.xlhkhsdt'
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
    )
    namhoc = fields.Char('Năm học')
    khoi = fields.Many2one(
        string="Khối",
        comodel_name="solienlac.khoi",
    )
    tongsohs = fields.Integer('Tổng số học sinh')
    tot_sl = fields.Integer('Số lượng HK Tốt')
    tot_pt = fields.Float('Phần trăm HK Tốt')
    kha_sl = fields.Integer('Số lượng HK Khá')
    kha_pt = fields.Float('Phần trăm HK Khá')
    tb_sl = fields.Integer('Số lượng HK Trung bình')
    tb_pt = fields.Float('Phần trăm HK Trung bình')
    y_sl = fields.Integer('Số lượng HK Yếu')
    y_pt = fields.Float('Phần trăm HK Yếu')

    @api.multi
    @api.onchange('khoi')
    def _compute_model(self):
        def laysoluong_hs(hanhkiem):
            return self.env['solienlac.hocsinh'].search_count(
                [
                    ('lop.khoi.id','=',self.khoi.id),
                    ('dantoc.tendantoc','not like','Kinh'),
                    ('hanhkiem.xeploai','=', hanhkiem),
                    ('hanhkiem.hocky', '=', self.hocky),
                    ('hanhkiem.namhoc', '=', self.namhoc),
                ]
            )
        def layphantram_hs(x,y):
            try:
                return round(float(x)/float(y)*100, 2)
            except:
                return 0.0
        _tongsohs = self.env['solienlac.hocsinh'].search_count([
                ('lop.khoi.id','=',self.khoi.id),
                ('dantoc.tendantoc','not like','Kinh'),
            ])
        _tot_sl = laysoluong_hs('tot')
        _kha_sl = laysoluong_hs('kha')
        _tb_sl  = laysoluong_hs('tb')
        _y_sl   = laysoluong_hs('yeu')
        _tot_pt = layphantram_hs(_tot_sl,_tongsohs)
        _kha_pt = layphantram_hs(_kha_sl,_tongsohs)
        _tb_pt = layphantram_hs(_tb_sl,_tongsohs)
        _y_pt = layphantram_hs(_y_sl,_tongsohs)

        self.tongsohs = _tongsohs
        self.tot_sl = _tot_sl
        self.tot_pt = _tot_pt
        self.kha_sl = _kha_sl
        self.kha_pt = _kha_pt
        self.tb_sl = _tb_sl
        self.tb_pt = _tb_pt
        self.y_sl = _y_sl
        self.y_pt = _y_pt
