# -*- coding: utf-8 -*-
from odoo import models, fields, api

class report_tinhhinhhocsinhthoihoc(models.Model):
    _name = 'solienlac.tinhhinhhocsinhthoihoc'
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        # required='True'
    )
    namhoc = fields.Char('Năm học', required='True')
    ngayhientai = fields.Date('Ngày hiện tại', required='True')
    khoi = fields.Many2one('solienlac.khoi', string='Khối', required='True')
    lydothoihoc = fields.Many2one('solienlac.lydothoihoc', string='Lý do thôi học')
    dohoclucyeukem = fields.Integer(string='Do học lực yếu kém')
    dohoancanhkhokhan = fields.Integer(string='Do hoàn cảnh khó khăn')
    doxanha = fields.Integer(string='Do xa nhà')
    lydokhac = fields.Integer(string='Lý do khác: tai nạn, ốm đau')
    tongsohocsinhthoihoc = fields.Integer(string='Tổng số học sinh thôi học')
    kyluatbuocthoihoc1nam = fields.Integer('Kỷ luật buộc thôi học 1 năm')
    tongsohocsinhdaunam = fields.Integer('Tổng sốhọc sinh đầu năm')
    tongsohocsinhcuoinam = fields.Integer('Tổng số học sinh cuối năm')
    sohocsinhchuyenden = fields.Integer('Số học sinh chuyển đến')
    sohocsinhchuyendi = fields.Integer('Số học sinh chuyển đi')
    @api.multi
    @api.onchange('khoi', 'hocky', 'namhoc')
    def demsohocsinh(self):
        sohosinhhientai =  self.env['solienlac.hocsinh'].search_count(
        [
            ('lydothoihoc.namhoc', '=', self.namhoc),
            ('lop.khoi.id', '=', self.khoi.id),
            ('lydothoihoc.lydothoihoc' ,'=', 'value1'),
        ]
        )
        self.tongsohocsinhthoihoc = self.env['solienlac.hocsinh'].search_count(
        [
            ('lydothoihoc.namhoc', '=', self.namhoc),
            # ('lydothoihoc.hocky', '=', self.hocky),
            ('lop.khoi.id', '=', self.khoi.id),
            ('lydothoihoc.lydothoihoc' ,'!=', 'value1'),
        ]
        )
        def demsohocsinhthoihoc(lydothoihoc):
            return self.env['solienlac.hocsinh'].search_count(
                [
                    ('lydothoihoc.namhoc', '=', self.namhoc),
                    # ('lydothoihoc.hocky', '=', self.hocky),
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('lydothoihoc.lydothoihoc', '=', lydothoihoc),
                ]
                )

        def demsohocsinhchuyenden():
            return self.env['solienlac.hocsinh'].search_count(
                [
                    ('lydothoihoc.namhoc', '=', self.namhoc),
                    # ('lydothoihoc.hocky', '=', self.hocky),
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('nguongochocsinh.nguongochocsinh', '=', 'value4'),
                ]
                )

        # if(self.tongsohocsinhdaunam != 0):
        self.tongsohocsinhcuoinam = sohosinhhientai + self.sohocsinhchuyenden - self.sohocsinhchuyendi - self.tongsohocsinhthoihoc
        self.sohocsinhchuyenden = demsohocsinhchuyenden()
        self.sohocsinhchuyendi = demsohocsinhthoihoc('value2')
        self.kyluatbuocthoihoc1nam = demsohocsinhthoihoc('value3')
        self.dohoclucyeukem = demsohocsinhthoihoc('value4')
        self.dohoancanhkhokhan = demsohocsinhthoihoc('value5')
        self.doxanha = demsohocsinhthoihoc('value6')
        self.lydokhac = demsohocsinhthoihoc('value7')
