# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random, string

# @api.multi
# @api.onchange('tinh')
# def set_value_huyen(self):
#     self.huyen = []
#     tmp1 = self.env['solienlac.quanhuyen'].search([
#                 ('matinhthanhpho', '=', self.tinh),
#             ])
#     lst = map(lambda x:x.matinhthanhpho, tmp1)
#     return {'domain':{'huyen': [('matinhthanhpho', 'in', lst)]}}
# @api.multi
# @api.onchange('tinh', 'huyen')
# def set_value_xa(self):
#     self.xa = []
#     tmp1 = self.env['solienlac.phuongxa'].search([
#                 ('TinhID', '=', self.tinh),
#                 ('QuanHuyenID', '=', self.huyen),
#             ])
#     lst = map(lambda x: x.QuanHuyenID, tmp1)
#     return {'domain':{'xa': [('QuanHuyenID', 'in', lst)]}}

# class hocsinh(models.Model):
#     _name = 'solienlac.hocsinh'
#     mahocsinh = fields.Char('Mã học sinh', required='True')
#     hoten = fields.Char('Họ tên', required='True')
#     gioitinh = fields.Selection([
#         ('Nam', 'Nam'),
#         ('Nu', 'Nữ'),
#         ('KXD', 'Không xác định')], string="Giới tính")
#     ngaysinh = fields.Date(string="Ngày sinh")
#     noisinh = fields.Char('Nơi sinh')
#     quequan = fields.Char('Quê quán')
#     lop = fields.Many2one('solienlac.lop', string='Lớp')
#     tuyenhoc = fields.Many2one('solienlac.tuyenhoc', string='Tuyến học')
#     phuongxa = fields.Many2one('solienlac.phuongxa', string='Phường Xã')
#     dantoc = fields.Many2one('solienlac.dantoc', string='Dân tộc')
#     tongiao = fields.Many2one('solienlac.tongiao', string='Tôn giáo')
#     chucvu = fields.Many2one('solienlac.chucvu', string='Chức vụ')
#     doituongchinhsach = fields.Many2many('solienlac.doituongchinhsach', string='Đối tượng chính sách')
#     doituonguutien = fields.Many2many('solienlac.doituonguutien', string='Đối tượng ưu tiên')
#     phuhuynh = fields.Many2many('solienlac.phuhuynh', string='Phụ huynh')
#
# class lop(models.Model):
#     _name = 'solienlac.lop'
#     malop = fields.Char('Mã lớp', required='True')
#     tenlop = fields.Char('Tên lớp', required='True')
#     nienkhoa = fields.Char('Niên khóa', required='True')
#     ghichu = fields.Char('Ghi chú', required='True')
#     khoi = fields.Many2one('solienlac.khoi', string='Khối')
#
# class banhoc(models.Model):
#     _name = 'solienlac.banhoc'
#     maban = fields.Char('Mã ban', required='True')
#     tenban = fields.Char('Tên ban')
#     monhoc = fields.Char('Môn học')
#     ghichu = fields.Char('Ghi chú')
#
# class monhoc(models.Model):
#     _name = 'solienlac.monhoc'
#     mamonhoc = fields.Char('Mã môn học', required='True')
#     tenmonhoc = fields.Char('Tên môn học', required='True')
#     heso = fields.Float('Hệ số')
#     ghichu = fields.Char('Ghi chú')
#     bomon = fields.Many2one('solienlac.bomon', string='Bộ môn')
#     banhoc = fields.Many2one('solienlac.banhoc', string='Ban hoc')
#
#
# class ketquahoctap(models.Model):
#     _name = 'solienlac.ketquahoctap'
#     hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')
#     monhoc = fields.Many2one('solienlac.monhoc', string='Môn học')
#     giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')
#     diemtongket = fields.Float('Điểm tổng kết')
#     kyhoc = fields.Integer('Năm học')
#     namhoc = fields.Integer('Học kỳ')
#     ngaycapnhat = fields.Date('Ngày cập nhật')
#     ykiengiaovien = fields.Char('Ý kiến giáo viên')
#
# class loaidiem(models.Model):
#     _name = 'solienlac.loaidiem'
#     maloai = fields.Char('Mã loai', required='True')
#     tenloai = fields.Char('Tên loai', required='True')
#     heso = fields.Float('Hệ số')
#     ghichu = fields.Char('Ghi chú')
#
# class diem(models.Model):
#     _name = 'solienlac.diem'
#     diem = fields.Float('Điểm')
#     ngaynhap = fields.Date('Ngày nhập')
#     ghichu = fields.Char('Ghi chú')
#     ketquahoctap = fields.Many2one('solienlac.ketquahoctap', string='Kết quả học tập')
#     loaidiem = fields.Many2one('solienlac.loaidiem', string='Loại điểm')
#     giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')
#
# class chucvu(models.Model):
#     _name = 'solienlac.chucvu'
#     machucvu = fields.Char('Mã chức vụ', required='True')
#     tenchucvu = fields.Char('Tên chức vụ', required='True')
#     ghichu = fields.Char('Ghi chú')
#
# class nenep(models.Model):
#     _name = 'solienlac.nenep'
#     dongphuc = fields.Integer('Đồng phục')
#     dihocmuon = fields.Integer('Đồng phục')
#     noichuyen = fields.Integer('Đồng phục')
#     noituc = fields.Integer('Đồng phục')
#     # dongphuc = fields.Integer('Đồng phục')
#     truybai = fields.Integer('Đồng phục')
#     ntvt = fields.Integer('Đồng phục')
#     hocky = fields.Integer('Đồng phục')
#     namhoc = fields.Integer('Đồng phục')
#     hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')
