# -*- coding: utf-8 -*-
import datetime
import time
from odoo import models, fields, api
class caphoc(models.Model):
    _name = 'solienlac.caphoc'
    _rec_name = 'tencaphoc'

    macaphoc = fields.Integer('Mã cấp học', required='True')
    tencaphoc = fields.Selection([
        ('1', 'Nhà trẻ'),
        ('2', 'Mẫu giáo'),
        ('3', 'Tiểu học'),
        ('4', 'Trung học cơ sở'),
        ('5', 'Trung học phổ thông'),
        ('6', 'Trung cấp chuyên nghiệp'),
        ('7', 'Cao đẳng'),
        ('8', 'Đại học'),
        ('9', 'Sau đại học'),
    ],default='1', string='Tên cấp học')
    ghichu = fields.Char('Ghi chú')

class captruong(models.Model):
    _name = 'solienlac.captruong'
    _rec_name = 'tencaptruong'

    macaptruong = fields.Integer('Mã cấp trường', required='True')
    tencaptruong = fields.Selection([
        ('1', 'Nhà trẻ'),
        ('2', 'Trường Mẫu giáo'),
        ('3', 'Trường Mầm non'),
        ('4', 'Trường Tiểu học'),
        ('5', 'Trường Trung học cơ sở'),
        ('6', 'Trường Trung học phổ thông'),
        ('7', 'Trường đa cấp (Tiểu học và THCS)'),
        ('8', 'Trường đa cấp (THCS và THPT)'),
        ('9', 'Trường đa cấp (Tiểu học,THCS và THPT)'),
        ('10', 'Trung tâm Giáo dục thường xuyên'),
        ('11', 'Trung tâm Kỹ thuật tổng hợp - Hướng nghiệp'),
        ('12', 'Trung cấp chuyên nghiệp'),
        ('13', 'Cao đẳng'),
        ('14', 'Đại học'),
        ('15', 'Nhóm trẻ độc lập'),
        ('16', 'Lớp mẫu giáo độc lập'),
        ('17', 'Lớp mầm non độc lập'),
    ],default='1', string='Tên cấp trường')
    ghichu = fields.Char('Ghi chú')

class truong(models.Model):
    _name = 'solienlac.truong'
    _rec_name = 'tentruong'

    matruong = fields.Char('Mã trường', required='True')
    tentruong = fields.Char('Tên trường')
    hieutruong = fields.Char('Hiệu trưởng')
    namthanhlap = fields.Integer('Năm thành lập')

    diachi = fields.Char('Địa chỉ')
    fax = fields.Char('Fax')
    email = fields.Char('Email')
    sodienthoai = fields.Char('Số điện thoại')
    website = fields.Char('Website')

    # matinhthanhpho = fields.Many2one('solienlac.tinhthanhpho', string='Tỉnh/Thành phố')
    # maquanhuyen = fields.Many2one('solienlac.quanhuyen', string='Quận/Huyện')
    # maphuongxa = fields.Many2one('solienlac.phuongxa', string='Xã/Phường')

    matinhthanhpho = fields.Integer('Tỉnh/Thành phố ID')
    maquanhuyen = fields.Integer('Quận/Huyện ID')
    maphuongxa = fields.Integer('Xã/Phường ID')


    hethonggiaoduc = fields.Integer('Hệ thống giáo dục ID')
    hangtruong = fields.Integer('Hạng trường ID')
    captruong = fields.Many2one('solienlac.captruong', string='Cấp trường ID')
    caphoc = fields.Many2one('solienlac.caphoc', string='Cấp học ID')
    truongchuyenbiet = fields.Integer('Trường chuyên biệt ID')
    loaihinhtruong = fields.Integer('Loại hình trường ID')

    loailopnho = fields.Integer('Loại lớp nhô')
    donviID = fields.Integer('Đơn vị')
    thanhthi = fields.Boolean('Thành thị')
    chatluongcao = fields.Boolean('Chất lượng cao')
    bdkk = fields.Boolean('BDKK')
    trangthai = fields.Boolean('Trạng thái')

    toado_x = fields.Integer('Tọa độ x')
    toado_y = fields.Integer('Tọa độ y')
    biengioi = fields.Boolean('Biên giới')


    giaovien = fields.One2many(string="Giáo viên của trường", comodel_name="solienlac.giaovien", inverse_name="truong")
    hocsinh = fields.One2many(string="Học sinh của trường", comodel_name="solienlac.hocsinh", inverse_name="truong")
    khoi = fields.One2many(string="Khối", comodel_name="solienlac.khoi", inverse_name="truong")


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
    chucvu = fields.Many2one('solienlac.chucvu', "Chức vụ")
    dien = fields.Selection([
            ('cohuu', 'Cơ hữu'),
            ('thinhgiang', 'Thỉnh giảng')], srting="Diện")
    vanbang = fields.Selection([
            ('trunghoccoso', 'Trung học cơ sở'),
            ('trunghocphothong', 'Trung học phổ thông'),
            ('trungcap', 'Trung cấp'),
            ('caodang', 'Cao đẳng'),
            ('daihoc', 'Đại học'),
            ('thacsi', 'Thạc sĩ'),
            ('tiensi', 'Tiến sĩ')], srting="Văn bằng")
    namvaonganh = fields.Date('Năm vào ngành')
    tinhtranghonnhan = fields.Selection(
        string="Tình trạng hôn nhân",
        selection=[
                ('chualapgiadinh', 'Chưa lập gia đình'),
                ('dalapgiadinh', 'Đã lập gia đình'),
                ('lyhon', 'Ly hôn'),
        ],
    )
    phuongxa = fields.Many2one('solienlac.phuongxa', string = "Phường/Xã")
    dantoc = fields.Many2one('solienlac.dantoc', string = "Dân tộc")
    tongiao = fields.Many2one('solienlac.tongiao', string = "Tôn giáo")
    to = fields.Many2one('solienlac.to', string = "Tổ")
    phongban = fields.Many2one('solienlac.phongban', string = "Phòng ban")
    bomon = fields.Many2many('solienlac.bomon', string = "Bộ môn")
    monhoc = fields.One2many('solienlac.monhoc_has_giaovien', 'giaovien', string = "Lớp")
    lops = fields.One2many(string="Lớp", comodel_name="solienlac.monhoc_has_giaovien", inverse_name="giaovien")
    truong = fields.Many2one('solienlac.truong', string = "Trường")
