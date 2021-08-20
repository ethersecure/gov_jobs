import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

res = []


def getdata(url):
	r = requests.get(url)
	return r.text


def getinfo():
	result = ''
	htmldata = getdata("https://www.sarkariresult.com/latestjob.php")
	soup = BeautifulSoup(htmldata, 'html.parser')
	
	for li in soup.find_all("div", id="post"):
		result += (li.get_text())
	res.set(result)

master = Tk()
master.configure(bg='light grey')

res = StringVar()

Label(master, text="List of the Jobs :",
	bg="light grey", font="100").grid(row=0, sticky=W)

Label(master, text="", textvariable=res, bg="light grey").grid(
	row=3, column=1, sticky=W)

b = Button(master, text="Get latest job", command=getinfo)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
