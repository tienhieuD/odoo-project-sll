# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random, string



class hocsinh(models.Model):
    mahocsinh = fields.Char('Mã học sinh', required='True')
    hoten = fields.Char('Họ tên', required='True')
    gioitinh = fields.Selection([
        ('Nam', 'Nam'),
        ('Nu', 'Nữ'),
        ('KXD', 'Không xác định')], string="Giới tính")
    ngaysinh = fields.Date(string="Ngày sinh")
    noisinh = fields.Char('Nơi sinh')
    quequan = fields.Char('Quê quán')
    lop = fields.Many2one('solienlac.lop', string='Lớp')
    tuyenhoc = fields.Many2one('solienlac.tuyenhoc', string='Tuyến học')
    phuongxa = fields.Many2one('solienlac.phuongxa', string='Phường Xã')
    dantoc = fields.Many2one('solienlac.dantoc', string='Dân tộc')
    tongiao = fields.Many2one('solienlac.tongiao', string='Tôn giáo')
    chucvu = fields.Many2one('solienlac.chucvu', string='Chức vụ')

class lop(models.Model):
    malop = fields.Char('Mã lớp', required='True')
    tenlop = fields.Char('Tên lớp', required='True')
    nienkhoa = fields.Char('Niên khóa', required='True')
    ghichu = fields.Char('Ghi chú', required='True')
    khoi = fields.Many2one('solienlac.khoi', string='Khối')

class banhoc(models.Model):
    maban = fields.Char('Mã ban', required='True')
    tenban = fields.Char('Tên ban')
    monhoc = fields.Char('Môn học')
    ghichu = fields.Char('Ghi chú')

class monhoc(models.Model):
    mamonhoc = fields.Char('Mã môn học', required='True')
    tenmonhoc = fields.Char('Tên môn học', required='True')
    heso = fields.Char('Hệ số')
    ghichu = fields.Char('Ghi chú')
    bomon = fields.Many2one('solienlac.bomon', string='Bộ môn')
    banhoc = fields.Many2one('solienlac.banhoc', string='Ban hoc')