class monhoc_has_giaovien(models.Model):
    _name = 'solienlac.monhoc_has_giaovien'
    _rec_name = 'lop'
    # namhoc = fields.Char('Năm học')

    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------


    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    monhoc = fields.Many2one('solienlac.monhoc', string='Môn học')
    giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')
    lop = fields.Many2one('solienlac.lop', string='Lớp')
    ngaybatdau = fields.Date('Ngày bắt đầu:')
    ngayketthuc = fields.Date('Ngày kết thúc: ')
class lop_has_giaovien(models.Model):
    _name = 'solienlac.lop_has_giaovien'
    _rec_name = 'giaovien'
    lop = fields.Many2one('solienlac.lop', string='Lớp')
    giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')
    # namhoc = fields.Char('Năm học')
    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    ngaybatdau = fields.Date('Ngày bắt đầu:')
    ngayketthuc = fields.Date('Ngày kết thúc: ')

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
    # maphuongxa = fields.Char("Mã phường/xã")
    tenphuongxa = fields.Char("Tên phường/xã")
    ghichu = fields.Char("Ghi chú")
    # quanhuyen = fields.Many2one('solienlac.quanhuyen', string = "Quận/Huyện")
    TinhID = fields.Integer('Tỉnh ID')
    QuanHuyenID = fields.Integer('Quận huyện ID')
    PhuongXaID = fields.Integer('Phường xã ID')
    VungDiaLyID = fields.Integer('Vùng địa lý ID')
    TenPhuongXa_VT=fields.Integer('Tên phường xã VT')
    KhoKhan=fields.Boolean('Khó khăn')
    BienGioi =fields.Boolean('Biên giới')
    HspcKvuc=fields.Char('Hệ số phụ cấp khu vực')

class quanhuyen(models.Model):
    _name = 'solienlac.quanhuyen'
    _rec_name = 'tenquanhuyen' # optional
    _description = 'Module description'
    maquanhuyen = fields.Integer("Mã quận/huyện")
    tenquanhuyen = fields.Char("Tên quận/huyện")
    ghichu = fields.Char("Ghi chú")
    # tinhthanhpho = fields.Many2one('solienlac.tinhthanhpho', string = "Tỉnh/Thành phố")
    tenquanhuyenVT=fields.Integer("Tên quận/huyện viết tắt")
    vungdialy = fields.Integer(string="Vùng địa lý")
    matinhthanhpho = fields.Integer(string="Mã tỉnh/thành phố")

class tinhthanhpho(models.Model):
    _name = 'solienlac.tinhthanhpho'
    _rec_name = 'tentinhthanhpho' # optional
    matinhthanhpho = fields.Integer("Mã tỉnh/thành phố")
    tentinhthanhpho = fields.Char("Tên tỉnh/thành phố")
    tentinhviettat = fields.Char('Tên tỉnh viết tắt')
    vungdialy = fields.Integer("Vùng địa lý")
    vungkinhte = fields.Integer("Vùng kinh tế")
    ghichu = fields.Char("Ghi chú")

class dantoc(models.Model):
    _name = 'solienlac.dantoc'
    _rec_name = 'tendantoc' # optional
    madantoc = fields.Integer("Mã dân tộc")
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
    sodienthoai = fields.Char("Số điện thoại")
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

class kyluathocsinh(models.Model):
    _name = 'solienlac.kyluathocsinh'
    _rec_name = 'lydokyluat' # optional
    lydokyluat = fields.Char(string='Lý do kỷ luật')
    hinhthuckyluat = fields.Selection(
        string="Hình thức kỷ luật",
        selection=[
                ('1', 'Phê bình trước lớp, trước trường'),
                ('2', 'Khiển trách và thông cáo với gia đình'),
                ('3', 'Cảnh cáo, ghi học bạ'),
                ('4', 'Buộc thôi học có thời hạn'),
                ('5', 'Khác'),
        ],
    )
    thoihantu = fields.Date(string="Thời hạn từ", )
    thoihanden = fields.Date(string="Thời hạn đến", )
    ghichu = fields.Char(string='Ghi Chú')
    hocsinh = fields.Many2many("solienlac.hocsinh",string="Học sinh")

