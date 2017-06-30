# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random, string

class DoiTuongChinhSach(models.Model):
    _name = 'solienlac.doituongchinhsach'
    tendoituongchinhsach = fields.Char(string='Tên Đối Tượng Chinh Sách')
    miengiam = fields.Float(string='Miễn Giảm')
    ghichu = fields.Char(string='Ghi Chú')

class KhenThuongKyLuat(models.Model):
    _name = 'solienlac.khenthuongkyluat'
    tenkhenthuongkyluat = fields.Char(string='Tên Khen Thưởng Kỷ Luật')
    hinhthuckhenthuongkyluat = fields.Char(string='Hình Thức Khen Thưởng Kỷ Luật')
    ghichu = fields.Char(string='Ghi Chú')

class KTKL_has_HocSinh(models.Model):
    _name = 'solienlac.khenthuongkyluat_hocsinh'
    ktkl = fields.Many2one('solienlac.khenthuongkyluat', string='ID Khen Thưởng Kỷ Luật', required='True')
    hocsinh = fields.Many2one('solienlac.hocsinh', string='ID Học Sinh', required='True')
    ngay_ktkl = fields.Date(string='Ngày Khen Thưởng Kỷ Luật')

class TuyenHoc(models.Model):
    _name = 'solienlac.tuyenhoc'
    matuyen = fields.Char(string='Mã Tuyến')
    tentuyen = fields.Char(string='Tên Tuyến')
    ghichu = fields.Char(string='Ghi Chú')

class Khoi(models.Model):
    _name = 'solienlac.khoi'
    makhoi = fields.Char(string='Mã Khối', required='True')
    tenkhoi = fields.Char(string='Tên Khối')
    ghichu = fields.Char('Ghi Chú')

class HanhKiem(models.Model):
    _name = 'solienlac.hanhkiem'
    hocky = fields.Char('Học Kỳ')
    namhoc = fields.Char('Năm Học')
    nhanxetcuagiaovien = fields.Char('Nhận Xét Của Giáo Viên')
    ghichu = fields.Char('Ghi Chú')
    hocsinh = fields.Many2many('solienlac.hocsinh', string='Học Sinh')

class PhuHuynh(models.Model):
    _name = 'solienlac.phuhuynh'
    hoten = fields.Char('Họ Tên')
    gioitinh = fields.Char('Giới Tính')
    ngaysinh = fields.Date('Ngày Sinh')
    sodienthoai = fields.Char('Số Điện Thoại')
    ghichu = fields.Char('Ghi Chú')
    phuongxa = fields.Many2one('solienlac.phuongxa', string='Xã\Phường')
    dantoc = fields.Many2one('solienlac.dantoc', string='Dân Tộc')
    tongiao = fields.Many2one('solienlac.tongiao', string='Tôn Giáo')



