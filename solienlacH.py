# -*- coding: utf-8 -*-
import datetime
import time
from odoo import models, fields, api

class giaovien(models.Model):
    _name = 'solienlac.giaovien'
    _rec_name = 'hoten' # optional
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
    bomon = fields.Many2many('solienlac.bomon', string = "Bộ môn")

class to(models.Model):
    _name = 'solienlac.to'
    _rec_name = 'tento' # optional
    mato = fields.Char("Mã tổ")
    tento = fields.Char("Tên tổ")
    ghichu = fields.Char("Ghi chú")
    totruong = fields.Many2one('solienlac.giaovien', string = "Tổ trưởng")

class phuongxa(models.Model):
    _name = 'solienlac.phuongxa'
    _rec_name = 'tenphuongxa' # optional
    maphuongxa = fields.Char("Mã phường/xã")
    tenphuongxa = fields.Char("Tên phường/xã")
    ghichu = fields.Char("Ghi chú")
    quanhuyen = fields.Many2one('solienlac.quanhuyen', string = "Quận/Huyện")

class quanhuyen(models.Model):
    _name = 'solienlac.quanhuyen'
    _rec_name = 'tenquanhuyen' # optional
    _description = 'Module description'
    maquanhuyen = fields.Char("Mã quận/huyện")
    tenquanhuyen = fields.Char("Tên quận/huyện")
    ghichu = fields.Char("Ghi chú")
    tinhthanhpho = fields.Many2one('solienlac.tinhthanhpho', string = "Tỉnh/Thành phố")

class tinhthanhpho(models.Model):
    _name = 'solienlac.tinhthanhpho'
    _rec_name = 'tentinhthanhpho' # optional
    matinhthanhpho = fields.Char("Mã tỉnh/thành phố")
    tentinhthanhpho = fields.Char("Tên tỉnh/thành phố")
    ghichu = fields.Char("Ghi chú")

class dantoc(models.Model):
    _name = 'solienlac.dantoc'
    _rec_name = 'tendantoc' # optional
    madantoc = fields.Char("Mã dân tộc")
    tendantoc = fields.Char("Tên dân tộc")
    ghichu = fields.Char("Ghi chú")

class tongiao(models.Model):
    _name = 'solienlac.tongiao'
    _rec_name = 'tentongiao' # optional
    matongiao = fields.Char("Mã tôn giáo")
    tentongiao = fields.Char("Tên tôn giáo")
    ghichu = fields.Char("Ghi chú")

class phongban(models.Model):
    """docstring for phongban."""
    _name = 'solienlac.phongban'
    _rec_name = 'tenphongban' # optional
    maphongban = fields.Char("Mã phòng ban")
    tenphongban = fields.Char("Tên phòng ban")
    sdt = fields.Char("Tên phòng ban")
    ghichu = fields.Char("Ghi chú")
    truongphong = fields.Many2one('solienlac.giaovien', string = "Trưởng phòng")

class doituongchinhsach(models.Model):
    _name = 'solienlac.doituongchinhsach'
    _rec_name = 'tendoituongchinhsach' # optional
    tendoituongchinhsach = fields.Char(string='Tên Đối Tượng Chinh Sách')
    miengiam = fields.Float(string='Miễn Giảm')
    ghichu = fields.Char(string='Ghi Chú')

class doituonguutien(models.Model):
    _name = 'solienlac.doituonguutien'
    _rec_name = 'tendoituonguutien' # optional
    tendoituonguutien = fields.Char(string='Tên Đối Tượng Ưu tiên')
    madoituonguutien = fields.Char(string='Mã Đối Tượng Ưu tiên')
    ghichu = fields.Char(string='Ghi Chú')

class khenthuongkyluat(models.Model):
    _name = 'solienlac.khenthuongkyluat'
    _rec_name = 'tenkhenthuongkyluat' # optional
    tenkhenthuongkyluat = fields.Char(string='Tên Khen Thưởng Kỷ Luật')
    hinhthuckhenthuongkyluat = fields.Char(string='Hình Thức Khen Thưởng Kỷ Luật')
    ghichu = fields.Char(string='Ghi Chú')

