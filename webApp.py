import tkinter as tk
from tkinter import *
import os
import sys
import covid_scrapper 

root = tk.Tk()

array = [] 
array = covid_scrapper.country_list
diction = covid_scrapper.dictionary
worldyData = covid_scrapper.world_data_list

def open_world_data():
    top = Toplevel()
    #top['background']='#E0FFFF'
    top.title('World Statistics')
    back_button = Button(top, text = 'Go to Main', command = top.destroy).pack()
    name_Text_world = Text(top)
    #name_Text_world.configure(bg = '#E0FFFF')
    name_Text_world.insert(INSERT, "Total Cases in the World are: " + worldyData[0] + "\n" + "\n" + "Total Deaths:" + worldyData[1]
    + "\n" + "\n" + "Total Recovered:" + worldyData[2])
    name_Text_world.pack()

def open_country_list():
    top1 = Toplevel()
    #top1['background']='#E0FFFF'
    top1.title('List of Countries')
    back_button1 = Button(top1, text = 'Go to Main', command = top1.destroy).pack()
    global clicked
    clicked = StringVar()
    clicked.set("Pick a country")
    drop = OptionMenu(top1, clicked , *array ).pack()
    button_of_selection = Button(top1, text = "Get Statistics", command = get_Country_Data).pack()

def get_Country_Data():
    top3 = Toplevel()
    #top3['background']='#E0FFFF'
    top3.title(clicked.get())
    strinName = clicked.get()
    back_button3 = Button(top3, text = 'Back', command = top3.destroy).pack()
    for key, value in diction.items():
        if key == strinName:
            name_Text = Text(top3)
            name_Text.insert(INSERT,"Country Name: " + value[1] + "\n" + "\n" + "Ranked: " + value[0] + "\n" + "\n"  + "Total Cases: " + value[2] + "\n"
            + "\n" + "New Cases: " + value[3] + "\n"+ "\n" + "Total Deaths: " + value[4] + "\n"+ "\n" + "New Deaths: " + value[5] + "\n"
            + "\n" + "Total Recovered: " + value[6] + "\n" + "\n" + "Active Cases: " + value[8] + "\n") 
            name_Text.pack()
            

worldwide_button = Button(root, text = "Worldwide Cases",padx=50, command = open_world_data)
countrywide_button = Button(root, text = "Countrywide Cases", padx =50, command = open_country_list)

worldwide_button.place(relx=0.5, rely=0.4, anchor=CENTER)
countrywide_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.title("Covid Insights Web Application")
root.geometry("600x450")
#root['background']='#E0FFFF'

root.mainloop()



