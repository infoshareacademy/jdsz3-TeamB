import tkinter as tk
from joblib import load

font = ('Verdana', 12)
large_font = ('Verdana', 22, 'bold')


class Credit(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Main)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='Kalkulator zdolności\nkredytowej', font=large_font).grid(row=0, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=1, sticky='nsew')
        tk.Button(self, text='Nowy klient', font=font,
                  command=lambda: master.switch_frame(New)).grid(row=2, sticky='nsew')
        tk.Button(self, text='Obecny klient', font=font,
                  command=lambda: master.switch_frame(Current)).grid(row=3, sticky='nsew')
        tk.Button(self, text='Wyjście', font=font, command=lambda: master.destroy()).grid(row=4, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=5, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=6, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=7, sticky='nsew')
        tk.Label(self, text='made by team: Fajni').grid(row=8, sticky='nsew')


class New(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='Nowy klient', font=large_font).grid(row=0, columnspan=3)
        tk.Label(self, text=' ', font=large_font).grid(row=1, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=4, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=8, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=13, columnspan=3, sticky='nsew')
        tk.Button(self, text='Main menu', font=font,
                  command=lambda: master.switch_frame(Main)).grid(row=14, columnspan=3, sticky='nsew')
        self.new_x_rating()
        self.get_income()
        self.get_age()
        self.get_education()
        self.get_sex()
        self.get_student()
        self.get_martial_male()
        self.get_ethnicity()

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()

    def get_income(self):
        income_validator = self.register(self.income_validation)
        income_label = tk.Label(self, text='Zarobki:', font=font)
        income_label.grid(row=2, column=0)
        self.income_entry = tk.Entry(self, bd=5, validate='key', validatecommand=(income_validator, '%P'))
        self.income_entry.grid(row=3, column=0)
        self.income_entry.focus_set()
        self.income_entry.bind('<Return>', self.push_income)
        self.income_entry.bind('<Tab>', self.focus_next_widget)
        self.income_entry.bind('<Tab>', self.push_income)

    def push_income(self, event=None):
        self.income = self.income_entry.get()
        print(self.income)
        self.new_x_rating[0][0] = (float(self.income) / 100)

    def income_validation(self, income):
        try:
            if income == "":
                return True
            elif float(income) and len(income) < 12:
                return True
            elif int(income) and len(income) < 9:
                return True
            else:
                raise ValueError
        except ValueError:
            self.bell()
            return False

    def get_age(self):
        age_validator = self.register(self.age_validation)
        age_label = tk.Label(self, text='Wiek:', font=font)
        age_label.grid(row=2, column=1)
        self.age_entry = tk.Entry(self, bd=5, validate='key', validatecommand=(age_validator, '%P'))
        self.age_entry.grid(row=3, column=1)
        self.age_entry.focus()
        self.age_entry.bind('<Return>', self.push_age)
        self.age_entry.bind('<Tab>', self.focus_next_widget)
        self.age_entry.bind('<Tab>', self.push_age)

    def push_age(self, event=None):
        self.age = self.age_entry.get()
        print(self.age)
        self.new_x_rating[0][1] = self.age

    def age_validation(self, age):
        try:
            if age == "":
                return True
            elif int(age) and len(age) < 3:
                return True
            else:
                raise ValueError
        except ValueError:
            self.bell()
            return False

    def get_education(self):
        education_validator = self.register(self.education_validation)
        education_label = tk.Label(self, text='Lata nauki:', font=font)
        education_label.grid(row=2, column=2)
        self.education_entry = tk.Entry(self, bd=5, validate='key', validatecommand=(education_validator, '%P'))
        self.education_entry.grid(row=3, column=2)
        self.education_entry.focus()
        self.education_entry.bind('<Return>', self.push_education)
        self.education_entry.bind('<Tab>', self.focus_next_widget)
        self.education_entry.bind('<Tab>', self.push_education)

    def push_education(self, event=None):
        self.education = self.education_entry.get()
        print(self.education)
        self.new_x_rating[0][2] = self.education

    def education_validation(self, education):
        try:
            if education == "":
                return True
            elif int(education) and len(education) < 3:
                return True
            else:
                raise ValueError
        except ValueError:
            self.bell()
            return False

    def get_sex(self):
        sex_label = tk.Label(self, text='Płeć:', font=font)
        sex_label.grid(row=5, column=0)
        self.sex_val = tk.IntVar(self, value=2)
        self.male_button = tk.Radiobutton(self, text='Mężczyzna', command=self.push_sex,
                                          font=font, variable=self.sex_val, value=1, indicatoron=1)
        self.male_button.grid(row=6, column=0)
        self.female_button = tk.Radiobutton(self, text='Kobieta', command=self.push_sex,
                                            font=font, variable=self.sex_val, value=0, indicatoron=1)
        self.female_button.grid(row=7, column=0)
        self.male_button.bind('<Return>', self.select_male)
        self.female_button.bind('<Return>', self.select_female)

    def push_sex(self, event=None):
        self.sex = self.sex_val.get()
        self.martial_sex()
        print(self.sex)
        self.new_x_rating[0][3] = self.sex


    def select_male(self, male_button):
        self.male_button.invoke()

    def select_female(self, female_button):
        self.female_button.invoke()

    def get_student(self):
        student_label = tk.Label(self, text='Studia w trakcie:', font=font)
        student_label.grid(row=5, column=1)
        self.student_val = tk.IntVar(self, value=2)
        self.yes_button = tk.Radiobutton(self, text='Tak', command=self.push_student,
                                         font=font, variable=self.student_val, value=1, indicatoron=1)
        self.yes_button.grid(row=6, column=1)
        self.no_button = tk.Radiobutton(self, text='Nie', command=self.push_student,
                                        font=font, variable=self.student_val, value=0, indicatoron=1)
        self.no_button.grid(row=7, column=1)
        self.male_button.bind('<Return>', self.select_yes)
        self.no_button.bind('<Return>', self.select_no)

    def push_student(self, event=None):
        self.student = self.student_val.get()
        print(self.student)
        self.new_x_rating[0][4] = self.student

    def select_yes(self, yes_button):
        self.yes_button.invoke()

    def select_no(self, no_button):
        self.no_button.invoke()

    def martial_sex(self):
        self.trapped_button.destroy()
        self.free_button.destroy()
        if self.sex == 1:
            self.get_martial_male()
        if self.sex == 0:
            self.get_martial_female()

    def get_martial_male(self):
        martial_label = tk.Label(self, text='Stan cywilny:', font=font)
        martial_label.grid(row=5, column=2)
        self.martial_val = tk.IntVar(self, value=2)
        self.trapped_button = tk.Radiobutton(self, text='Żonaty', command=self.push_martial,
                                             font=font, variable=self.martial_val, value=1, indicatoron=1)
        self.trapped_button.grid(row=6, column=2)
        self.free_button = tk.Radiobutton(self, text='Kawaler', command=self.push_martial,
                                          font=font, variable=self.martial_val, value=0, indicatoron=1)
        self.free_button.grid(row=7, column=2)
        self.trapped_button.bind('<Return>', self.select_trapped)
        self.free_button.bind('<Return>', self.select_free)

    def get_martial_female(self):
        martial_label = tk.Label(self, text='Stan cywilny:', font=font)
        martial_label.grid(row=5, column=2)
        self.martial_val = tk.IntVar(self, value=2)
        self.trapped_button = tk.Radiobutton(self, text='Zamężna', command=self.push_martial,
                                             font=font, variable=self.martial_val, value=1, indicatoron=1)
        self.trapped_button.grid(row=6, column=2)
        self.free_button = tk.Radiobutton(self, text='Panna', command=self.push_martial,
                                          font=font, variable=self.martial_val, value=0, indicatoron=1)
        self.free_button.grid(row=7, column=2)
        self.trapped_button.bind('<Return>', self.select_trapped)
        self.free_button.bind('<Return>', self.select_free)

    def push_martial(self, event=None):
        self.martial = self.martial_val.get()
        print(self.martial)
        self.new_x_rating[0][5] = self.martial

    def select_trapped(self, trapped_button):
        self.trapped_button.invoke()

    def select_free(self, free_button):
        self.free_button.invoke()

    def get_ethnicity(self):
        ethnicity_label = tk.Label(self, text='Etniczność:', font=font)
        ethnicity_label.grid(row=9, column=1)
        self.ethnicity_val = tk.IntVar(self, value=0)
        self.caucasian_button = tk.Radiobutton(self, text='Kaukaska', command=self.push_ethnicity,
                                             font=font, variable=self.ethnicity_val, value=1, indicatoron=1)
        self.caucasian_button.grid(row=10, column=1)
        self.asian_button = tk.Radiobutton(self, text='Azjatycka', command=self.push_ethnicity,
                                          font=font, variable=self.ethnicity_val, value=2, indicatoron=1)
        self.asian_button.grid(row=11, column=1)
        self.nigger_button = tk.Radiobutton(self, text='Afroamerykańska', command=self.push_ethnicity,
                                           font=font, variable=self.ethnicity_val, value=3, indicatoron=1)
        self.nigger_button.grid(row=12, column=1)
        self.caucasian_button.bind('<Return>', self.select_caucasian)
        self.asian_button.bind('<Return>', self.select_asian)
        self.nigger_button.bind('<Return>', self.select_nigger)

    def push_ethnicity(self, event=None):
        self.ethnicity = self.ethnicity_val.get()
        print(self.ethnicity)
        self.new_x_rating[0][6] = self.ethnicity
        print(self.new_x_rating)
        self.predict_rating()

    def select_caucasian(self, caucasian_button):
        self.caucasian_button.invoke()

    def select_asian(self, asian_button):
        self.asian_button.invoke()

    def select_nigger(self, nigger_button):
        self.nigger_button.invoke()

    def new_x_rating(self):
        self.new_x_rating = [[0.0, 0, 0, 0, 0, 0, 0]]

    def predict_rating(self):
        scaler_rating = load('svr_scaler_rating.joblib')
        model_rating = load('svr_model_rating.joblib')
        x_new_rating_scaler = scaler_rating.transform(self.new_x_rating)
        y_new_rating = model_rating.predict(x_new_rating_scaler)
        self.rating = int(y_new_rating)
        print(self.rating)


class Current(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='Obecny klient', font=large_font).grid(row=0, columnspan=3)
        tk.Button(self, text='Main menu', font=font,
                  command=lambda: master.switch_frame(Main)).grid(row=11, columnspan=3, sticky='nsew')


if __name__ == '__main__':
    app = Credit()
    app.title('Tic Tac Toe')
    app.geometry('500x600+10+10')
    app.resizable(False, False)
    app.mainloop()
