# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random, string

class DoiTuongChinhSach(models.Model):
    _name = 'solienlac.doituongchinhsach'
    # name = fields.Interger(string='ID Đối Tượng Chính Sách', required='True')
    tendoituongchinhsach = fields.Char(string='Tên Đối Tượng Chinh Sách')
    miengiam = fields.Float(string='Miễn Giảm')
    ghichu = fields.Char(string='Ghi Chú')

class KhenThuongKyLuat(models.Model):
    _name = 'solienlac.khenthuongkyluat'
    # name = fields.Many2one('solienlac.khenthuongkyluat_hocsinh', string='ID Khen Thường Kỷ Luật', required='True')
    tenkhenthuongkyluat = fields.Char(string='Tên Khen Thưởng Kỷ Luật')
    hinhthuckhenthuongkyluat = fields.Char(string='Hình Thức Khen Thưởng Kỷ Luật')
    ghichu = fields.Char(string='Ghi Chú')

class KTKL_has_HocSinh(models.Model):
    _name = 'solienlac.khenthuongkyluat_hocsinh'
    id_ktkl = fields.Many2one('solienlac.khenthuongkyluat', string='ID Khen Thưởng Kỷ Luật', required='True')
    id_hocsinh = fields.Many2one('solienlac.hocsinh', string='ID Học Sinh', required='True')
    ngay_ktkl = fields.Date(string='Ngày Khen Thưởng Kỷ Luật')

class TuyenHoc(models.Model):
    _name = 'solienlac.tuyenhoc'
    # name = fields.Interger(string='ID Tuyến Học', required='True')
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
    # hocsinh_idhocsinh = fields.Many2many('solienlac.hocsinh', string='Học Sinh')

class TonGiao(models.Model):
    _name = 'solienlac.tongiao'
    matongiao = fields.Char('Mã Tôn Giáo', required='True')
    tentongiao = fields.Char('Tên Tôn Giáo')
    ghichu = fields.Char('Ghi Chú')

class DanToc(models.Model):
    _name = 'solienlac.dantoc'
    matongiao = fields.Char('Mã Dân Tộc', required='True')
    tentongiao = fields.Char('Tên Dân Tộc')
    ghichu = fields.Char('Ghi Chú')

class PhuHuynh(models.Model):
    _name = 'solienlac.phuhuynh'
    hoten = fields.Char('Họ Tên')
    gioitinh = fields.Char('Giới Tính')
    ngaysinh = fields.Date('Ngày Sinh')
    sodienthoai = fields.Char('Số Điện Thoại')
    ghichu = fields.Char('Ghi Chú')
    phuongxa_idphuongxa = fields.Many2one('solienlac.phuongxa', string='Xã\Phường')
    dantoc_iddantoc = fields.Many2one('solienlac.dantoc', string='Dân Tộc')
    tongiao_idtongiao = fields.Many2one('solienlac.tongiao', string='Tôn Giáo')

class TinhThanhPho(models.Model):
    _name = 'solienlac.tinhthanhpho'
    matinhthanhpho = fields.Char(string='Mã Tỉnh\Thành Phố')
    tentinhthanhpho = fields.Char(string='Tên Tỉnh\Thành Phố')
    ghichu = fields.Char(string='Ghi Chú')

class QuanHuyen(models.Model):
    _name = 'solienlac.quanhuyen'
    maquanhuyen = fields.Char(string='Mã Quận Huyện')
    tenphuongxa = fields.Char(string='Tên Quận Huyện')
    ghichu = fields.Char(string='Ghi Chú')
    quanhuyen_idquanhuyen = fields.Many2one('solienlac.tinhthanhpho', string='Tỉnh\Thành Phố')

class PhuongXa(models.Model):
    _name = 'solienlac.phuongxa'
    maphuongxa = fields.Char(string='Mã Phường Xã')
    tenphuongxa = fields.Char(string='Tên Phường Xã')
    ghichu = fields.Char(string='Ghi Chú')
    quanhuyen_idquanhuyen = fields.Many2one('solienlac.quanhuyen', string='Quận\Huyện')



