# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
import time, datetime
from datetime import date

# class tinhhinhhocsinhthoihoc(models.Model):
#     _name = 'solienlac.tinhhinhhocsinhthoihoc'
#     hocky = fields.Selection(
#         string="Học kỳ",
#         selection=[
#                 ('i', 'Học kỳ I'),
#                 ('ii', 'Học kỳ II'),
#                 ('iii', 'Cả năm'),
#     ],)
#     namhoc = fields.Char('Năm học', required='True')
#     ngayhientai = fields.Date('Ngày hiện tại', required='True')
#     khoi = fields.Many2one('solienlac.khoi', string='Khối', required='True')
#     lydothoihoc = fields.Many2one('solienlac.lydothoihoc', string='Lý do thôi học')
#     dohoclucyeukem = fields.Integer(string='Do học lực yếu kém')
#     dohoancanhkhokhan = fields.Integer(string='Do hoàn cảnh khó khăn')
#     doxanha = fields.Integer(string='Do xa nhà')
#     lydokhac = fields.Integer(string='Lý do khác: tai nạn, ốm đau')
#     tongsohocsinhthoihoc = fields.Integer(string='Tổng số học sinh thôi học')
#     kyluatbuocthoihoc1nam = fields.Integer('Kỷ luật buộc thôi học 1 năm')
#     tongsohocsinhdaunam = fields.Integer('Tổng sốhọc sinh đầu năm')
#     tongsohocsinhcuoinam = fields.Integer('Tổng số học sinh cuối năm')
#     sohocsinhchuyenden = fields.Integer('Số học sinh chuyển đến')
#     sohocsinhchuyendi = fields.Integer('Số học sinh chuyển đi')
#     @api.multi
#     @api.onchange('khoi', 'hocky', 'namhoc')
#     def demsohocsinh(self):
#         def demsohocsinhhientai():
#             return self.env['solienlac.hocsinh'].search_count([
#                 ('lydothoihoc.namhoc', '=', self.namhoc),
#                 ('lop.khoi.id', '=', self.khoi.id),
#                 ('lydothoihoc.lydothoihoc' ,'=', 'value1')
#             ])
#         def demsohocsinhchuyenden(truoc_sau):
#             if(truoc_sau == 'truoc'):
#                 return self.env['solienlac.hocsinh'].search_count([
#                     ('lydothoihoc.namhoc', '=', self.namhoc),
#                     ('lop.khoi.id', '=', self.khoi.id),
#                     ('nguongochocsinh.nguongochocsinh' ,'=', 'value4'),
#                     ('nguongochocsinh.thoidiemnhaptruong', '<', self.ngayhientai),
#                 ])
#             return self.env['solienlac.hocsinh'].search_count([
#                 ('lydothoihoc.namhoc', '=', self.namhoc),
#                 ('lop.khoi.id', '=', self.khoi.id),
#                 ('nguongochocsinh.nguongochocsinh' ,'=', 'value4'),
#                 ('nguongochocsinh.thoidiemnhaptruong', '>=', self.ngayhientai),
#             ])
#         def demsohocsinhchuyendi(truoc_sau):
#             if(truoc_sau == 'truoc'):
#                 return self.env['solienlac.hocsinh'].search_count([
#                     ('lydothoihoc.namhoc', '=', self.namhoc),
#                     ('lop.khoi.id', '=', self.khoi.id),
#                     ('lydothoihoc.lydothoihoc' ,'=', 'value2'),
#                     ('lydothoihoc.thoidiemthoihoc', '<', self.ngayhientai),
#                 ])
#             return self.env['solienlac.hocsinh'].search_count([
#                 ('lydothoihoc.namhoc', '=', self.namhoc),
#                 ('lop.khoi.id', '=', self.khoi.id),
#                 ('lydothoihoc.lydothoihoc' ,'=', 'value2'),
#                 ('lydothoihoc.thoidiemthoihoc', '>=', self.ngayhientai),
#             ])
#         def demsohocsinhthoihoc(flag, truoc_sau, lydothoihoc):
#             if flag:
#                 if truoc_sau == 'truoc':
#                     return self.env['solienlac.hocsinh'].search_count([
#                         ('lydothoihoc.namhoc', '=', self.namhoc),
#                         # ('lydothoihoc.hocky', '=', self.hocky),
#                         ('lop.khoi.id', '=', self.khoi.id),
#                         ('lydothoihoc.lydothoihoc' ,'!=', lydothoihoc),
#                         ('lydothoihoc.lydothoihoc' ,'!=', 'value2'),
#                         ('lydothoihoc.thoidiemthoihoc', '<', self.ngayhientai),
#                     ])
#                 return self.env['solienlac.hocsinh'].search_count([
#                     ('lydothoihoc.namhoc', '=', self.namhoc),
#                     # ('lydothoihoc.hocky', '=', self.hocky),
#                     ('lop.khoi.id', '=', self.khoi.id),
#                     ('lydothoihoc.lydothoihoc' ,'!=', lydothoihoc),
#                     ('lydothoihoc.lydothoihoc' ,'!=', 'value2'),
#                     ('lydothoihoc.thoidiemthoihoc', '>=', self.ngayhientai),
#                 ])
#             return self.env['solienlac.hocsinh'].search_count([
#                     ('lydothoihoc.namhoc', '=', self.namhoc),
#                     # ('lydothoihoc.hocky', '=', self.hocky),
#                     ('lop.khoi.id', '=', self.khoi.id),
#                     ('lydothoihoc.lydothoihoc', '=', lydothoihoc),
#                 ])
#
#         n_ht = demsohocsinhhientai()
#         n_den_truoc = demsohocsinhchuyenden('truoc')
#         n_di_truoc = demsohocsinhchuyendi('truoc')
#         n_thoi_truoc = demsohocsinhthoihoc(1, 'truoc', 'value1')
#         n_den_sau = demsohocsinhchuyenden('sau')
#         n_di_sau = demsohocsinhchuyendi('sau')
#         n_thoi_sau = demsohocsinhthoihoc(1, 'sau', 'value1')
#
#         self.tongsohocsinhthoihoc = demsohocsinhthoihoc(1, 'truoc', 'value1') + demsohocsinhthoihoc(1, 'sau', 'value1')
#         self.tongsohocsinhdaunam = n_ht #- n_den_truoc + n_di_truoc + n_thoi_truoc
#         self.tongsohocsinhcuoinam = n_ht + n_den_sau - n_di_sau - n_thoi_sau
#         self.sohocsinhchuyenden = n_den_truoc + n_den_sau
#         self.sohocsinhchuyendi = n_di_truoc + n_di_sau
#         self.dohoclucyeukem = demsohocsinhthoihoc(0, 'truoc', 'value4') + demsohocsinhthoihoc(0, 'sau', 'value4')
#         self.doxanha = demsohocsinhthoihoc(0, 'truoc', 'value5') + demsohocsinhthoihoc(0, 'sau', 'value4')
#         self.dohoancanhkhokhan = demsohocsinhthoihoc(0, 'truoc', 'value6') + demsohocsinhthoihoc(0, 'sau', 'value6')
#         self.lydokhac = demsohocsinhthoihoc(0, 'truoc', 'value7') + demsohocsinhthoihoc(0, 'sau', 'value7')

