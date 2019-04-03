from tkinter import *
from tkinter import messagebox
from pack import first_fun as ff, second_fun as sf, third_fun as tf
import random
import re
import os.path


class Tkinter:
    A = set()
    B = set()
    C = set()
    D = set()
    U = set()
    i = 0
    j = 0
    k = 0
    link1 = os.path.abspath(r"long_result.txt")
    link2 = os.path.abspath(r"short_result.txt")
    link3 = os.path.abspath(r"result_z.txt")

    def __init__(self, root):
        self.root = root

    def wallpaper(self, root, gif):
        root.geometry("1920x1080")
        root.resizable(True, True)
        background = PhotoImage(file=gif)
        label = Label(root, cursor="spider", image=background)
        label.image = background
        label.pack()

    def first_window(self):
        main_menu = Menu(self.root)
        menu_select_window = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Select window", menu=menu_select_window)
        menu_select_window.add_command(label="Second window", command=self.second_window)
        menu_select_window.add_separator()
        menu_select_window.add_command(label="Third window", command=self.third_window)
        menu_select_window.add_separator()
        menu_select_window.add_command(label="Four window", command=self.four_window)
        menu_select_window.add_separator()
        menu_select_window.add_command(label="Five window", command=self.five_window)
        main_menu.add_command(label="Exit", command=exit)
        self.wallpaper(self.root, r"file\apple.gif")
        self.root.config(menu=main_menu)

        about_me_label = Label(self.root, text="Zikratyi Dmytro, group IV-81, list`s number 12",
                               font=("Times New Roman", 16), bg="#490063", fg="white", cursor="spider")
        about_me_label.place(x=550, y=10)

        # generate random set
        set_a_scale = Scale(self.root, orient="hor", length=400, bd=5, tickinterval=15, resolution=1, from_=0,
                            to=255, bg="#490063", fg="white", cursor="spider", relief="raised")
        set_a_scale.place(x=900, y=500)

        set_a_scale_button = Button(self.root, text="Random set A\n by its power", font=("Times New Roman", 16),
                                    bg="#490063", fg="white", bd=9, width=12, activebackground="white",
                                    activeforeground="#490063", cursor="spider", relief="raised",
                                    command=lambda: self.generate_a(set_a_scale))
        set_a_scale_button.place(x=1325, y=500)

        set_b_scale = Scale(self.root, orient="hor", length=400, bd=5, tickinterval=15, resolution=1, from_=0,
                            to=255, bg="#490063", fg="white", cursor="spider", relief="raised")
        set_b_scale.place(x=900, y=600)

        set_b_scale_button = Button(self.root, text="Random set B\n by its power", font=("Times New Roman", 16),
                                    bg="#490063", fg="white", bd=9, width=12, activebackground="white",
                                    activeforeground="#490063", cursor="spider", relief="raised",
                                    command=lambda: self.generate_b(set_b_scale))
        set_b_scale_button.place(x=1325, y=600)

        set_c_scale = Scale(self.root, orient="hor", length=400, bd=5, tickinterval=15, resolution=1, from_=0,
                            to=255, bg="#490063", fg="white", cursor="spider", relief="raised")
        set_c_scale.place(x=900, y=700)

        set_c_scale_button = Button(self.root, text="Random set C\n by its power", font=("Times New Roman", 16),
                                    bg="#490063", fg="white", bd=9, width=12, activebackground="white",
                                    activeforeground="#490063", cursor="spider", relief="raised",
                                    command=lambda: self.generate_c(set_c_scale))
        set_c_scale_button.place(x=1325, y=700)

        # input set by user
        set_a_entry = Entry(self.root, width=28, bd=9, font=("Times New Roman", 16), bg="#490063", fg="white",
                            cursor="spider")
        set_a_entry .place(x=50, y=100)

        set_a_entry_button = Button(self.root, text="Set A", font=("Times New Roman", 16), bg="#490063", fg="white",
                                    bd=5, width=12, activebackground="white", activeforeground="#490063",
                                    cursor="spider", relief="raised", command=lambda: self.enter_a(set_a_entry))
        set_a_entry_button.place(x=400, y=100)

        set_b_entry = Entry(self.root, width=28, bd=9, font=("Times New Roman", 16), bg="#490063", fg="white",
                            cursor="spider")
        set_b_entry.place(x=50, y=200)

        set_b_entry_button = Button(self.root, text="Set B", font=("Times New Roman", 16), bg="#490063", fg="white",
                                    bd=5, width=12, activebackground="white", activeforeground="#490063",
                                    cursor="spider", relief="raised", command=lambda: self.enter_b(set_b_entry))
        set_b_entry_button.place(x=400, y=200)

        set_c_entry = Entry(self.root, width=28, bd=9, font=("Times New Roman", 16), bg="#490063", fg="white",
                            cursor="spider")
        set_c_entry.place(x=50, y=300)

        set_c_entry_button = Button(self.root, text="Set C", font=("Times New Roman", 16), bg="#490063", fg="white",
                                    bd=5, width=12, activebackground="white", activeforeground="#490063",
                                    cursor="spider", relief="raised", command=lambda: self.enter_c(set_c_entry))
        set_c_entry_button.place(x=400, y=300)

        # input range of universal set
        start_u = Entry(self.root, width=13, bd=7, font=("Times New Roman", 16), bg="#490063", fg="white", cursor="spider")
        start_u.place(x=50, y=400)

        end_u = Entry(self.root, width=13, bd=7, font=("Times New Roman", 16), bg="#490063", fg="white", cursor="spider")
        end_u.place(x=220, y=400)

        start_end_u_button = Button(self.root, text="Set range", font=("Times New Roman", 16), bg="#490063", fg="white",
                                    bd=3, width=12, activebackground="white", activeforeground="#490063", cursor="spider",
                                    relief="raised", command=lambda: self.universal_set(start_u, end_u))
        start_end_u_button.place(x=400, y=400)

        # variant
        group_label = Label(self.root, text="My group", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                            width=12, height=1, cursor="spider", relief="raised")
        group_label.place(x=1000, y=100)

        group_entry = Entry(self.root, width=5, bd=5, font=("Times New Roman", 14), bg="#490063", fg="white",
                            cursor="spider")
        group_entry.place(x=1200, y=100)

        number_label = Label(self.root, text="My number", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                             width=12, height=1, cursor="spider", relief="raised")
        number_label.place(x=1000, y=150)

        number_entry = Entry(self.root, width=5, bd=5, font=("Times New Roman", 14), bg="#490063", fg="white",
                             cursor="spider")
        number_entry.place(x=1200, y=150)

        variant_text = Text(self.root, font=("Times New Roman", 14), height=1, width=5, wrap="word", bg="#490063",
                            fg="white", bd=7, cursor="spider", relief="raised")
        variant_text.place(x=1200, y=200)

        variant_button = Button(self.root, text="My variant", font=("Times New Roman", 14), bg="#490063", fg="white",
                                bd=5, height=1, width=14, activebackground="white", activeforeground="#490063",
                                cursor="spider", command=lambda: self.variant(group_entry, number_entry, variant_text))
        variant_button.place(x=1000, y=200)

    def second_window(self):
        root_2 = Toplevel(self.root)
        root_2.title("Second window")
        self.wallpaper(root_2, r"file\apple.gif")
        self.for_window_2_3(root_2)

        # reflection sets
        set_a_w2_text = Text(root_2, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_a_w2_text.place(x=125, y=10)

        set_b_w2_text = Text(root_2, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_b_w2_text.place(x=125, y=90)

        set_c_w2_text = Text(root_2, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_c_w2_text.place(x=125, y=170)

        fill_set_w2_button = Button(root_2, text="Fill\nsets", font=("Times New Roman", 16), bg="#490063", fg="white",
                                    bd=3, height=9, width=3, activebackground="white", activeforeground="#490063",
                                    cursor="spider", relief="raised",
                                    command=lambda: [self.try_except(set_a_w2_text, self.A),
                                                     self.try_except(set_b_w2_text, self.B),
                                                     self.try_except(set_c_w2_text, self.C)])
        fill_set_w2_button.place(x=780, y=7)

        # step for step
        act_w2_text = Text(root_2, font=("Times New Roman", 16), height=6, width=67, wrap="word",
                           bg="#490063", fg="white", bd=5, cursor="spider", relief="raised")
        act_w2_text.place(x=10, y=325)

        realization_w2_text = Text(root_2, font=("Times New Roman", 16), height=6, width=67, wrap="word",
                                   bg="#490063", fg="white", bd=5, cursor="spider", relief="raised")
        realization_w2_text.place(x=10, y=525)

        act_and_realization_w2_button = Button(root_2, text="Act and realization", font=("Times New Roman", 16),
                                               bg="#490063", fg="white", bd=3, height=1, width=20,
                                               activebackground="white", activeforeground="#490063", cursor="spider",
                                               relief="raised", command=lambda:
                                               self.act_and_realization_w2(act_w2_text, realization_w2_text))
        act_and_realization_w2_button.place(x=285, y=700)

        # result
        set_d_w2_text = Text(root_2, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_d_w2_text.place(x=880, y=525)

        # result
        result_d_w2_button = Button(root_2, text="Result D", font=("Times New Roman", 14), bg="#490063", fg="white", bd=5,
                                    height=1, width=10, activebackground="white", activeforeground="#490063",
                                    cursor="spider", relief="raised",
                                    command=lambda: self.try_except(set_d_w2_text,
                                                                    ff.long_result(self.A, self.B, self.C, self.U)))
        result_d_w2_button.place(x=880, y=600)

        save_d_w2_button = Button(root_2, text="Save result", font=("Times New Roman", 16), bg="#490063", fg="white",
                                  bd=3, width=10, activebackground="white", activeforeground="#490063", cursor="spider",
                                  height=1, relief="raised", command=lambda:
                                  self.save_result_in_file(self.link1, "D",
                                                           ff.long_result(self.A, self.B, self.C, self.U)))
        save_d_w2_button.place(x=1010, y=600)

    def third_window(self):
        root_3 = Toplevel(self.root)
        root_3.title("Third window")
        root_3.geometry("1920x1080")
        self.wallpaper(root_3, r"file\apple.gif")
        self.for_window_2_3(root_3)

        # reflection sets
        set_a_w3_text = Text(root_3, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_a_w3_text.place(x=125, y=10)

        set_b_w3_text = Text(root_3, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_b_w3_text.place(x=125, y=90)

        set_c_w3_text = Text(root_3, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_c_w3_text.place(x=125, y=170)

        fill_set_w3_button = Button(root_3, text="Fill\nsets", font=("Times New Roman", 16), bg="#490063", fg="white",
                                    bd=3, height=9, width=3, activebackground="white", activeforeground="#490063",
                                    cursor="spider", relief="raised",
                                    command=lambda: [self.try_except(set_a_w3_text, self.A),
                                                     self.try_except(set_b_w3_text, self.B),
                                                     self.try_except(set_c_w3_text, self.C)])
        fill_set_w3_button.place(x=780, y=7)

        # step for step
        act_w3_text = Text(root_3, font=("Times New Roman", 16), height=6, width=67, wrap="word",
                           bg="#490063", fg="white", bd=5, cursor="spider", relief="raised")
        act_w3_text.place(x=10, y=325)

        realization_w3_text = Text(root_3, font=("Times New Roman", 16), height=6, width=67, wrap="word",
                                   bg="#490063", fg="white", bd=5, cursor="spider", relief="raised")
        realization_w3_text.place(x=10, y=525)

        act_and_realization_w3_button = Button(root_3, text="Act and realization", font=("Times New Roman", 16),
                                               bg="#490063", fg="white", bd=3, height=1, width=20,
                                               activebackground="white", activeforeground="#490063",
                                               cursor="spider", relief="raised",
                                               command=lambda: self.act_and_realization_w3(act_w3_text,
                                                                                           realization_w3_text))
        act_and_realization_w3_button.place(x=285, y=700)

        # result
        set_d_w3_text = Text(root_3, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        set_d_w3_text.place(x=880, y=525)

        result_d_w3_button = Button(root_3, text="Result D", font=("Times New Roman", 14), bg="#490063", fg="white", bd=5,
                                    height=1, width=10, activebackground="white", activeforeground="#490063",
                                    cursor="spider", relief="raised",
                                    command=lambda: self.try_except(set_d_w3_text,
                                                                    sf.short_result(self.A, self.B, self.C, self.U)))
        result_d_w3_button.place(x=880, y=600)

        save_d_w3_button = Button(root_3, text="Save result", font=("Times New Roman", 16), bg="#490063", fg="white",
                                  bd=3, width=10, activebackground="white", activeforeground="#490063", cursor="spider",
                                  height=1, relief="raised",
                                  command=lambda: self.save_result_in_file(self.link2, "D",
                                                                           sf.short_result(self.A, self.B, self.C,
                                                                                           self.U)))
        save_d_w3_button.place(x=1010, y=600)

    def four_window(self):
        root_4 = Toplevel(self.root)
        root_4.title("Four window")
        self.wallpaper(root_4, r"file\apple.gif")

        # reflection sets
        set_x_label = Label(root_4, text="Set X = ", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                            width=7, height=2, cursor="spider", relief="raised")
        set_x_label.place(x=10, y=10)

        set_x_text = Text(root_4, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063", fg="white",
                          bd=5, cursor="spider", relief="raised")
        set_x_text.place(x=125, y=10)

        set_y_label = Label(root_4, text="Set Y = ", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                            width=7, height=2, cursor="spider", relief="raised")
        set_y_label.place(x=10, y=90)

        set_y_text = Text(root_4, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063", fg="white",
                          bd=5, cursor="spider", relief="raised")
        set_y_text.place(x=125, y=90)

        set_z_label = Label(root_4, text="Set Z = ", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                            width=7, height=2, cursor="spider", relief="raised")
        set_z_label.place(x=10, y=170)

        # result
        set_z_text = Text(root_4, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063", fg="white",
                          bd=5, cursor="spider", relief="raised")
        set_z_text.place(x=125, y=170)

        set_z_button = Button(root_4, text="Result Z", font=("Times New Roman", 16),
                              bg="#490063", fg="white", bd=5, height=1, width=10, activebackground="white",
                              activeforeground="#490063", cursor="spider", relief="raised",
                              command=lambda: [self.try_except(set_x_text, self.U - self.A), self.try_except(set_y_text,
                                                                                                    self.C),
                              self.try_except(set_z_text, tf.result_z(self.A, self.C, self.U))])
        set_z_button.place(x=275, y=260)

        save_z_button = Button(root_4, text="Save result", font=("Times New Roman", 16), bg="#490063", fg="white",
                               bd=5, width=10, activebackground="white", activeforeground="#490063", cursor="spider",
                               height=1, relief="raised",
                               command=lambda: self.save_result_in_file(self.link3, "Z",
                                                                        tf.result_z(self.A, self.C, self.U)))
        save_z_button.place(x=425, y=260)

    def five_window(self):
        root_5 = Toplevel(self.root)
        root_5.title("Five window")
        self.wallpaper(root_5, r"file\apple.gif")

        # reflection sets
        long_result_label = Label(root_5, text="First file", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                                  width=9, height=2, cursor="spider", relief="raised")
        long_result_label.place(x=10, y=10)

        long_result_text = Text(root_5, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                                fg="white", bd=5, cursor="spider", relief="raised")
        long_result_text.place(x=150, y=10)

        short_result_label = Label(root_5, text="Second file", font=("Times New Roman", 16), bg="#490063", fg="white",
                                   bd=5, width=9, height=2, cursor="spider", relief="raised")
        short_result_label.place(x=10, y=90)

        short_result_text = Text(root_5, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                                 fg="white", bd=5, cursor="spider", relief="raised")
        short_result_text.place(x=150, y=90)

        result_z_label = Label(root_5, text="Third file", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                               width=9, height=2, cursor="spider", relief="raised")
        result_z_label.place(x=10, y=170)

        result_z_text = Text(root_5, font=("Times New Roman", 16), height=2, width=57, wrap="word", bg="#490063",
                             fg="white", bd=5, cursor="spider", relief="raised")
        result_z_text.place(x=150, y=170)

        set_z_button = Button(root_5, text="Read files", font=("Times New Roman", 16),
                              bg="#490063", fg="white", bd=5, height=1, width=10, activebackground="white",
                              activeforeground="#490063", cursor="heart", relief="raised",
                              command=lambda: [self.read_with_file(self.link1, long_result_text),
                                               self.read_with_file(self.link2, short_result_text),
                                               self.read_with_file(self.link3, result_z_text)])
        set_z_button.place(x=375, y=260)

        # step for step
        act_w5_text = Text(root_5, font=("Times New Roman", 16), height=3, width=57, wrap="word",
                           bg="#490063", fg="white", bd=5, cursor="spider", relief="raised")
        act_w5_text.place(x=150, y=350)

        act_w5_button = Button(root_5, text="Act and realization", font=("Times New Roman", 16), bg="#490063", fg="white",
                               bd=3, height=1, width=20, activebackground="white", activeforeground="#490063",
                               cursor="spider", relief="raised", command=lambda: self.act_w5(act_w5_text))
        act_w5_button.place(x=330, y=450)

        # check
        true_text = Text(root_5, font=("Times New Roman", 16), height=7, width=57, wrap="word",
                         bg="#490063", fg="white", bd=5, cursor="spider", relief="raised")
        true_text.place(x=150, y=550)
        true_button = Button(root_5, text="Check", font=("Times New Roman", 16), bg="#490063", fg="white",
                             bd=10, height=1, width=9, activebackground="white", activeforeground="#490063",
                             cursor="spider", relief="raised",
                             command=lambda: [self.check(true_text, "D", ff.operation_7, sf.operation_2),
                             self.check(true_text, "Z", tf.set_z, self.C - (self.U - self.B))])
        true_button.place(x=10, y=550)

    # pack generate
    def generate_a(self, scale_a):
        self.A.clear()
        for i in range(scale_a.get()):
            self.A.add(random.randrange(256))

    def generate_b(self, scale_b):
        self.B.clear()
        for i in range(scale_b.get()):
            self.B.add(random.randrange(256))

    def generate_c(self, scale_c):
        self.C.clear()
        for i in range(scale_c.get()):
            self.C.add(random.randrange(256))

    # pack input
    def convert(self, entry):
        reg = re.compile(",+")
        s_e_t = reg.split(entry)
        list_set = [int(i) for i in s_e_t]
        return set(list_set)

    def enter_a(self, entry_a):
        self.A.clear()
        self.A = self.convert(entry_a.get())

    def enter_b(self, entry_b):
        self.B.clear()
        self.B = self.convert(entry_b.get())

    def enter_c(self, entry_c):
        self.C.clear()
        self.C = self.convert(entry_c.get())

    # error
    def try_except(self, text, result):
        try:
            if len(result) != 0:
                try:
                    text.delete(1.0, END)
                    text.insert(END, result)
                except AttributeError:
                    pass
            else:
                try:
                    text.delete(1.0, END)
                    text.insert(END, "{Ø}")
                except AttributeError:
                    pass
        except TypeError:
            pass

    # pack universal set
    def universal_set(self, start, end):
        self.U.clear()
        try:
            if 0 <= int(start.get()) < int(end.get()) <= 255:
                for i in range(int(start.get()), int(end.get()) + 1):
                    self.U.add(i)
            else:
                messagebox.showinfo("Error", "Entered wrong range!")
        except ValueError:
            pass

    # variant
    def variant(self, group, number, text):
        group = group.get().split("-")
        result = (int(number.get()) + int(group[1]) % 60) % 30 + 1
        self.try_except(text, str(result))
        task_label = Label(self.root, text="D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C))", font=("Times New Roman", 16),
                           bg="#490063", fg="white", bd=5, width=30, height=1, cursor="spider", relief="raised")
        task_label.place(x=1000, y=250)

    # add
    def for_window_2_3(self, root):
        # reflection sets
        set_a_label = Label(root, text="Set A = ", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5, width=7,
                            height=2, cursor="spider", relief="raised")
        set_a_label.place(x=10, y=10)

        set_b_label = Label(root, text="Set B = ", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5, width=7,
                            height=2, cursor="spider", relief="raised")
        set_b_label.place(x=10, y=90)

        set_c_label = Label(root, text="Set C = ", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5, width=7,
                            height=2, cursor="spider", relief="raised")
        set_c_label.place(x=10, y=170)

        # result
        set_d_label = Label(root, text="Set D = ", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                            width=7, height=2, cursor="spider", relief="raised")
        set_d_label.place(x=765, y=525)

    # add to act_and_realization_(w2, w3, w5)
    def add(self, operation=None, act_text=None, act_format=None, realization_text=None, realization_format=None):
        if len(operation) != 0:
            self.try_except(act_text, act_format)
            self.try_except(realization_text, realization_format)
            return operation
        else:
            self.try_except(act_text, act_format)
            self.try_except(realization_text, realization_format)
            return "{Ø}"

    def act_and_realization_w2(self, act_text, realization_text):
        global new_operation_w2_1, new_operation_w2_2, new_operation_w2_3, new_operation_w2_4, new_operation_w2_5,\
            new_operation_w2_6, new_operation_w2_7, new_operation_w2_8, new_operation_w2_9
        if self.j == 0:
            if len(ff.operation_1) != 0:
                new_operation_w2_1 = self.add(ff.operation_1, act_text,
                                              "¬A = {} \ {} = {}".format(self.U, self.A, ff.operation_1),
                                              realization_text, "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬(({} ∪ ¬{}) ∩ (¬{} ∪ ¬{})) "
                                                                "".
                                              format(ff.operation_1, self.B, self.B, self.C))
                self.j += 1
            else:
                new_operation_w2_1 = self.add(ff.operation_1, act_text,
                                              "¬A = {} \ {} = {}".format(self.U, self.A, "{Ø}"),
                                              realization_text, "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬(({} ∪ ¬{}) ∩ (¬{} ∪ ¬{}))"
                                                                "".
                                              format("{Ø}", self.B, self.B, self.C))
                self.j += 1
        elif self.j == 1:
            if len(ff.operation_2) != 0:
                new_operation_w2_2 = self.add(ff.operation_2, act_text, "¬B = {} \ {} = {}".
                                              format(self.U, self.B, ff.operation_2), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬(({} ∪ {}) ∩ ({} ∪ ¬{}))".
                                              format(new_operation_w2_1, ff.operation_2, ff.operation_2, self.C))
                self.j += 1
            else:
                new_operation_w2_2 = self.add(ff.operation_2, act_text, "¬B= {} \ {} = {}".
                                              format(self.U, self.B, "{Ø}"), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬(({} ∪ {}) ∩ ({} ∪ ¬{}))".
                                              format(new_operation_w2_1, "{Ø}", "{Ø}", self.C))
                self.j += 1
        elif self.j == 2:
            if len(ff.operation_3) != 0:
                new_operation_w2_3 = self.add(ff.operation_3, act_text, "(¬A ∪ ¬B) = {} \ {} = {}".
                                              format(new_operation_w2_1, new_operation_w2_2, ff.operation_3), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({} ∩ ({} ∪ ¬{}))".
                                              format(ff.operation_3, new_operation_w2_2, self.C))
                self.j += 1
            else:
                new_operation_w2_3 = self.add(ff.operation_3, act_text, "(¬A ∪ ¬B) = {} \ {} = {}".
                                              format(new_operation_w2_1, new_operation_w2_2, "{Ø}"), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({} ∩ ({} ∪ ¬{}))".
                                              format("{Ø}", new_operation_w2_2, self.C))
                self.j += 1
        elif self.j == 3:
            if len(ff.operation_4) != 0:
                new_operation_w2_4 = self.add(ff.operation_4, act_text, "¬C = {} \ {} = {}".
                                              format(self.U, self.C, ff.operation_4), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({} ∩ ({} ∪ {}))".
                                              format(new_operation_w2_3, new_operation_w2_2, ff.operation_4))
                self.j += 1
            else:
                new_operation_w2_4 = self.add(ff.operation_4, act_text, "¬C = {} \ {} = {}".
                                              format(self.U, self.C, "{Ø}"), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({} ∩ ({} ∪ {}))".
                                              format(new_operation_w2_3, new_operation_w2_2, "{Ø}"))
                self.j += 1
        elif self.j == 4:
            if len(ff.operation_5) != 0:
                new_operation_w2_5 = self.add(ff.operation_5, act_text, "¬B ∪ ¬C = {} ∪ {} = {}".
                                              format(new_operation_w2_2, new_operation_w2_4, ff.operation_5), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({} ∩ {})".
                                              format(new_operation_w2_3, ff.operation_5))
                self.j += 1
            else:
                new_operation_w2_5 = self.add(ff.operation_5, act_text, "¬B ∪ ¬C = {} ∪ {} = {}".
                                              format(new_operation_w2_2, new_operation_w2_4, "{Ø}"), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({} ∩ {})".
                                              format(new_operation_w2_3, "{Ø}"))
                self.j += 1
        elif self.j == 5:
            if len(ff.operation_6) != 0:
                new_operation_w2_6 = self.add(ff.operation_6, act_text, "(¬A ∪ ¬B) ∩ (¬B ∪ ¬C) = {} ∩ {} = {}".
                                              format(new_operation_w2_3, new_operation_w2_5, ff.operation_6),
                                              realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({})".
                                              format(ff.operation_6))
                self.j += 1
            else:
                new_operation_w2_6 = self.add(ff.operation_6, act_text, "(¬A ∪ ¬B) ∩ (¬B ∪ ¬C) = {} ∩ {} = {}".
                                              format(new_operation_w2_3, new_operation_w2_5, "{Ø}"), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = ¬({})".
                                              format("{Ø}"))
                self.j += 1
        elif self.j == 6:
            if len(ff.operation_7) != 0:
                new_operation_w2_7 = self.add(ff.operation_7, act_text, "¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = {} \ {} = {}".
                                              format(self.U, new_operation_w2_6, ff.operation_7), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = {}".
                                              format(ff.operation_7))
                self.j += 1
            else:
                new_operation_w2_7 = self.add(ff.operation_7, act_text, "¬(¬A ∩ B) ∪ ¬(¬B ∪ C) = {} \ {} = {}".
                                              format(self.U, new_operation_w2_6, "{Ø}"), realization_text,
                                              "D = ¬((¬A ∪ ¬B) ∩ (¬B ∪ ¬C)) = {}".
                                              format("{Ø}"))
                self.j += 1
        else:
            try:
                act_text.delete(1.0, END)
                realization_text.delete(1.0, END)
                self.j = 0
            except AttributeError:
                pass
        pass

    def act_and_realization_w3(self, act_text, realization_text):
        global new_operation_w3_1, new_operation_w3_2, new_operation_w3_3
        if self.i == 0:
            if len(sf.operation_1) != 0:
                new_operation_w3_1 = self.add(sf.operation_1, act_text, "A ∪ C = {} ∪ {} = {}".
                                              format(self.A, self.C, sf.operation_1), realization_text,
                                              "D = B ∩ (A ∪ C) = {} ∩ ({} ∪ {})".format(self.B, self.A,
                                                                                         self.C))
                self.i += 1
            else:
                new_operation_w3_1 = self.add(sf.operation_1, act_text,
                                              "A ∪ C = {} ∪ {} = {}".format(self.A, self.C, "{Ø}"), realization_text,
                                              "D = B ∩ (A ∪ C) = {} ∩ ({})".format(self.B, "{Ø}"))
                self.i += 1
        elif self.i == 1:
            if len(sf.operation_2) != 0:
                new_operation_w3_2 = self.add(sf.operation_2, act_text, "B ∩ (A ∪ C) = {} ∩ {} = {}".
                                              format(self.B, new_operation_w3_1, sf.operation_2), realization_text,
                                              "D = B ∩ (A ∪ C) = {}".format(sf.operation_2))
                self.i += 1
            else:
                new_operation_w3_2 = self.add(sf.operation_2, act_text, "B ∩ (A ∪ C) = {} ∩ {} = {}".
                                              format(self.B, new_operation_w3_1, "{Ø}"), realization_text,
                                              "D = B ∩ (A ∪ C) = {}".format("{Ø}"))
                self.i += 1
        else:
            try:
                act_text.delete(1.0, END)
                realization_text.delete(1.0, END)
                self.i = 0
            except AttributeError:
                pass

    def act_w5(self, act_text):
        global new_operation_w5_1, new_operation_w5_2
        operation_1 = self.U - self.A
        operation_2 = (operation_1-self.C) | (self.C - operation_1)
        if self.k == 0:
            if len(operation_1) != 0:
                new_operation_w5_1 = self.add(operation_1, act_text, "X = {} \ {} = {}".format(self.U, self.A,
                                                                                               operation_1))
                self.k += 1
            else:
                new_operation_w5_1 = self.add(operation_1, act_text, "X = {} \ {} = {}".format(self.U, self.A, "{Ø}"))
                self.k += 1
        elif self.k == 1:
            if len(operation_2) != 0:
                new_operation_w5_2 = self.add(operation_1, act_text,
                                              "Z = X  Y = {}  {} = {}".format(new_operation_w5_1,self.C,
                                                                                operation_2))
                self.k += 1
            else:
                new_operation_w5_2 = self.add(operation_1, act_text,
                                              "Z = X  Y = {}  {} = {}".format(new_operation_w5_1, self.C, "{Ø}"))
                self.k += 1
        else:
            try:
                act_text.delete(1.0, END)
                self.k = 0
            except AttributeError:
                pass

    def check(self, text, letter, first_result, second_result):
        if len(first_result) == 0:
            first_result = "{Ø}"
        if len(second_result) == 0:
            second_result = "{Ø}"

        if first_result == second_result:
            try:
                text.insert(END,
                            "Lucky me :). Sets are equals in two cases!\n{} = {} = {}\n".format(letter, first_result,
                                                                                                second_result))
                self.success("100 %")
            except AttributeError:
                pass
        else:
            text.insert(END,
                        "Unfortunately. Sets aren't equals in two cases!\n {} = {} ≠ {}\n".format(letter, first_result,
                                                                                                  second_result))
            self.success("0 %")

    def success(self, text):
        success_label = Label(self.root, text="My success", font=("Times New Roman", 16), bg="#490063", fg="white", bd=5,
                              width=12, height=1, cursor="spider", relief="raised")
        success_label.place(x=1300, y=50)

        can = Canvas(self.root, height=150, width=150, bd=0, highlightthickness=0, relief="ridge", bg="#490063",
                     cursor="spider")
        can.create_oval(0, 0, 140, 140, width=2, fill="pink")
        can.create_text(70, 70, text=text, justify=CENTER, font=("Times New Roman", 20))
        can.place(x=1300, y=100)

    def save_result_in_file(self, link, set_name, result):
        with open(link, "a") as f:
            if len(result) != 0:
                f.write("Set {} = {}\n".format(str(set_name), str(result)))
            else:
                f.write("Set {} is empty!\n".format(str(set_name)))

    def read_with_file(self, link, text):
        with open(link, "r+") as f:
            self.try_except(text, f.read())


def main():
    root = Tk()
    root.title("First window")
    ex_class = Tkinter(root)
    ex_class.first_window()
    root.mainloop()


if __name__ == "__main__":
    main()