class khenthuongkyluat_hocsinh(models.Model):
    _name = 'solienlac.khenthuongkyluat_hocsinh'
    _rec_name = 'ngay_ktkl' # optional
    ktkl = fields.Many2one('solienlac.khenthuongkyluat', string='ID Khen Thưởng Kỷ Luật', required='True')
    hocsinh = fields.Many2one('solienlac.hocsinh', string='ID Học Sinh', required='True')
    ngay_ktkl = fields.Date(string='Ngày Khen Thưởng Kỷ Luật')

class tuyenhoc(models.Model):
    _name = 'solienlac.tuyenhoc'
    _rec_name = 'tentuyen' # optional
    matuyen = fields.Char(string='Mã Tuyến')
    tentuyen = fields.Char(string='Tên Tuyến')
    ghichu = fields.Char(string='Ghi Chú')

class khoi(models.Model):
    _name = 'solienlac.khoi'
    _rec_name = 'tenkhoi' # optional
    makhoi = fields.Char(string='Mã Khối', required='True')
    tenkhoi = fields.Char(string='Tên Khối')
    ghichu = fields.Char('Ghi Chú')

class hanhkiem(models.Model):
    _name = 'solienlac.hanhkiem'
    _rec_name = 'xeploai' # optional
    hocky = fields.Char('Học Kỳ')
    namhoc = fields.Char('Năm Học')
    xeploai = fields.Selection(
        string="Xếp loại",
        selection=[
                ('tot', 'Tốt'),
                ('kha', 'Khá'),
                ('tb', 'Trung bình'),
                ('yeu', 'Yếu'),
                ('kem', 'Kém'),
        ],
    )
    nhanxetcuagiaovien = fields.Char('Nhận Xét Của Giáo Viên')
    ghichu = fields.Char('Ghi Chú')
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học Sinh')

class phuhuynh(models.Model):
    _name = 'solienlac.phuhuynh'
    _rec_name = 'hoten' # optional
    hoten = fields.Char('Họ Tên')
    gioitinh = fields.Char('Giới Tính')
    ngaysinh = fields.Date('Ngày Sinh')
    sodienthoai = fields.Char('Số Điện Thoại')
    ghichu = fields.Char('Ghi Chú')
    phuongxa = fields.Many2one('solienlac.phuongxa', string='Xã\Phường')
    dantoc = fields.Many2one('solienlac.dantoc', string='Dân Tộc')
    tongiao = fields.Many2one('solienlac.tongiao', string='Tôn Giáo')

class bomon(models.Model):
    _name = 'solienlac.bomon'
    _rec_name = 'tenbomon' # optional
    mabomon = fields.Char('Mã bộ môn')
    tenbomon = fields.Char('Tên bộ môn')
    truongbomon = fields.Many2one('solienlac.giaovien', string = "Trưởng bộ môn")

class bangdiemdanh(models.Model):
    _name = 'solienlac.bangdiemdanh'
    _rec_name = 'mabangdiemdanh' # optional
    mabangdiemdanh= fields.Char('Mã bảng điểm danh')
    ngayvang= fields.Date('Ngày vắng')
    tietvang= fields.Integer('Tiết vắng')
    ghichu= fields.Char('Ghi chú')
    hocsinh= fields.Many2one('solienlac.hocsinh', string='Học sinh')
    monhoc= fields.Many2one('solienlac.monhoc', string = 'Môn học')
    giaoviendiemdanh= fields.Many2one('solienlac.giaovien', string = 'Giáo viên điểm danh')

