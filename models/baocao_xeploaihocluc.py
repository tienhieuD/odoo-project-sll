# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
class xeploaihocluc(models.Model):
    _name = 'solienlac.xeploaihocluc'

    khoi = fields.Many2one('solienlac.khoi', string='Khối')
    phanban = fields.Many2one('solienlac.banhoc', string='Phân ban')

    tongsohocsinh_nam = fields.Integer('Tổng số học sinh nam')
    tongsohocsinh_nu = fields.Integer('Tổng số học sinh nữ')
    tot_nam = fields.Integer('Số học sinh nam(xếp loại tốt)')
    tot_nu = fields.Integer('Số học sinh nữ(xếp loại tốt)')
    kha_nam = fields.Integer('Số học sinh nam(xếp loại khá)')
    kha_nu = fields.Integer('Số học sinh nữ(xếp loại khá)')
    tb_nam = fields.Integer('Số học sinh nam(xếp loại trung bình)')
    tb_nu = fields.Integer('Số học sinh nữ(xếp loại trung bình)')
    yeu_nam = fields.Integer('Số học sinh nam(xếp loại yếu)')
    yeu_nu = fields.Integer('Số học sinh nữ(xếp loại yếu)')

    tongbancoban_tongsohocsinh_nam = fields.Integer('Tổng số học sinh nam ban cơ bản')
    tongbancoban_tongsohocsinh_nu = fields.Integer('Tổng số học sinh nữ ban cơ bản')
    tongbancoban_tot_nam = fields.Integer('Số học sinh nam ban cơ bản(xếp loại tốt)')
    tongbancoban_tot_nu = fields.Integer('Số học sinh nữ ban cơ bản(xếp loại tốt)')
    tongbancoban_kha_nam = fields.Integer('Số học sinh nam ban cơ bản(xếp loại khá)')
    tongbancoban_kha_nu = fields.Integer('Số học sinh nữ ban cơ bản(xếp loại khá)')
    tongbancoban_tb_nam = fields.Integer('Số học sinh nam ban cơ bản(xếp loại trung bình)')
    tongbancoban_tb_nu = fields.Integer('Số học sinh nữ ban cơ bản(xếp loại trung bình)')
    tongbancoban_yeu_nam = fields.Integer('Số học sinh nam ban cơ bản(xếp loại yếu)')
    tongbancoban_yeu_nu = fields.Integer('Số học sinh nữ ban cơ bản(xếp loại yếu)')

    tongkhoi_tongsohocsinh_nam = fields.Integer('Tổng số học sinh nam của khối')
    tongkhoi_tongsohocsinh_nu = fields.Integer('Tổng số học sinh nữ của khối')
    tongkhoi_tot_nam = fields.Integer('Tổng số học sinh nam của khối(xếp loại tốt)')
    tongkhoi_tot_nu = fields.Integer('Tổng số học sinh nữ của khối(xếp loại tốt)')
    tongkhoi_kha_nam = fields.Integer('Tổng số học sinh nam của khối(xếp loại khá)')
    tongkhoi_kha_nu = fields.Integer('Tổng số học sinh nữ của khối(xếp loại khá)')
    tongkhoi_tb_nam = fields.Integer('Tổng số học sinh nam của khối(xếp loại trung bình)')
    tongkhoi_tb_nu = fields.Integer('Tổng số học sinh nữ của khối(xếp loại trung bình)')
    tongkhoi_yeu_nam = fields.Integer('Tổng số học sinh nam của khối(xếp loại yếu)')
    tongkhoi_yeu_nu = fields.Integer('Tổng số học sinh nữ của khối(xếp loại yếu)')

    @api.multi
    @api.onchange('khoi', 'phanban')
    def xeploaihanhkiem(self):
        def demsohocsinh(xeploai_phanban, xeploai, gioitinh):
            if(xeploai_phanban == 'xeploai_phanban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('lop.banhoc.tenban', '=', self.phanban.tenban),
                    ('hanhkiem.xeploai', '=', xeploai),
                    ('gioitinh', '=', gioitinh)
                ])
            elif(xeploai_phanban == 'khongxeploai_phanban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('lop.banhoc.tenban', '=', self.phanban.tenban),
                    ('gioitinh', '=', gioitinh),
                ])
            elif(xeploai_phanban == 'xeploai_phanban_coban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('lop.banhoc.tenban', '!=', 'tunhien'),
                    ('lop.banhoc.tenban', '!=', 'xahoi'),
                    ('hanhkiem.xeploai', '=', xeploai),
                    ('gioitinh', '=', gioitinh),
                ])
            elif(xeploai_phanban == 'khongxeploai_phanban_coban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('lop.banhoc.tenban', '!=', 'tunhien'),
                    ('lop.banhoc.tenban', '!=', 'xahoi'),
                    ('gioitinh', '=', gioitinh)
                ])
            elif(xeploai_phanban == 'xeploai_khongphanban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('hanhkiem.xeploai', '=', xeploai),
                    ('gioitinh', '=', gioitinh),
                ])
            elif(xeploai_phanban == 'khongxeploai_khongphanban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('gioitinh', '=', gioitinh),
                ])
            return 0
