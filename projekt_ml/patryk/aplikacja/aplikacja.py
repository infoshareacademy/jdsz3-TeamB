import tkinter as tk
from joblib import load
import csv
import os.path
from numpy import genfromtxt

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
        tk.Label(self, text=' ', font=large_font).grid(row=2, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=3, sticky='nsew')
        tk.Button(self, text='Nowy klient', font=font,
                  command=lambda: master.switch_frame(New)).grid(row=4, sticky='nsew')
        tk.Button(self, text='Obecny klient', font=font,
                  command=lambda: master.switch_frame(Current)).grid(row=5, sticky='nsew')
        tk.Button(self, text='Wyjście', font=font, command=lambda: master.destroy()).grid(row=6, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=7, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=8, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=9, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=10, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=11, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=12, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=13, sticky='nsew')
        tk.Label(self, text='made by team: Fajni').grid(row=14, sticky='nsew')


class New(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='Nowy klient', font=large_font).grid(row=0, columnspan=3)
        tk.Label(self, text=' ', font=large_font).grid(row=1, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=4, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=8, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=11, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=14, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=17, columnspan=3, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=12, column=0, sticky='nsew')
        tk.Label(self, text=' ', font=large_font).grid(row=13, column=0, sticky='nsew')
        tk.Button(self, text='Main menu', font=font,
                  command=lambda: master.switch_frame(Main)).grid(row=18, columnspan=3, sticky='nsew')
        tk.Button(self, text='Reset', font=font,
                  command=lambda: self.reset(master)).grid(row=16, column=0, sticky='nsew')
        self.income = 0
        self.age = 0
        self.education = 0
        self.rating = 0
        self.sex = 2
        self.student = 2
        self.martial = 2
        self.ethnicity = 0
        self.new_x_rating = [[0.0, 0, 0, 0, 0, 0, 0]]
        self.limit = 0
        self.new_x_limit = [[0.0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.count_button()
        self.save_button()
        self.get_income()
        self.get_age()
        self.get_education()
        self.get_sex()
        self.get_student()
        self.get_martial_male()
        self.get_ethnicity()
        self.show_rating()
        self.show_limit()

    def check_save_button(self):
        if self.income != 0 and self.age != 0 and self.education != 0 and self.sex != 2\
                and self.student != 2 and self.martial != 2 and self.ethnicity != 0:
            self.save.destroy()
            self.save = tk.Button(self, text='Zapisz', command=self.save_file, font=font)
            self.save.grid(row=15, column=0, sticky='nsew')

    def save_file(self):
        check_file = os.path.isfile('nowi_klienci.csv')
        if not check_file:
            self.client_id = 401
        else:
            my_data = genfromtxt('nowi_klienci.csv', delimiter=',')
            last_id = my_data[-1][0]
            self.client_id = int(last_id + 1)
        nowi_klienci = open('nowi_klienci.csv', 'a', newline='')
        columns = ['NumerKlienta', 'Income', 'Rating', 'Limit', 'Age', 'Education', 'GenderNumeric',
                   'StudentNumeric', 'MarriedNumeric','EthnicityNumeric', 'Rating_Y']
        writer = csv.DictWriter(nowi_klienci, fieldnames=columns)
        if not check_file:
            writer.writeheader()
        writer.writerow({'NumerKlienta': self.client_id, 'Income': self.income, 'Rating': self.rating,
                         'Limit': self.limit, 'Age': self.age,'Education': self.education,
                         'GenderNumeric': self.sex, 'StudentNumeric': self.student,'MarriedNumeric': self.martial,
                         'EthnicityNumeric': self.ethnicity, 'Rating_Y': self.rating_y})
        self.popup_save_message()

    def popup_save_message(self):
        popup = tk.Toplevel()
        tk.Label(popup).pack()
        popup_text = 'Nowy numer klienta:'
        popup_id = self.client_id
        tk.Label(popup, text=popup_text, font=font).pack()
        tk.Label(popup, text=popup_id, font=large_font).pack()
        tk.Label(popup).pack()
        tk.Button(popup, text='Close', font=font, command=lambda: popup.destroy()).pack()
        tk.Label(popup).pack()
        popup.geometry('250x160+10+10')
        popup.resizable(False, False)
        popup.title('Zapisano')
        self.save.destroy()
        self.save_button()
        #popup.iconbitmap(icon)

    def save_button(self):
        self.save = tk.Button(self, text='Zapisz', font=font, state='disabled')
        self.save.grid(row=15, column=0, sticky='nsew')

    def reset(self, master):
        self.destroy()
        master.switch_frame(New)

    def count_button(self):
        self.count = tk.Button(self, text='Oblicz rating\noraz limit', font=font, state='disabled')
        self.count.grid(row=12, rowspan=2, column=0, sticky='nsew')

    def check_count_button(self):
        if self.income != 0 and self.age != 0 and self.education != 0 and self.sex != 2\
                and self.student != 2 and self.martial != 2 and self.ethnicity != 0:
            self.count.destroy()
            self.count_active = tk.Button(self, text='Oblicz rating\noraz limit', font=font,
                                          command=self.predict_rating)
            self.count_active.grid(row=12, rowspan=2, column=0, sticky='nsew')

    def get_income(self):
        income_validator = self.register(self.income_validation)
        income_label = tk.Label(self, text='Zarobki:', font=font)
        income_label.grid(row=2, column=0)
        self.income_entry = tk.Entry(self, bd=5, validate='key', validatecommand=(income_validator, '%P'))
        self.income_entry.grid(row=3, column=0)
        self.income_entry.focus_set()
        self.income_entry.bind('<Return>', self.push_income)
        self.income_entry.bind('<Tab>', self.push_income)
        self.income_entry.bind('<FocusOut>', self.push_income)

    def push_income(self, event=None):
        if self.income_entry.get() == '':
            self.income = 0
        else:
            self.income = float(self.income_entry.get())
        print(self.income)
        self.new_x_rating[0][0] = (float(self.income) / 100)
        self.new_x_limit[0][0] = (float(self.income) / 100)
        self.check_count_button()

    def income_validation(self, income):
        try:
            if income == '':
                return True
            elif float(income) and len(income) < 10:
                return True
            elif int(income) and len(income) < 7:
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
        self.age_entry.bind('<Tab>', self.push_age)
        self.age_entry.bind('<FocusOut>', self.push_age)

    def push_age(self, event=None):
        if self.age_entry.get() == '':
            self.age = 0
        else:
            self.age = int(self.age_entry.get())
        print(self.age)
        self.new_x_rating[0][1] = self.age
        self.new_x_limit[0][2] = self.age
        self.check_count_button()

    def age_validation(self, age):
        try:
            if age == '':
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
        self.education_entry.bind('<Tab>', self.push_education)
        self.education_entry.bind('<FocusOut>', self.push_education)

    def push_education(self, event=None):
        if self.education_entry.get() == '':
            self.education = 0
        else:
            self.education = int(self.education_entry.get())
        print(self.education)
        self.new_x_rating[0][2] = self.education
        self.new_x_limit[0][3] = self.education
        self.check_count_button()

    def education_validation(self, education):
        try:
            if education == '':
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
        self.push_income()
        self.push_age()
        self.push_education()
        self.sex = int(self.sex_val.get())
        self.martial_sex()
        print(self.sex)
        self.new_x_rating[0][3] = self.sex
        self.new_x_limit[0][4] = self.sex
        self.check_count_button()

    def select_male(self, male_button):
        self.male_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

    def select_female(self, female_button):
        self.female_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

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
        self.yes_button.bind('<Return>', self.select_yes)
        self.no_button.bind('<Return>', self.select_no)

    def push_student(self, event=None):
        self.push_income()
        self.push_age()
        self.push_education()
        self.student = int(self.student_val.get())
        print(self.student)
        self.new_x_rating[0][4] = self.student
        self.new_x_limit[0][5] = self.student
        self.check_count_button()

    def select_yes(self, yes_button):
        self.yes_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

    def select_no(self, no_button):
        self.no_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

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
        self.push_income()
        self.push_age()
        self.push_education()
        self.martial = int(self.martial_val.get())
        print(self.martial)
        self.new_x_rating[0][5] = self.martial
        self.new_x_limit[0][6] = self.martial
        self.check_count_button()

    def select_trapped(self, trapped_button):
        self.trapped_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

    def select_free(self, free_button):
        self.free_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

    def get_ethnicity(self):
        ethnicity_label = tk.Label(self, text='Etniczność:', font=font)
        ethnicity_label.grid(row=9, column=1)
        self.ethnicity_val = tk.IntVar(self, value=0)
        self.caucasian_button = tk.Radiobutton(self, text='Kaukaska', command=self.push_ethnicity,
                                             font=font, variable=self.ethnicity_val, value=1, indicatoron=1)
        self.caucasian_button.grid(row=10, column=0)
        self.asian_button = tk.Radiobutton(self, text='Azjatycka', command=self.push_ethnicity,
                                          font=font, variable=self.ethnicity_val, value=2, indicatoron=1)
        self.asian_button.grid(row=10, column=1)
        self.nigger_button = tk.Radiobutton(self, text='Afroamerykańska', command=self.push_ethnicity,
                                           font=font, variable=self.ethnicity_val, value=3, indicatoron=1)
        self.nigger_button.grid(row=10, column=2)
        self.caucasian_button.bind('<Return>', self.select_caucasian)
        self.asian_button.bind('<Return>', self.select_asian)
        self.nigger_button.bind('<Return>', self.select_nigger)

    def push_ethnicity(self, event=None):
        self.push_income()
        self.push_age()
        self.push_education()
        self.ethnicity = int(self.ethnicity_val.get())
        print(self.ethnicity)
        self.new_x_rating[0][6] = self.ethnicity
        self.new_x_limit[0][7] = self.ethnicity
        self.check_count_button()
        print(self.new_x_rating)

    def select_caucasian(self, caucasian_button):
        self.caucasian_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

    def select_asian(self, asian_button):
        self.asian_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

    def select_nigger(self, nigger_button):
        self.nigger_button.invoke()
        self.push_income()
        self.push_age()
        self.push_education()

    def predict_rating(self):
        scaler_rating = load('svr_scaler_rating.joblib')
        model_rating = load('svr_model_rating.joblib')
        x_new_rating_scaler = scaler_rating.transform(self.new_x_rating)
        y_new_rating = model_rating.predict(x_new_rating_scaler)
        if self.income < 1000 or self.age < 18 or self.education < 8:
            self.rating = 0
        else:
            self.rating = int(y_new_rating)
        self.new_x_limit[0][1] = self.rating
        self.show_rating_change()
        print(self.rating)

    def show_rating(self):
        rating_label = tk.Label(self, text='Rating:  ', font=font)
        rating_label.grid(row=12, column=1, rowspan=2, sticky='e')
        if self.rating <= 274:
            bg_color = 'red'
            self.rating_y = 0
        elif 274 < self.rating <= 299:
            bg_color = 'yellow'
            self.rating_y = 1
        elif self.rating > 299:
            bg_color = 'green'
            self.rating_y = 2
        self.new_x_limit[0][8] = self.rating_y
        rating_text = self.rating
        self.rating_color = tk.LabelFrame(self, bg=bg_color, relief='raised', font=font)
        self.rating_color.grid(row=12, column=2, rowspan=2, sticky='nsew')
        self.rating_color_text = tk.Label(self.rating_color, bg=bg_color, text=rating_text, font=large_font)
        self.rating_color_text.pack(expand=True, fill="none")

    def show_rating_change(self):
        self.rating_color.destroy()
        self.rating_color_text.destroy()
        self.show_rating()
        self.predict_limit()

    def predict_limit(self):
        scaler_limit = load('svr_scaler_limit.joblib')
        model_limit = load('svr_model_limit.joblib')
        x_new_limit_scaler = scaler_limit.transform(self.new_x_limit)
        y_new_limit = model_limit.predict(x_new_limit_scaler)
        self.limit = int(y_new_limit)
        self.show_limit_change()
        print(self.limit)

    def show_limit(self):
        limit_label = tk.Label(self, text='Limit:  ', font=font)
        limit_label.grid(row=15, column=1, rowspan=2, sticky='e')
        if self.rating_y == 0:
            limit_text = 0
        else:
            limit_text = self.limit
        self.limit_color = tk.LabelFrame(self, relief='raised', font=font)
        self.limit_color.grid(row=15, column=2, rowspan=2, sticky='nsew')
        self.limit_color_text = tk.Label(self.limit_color, text=limit_text, font=large_font)
        self.limit_color_text.pack(expand=True, fill="none")

    def show_limit_change(self):
        self.limit_color.destroy()
        self.limit_color_text.destroy()
        self.show_limit()
        self.check_save_button()


class Current(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='Obecny klient', font=large_font).grid(row=0, columnspan=3)
        tk.Button(self, text='Main menu', font=font,
                  command=lambda: master.switch_frame(Main)).grid(row=11, columnspan=3, sticky='nsew')


if __name__ == '__main__':
    app = Credit()
    app.title('Kalkulator zdolności kredytowej')
    app.geometry('520x700+10+10')
    app.resizable(False, False)
    app.mainloop()
