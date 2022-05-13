from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class QuanLyChiTieu:
    def __init__(self):
        self.Dic={}
        self.TongCTNgay=0
        self.TongCTThang=0
        self.TongTCNgay=0
        self.TongTCThang =0
        self.CTThang=[]
        for i in range(30):
            list=[]
            self.CTThang.append(list)
        # PHẦN GIAO DIỆN
        self.window= Tk()
        self.window.title("Expense management")

        # Lấy chiều dài chiều rộng của màn hình
        self.CRManHinh = self.window.winfo_screenwidth()
        self.CCManHinh = self.window.winfo_screenheight()

        # Điều chỉnh chiều rộng và cao của cửa sổ
        self.CRCuaSo = 850
        self.CCCuaSo = 420

        # Vị trí cửa sổ
        self.window.geometry("%dx%d+%d+%d" % (self.CRCuaSo, self.CCCuaSo,
                             (self.CRManHinh - self.CRCuaSo) / 2, (self.CCManHinh - self.CCCuaSo) / 2))
        self.window.resizable(width=False,height=False)

        # Chèn background
        self.anh= Image.open(r'Anh.png')
        self.anh= ImageTk.PhotoImage(self.anh)
        self.background = Label(self.window, image=self.anh)
        self.background.place(x=0, y=0)

        # Phần tiêu đề
        self.Tieude = Label(master=self.window,text="QUẢN LÝ CHI TIÊU",font=("Pacifico Regular",18,"bold"))
        self.Tieude.place(x=290,y=8)

        # Danh sách tháng
        self.Thang = Label(master=self.window,text="Tháng 5",font=("Arial",15,"bold"))
        self.Thang.place(x= 120,y=75)

        # Danh sách ngày
        self.Ngay= Label(master=self.window,text="Ngày",font=("Arial",10,"bold"))
        self.DSNgay= Combobox(self.window,state="readonly")
        self.DSNgay.bind("<<ComboboxSelected>>", self.Thong_tin_ngay)

        self.DSNgay['value']=("1","2","3","4","5","6","7","8","9","10",
                        "11","12","13","14","15","16","17","18","19","20",
                        "21","22","23","24","25","26","27","28","29","30")

        self.Ngay.place(x=40,y=110)
        self.DSNgay.place(x=120,y=112)

        # Phần trợ cấp
        self.Trocap = Label(master=self.window,text="Trợ cấp",font=("Arial",10,"bold"))
        self.TrocapEntry = Entry(master=self.window,width=23)

        self.Trocap.place(x=40,y=140)
        self.TrocapEntry.place(x=120,y=142)

        # Phần danh sách chi tiêu
        self.Chitieu= Label(master=self.window,text="Chi tiêu",font=("Arial",10,"bold"))
        self.DSChiTieu = Combobox(self.window, state="readonly")
        self.DSChiTieu['value']=("Shopee","Ăn uống","Mua sắm","Áo quần","Mỹ phẩm","Đi lại","Du lịch","Đổ xăng","Điện thoại","Khác")

        self.Chitieu.place(x=40,y=170)
        self.DSChiTieu.place(x=120,y=172)

        # Số tiền chi tiêu cho sản phẩm
        self.SoTien= Label(master=self.window,text="Số tiền",font=("Arial",10,"bold"))
        self.SoTienEntry= Entry(master=self.window,width=23)

        self.SoTien.place(x=40,y=200)
        self.SoTienEntry.place(x=120,y=202)

        # Các nút bấm
        self.Them = Button(master=self.window, text="Thêm",width=10,command=self.Them_chi_tieu)
        self.CapNhat = Button(master=self.window,text="Cập nhật",width=10,command=self.Cap_nhat_chi_tieu)
        self.Xoa = Button(master=self.window,text="Xóa",width=10,command=self.Xoa_chi_tieu)
        self.Lammoi = Button(master=self.window,text="Làm mới",width=15,command=self.Lam_moi)
        self.ThongKeCTNgay= Button(master=self.window,text="Thống kê chi tiêu ngày",width=37,command=self.Thong_ke_CT_ngay)
        self.ThongKeCTThang= Button(master=self.window,text="Thống kê chi tiêu tháng",width=37,command=self.Thong_ke_chi_tieu_thang)

        self.Them.place(x=40, y =250)
        self.CapNhat.place(x=120,y=250)
        self.Xoa.place(x=200,y=250)
        self.Lammoi.place(x=280, y =250)
        self.ThongKeCTNgay.place(x=40,y = 280)
        self.ThongKeCTThang.place(x=40,y=310)

        # Tổng chi tiêu tháng
        self.TongChiTieuThang = Label(master=self.window,text="TỔNG CHI TIÊU THÁNG: ",font=("Arial",13,"bold"))
        self.TongChiTieuThang.place(x=40,y=343)

        # Tổng trợ cấp tháng
        self.TongTroCapThang= Label(master=self.window,text="TỔNG TRỢ CẤP THÁNG: ",font=("Arial",13,"bold"))
        self.TongTroCapThang.place(x=40,y=370)

        # Phần thống kê chi tiêu trong ngày
        self.DSCTNgay= Label(master=self.window,text="Danh sách chi tiêu trong ngày : ",font=("Arial",10,"bold"))
        self.DSChiTieuTrongNgay = ttk.Treeview(master=self.window,columns=("Name","Price","Bonus"), height=5)
        self.DSChiTieuTrongNgay.bind('<Double-ButtonRelease-1>',self.SelectItemNgay)

        self.DSChiTieuTrongNgay.heading("Name",text="Name")
        self.DSChiTieuTrongNgay.heading("Price",text="Price")
        self.DSChiTieuTrongNgay.heading("Bonus",text="Bonus")
        self.DSChiTieuTrongNgay.column("#0", stretch=NO, minwidth=0, width=0)

        self.DSChiTieuTrongNgay.column("Name",stretch=NO, minwidth=0, width=134)
        self.DSChiTieuTrongNgay.column("Price", stretch=NO, minwidth=0, width=134)
        self.DSChiTieuTrongNgay.column("Bonus",stretch=NO, minwidth=0,width=134)

        self.DSCTNgay.place(x=400,y=70)
        self.DSChiTieuTrongNgay.place(x=400,y=97)

        # Danh sách các chi tiêu trong tháng
        self.DSThang= Label(master=self.window,text="Danh sách chi tiêu trong tháng: ",font=("Arial",10,"bold"))
        self.DSChiTieuTrongThang = ttk.Treeview(master=self.window,columns=("Date","Price","Bonus"), height=5)

        self.DSChiTieuTrongThang.heading("Date",text="Date")
        self.DSChiTieuTrongThang.heading("Price",text="Price")
        self.DSChiTieuTrongThang.heading("Bonus",text="Bonus")

        self.DSChiTieuTrongThang.column("Date",stretch=NO,minwidth=0,width=134)
        self.DSChiTieuTrongThang.column("Price",stretch=NO,minwidth=0,width=134)
        self.DSChiTieuTrongThang.column("Bonus", stretch=NO, minwidth=0, width=134)
        self.DSChiTieuTrongThang.column("#0", stretch=NO, minwidth=0, width=0)

        self.DSThang.place(x=400,y=233)
        self.DSChiTieuTrongThang.place(x=400,y=260)

    # Hàm dùng để hiễn thị chi tiêu trong ngày đã thêm
    def Thong_tin_ngay(self,a):
        self.TrocapEntry.delete(0, END)
        self.DSChiTieu.set("")
        self.SoTienEntry.delete(0, END)
        Ngay = self.DSNgay.get()
        if Ngay != "":
            for i in self.DSChiTieuTrongNgay.get_children():
                self.DSChiTieuTrongNgay.delete(i)
            for j in range(len(self.CTThang)):
                if Ngay == f"{j + 1}":
                    for k in range(len(self.CTThang[j])):
                        self.DSChiTieuTrongNgay.insert('', 'end', values=(self.CTThang[j][k][0],self.CTThang[j][k][1],self.CTThang[j][k][2]))

    # Hàm thêm chi tiêu trong ngày
    def Them_chi_tieu(self):
        SoTien= self.SoTienEntry.get()
        ChiTieu= self.DSChiTieu.get()
        TroCap = self.TrocapEntry.get()
        Ngay = self.DSNgay.get()

        if SoTien=="":
            messagebox.showinfo("Message Title", "Vui lòng nhập số tiền")
        elif (SoTien.isdigit()) and (TroCap.isdigit() or TroCap==""):
            self.DSChiTieuTrongNgay.insert('', 'end', values=(ChiTieu,SoTien,TroCap))
            for i in range(len(self.CTThang)):
                if Ngay == f"{i+1}":
                    self.CTThang[i].append([ChiTieu,SoTien,TroCap])
        else:
            messagebox.showinfo("Message Title", "Error")

    # Hàm cập nhật chi tiêu trong ngày
    def Cap_nhat_chi_tieu(self):
        selected = self.DSChiTieuTrongNgay.focus()
        Ngay = self.DSNgay.get()
        ThuTu = self.DSChiTieuTrongNgay.get_children()
        TroCap = self.TrocapEntry.get()
        SoTien = self.SoTienEntry.get()

        if SoTien=="":
            messagebox.showinfo("Message Title", "Vui lòng nhập số tiền")
        elif (SoTien.isdigit()) and (TroCap.isdigit() or TroCap == ""):
            k = 0
            for i in range(len(ThuTu)):
                if ThuTu[i] == f"{selected}":
                    k = i
                    break
            m = 0
            for j in range(len(self.CTThang)):
                if Ngay == f"{j+1}":
                    m=j
                    break
            self.CTThang[m][k] = [self.DSChiTieu.get(), self.SoTienEntry.get(), self.TrocapEntry.get()]
            self.DSChiTieuTrongNgay.item(selected,values=(self.DSChiTieu.get(), self.SoTienEntry.get(), self.TrocapEntry.get()))
        else:
            messagebox.showinfo("Message Title", "Error")

    # Hàm xóa chi tiêu trong ngày
    def Xoa_chi_tieu(self):
        selected = self.DSChiTieuTrongNgay.focus()
        ThuTu = self.DSChiTieuTrongNgay.get_children()
        Ngay = self.DSNgay.get()

        k=0
        for i in range(len(ThuTu)):
            if ThuTu[i] == f"{selected}":
                k=i
                break

        m=0
        for i in range(len(self.CTThang)):
            if Ngay == f"{i + 1}":
                m=i
                break

        del self.CTThang[m][k]
        self.DSChiTieuTrongNgay.delete(selected)

    # Hàm làm mới dữ liệu để nhập
    def Lam_moi(self):
        self.TrocapEntry.delete(0,END)
        self.DSChiTieu.set("")
        self.SoTienEntry.delete(0,END)

    # Hàm thống kê chi tiêu trong ngày
    def Thong_ke_CT_ngay(self):
        Ngay=self.DSNgay.get()
        if len(self.DSChiTieuTrongThang.get_children()) == 0:
            self.DSChiTieuTrongThang.insert('', 'end', values=("Ngày " + Ngay, self.Tong_chi_tieu_ngay(), self.Tong_tro_cap_ngay()))
        else:
            for line in self.DSChiTieuTrongThang.get_children():
                text = self.DSChiTieuTrongThang.item(line)['values'][0]
                if f"{text}" == f"Ngày {Ngay}":
                    self.DSChiTieuTrongThang.item(line, values=("Ngày " + Ngay, self.Tong_chi_tieu_ngay(), self.Tong_tro_cap_ngay()))
                    break
                elif text !="" and f"{text}" != f"Ngày {Ngay}":
                    k=0
                    for lin in self.DSChiTieuTrongThang.get_children():
                        text1 = self.DSChiTieuTrongThang.item(lin)['values'][0]
                        if f"{text1}" != f"Ngày {Ngay}":
                            k=0
                        else:
                            k=lin
                            break
                    if k== 0:
                        self.DSChiTieuTrongThang.insert('', 'end', values=("Ngày " + Ngay, self.Tong_chi_tieu_ngay(), self.Tong_tro_cap_ngay()))
                        break
                    else:
                        self.DSChiTieuTrongThang.item(k, values=("Ngày " + Ngay, self.Tong_chi_tieu_ngay(), self.Tong_tro_cap_ngay()))
        bienlai_popup = Toplevel()
        bienlai_popup.title("Biên lai ngày %s" % Ngay)
        bienlai_popup.geometry("400x200")
        bienlai_popup.resizable(False, False)
        all_data_today = self.DSChiTieuTrongNgay.get_children()
        DSCTNgay = Label(master=bienlai_popup,text="Danh sách chi tiêu trong ngày : ",font=("Arial",10,"bold"))
        DSChiTieuTrongNgay = ttk.Treeview(master=bienlai_popup,columns=("Name","Price","Bonus"), height=5)
        DSChiTieuTrongNgay.bind('<Double-ButtonRelease-1>',self.SelectItemNgay)
        DSChiTieuTrongNgay.heading("Name",text="Name")
        DSChiTieuTrongNgay.heading("Price",text="Price")
        DSChiTieuTrongNgay.heading("Bonus",text="Bonus")
        DSChiTieuTrongNgay.column("#0", stretch=NO, minwidth=0, width=0)

        DSChiTieuTrongNgay.column("Name",stretch=NO, minwidth=0, width=134)
        DSChiTieuTrongNgay.column("Price", stretch=NO, minwidth=0, width=134)
        DSChiTieuTrongNgay.column("Bonus",stretch=NO, minwidth=0,width=134)

        DSCTNgay.pack()
        DSChiTieuTrongNgay.pack()
        if len(all_data_today) == 0:
            messagebox.showinfo("Message Title", "Không có dữ liệu")
        else:
            for line in all_data_today:
                text = self.DSChiTieuTrongNgay.item(line)['values'][0]
                DSChiTieuTrongNgay.insert('', 'end', values=(text, self.DSChiTieuTrongNgay.item(line)['values'][1], self.DSChiTieuTrongNgay.item(line)['values'][2]))
            DSChiTieuTrongNgay.insert('', 'end', values=("Tổng chi tiêu", self.Tong_chi_tieu_ngay(), self.Tong_tro_cap_ngay()))

    # Hàm tính tổng chi tiêu trong ngày
    def Tong_chi_tieu_ngay(self):
        self.TongCTNgay = 0
        Ngay = self.DSNgay.get()
        for i in range(len(self.CTThang)):
            if Ngay == f"{i+1}":
                for j in range(len(self.CTThang[i])):
                    self.TongCTNgay += float(self.CTThang[i][j][1])
                break
        return self.TongCTNgay

    # Hàm tính tổng trợ cấp trong ngày
    def Tong_tro_cap_ngay(self):
        self.TongTCNgay =0
        Ngay = self.DSNgay.get()
        for i in range(len(self.CTThang)):
            if Ngay == f"{i + 1}":
                for j in range(len(self.CTThang[i])):
                    if self.CTThang[i][j][2] != "":
                        self.TongTCNgay += float(self.CTThang[i][j][2])
                break
        return self.TongTCNgay

    # Hàm tính tổng chi tiêu trong tháng
    def Tong_chi_tieu_thang(self):
        self.TongCTThang =0
        for i in range(len(self.CTThang)):
            for j in range(len(self.CTThang[i])):
                self.TongCTThang += float(self.CTThang[i][j][1])
        self.TongChiTieuThang.configure(text=f"TỔNG CHI TIÊU THÁNG: {round(self.TongCTThang)} VNĐ")
        return self.TongCTThang

    # Hàm tính tổng trợ cấp trong tháng
    def Tong_tro_cap_thang(self):
        self.TongTCThang =0
        for i in range(len(self.CTThang)):
            for j in range(len(self.CTThang[i])):
                if self.CTThang[i][j][2] != "":
                    self.TongTCThang += float(self.CTThang[i][j][2])
        self.TongTroCapThang.configure(text=f"TỔNG TRỢ CẤP THÁNG: {round(self.TongTCThang)} VNĐ")
        return self.TongTCThang

    # Hàm thống kê các chi tiêu trong tháng
    def Thong_ke_chi_tieu_thang(self):
        ChiTieu= self.Tong_chi_tieu_thang()
        TroCap= self.Tong_tro_cap_thang()

    # Hàm chỉ định sự kiện hiển thị thông tin sản phẩm khi nhấn đúp chuột trái
    def SelectItemNgay(self,a):
        selected = self.DSChiTieuTrongNgay.focus()
        Lis = self.DSChiTieuTrongNgay.item(selected)['values']

        self.TrocapEntry.delete(0,END)
        self.TrocapEntry.insert(0,Lis[2])

        self.SoTienEntry.delete(0,END)
        self.SoTienEntry.insert(0,Lis[1])

        for i in range(len(self.DSChiTieu['value'])):
            if self.DSChiTieu['value'][i] == Lis[0]:
                self.DSChiTieu.set(Lis[0])

if __name__ == "__main__":
    app = QuanLyChiTieu()
    app.window.mainloop()