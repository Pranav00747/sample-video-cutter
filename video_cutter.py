from tkinter import *
import webbrowser
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
import os
from moviepy.editor import *

class video_cutter:
 @staticmethod
 def create_main_ui(caption):
    tt = Tk()
    tt.overrideredirect(1)
    tt.geometry("%dx%d"%(tt.winfo_screenwidth(), tt.winfo_screenheight()))
    tt.config(bg='#003366')
    tt.title(caption)
    return tt
 @staticmethod
 def in_comp(t, par):
   close1 = Label(t, text="x", bg='#001933', fg='#ffffff')
   close1.place(x=t.winfo_screenwidth()-60, y=12)
   def m_c(e):
     par.destroy()
   def m_e(e):
    close1.config(fg='#cc6600')
   def m_l(e):
    close1.config(fg='#ffffff')
   close1.bind('<Enter>', m_e)
   close1.bind('<Leave>', m_l)
   close1.bind('<Button-1>', m_c)
   copyr = Label(par, text="Copyright of @Pranav", bg='#003366', fg='#ffffff', font=(8))
   copyr.place(x=par.winfo_screenwidth()/2-100, y=par.winfo_screenheight()-60)
   def m_ce1(e):
    copyr.config(fg='#cc6600', font=(8))
   def m_cl1(e):
    copyr.config(fg='#ffffff', font=(10))
   def only_this_now():
        webbrowser.open("https://github.com/Pranav00747")
   def m_cc1(e):
      only_this_now()
   copyr.bind('<Enter>', m_ce1)
   copyr.bind('<Leave>', m_cl1)
   copyr.bind('<Button-1>', m_cc1)
 def mid_comp(par):
   er1 = StringVar()
   er2 = StringVar()
   er3 = StringVar()
   er4 = StringVar()
   cc1 = StringVar()
   global path1
   global path2
   img_main = Image.open("video_cutter.jpg")
   img_main = img_main.resize((96, 96))
   img_main1 = Image.open("video_cutter.jpg")
   img_main1 = img_main.resize((128, 128))
   global logo_img
   global logo_img1
   logo_img = ImageTk.PhotoImage(img_main)
   logo_img1 = ImageTk.PhotoImage(img_main1)
   img_l = Label(par, image=logo_img, bg='#003366')
   img_l.place(x=10, y=60)
   def i_e(e):
     img_l.config(image=logo_img1)
   def i_l(e):
     img_l.config(image=logo_img)
   img_l.bind('<Enter>', i_e)
   img_l.bind('<Leave>', i_l)
   lab1 = Label(par, text="Video Cut", bg='#003366', fg='#ffffff', font=('Calibri', 16))
   lab1.place(x=160, y=60)
   s1 = Label(par, text="Source :", bg="#003366", fg="#ffffff", font=('Calibri', 10))
   s1.place(x=168, y=180)
   d1 = Label(par, text="Destination :", bg="#003366", fg="#ffffff", font=('Calibri', 10))
   d1.place(x=168, y=240)
   ss1 = Label(par, text="Start Seconds:", bg='#003366', fg='#ffffff', font=('Calibri', 10))
   ss1.place(x=168, y=300)
   se1 = Label(par, text="End Seconds:", bg='#003366', fg='#ffffff', font=('Calibri', 10))
   se1.place(x=368, y=300)
   rot1 = Label(par, text="Rotate :", bg='#003366', fg='#ffffff', font=('Calibri', 10))
   rot1.place(x=168, y=360)
   src1 = Entry(par, textvariable=er1, width=100, state="disabled")
   src1.place(x=228, y=180)
   dst1 = Entry(par, textvariable=er2, width=100, state="disabled")
   dst1.place(x=248, y=240)
   sse1 = Entry(par, textvariable=er3, width=10)
   sse1.place(x=268, y=300)
   see1 = Entry(par, textvariable=er4, width=10)
   see1.place(x=448, y=300)
   cb1 = ttk.Combobox(par, textvariable=cc1, width=10)
   cb1['values']=('None', '90', '180')
   cb1.place(x=228, y=360)
   cb1.current()
   br1 = Label(par, text="Browse", width=10, height=2, bg='#000033', fg='#ffffff', font=('Calibri', 8))
   br1.place(x=840, y=170)
   def b1_e(e):
    br1.config(bg='#000044')
   def b1_l(e):
    br1.config(bg='#000033')
   def b1_c(e):
     path1 = filedialog.askopenfilename(initialdir="/", title="Please Select Source Files", filetypes=(("MP4 Files", "*.mp4*"), ("All Files", "*.*")))
     er1.set(path1)
   br1.bind('<Enter>', b1_e)
   br1.bind('<Leave>', b1_l)
   br1.bind('<Button-1>', b1_c)
   br2 = Label(par, text="Browse", width=10, height=2, bg='#000033', fg='#ffffff', font=('Calibri', 8))
   br2.place(x=860, y=240)
   def b2_e(e):
    br2.config(bg='#000044')
   def b2_l(e):
    br2.config(bg='#000033')
   def b2_c(e):
    path2 = filedialog.askdirectory(title="Please Select Destination Directory")
    er2.set(path2)
   br2.bind('<Enter>', b2_e)
   br2.bind('<Leave>', b2_l)
   br2.bind('<Button-1>', b2_c)
   cut1 = Label(par, text="Cut Video", width=10, height=3, bg='#000022', fg='#ffffff', font=('Calibri', 10))
   cut1.place(x=368, y=400)
   def b1_e(e):
     cut1.config(bg='#000033', font=('Calibri', 12))
   def b1_l(e):
     cut1.config(bg='#000022', font=('Calibri', 10))
   def b1_c_main(e):
      if er1.get()!="" and er2.get()!="" and er3.get()!="" and er4.get()!="" and cc1.get()!="":
       if (int(er3.get()) >= 0) and (int(er4.get()) > 0):
        if os.path.isfile(er1.get()) and os.path.isdir(er2.get()):
            dir_1, file_1 = os.path.split(er1.get())
            main_path = os.path.join(er2.get(), file_1)
            clp = VideoFileClip(er1.get())
            if (int(er3.get())>=0) and (int(er4.get())>0 and int(er4.get()) < clp.duration):
              clp = clp.subclip(int(er3.get()), int(er4.get()))
              if cc1.get()=="90" or cc1.get()=="180":
                  clp = clp.rotate(int(cc1.get()))
              clp.write_videofile(main_path)
      else:
       err = Tk()
       err.overrideredirect(1)
       err.geometry('600x200+260+260')
       err.configure(bg='#000011')
       err_msg = Label(err, text="Please fill all details everything.", bg='#000011', fg='#ffffff', font=('Calibri', 12))
       err_msg.place(x=220, y=80)
       def clk(e):
         err.destroy()
       err.bind('<Button-1>', clk)

   cut1.bind('<Enter>', b1_e)
   cut1.bind('<Leave>', b1_l)
   cut1.bind('<Button-1>', b1_c_main)
   clear1 = Label(par, text="Clear", width=10, height=3, bg='#000022', fg='#ffffff', font=('Calibri', 10))
   clear1.place(x=468, y=400)
   def b2_e(e):
     clear1.config(bg='#000033', font=('Calibri', 12))
   def b2_l(e):
     clear1.config(bg='#000022', font=('Calibri', 10))
   def b2_c(e):
     if er1.get()!="" or er2.get()!="" or er3.get()!="" or er4.get()!="" or cc1.get()!="":
        er1.set("")
        er2.set("")
        er3.set("")
        er4.set("")
        cc1.set("")
   clear1.bind('<Enter>', b2_e)
   clear1.bind('<Leave>', b2_l)
   clear1.bind('<Button-1>', b2_c)
if __name__=="__main__":
 vc = video_cutter.create_main_ui('Video Cutter and Joiner')
 can1 = Canvas(vc, bg='#001933', width=vc.winfo_screenwidth(), height=36, highlightthickness=0)
 can1.place(x=0, y=0)
 can1.create_text(80, 18, fill='#ffffff', text="Video Cutter", font=(18))
 img = Image.open("video_cutter.jpg")
 img = img.resize((22, 22))
 global m_img
 m_img = ImageTk.PhotoImage(img)
 can1.create_image(20, 18, image=m_img)
 video_cutter.in_comp(can1, vc)
 video_cutter.mid_comp(vc)
 vc.mainloop()