class khenthuonghocsinh(models.Model):
    _name = 'solienlac.khenthuonghocsinh'
    _rec_name = 'lydokhenthuong' # optional
    lydokhenthuong = fields.Char(string="Lý do khen thưởng", )
    hinhthuckhenthuong = fields.Selection(
        string="Hình thức khen thưởng",
        selection=[
                ('1', 'Khen trước lớp, trước trường'),
                ('2', 'Được tặng danh hiệu'),
                ('3', 'Được ghi tên vào bảng danh dự của trường'),
                ('4', 'Được khen thưởng đặc biệt'),
                ('5', 'Khác'),
        ],
    )
    ngaykhenthuong = fields.Date(string="Ngày khen thưởng", )
    ghichu = fields.Char(string="Ghi chú", )
    hocsinh = fields.Many2many("solienlac.hocsinh",string="Học sinh")

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
    makhoi = fields.Integer(string='Mã Khối', )
    tenkhoi = fields.Char(string='Tên Khối')
    ghichu = fields.Char('Ghi Chú')
    truong = fields.Many2one('solienlac.truong', string = "Trường")

class hanhkiem(models.Model):
    _name = 'solienlac.hanhkiem'
    _rec_name = 'xeploai' # optional
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char('Năm học')

    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

    xeploai = fields.Selection(
        string="Xếp loại",
        selection=[
                ('tot', 'Tốt'),
                ('kha', 'Khá'),
                ('tb', 'Trung bình'),
                ('yeu', 'Yếu'),
                # ('kem', 'Kém'),
        ],
    )
    nhanxetcuagiaovien = fields.Char('Nhận Xét Của Giáo Viên')
    ghichu = fields.Char('Ghi Chú')
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học Sinh')

class phuhuynh(models.Model):
    _name = 'solienlac.phuhuynh'
    _rec_name = 'hoten' # optional
    hoten = fields.Char('Họ Tên')
    gioitinh = fields.Selection([
            ('Nam', 'Nam'),
            ('Nu', 'Nữ'),
            ('KXD', 'Không xác định')], string = "Giới tính")
    ngaysinh = fields.Date('Ngày Sinh')
    sodienthoai = fields.Char('Số Điện Thoại')
    ghichu = fields.Char('Ghi Chú')
    phuongxa = fields.Many2one('solienlac.phuongxa', string='Xã\Phường')
    dantoc = fields.Many2one('solienlac.dantoc', string='Dân Tộc')
    tongiao = fields.Many2one('solienlac.tongiao', string='Tôn Giáo')

    nghenghiep = fields.Selection([
          	('value1', 'Công chức'),
            ('value2', 'Viên chức'),
            ('value3', 'Công nhân'),
            ('value4', 'Nông dân'),
            ('value5', 'Công an'),
            ('value6', 'Bộ đội'),
            ('value7', 'Doanh nhân'),
            ('value8', 'Lao động tự do'),
            ('value9', 'Nội trợ'),
            ('value10', 'Khác'),
        ], string = "Nghề nghiệp")
    quanhe = fields.Selection([
          	('value1', 'Bố đẻ'),
            ('value2', 'Mẹ đẻ'),
            ('value3', 'Anh ruột'),
            ('value4', 'Chị ruột'),
            ('value5', 'Em trai ruột'),
            ('value6', 'Em gái ruột'),
            ('value7', 'Bố dượng'),
            ('value8', 'Mẹ dượng'),
            ('value9', 'Bố nuôi'),
            ('value10', 'Mẹ nuôi'),
            ('value11', 'Vợ'),
            ('value12', 'Chồng'),
        ], string = "Nghề nghiệp")

    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học Sinh')

