from tkinter import *
root = Tk()

root.title("sales")
root.geometry("400x200")

month = ("january","febuary","march","april","may","june","july","august","september","october","november","december")
profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)
month_label = Label(root, text = month)
month_label.place(relx = 0.5, rely = 0.3, anchor = CENTER)
profits_label = Label(root, text = profits)
profits_label.place(relx = 0.5, rely = 0.4, anchor = CENTER)
max_profit_label = Label(root)
max_profit_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
min_profit_label = Label(root)
min_profit_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def findprofit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)

    print(max_profit_index)
    max_profit_month = month[max_profit_index]
    max_profit_label["text"] = "maximum profit of "+str (max_profit)+" was recorded in the month of "+str(max_profit_month)
    print("maximum profit of "+str (max_profit)+" was recorded in the month of "+str(max_profit_month))

    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    

    print(min_profit_index)
    min_profit_month = month[min_profit_index]
    min_profit_label["text"] = "minimum profit of "+str (min_profit)+" was recorded in the month of "+str(min_profit_month)
    print("minimum profit of "+str (min_profit)+" was recorded in the month of "+str(min_profit_month))

btn1 = Button(root, text = "start", command = findprofit)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()


