# -*- coding: utf-8 -*-
import datetime
import time
from odoo import models, fields, api

class giaovien(models.Model):
    _name = 'solienlac.giaovien'
    sml = fields.Char("SML")
    magiaovien = fields.Char("Mã giáo viên")
    hoten = fields.Char("Họ tên")
    gioitinh = fields.Selection([
            ('Nam', 'Nam'),
            ('Nu', 'Nữ'),
            ('KXD', 'Không xác định')], string = "Giới tính")
    ngaysinh = fields.Date(string="Ngày sinh")
    noisinh = fields.Char("Nơi sinh")
    sodienthoai = fields.Char("Số điện thoại")
    socmnd = fields.Char("Số chứng minh thư/căn cước")
    email = fields.Char("Email")
    matkhau = fields.Char("Mật khẩu")
    phuongxa = fields.Many2one('solienlac.phuongxa', string = "Phường/Xã")
    dantoc = fields.Many2one('solienlac.dantoc', string = "Dân tộc")
    tongiao = fields.Many2one('solienlac.tongiao', string = "Tôn giáo")
    to = fields.Many2one('solienlac.to', string = "Tổ")
    phongban = fields.Many2one('solienlac.phongban', string = "Phòng ban")

class to(models.Model):
    _name = 'solienlac.to'
    mato = fields.Char("Mã tổ")
    tento = fields.Char("Tên tổ")
    ghichu = fields.Char("Ghi chú")
    totruong = fields.Many2one('solienlac.giaovien', string = "Tổ trưởng")

class phuongxa(models.Model):
    _name = 'solienlac.phuongxa'
    maphuongxa = fields.Char("Mã phường/xã")
    tenphuongxa = fields.Char("Tên phường/xã")
    ghichu = fields.Char("Ghi chú")
    quanhuyen = fields.Many2one('solienlac.quanhuyen', string = "Quận/Huyện")

class quanhuyen(models.Model):
    _name = 'solienlac.quanhuyen'
    maquanhuyen = fields.Char("Mã quận/huyện")
    tenquanhuyen = fields.Char("Tên quận/huyện")
    ghichu = fields.Char("Ghi chú")
    tinhthanhpho = fields.Many2one('solienlac.quanhuyen', string = "Tỉnh/Thành phố")

class tinhthanhpho(models.Model):
    _name = 'solienlac.tinhthanhpho'
    matinhthanhpho = fields.Char("Mã tỉnh/thành phố")
    tentinhthanhpho = fields.Char("Tên tỉnh/thành phố")
    ghichu = fields.Char("Ghi chú")

class dantoc(models.Model):
    _name = 'solienlac.dantoc'
    madantoc = fields.Char("Mã dân tộc")
    tendantoc = fields.Char("Tên dân tộc")
    ghichu = fields.Char("Ghi chú")

class tongiao(models.Model):
    _name = 'solienlac.dantoc'
    matongiao = fields.Char("Mã tôn giáo")
    tentongiao = fields.Char("Tên tôn giáo")
    ghichu = fields.Char("Ghi chú")

class phongban(models.Model):
    """docstring for phongban."""
    _name = 'solienlac.phongban'
    maphongban = fields.Char("Mã phòng ban")
    tenphongban = fields.Char("Tên phòng ban")
    sdt = fields.Char("Tên phòng ban")
    ghichu = fields.Char("Ghi chú")
    truongphong = fields.Many2one('solienlac.giaovien', string = "Trưởng phòng")