class bomon(models.Model):
    _name = 'solienlac.bomon'
    _rec_name = 'tenbomon' # optional
    mabomon = fields.Integer('Mã bộ môn')
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
    danhhieuhocsinh = fields.One2many('solienlac.danhhieuhocsinh', 'hocsinh', string = 'Danh hiệu học sinh')
    khenthuonghocsinh = fields.Many2many('solienlac.khenthuonghocsinh', string = 'Thành tích khen thưởng')
    kyluathocsinh = fields.Many2many('solienlac.kyluathocsinh', string = 'Kỷ luật học sinh')
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
    truong = fields.Many2one('solienlac.truong', string = "Trường")
    tuyenhoc = fields.Many2one('solienlac.tuyenhoc', string='Tuyến học')

    phuongxa = fields.Many2one('solienlac.phuongxa', string='Phường\Xã')
    quanhuyen = fields.Many2one('solienlac.quanhuyen', string='Quận\Huyện')
    tinhthanhpho = fields.Many2one('solienlac.tinhthanhpho', string='Tỉnh\Thành phố')

    dantoc = fields.Many2one('solienlac.dantoc', string='Dân tộc')
    tongiao = fields.Many2one('solienlac.tongiao', string='Tôn giáo')
    chucvu = fields.Many2one('solienlac.chucvu', string='Chức vụ')
    doituongchinhsach = fields.Many2many('solienlac.doituongchinhsach', string='Đối tượng chính sách')
    doituonguutien = fields.Many2many('solienlac.doituonguutien', string='Đối tượng ưu tiên')
    phuhuynh = fields.Many2many('solienlac.phuhuynh', string='Phụ huynh')
    hanhkiem = fields.One2many("solienlac.hanhkiem", "hocsinh", string="Hạnh kiểm")
    ketquahoctap = fields.One2many('solienlac.ketquahoctap', 'hocsinh', string="Kết quả học tập")
    bangdiem = fields.One2many('solienlac.bangdiem', 'hocsinh', string="Bảng điểm")
    nenep = fields.One2many('solienlac.nenep', 'hocsinh', string="Nề nếp")
    noitru = fields.Boolean('Nội trú')
    tinhtranghocsinh = fields.Selection(
        string="Tình trạng học sinh",
        selection=[
                ('value1', 'Học bình thường'),
                ('value2', 'Đã nghỉ học'),
        ],default='value1'
    )
    nguongochocsinh = fields.Many2one('solienlac.nguongochocsinh', string='Nguồn gốc học sinh')
    nangkhieu = fields.Selection(
        string="Năng khiếu",
        selection=[
                ('value1', 'Không có năng khiếu'),
                ('value2', 'Thể dục, thể thao'),
                ('value3', 'Âm nhạc'),
                ('value4', 'Mỹ thuật'),
                ('value5', 'Toán'),
                ('value6', 'Lý'),
                ('value7', 'Hóa'),
                ('value8', 'Sinh'),
                ('value9', 'Văn'),
                ('value10', 'Sử'),
                ('value11', 'Địa'),
                ('value12', 'Ngoại ngữ'),
                ('value13', 'Tin'),
                ('value14', 'Tự nhiên'),
                ('value15', 'Xã hội'),
                ('value16', 'Hoạt động xã hội'),
                ('value17', 'Khác'),
                ('value18', 'Không xác định'),
        ],default='value1',
    )
    monhocnghe = fields.Many2one(string="Môn học nghề",comodel_name="solienlac.monhocnghe")
    loaihocsinhnhaptruong = fields.Selection(
        string="Loại học sinh nhập trường",
        selection=[
                ('value1', 'Tuyển mới'),
                ('value2', 'Chuyển đến'),
                ('value3', 'Lên lớp'),
                ('value4', 'Ở lại lớp'),
                ('value5', 'Thí sinh tự do	Trong thi tốt nghiệp'),
                ('value6', 'Thi lại	Xét lên lớp'),
                ('value7', 'Rèn luyện lại	Xét lên lớp'),
                ('value8', 'TL&RLL	Xét lên lớp'),
        ],default='value1'
    )
    khuyettat = fields.Selection(
        string="Khuyết tật",
        selection=[
                ('value1', 'Không'),
                ('value2', 'Khiếm thính'),
                ('value3', 'Khiếm thị'),
                ('value4', 'Khó khăn vê hoạt động'),
                ('value5', 'Khó khăn về trí tuệ'),
                ('value6', 'Đa tật'),
                ('value7', 'Khuyết tật khác'),
                ('value8', 'Không xác định'),
        ],default='value1'
    )
    tochucdoanthe = fields.Many2one('solienlac.tochucdoanthe', string='Tổ chức')
    thoihoc = fields.Selection(
        string="Thôi học",
        selection=[
                ('value1', 'Không'),
                ('value2', 'Khiếm thính'),
                ('value3', 'Khiếm thị'),
                ('value4', 'Khó khăn vê hoạt động'),
                ('value5', 'Khó khăn về trí tuệ'),
                ('value6', 'Đa tật'),
                ('value7', 'Khuyết tật khác'),
                ('value8', 'Không xác định'),
        ],
    )
    lydothoihoc = fields.Many2one(string="Lý do thôi học",comodel_name="solienlac.lydothoihoc")

    @api.multi
    @api.onchange('tinhthanhpho')
    def set_value_huyen(self):
        self.quanhuyen = []
        tmp1 = self.env['solienlac.quanhuyen'].search([
                    ('matinhthanhpho', '=', self.tinhthanhpho.matinhthanhpho),
                ])
        lst = map(lambda x:x.matinhthanhpho, tmp1)
        return {'domain':{'quanhuyen': [('matinhthanhpho', 'in', lst)]}}
    @api.multi
    @api.onchange('tinhthanhpho', 'quanhuyen')
    def set_value_xa(self):
        self.phuongxa = []
        tmp1 = self.env['solienlac.phuongxa'].search([
                    ('TinhID', '=', self.tinhthanhpho.matinhthanhpho),
                    ('QuanHuyenID', '=', self.quanhuyen.maquanhuyen),
                ])
        lst = map(lambda x: x.QuanHuyenID, tmp1)
        return {'domain':{'phuongxa': [('QuanHuyenID', 'in', lst)]}}