class gvdd_hskt(models.Model):
    _name = 'solienlac.gvdd_hskt'
    description = 'Số hiệu giáo viên giảng dạy và học sinnh khuyết tật'
    khoi = fields.Many2one('solienlac.khoi', string='Khối', required='True')
    giaovien_ts = fields.Integer('Số lượng giáo viên')
    giaovien_nu = fields.Integer('Số lượng giáo viên nữ')
    khiemthi_ts = fields.Integer('Số lượng học sinh khiếm thị')
    khiemthi_nu = fields.Integer('Số lượng học sinh khiếm thị nữ')
    khiemthinh_ts = fields.Integer('Số lượng học sinh khiếm thính')
    khiemthinh_nu = fields.Integer('Số lượng học sinh khiếm thính nữ')
    champhattrientritue_ts = fields.Integer('Số lượng học sinh chậm phát triển trí tuệ')
    champhattrientritue_nu = fields.Integer('Số lượng học sinh chậm phát triển trí tuệ nữ')
    vandong_ts = fields.Integer('Số lượng học sinh vận đông')
    vandong_nu = fields.Integer('Số lượng học sinh vận động nữ')
    tatkhac_ts = fields.Integer('Số lượng học sinh tật khác')
    tatkhac_nu = fields.Integer('Số lượng học sinh tật khác nữ')
    datat_ts = fields.Integer('Số lượng học sinhđa tật ')
    datat_nu = fields.Integer('Số lượng học sinh đa tật nữ')


    @api.multi
    @api.onchange('khoi')
    def demsogiaovien(self):
        # dem = 0
        # list_gv = self.env['solienlac.giaovien'].search([])
        # for gv in list_gv:
        #     self.giaovien_ts = gv.lops
        #     f = open('example.log', 'w')
        #     f.write('0123456789abcdef')
        #     f.close()

        self.giaovien_ts = self.env['solienlac.giaovien'].search_count([('lops.lop.khoi.id', '=', self.khoi.id)])
        self.giaovien_nu = self.env['solienlac.giaovien'].search_count([('lops.lop.khoi.id', '=', self.khoi.id), ('gioitinh', '=', 'Nu')])
        # self.giaovien_ts = dem
        def demhocsinhkhuyettat(type, flag = False):
            if(flag != True):
                return self.env['solienlac.hocsinh'].search_count([('lop.khoi.id', '=', self.khoi.id), ('khuyettat', '=', type)])
            return self.env['solienlac.hocsinh'].search_count([('lop.khoi.id', '=', self.khoi.id), ('khuyettat', '=', type), ('gioitinh', '=', 'Nu')])
        self.khiemthi_ts = demhocsinhkhuyettat('value3')
        self.khiemthi_nu = demhocsinhkhuyettat('value3', True)
        self.khiemthinh_ts = demhocsinhkhuyettat('value2')
        self.khiemthinh_nu = demhocsinhkhuyettat('value2', True)
        self.champhattrientritue_ts = demhocsinhkhuyettat('value5')
        self.champhattrientritue_nu = demhocsinhkhuyettat('value5', True)
        self.vandong_ts = demhocsinhkhuyettat('value4')
        self.vandong_nu = demhocsinhkhuyettat('value4', True)
        self.tatkhac_ts = demhocsinhkhuyettat('value7')
        self.tatkhac_nu = demhocsinhkhuyettat('value7', True)
        self.datat_ts = demhocsinhkhuyettat('value6')
        self.datat_nu = demhocsinhkhuyettat('value6', True)