class hocsinh(models.Model):
    _name = 'solienlac.hocsinh'
    _rec_name = 'hoten' # optional
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
    doituongchinhsach = fields.Many2many('solienlac.doituongchinhsach', string='Đối tượng chính sách')
    doituonguutien = fields.Many2many('solienlac.doituonguutien', string='Đối tượng ưu tiên')
    phuhuynh = fields.Many2many('solienlac.phuhuynh', string='Phụ huynh')
    hanhkiem = fields.One2many("solienlac.hanhkiem", "hocsinh", string="Hạnh kiểm")

class lop(models.Model):
    _name = 'solienlac.lop'
    _rec_name = 'tenlop' # optional
    malop = fields.Char('Mã lớp', required='True')
    tenlop = fields.Char('Tên lớp', required='True')
    nienkhoa = fields.Char('Niên khóa', required='True')
    ghichu = fields.Char('Ghi chú', required='True')
    khoi = fields.Many2one('solienlac.khoi', string='Khối')

class banhoc(models.Model):
    _name = 'solienlac.banhoc'
    _rec_name = 'tenban' # optional
    maban = fields.Char('Mã ban', required='True')
    tenban = fields.Char('Tên ban')
    monhoc = fields.Char('Môn học')
    ghichu = fields.Char('Ghi chú')

class monhoc(models.Model):
    _name = 'solienlac.monhoc'
    _rec_name = 'tenmonhoc' # optional
    mamonhoc = fields.Char('Mã môn học', required='True')
    tenmonhoc = fields.Char('Tên môn học', required='True')
    heso = fields.Float('Hệ số')
    ghichu = fields.Char('Ghi chú')
    bomon = fields.Many2one('solienlac.bomon', string='Bộ môn')
    banhoc = fields.Many2one('solienlac.banhoc', string='Ban hoc')


class ketquahoctap(models.Model):
    _name = 'solienlac.ketquahoctap'
    _rec_name = 'hocsinh' # optional
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')
    monhoc = fields.Many2one('solienlac.monhoc', string='Môn học')
    giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')
    diemtongket = fields.Float('Điểm tổng kết')
    kyhoc = fields.Integer('Năm học')
    namhoc = fields.Integer('Học kỳ')
    ngaycapnhat = fields.Date('Ngày cập nhật')
    ykiengiaovien = fields.Char('Ý kiến giáo viên')

class loaidiem(models.Model):
    _name = 'solienlac.loaidiem'
    _rec_name = 'tenloai' # optional
    maloai = fields.Char('Mã loai', required='True')
    tenloai = fields.Char('Tên loai', required='True')
    heso = fields.Float('Hệ số')
    ghichu = fields.Char('Ghi chú')

class diem(models.Model):
    _name = 'solienlac.diem'
    _rec_name = 'diem' # optional
    diem = fields.Float('Điểm')
    ngaynhap = fields.Date('Ngày nhập')
    ghichu = fields.Char('Ghi chú')
    ketquahoctap = fields.Many2one('solienlac.ketquahoctap', string='Kết quả học tập')
    loaidiem = fields.Many2one('solienlac.loaidiem', string='Loại điểm')
    giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')

class chucvu(models.Model):
    _name = 'solienlac.chucvu'
    _rec_name = 'tenchucvu' # optional
    machucvu = fields.Char('Mã chức vụ', required='True')
    tenchucvu = fields.Char('Tên chức vụ', required='True')
    ghichu = fields.Char('Ghi chú')

class nenep(models.Model):
    _name = 'solienlac.nenep'
    _rec_name = 'hocsinh' # optional
    dongphuc = fields.Integer('Đồng phục')
    dihocmuon = fields.Integer('Đồng phục')
    noichuyen = fields.Integer('Đồng phục')
    noituc = fields.Integer('Đồng phục')
    # dongphuc = fields.Integer('Đồng phục')
    truybai = fields.Integer('Đồng phục')
    ntvt = fields.Integer('Đồng phục')
    hocky = fields.Integer('Đồng phục')
    namhoc = fields.Integer('Đồng phục')
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')