class lydothoihoc(models.Model):
    _name = 'solienlac.lydothoihoc'
    _rec_name = 'lydothoihoc'
    lydothoihoc = fields.Selection(
        string="Lý do thôi học",
        selection=[
                ('value1', 'Không'),
                ('value2', 'Chuyển đi'),
                ('value3', 'Kỷ luật buộc thôi học 1 năm'),
                ('value4', 'Học lực yếu kém'),
                ('value5', 'Xa nhà'),
                ('value6', 'Gia đình hoàn cảnh khó khăn'),
                ('value7', 'Lý do khác: tai nạn, ốm đau'),
        ],default='value1'
    )
    thoidiemthoihoc = fields.Date('Thời điểm thôi học')
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char('Năm học')

    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

    ghichu = fields.Char('Ghi chú')
    hocsinh = fields.One2many('solienlac.hocsinh', 'lydothoihoc', string='Học sinh')

class nguongochocsinh(models.Model):
    _name = 'solienlac.nguongochocsinh'
    _rec_name = 'nguongochocsinh'
    nguongochocsinh = fields.Selection(
        string="Nguồn gốc học sinh",
        selection=[
                ('value1', 'Tuyển sinh'),
                ('value2', 'Được lên lớp'),
                ('value3', 'Ở lại lớp'),
                ('value4', 'Chuyển đến'),
        ],default='value1',
    )
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char('Năm học')
    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

    thoidiemnhaptruong = fields.Date('Thời điểm nhập trường')
    hocsinh = fields.One2many('solienlac.hocsinh', 'nguongochocsinh', string='Học sinh')
    ghichu = fields.Char('Ghi chú')
class monhocnghe(models.Model):
    _name = 'solienlac.monhocnghe'
    _rec_name = 'tenmonhocnghe'
    mamonhocnghe = fields.Char("Mã môn học ", required='True')
    tenmonhocnghe = fields.Selection(
        string="Môn học nghề",
        selection=[
                ('value1', 'Không học nghề'),
                ('value2', 'Tin học ứng dụng'),
                ('value3', 'Mộc'),
                ('value4', 'May'),
                ('value5', 'Nấu ăn'),
                ('value6', 'Nhiếp ảnh'),
                ('value7', 'Điện dân dụng'),
                ('value8', 'Điện tử'),
                ('value9', 'Thêu'),
                ('value10', 'Nề'),
                ('value11', 'Đan len'),
                ('value12', 'Đan lưới'),
                ('value13', 'Lâm sinh'),
        ],default='value1'
    )
    ghichu = fields.Char('Ghi chú')

class tochucdoanthe(models.Model):
    _name = 'solienlac.tochucdoanthe'
    _rec_name = 'vitridoanthe'
    vitridoanthe = fields.Selection(
        string="Vị trí đoàn thể",
        selection=[
                ('value1', 'Không'),
                ('value2', 'Đội viên'),
                ('value3', 'Đoàn viên'),
                ('value4', 'Đảng viên'),
                ('value5', 'Không xác định'),
        ],default='value1'
    )
    chucvudoanthe = fields.Selection(
        string="Field name",
        selection=[
                ('value1', 'Không'),
                ('value2', 'Liên đội trưởng'),
                ('value3', 'Liên đội phó'),
                ('value4', 'Bí thư đoàn trường'),
                ('value5', 'Phó Bí thư đoàn trường'),
                ('value6', 'Bí thư chi đoàn'),
                ('value7', 'Phó Bí thư chi đoàn'),
                ('value8', 'Chi đội trưởng'),
                ('value9', 'Chi đội phó'),
        ],
    )
    ngaygianhap = fields.Date('Ngày gia nhập')
    ghichu = fields.Char('Ghi chú')

class lop(models.Model):
    _name = 'solienlac.lop'
    # _inherit = 'solienlac.hocsinh'
    _rec_name = 'tenlop' # optional
    malop = fields.Char('Mã lớp', required='True')
    tenlop = fields.Char('Tên lớp', required='True')
    nienkhoa = fields.Char('Niên khóa')
    ghichu = fields.Char('Ghi chú')
    khoi = fields.Many2one('solienlac.khoi', string='Khối')
    # truong = fields.Many2one('solienlac.truong', string = "Trường")
    hocsinh = fields.One2many('solienlac.hocsinh', 'lop', string='Học sinh')
    monhoc = fields.One2many('solienlac.monhoc_has_giaovien', 'lop', string='Môn học')
    giaovien = fields.One2many('solienlac.lop_has_giaovien', 'lop', string='Giáo viên')

    siso = fields.Integer(string='Sĩ số')
    lopdacbiet = fields.Selection(
        string="Lớp đặc biệt",
        selection=[
                ('khong', 'Không'),
                ('nhomghep', 'Nhóm ghép'),
                ('nhombantru', 'Nhóm bán trú'),
                ('nhom1buoi', 'Nhóm 1 buổi/ngày'),
                ('nhom2buoi', 'Nhóm 2 buổi/ngày'),
                ('nhomhoanhapchotrekhuyettat', 'Nhóm hòa nhập cho trẻ khuyết tật'),
                ('lopghep', 'Lớp ghép'),
                ('lopbantru', 'Lớp bán trú'),
                ('lop1buoi', 'Lớp 1 buổi/ngày'),
                ('lop2buoi', 'Lớp 2 buổi/ngày'),
                ('lophoanhap', 'Lớp hòa nhập '),
                ('lopchotrekhuyettat', 'Lớp cho trẻ Khuyết tật'),
                ('lopdantocnoitru', 'Lớp dân tộc nội trú'),
                ('lophocnghephothong', 'Lớp học nghề phổ thông'),
                ('lopnoitru', 'Lớp nội trú'),
                ('loptinhthuong', 'Lớp tình thương'),
                ('lopsauxoamuchu', 'Lớp sau xoá mù chữ'),
        ], default = 'khong'
    )
    lopnho = fields.Selection(
        string="Lớp nhô",
        selection=[
                ('khong', 'Không'),
                ('nhotren', 'Nhô trên'),
                ('nhoduoi', 'Nhô duoi'),
                ('nhotrenduoi', 'Nhô trên và dưới'),
        ],default='khong'
    )
    hengoaingu = fields.Selection(
        string="Hệ ngoại ngữ",
        selection=[
                ('1', 'Tiếng Anh'),
                ('2', 'Tiếng Pháp'),
                ('3', 'Tiếng Trung'),
                ('4', 'Tiếng Nga'),
                ('5', 'Tiếng Nhật'),
                ('6', 'Tiếng Đức'),
                ('7', 'Tiếng Hàn'),
                ('8', 'Tiếng khác'),
                ('9', 'Không học'),
        ],
    )
    banhoc = fields.Many2one('solienlac.banhoc', string='Phân ban')