class xeploaihanhkiem(models.Model):
    _name = 'solienlac.xeploaihanhkiem'

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
        self.tongbancoban_tot_nam = demsohocsinh('xeploai_phanban_coban', 'tot', 'Nam')
        self.tongbancoban_tot_nu = demsohocsinh('xeploai_phanban_coban', 'tot', 'Nu')

        self.tongbancoban_kha_nam = demsohocsinh('xeploai_phanban_coban', 'kha', 'Nam')
        self.tongbancoban_kha_nu = demsohocsinh('xeploai_phanban_coban', 'kha', 'Nu')

        self.tongbancoban_tb_nam = demsohocsinh('xeploai_phanban_coban', 'tb', 'Nam')
        self.tongbancoban_tb_nu = demsohocsinh('xeploai_phanban_coban', 'tb', 'Nu')

        self.tongbancoban_yeu_nam = demsohocsinh('xeploai_phanban_coban', 'yeu', 'Nam')
        self.tongbancoban_tb_nu = demsohocsinh('xeploai_phanban_coban', 'yeu', 'Nu')

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
    def xeploaihocluc(self):
        def demsohocsinh(xeploai_phanban, xeploai, gioitinh):
            if(xeploai_phanban == 'xeploai_phanban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('lop.banhoc.tenban', '=', self.phanban.tenban),
                    ('bangdiem.xeploai', '=', xeploai),
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
                    ('bangdiem.xeploai', '=', xeploai),
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
                    ('bangdiem.xeploai', '=', xeploai),
                    ('gioitinh', '=', gioitinh),
                ])
            elif(xeploai_phanban == 'khongxeploai_khongphanban'):
                return self.env['solienlac.hocsinh'].search_count([
                    ('lop.khoi.id', '=', self.khoi.id),
                    ('gioitinh', '=', gioitinh),
                ])
            return 0


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
        self.tongbancoban_tot_nam = demsohocsinh('xeploai_phanban_coban', 'tot', 'Nam')
        self.tongbancoban_tot_nu = demsohocsinh('xeploai_phanban_coban', 'tot', 'Nu')

        self.tongbancoban_kha_nam = demsohocsinh('xeploai_phanban_coban', 'kha', 'Nam')
        self.tongbancoban_kha_nu = demsohocsinh('xeploai_phanban_coban', 'kha', 'Nu')

        self.tongbancoban_tb_nam = demsohocsinh('xeploai_phanban_coban', 'tb', 'Nam')
        self.tongbancoban_tb_nu = demsohocsinh('xeploai_phanban_coban', 'tb', 'Nu')

        self.tongbancoban_yeu_nam = demsohocsinh('xeploai_phanban_coban', 'yeu', 'Nam')
        self.tongbancoban_tb_nu = demsohocsinh('xeploai_phanban_coban', 'yeu', 'Nu')

        self.tongbancoban_tongsohocsinh_nam = demsohocsinh('khongxeploai_phanban_coban', 'kxl', 'Nam')
        self.tongbancoban_tongsohocsinh_nu = demsohocsinh('khongxeploai_phanban_coban', 'kxl', 'Nu')

        #--------------------   tổng số học sinh của khối -----------------------------------------
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