#

        #--------------------   tổng số học sinh từng ban + từng khối ----------------
        self.tot_nam = demsohocsinh('xeploai_phanban', 'tot', 'Nam')
        self.tot_nu = demsohocsinh('xeploai_phanban', 'tot', 'Nu')

        self.kha_nam = demsohocsinh('xeploai_phanban', 'kha', 'Nam')
        self.kha_nu = demsohocsinh('xeploai_phanban', 'kha', 'Nu')

        self.tb_nam = demsohocsinh('xeploai_phanban', 'tb', 'Nam')
        self.tb_nu = demsohocsinh('xeploai_phanban', 'tb', 'Nu')

        self.yeu_nam = demsohocsinh('xeploai_phanban', 'yeu', 'Nam')
        self.yeu_nu = demsohocsinh('xeploai_phanban', 'yeu', 'Nu')

        self.tongsohocsinh_nam = demsohocsinh('khongxeploai_phanban', 'kxl', 'Nam')
        self.tongsohocsinh_nu = demsohocsinh('khongxeploai_phanban', 'kxl', 'Nu')

        #--------------------   tổng số học sinh ban cơ bản ----------------
        self.tongbancoban_tot_nam = demsohocsinh('phanban_coban', 'tot', 'Nam')
        self.tongbancoban_tot_nu = demsohocsinh('phanban_coban', 'tot', 'Nu')

        self.tongbancoban_kha_nam = demsohocsinh('phanban_coban', 'kha', 'Nam')
        self.tongbancoban_kha_nu = demsohocsinh('phanban_coban', 'kha', 'Nu')

        self.tongbancoban_tb_nam = demsohocsinh('phanban_coban', 'tb', 'Nam')
        self.tongbancoban_tb_nu = demsohocsinh('phanban_coban', 'tb', 'Nu')

        self.tongbancoban_yeu_nam = demsohocsinh('phanban_coban', 'yeu', 'Nam')
        self.tongbancoban_tb_nu = demsohocsinh('phanban_coban', 'yeu', 'Nu')

        self.tongbancoban_tongsohocsinh_nam = demsohocsinh('khongxeploai_phanban_coban', 'kxl', 'Nam')
        self.tongbancoban_tongsohocsinh_nu = demsohocsinh('khongxeploai_phanban_coban', 'kxl', 'Nu')

        #--------------------   tổng số học sinh của khối ----------------
        self.tongkhoi_tot_nam = demsohocsinh('xeploai_khongphanban', 'tot', 'Nam')
        self.tongkhoi_tot_nu = demsohocsinh('xeploai_khongphanban', 'tot', 'Nu')

        self.tongkhoi_kha_nam = demsohocsinh('xeploai_khongphanban', 'kha', 'Nam')
        self.tongkhoi_kha_nu = demsohocsinh('xeploai_khongphanban', 'kha', 'Nu')

        self.tongkhoi_tb_nam = demsohocsinh('xeploai_khongphanban', 'tb', 'Nam')
        self.tongkhoi_tb_nu = demsohocsinh('xeploai_khongphanban', 'tb', 'Nu')

        self.tongkhoi_yeu_nam = demsohocsinh('xeploai_khongphanban', 'yeu', 'Nam')
        self.tongkhoi_yeu_nu = demsohocsinh('xeploai_khongphanban', 'yeu', 'Nu')

        self.tongkhoi_tongsohocsinh_nam = demsohocsinh('khongxeploai_khongphanban', 'kxl', 'Nam')
        self.tongkhoi_tongsohocsinh_nu = demsohocsinh('khongxeploai_khongphanban', 'kxl', 'Nu')