class banhoc(models.Model):
    _name = 'solienlac.banhoc'
    _rec_name = 'tenban' # optional
    maban = fields.Char('Mã ban', required='True')
    tenban = fields.Selection([
        ('tunhien', 'Ban tự nhiên'),
        ('xahoi', 'Ban xã hội'),
        ('coban_kpb', 'Ban cơ bản(Không phân ban)'),
        ('coban_a', 'Ban cơ bản(A)'),
        ('coban_b', 'Ban cơ bản(B)'),
        ('coban_c', 'Ban cơ bản(C)'),
        ('coban_d', 'Ban cơ bản(D)'),
    ], default = 'coban_kpb' ,string='Phân ban')
    lop = fields.One2many('solienlac.lop', 'banhoc', string='Lớp')
    ghichu = fields.Char('Ghi chú')

class monhoc(models.Model):
    _name = 'solienlac.monhoc'
    _rec_name = 'tenmonhoc' # optional

    mamonhoc = fields.Integer('Mã môn học',)
    tenmonhoc = fields.Char('Tên môn học')
    heso = fields.Float('Hệ số')
    ghichu = fields.Char('Ghi chú')
    bomon = fields.Many2one('solienlac.bomon', string='Bộ môn')
    banhoc = fields.Many2many('solienlac.banhoc', string='Ban hoc')
    giaovien = fields.One2many('solienlac.monhoc_has_giaovien', 'monhoc', string='Giáo viên')

class ketquahoctap(models.Model):
    _name = 'solienlac.ketquahoctap'
    _rec_name = 'monhoc' # optional
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')
    monhoc = fields.Many2one('solienlac.monhoc', string='Môn học')
    giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')
    diemtongket = fields.Float('Điểm tổng kết')
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char('Năm học')

    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

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
    machucvu = fields.Integer('Mã chức vụ', )
    tenchucvu = fields.Char('Tên chức vụ', )
    ghichu = fields.Char('Ghi chú')

class nenep(models.Model):
    _name = 'solienlac.nenep'
    _rec_name = 'namhoc' # optional
    dongphuc = fields.Integer('Đồng phục')
    dihocmuon = fields.Integer('Đi học muộn')
    noichuyen = fields.Integer('Nói chuyện')
    noituc = fields.Integer('Nói tục')
    # dongphuc = fields.Integer('Đồng phục')
    truybai = fields.Integer('Truy bài')
    ntvt = fields.Integer('NTVT')
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char('Năm học')

    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')

class diemthanhphan(models.Model):
    _name = 'solienlac.diemthanhphan'
    bangdiem_thanhphan = fields.Many2one('solienlac.bangdiem_thanhphan', string='Kết quả thành phần')
    diem = fields.Float(string="Điểm sô")
    heso = fields.Float(string="Hệ số")
    ngaycapnhat = fields.Datetime(string="Ngày cập nhật")
    loaidiem = fields.Selection(
        string="Loại điểm",
        selection=[
                ('mieng', 'Điểm kiểm tra miệng'),
                ('15p', 'Điểm kiểm tra HS1'),
                ('1t', 'Điểm kiểm tra HS2'),
                ('hk', 'Điểm kiểm tra Học kỳ'),
                ('tn', 'Điểm kiểm tra khác'),
        ],
    )