#------------------------------- Tình hình giáo viên trong tổ theo môn -------------------------------
    class tinhhinhgiaovientrongto(models.Model):
        _name = "solienlac.tinhhinhgiaovientrongto"

        monhoc = fields.Many2one('solienlac.monhoc', 'Môn học')
        # hoten = fields.Many2one('solienlac.giaovien', string='Họ và Tên GV')

        chucvu = fields.Char('Chức vụ')
        vanbang = fields.Char('Văn bằng')
        namvaonganh = fields.Char('Năm vào ngành')
        # namvaonganh = fields.Date('Năm vào ngành')
        phanconggiangday = fields.Many2many('solienlac.lop', string='Phân công giảng dạy')
        phanconggiangday = fields.Char('Phân công giảng dạy')
        sodienthoai = fields.Char('DTDĐ')
        giaovien = fields.Many2one('solienlac.giaovien')
        #@api.model
        @api.multi
        @api.onchange('monhoc')
        def set_giaovien(self):
            self.giaovien = []
            tmp1 = self.env['solienlac.monhoc_has_giaovien'].search([
                        ('monhoc.id', '=', self.monhoc.id),
                    ])
            lst = map(lambda x: x.giaovien.id, tmp1)
            return {'domain':{'giaovien': [('id', 'in', lst)]}}

        @api.multi
        @api.onchange('monhoc', 'giaovien')
        def tinhhinhgiaovientrongto(self):
            tmp1 = self.env['solienlac.giaovien'].search([
                        ('lops.monhoc.id', '=', self.monhoc.id),
                        ('id', '=', self.giaovien.id)
                    ])
            def set_phanconggiangday(self):
                temp = self.env['solienlac.monhoc_has_giaovien'].search([
                            ('monhoc.id', '=', self.monhoc.id),
                            ('giaovien.id', '=', self.giaovien.id)
                        ])
                lst = map(lambda x: x.lop.tenlop, temp)
                s = " ,".join(str(x) for x in lst)
                return s
            def fomat_namvaonganh():
                try:
                    myyear = str(tmp1.namvaonganh)
                    y, d, m = myyear.split('-')
                    return y
                except ValueError:
                    return '0'
            self.phanconggiangday = set_phanconggiangday(self)
            self.chucvu = tmp1.chucvu.tenchucvu
            self.vanbang = tmp1.vanbang

            self.namvaonganh = fomat_namvaonganh()
            self.sodienthoai = tmp1.sodienthoai