class bangdiem_thanhphan(models.Model):
    _name = 'solienlac.bangdiem_thanhphan'
    monhoc = fields.Many2one('solienlac.monhoc', string='Môn học')
    bangdiem = fields.Many2one('solienlac.bangdiem', string='Kết quả học tập')
    diemthanhphan = fields.One2many("solienlac.diemthanhphan", "bangdiem_thanhphan", string="Điểm thành phần")
    diemtongket = fields.Float(string="Điểm tổng kết môn")
    ghichu = fields.Char(string="Ghi chú")
    giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên bộ môn')
    ykiengiaovien = fields.Char('Ý kiến giáo viên bộ môn')
    ngaycapnhat = fields.Datetime(string="Ngày cập nhật")

class bangdiem(models.Model):
    _name = 'solienlac.bangdiem'
    kyhoc = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char('Năm học')
    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

    kythi = fields.Selection(
        string="Kỳ thi",
        selection=[
                ('1', 'Học kỳ'),
                ('2', 'Thi Tốt nghiệp'),
                ('3', 'Thi HSG'),
                ('4', 'Thi nghề phổ thông'),
                ('99', 'Thi khác'),
        ],
    )
    bangdiem_thanhphan = fields.One2many("solienlac.bangdiem_thanhphan", "bangdiem", string="Bảng điểm thành phần")
    diemtongket = fields.Float('Điểm tổng kết')
    xeploai = fields.Selection([
        ('tot', 'Tốt'),
        ('kha', 'Khá'),
        ('tb', 'Trung bình'),
        ('yeu', 'Yếu'),
        # ('kem', 'Kém'),
    ],string='Xếp loại học lực')
    giaovien = fields.Many2one('solienlac.giaovien', string='Giáo viên')
    ykiengiaovien = fields.Char('Ý kiến giáo viên')
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')
    ghichu = fields.Char(string="Ghi chú", )
    ngaycapnhat = fields.Date('Ngày cập nhật')

class danhhieuhocsinh(models.Model):
    _name = 'solienlac.danhhieuhocsinh'
    _rec_name = 'hocky' # optional
    # _description = 'Danh hiệu của học sinh tính theo kỳ'
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char(string="Năm học", )

    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

    danhhieu = fields.Selection(
        string="Danh hiệu",
        selection=[
                ('kc', 'Chưa đạt danh hiệu gì'),
                ('hsxs', 'Học sinh xuất sắc'),
                ('hsg', 'Học sinh giỏi'),
                ('hstt', 'Học sinh tiên tiến'),
        ],
    )
    ykiengiaovien = fields.Char('Ý kiến giáo viên')
    ghichu = fields.Char('Ghi chú')
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')

class nhapdiemhocsinh(models.Model):
    _name = 'solienlac.nhapdiemhocsinh'
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc
    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    napdulieu = fields.Boolean('Nạp lại dữ liệu')
    giaovien = fields.Many2one(
        string="Giáo viên",
        comodel_name="solienlac.giaovien",
    )
    lop = fields.Many2one(
        string="Lớp",
        comodel_name="solienlac.lop",
    )
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    # namhoc = fields.Char(string="Năm học", )

    #---------- define fields namhoc ------------
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc

    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)

    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    #---------- end define fields namhoc ------------

    monhoc = fields.Many2one(
        string="Môn học",
        comodel_name="solienlac.monhoc",
    )
    nhapdiemchitiet = fields.Many2many(
        comodel_name='solienlac.nhapdiemchitiet',
        string='Chi tiết',
        store=True,
    )

    @api.multi
    @api.onchange('lop','namhoc','hocky','monhoc','napdulieu')
    def _compute_model(self):
        '''My defining function'''
        # Get hocsinh object
        def get_hs(self, id):
            return self.env['solienlac.hocsinh'].search([('id','=',id)])[0]

        '''Sumany'''
        # Load data
        self.napdulieu = False

        # Get (hocsinh object list)
        lst_hs = self.env['solienlac.hocsinh'].search([
            ('tinhtranghocsinh', '=', 'value1'), #value1 = học bình thường
            ('lop.id', '=', self.lop.id),
        ])

        # Get (nhapdiemchitiet object list)
        lst_hs_nhapdiem = self.env['solienlac.nhapdiemchitiet'].search([
            ('hocsinh.lop.id','=',self.lop.id),
            ('hocsinh.tinhtranghocsinh', '=', 'value1'), # value1 = học bình thường
            ('hocky','=',self.hocky), # notice, how about a year
            ('namhoc','=',self.namhoc),
            ('monhoc.id','=',self.monhoc.id),
        ])

        # Get (hocsinh object list) just hocsinh id
        lst_hs_id = map(lambda x: x.id, lst_hs)

        # Get (nhapdiemchitiet object list) just hocsinh id
        lst_hs_nhapdiem_id = map(lambda x: x.hocsinh.id, lst_hs_nhapdiem)

        # Get hocsinh id is not exsit in nhapdiemchitiet
        lst_hs_thieu = filter(lambda x: x not in lst_hs_nhapdiem_id, lst_hs_id)

        if len(lst_hs_thieu) == 0:
            # In case the teacher wanna edit the score
            # hocsinh(s) are created before (at the else case)
            self.nhapdiemchitiet = lst_hs_nhapdiem
        else:
            # Adding hocsinh at lst_hs_thieu into nhapdiemchitiet and show it
            self.nhapdiemchitiet = [] # important
            flag = True

            # Create list for checking null value
            lst_chk = [self.hocky, self.namhoc, self.monhoc, self.lop, self.giaovien] # notice: how about self.giaovien

            # Check for all fields are inputed
            for item in lst_chk:
                if str(item) == '':
                    flag = False

            if flag:
                # Create objects nhapdiemchitiet
                for id in lst_hs_thieu:
                    vals = {
                        'hocsinh'     : id,
                        'giaovien'    : self.giaovien.id,
                        'hocky'       : self.hocky,
                        'namhoc'      : self.namhoc,
                        'monhoc'      : self.monhoc.id,
                    }
                    self.env['solienlac.nhapdiemchitiet'].sudo().create(vals)

                # Reload lst_hs_nhapdiem
                lst_hs_nhapdiem = self.env['solienlac.nhapdiemchitiet'].search([
                    ('hocsinh.lop.id','=',self.lop.id),
                    ('hocsinh.tinhtranghocsinh', '=', 'value1'), # value1 = học bình thường
                    ('hocky','=',self.hocky), # notice, how about a year
                    ('namhoc','=',self.namhoc),
                    ('monhoc.id','=',self.monhoc.id),
                ])
                # Show objects nhapdiemchitiet has just created
                self.nhapdiemchitiet = lst_hs_nhapdiem

class nhapdiemchitiet(models.Model):
    _name = 'solienlac.nhapdiemchitiet'
    @api.model
    def _get_list_namhoc(self):
        lst_namhoc=[]
        for year in range(1990,2050):
            item = str(year) + "-" + str(year+1)
            lst_namhoc.append( (item, item) )
        return lst_namhoc
    @api.model
    def _get_namhoc_now(self):
        now = datetime.datetime.now()
        year = now.year
        if now.month <= 9:
            year -= 1
        return str(year) + "-" + str(year+1)
    giaovien = fields.Many2one(
        string="Giáo viên",
        comodel_name="solienlac.giaovien",
    )
    hocky = fields.Selection(
        string="Học kỳ",
        selection=[
                ('i', 'Học kỳ I'),
                ('ii', 'Học kỳ II'),
                ('iii', 'Cả năm'),
        ],
        default = 'i'
    )
    namhoc = fields.Selection(
        string="Năm học",
        selection= _get_list_namhoc,
        default = _get_namhoc_now,
    )
    monhoc = fields.Many2one(
        string="Môn học",
        comodel_name="solienlac.monhoc",
    )
    hocsinh = fields.Many2one('solienlac.hocsinh', string='Học sinh')
    diemmieng1 = fields.Char('[M]')
    diemmieng2 = fields.Char('[M]')
    diemmieng3 = fields.Char('[M]')
    diemmieng4 = fields.Char('[M]')
    diemmieng5 = fields.Char('[M]')
    diem15phut1 = fields.Char('[15]')
    diem15phut2 = fields.Char('[15]')
    diem15phut3 = fields.Char('[15]')
    diem15phut4 = fields.Char('[15]')
    diem15phut5 = fields.Char('[15]')
    diem1tiet1 = fields.Char('[HS2]')
    diem1tiet2 = fields.Char('[HS2]')
    diem1tiet3 = fields.Char('[HS2]')
    diem1tiet4 = fields.Char('[HS2]')
    diem1tiet5 = fields.Char('[HS2]')
    diemhocky = fields.Char('[HK]')
    diemtongket = fields.Char(string='Tổng kểt', compute='_compute_final')
    xephang = fields.Integer('#')
    @api.depends('diemhocky')
    def _compute_final(self):
        def convert_to_float(n):
            try:
                n = str(n)
                n = n.replace(',','.')
                return float(n)
            except:
                return -1.0

        for record in self:
            lst_diem_mieng = [
                record.diemmieng1, record.diemmieng2,
                record.diemmieng3, record.diemmieng4, record.diemmieng5
            ]
            lst_diem_15 = [
                record.diem15phut1, record.diem15phut2,
                record.diem15phut3, record.diem15phut4, record.diem15phut5
            ]
            lst_diem_1t = [
                record.diem1tiet1, record.diem1tiet2,
                record.diem1tiet3, record.diem1tiet4, record.diem1tiet5
            ]

            lst_diem_mieng = [convert_to_float(x) for x in lst_diem_mieng]
            lst_diem_mieng = filter(lambda x: x != -1.0, lst_diem_mieng)
            lst_diem_15 = [convert_to_float(x) for x in lst_diem_15]
            lst_diem_15 = filter(lambda x: x != -1.0, lst_diem_15)
            lst_diem_1t = [convert_to_float(x) for x in lst_diem_1t]
            lst_diem_1t = filter(lambda x: x != -1.0, lst_diem_1t)
            diemhk = convert_to_float(record.diemhocky) if convert_to_float(record.diemhocky) != -1.0 else 0

            he_so = len(lst_diem_mieng) + len(lst_diem_15) + 2*len(lst_diem_1t) + 3
            tong  = sum(lst_diem_mieng) + sum(lst_diem_15) + 2*sum(lst_diem_1t) + 3*convert_to_float(record.diemhocky)
            diemtk = float(tong)/float(he_so)

            record.diemtongket = diemtk