class hocsinhtruongngoaiconglap(models.Model):
    _name = 'solienlac.hocsinhtruongngoaiconglap'

    khoi = fields.Many2one('solienlac.khoi', 'Khối')
    solop = fields.Integer('Số lớp')

    ts_hs = fields.Integer('Tổng số học sinh')
    hs_ngoaitinh = fields.Integer('Số học sinh ngoài tỉnh')
    tyle_hs = fields.Float('Tỷ lệ học sinh ngoài tỉnh')

    ts_hs_nt = fields.Integer('Tổng số học sinh nội trú')
    hs_ngoaitinh_nt = fields.Integer('Số học sinh ngoại tỉnh nội trú')
    tyle_hs_nt = fields.Float('Tỷ lệ học sinh ngoài tỉnh nội trú')

    @api.multi
    @api.onchange('khoi')
    def hocsinhtruongngoaiconglap(self):
        def demsolop():
            return self.env['solienlac.lop'].search_count([
                        ('khoi.id', '=', self.khoi.id),
                        ('khoi.truong', '=', self.khoi.id),
                    ])
        def demsohocsinhngoaitinh(noitru = True):
            temp = self.env['solienlac.hocsinh'].search([
                        ('lop.khoi.id', '=', self.khoi.id),
                        ('noitru', '=', noitru),
                        ('tinhtranghocsinh', '=', 'value1')
            ])
            dem = 0
            for val in temp:
                if(val.truong.matinhthanhpho != val.tinhthanhpho.matinhthanhpho):
                    dem += 1
            return dem

        def demtongsohocsinh(noitru = True):
                return self.env['solienlac.hocsinh'].search_count([
                            ('lop.khoi.id', '=', self.khoi.id),
                            ('noitru', '=', noitru),
                            ('tinhtranghocsinh', '=', 'value1')
                        ])
        def tinhtyle(tongso,  ngoaitinh):
            if(tongso > 0):
                return (1.0*ngoaitinh/tongso)*100
            return 0
        self.solop = demsolop()

        self.ts_hs = demtongsohocsinh() + demtongsohocsinh(False)
        self.hs_ngoaitinh = demsohocsinhngoaitinh() + demsohocsinhngoaitinh(False)


        self.tyle_hs =tinhtyle(self.ts_hs, self.hs_ngoaitinh)

        self.ts_hs_nt = demtongsohocsinh()
        self.hs_ngoaitinh_nt = demsohocsinhngoaitinh()
        self.tyle_hs_nt = tinhtyle(self.ts_hs_nt, self.hs_ngoaitinh_nt)

#------------------  8b  ---------------------------
class hocsinhnutruongngoaiconglap(models.Model):
    _name = 'solienlac.hocsinhnutruongngoaiconglap'

    khoi = fields.Many2one('solienlac.khoi', 'Khối')
    solop = fields.Integer('Số lớp')

    ts_hs = fields.Integer('Tổng số học sinh nữ')
    hs_ngoaitinh = fields.Integer('Số học sinh nữ ngoài tỉnh')
    tyle_hs = fields.Float('Tỷ lệ học sinh nữ ngoài tỉnh')

    ts_hs_nt = fields.Integer('Tổng số học sinh nữ nội trú')
    hs_ngoaitinh_nt = fields.Integer('Số học sinh nữ ngoại tỉnh nội trú')
    tyle_hs_nt = fields.Float('Tỷ lệ học sinh nữ ngoài tỉnh nội trú')

    @api.multi
    @api.onchange('khoi')
    def hocsinhtruongngoaiconglap(self):
        def demsolop():
            return self.env['solienlac.lop'].search_count([
                        ('khoi.id', '=', self.khoi.id),
                    ])
        def demsohocsinhngoaitinh(noitru = True):
            dem = 0
            temp = self.env['solienlac.hocsinh'].search([
                        ('lop.khoi.id', '=', self.khoi.id),
                        ('noitru', '=', noitru),
                        ('gioitinh', '=', "Nu"),
                        ('tinhtranghocsinh', '=', 'value1')
            ])
            for val in temp:
                if(val.truong.matinhthanhpho != val.tinhthanhpho.matinhthanhpho):
                    dem += 1
            return dem
        def demtongsohocsinh(noitru = True):
                return self.env['solienlac.hocsinh'].search_count([
                            ('lop.khoi.id', '=', self.khoi.id),
                            ('noitru', '=', noitru),
                            ('gioitinh', '=', 'Nu'),
                            ('tinhtranghocsinh', '=', 'value1')
                        ])
        def tinhtyle(tongso,  ngoaitinh):
            if(tongso > 0):
                return (1.0*ngoaitinh/tongso)*100
            return 0
        self.solop = demsolop()

        self.ts_hs = demtongsohocsinh() + demtongsohocsinh(False)
        self.hs_ngoaitinh = demsohocsinhngoaitinh() + demsohocsinhngoaitinh(False)
        self.tyle_hs =tinhtyle(self.ts_hs, self.hs_ngoaitinh)

        self.ts_hs_nt = demtongsohocsinh()
        self.hs_ngoaitinh_nt = demsohocsinhngoaitinh()
        self.tyle_hs_nt = tinhtyle(self.ts_hs_nt, self.hs_ngoaitinh_nt)

# class giaovientruongngoaiconglap
