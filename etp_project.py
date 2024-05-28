from tkinter import *
import csv
import time

def add():
    root = Tk()
    root.title("ADD EXPENSE")
    root.configure(bg="#39DC98")
    root.geometry('800x400')

    options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
    clicked = StringVar()
    clicked.set("January")

    expense_types=["Fees","Food","Rent","Electricity","Entertainment","Other"]
    click=StringVar()
    click.set(expense_types[0])

    month = Label(root, text="Select Month", fg="black", bg="#39DC98", height=2, width=20, font=('bold')).grid(row=3, column=3)
    mnth = OptionMenu(root, clicked, *options)
    mnth.grid(row=3, column=4)

    type_lbl = Label(root, text="Type of Expense", bg="#39DC98", fg="black", height=2, width=20, font=('bold')).grid(row=4, column=3)
    typ = OptionMenu(root, click,*expense_types)
    typ.grid(row=4, column=4)

    amount_lbl = Label(root, text="Amount", bg="#39DC98", fg="black", height=2, width=10, font=('bold')).grid(row=5, column=3)
    amount = Entry(root, width=25)
    amount.grid(row=5, column=4)

    lab = Label(root, width=10, height=2, bg="#39DC98").grid(row=0, column=0)
    lab = Label(root, width=10, height=3, bg="#39DC98").grid(row=6, column=0)
    lab = Label(root, width=10, height=5, bg="#39DC98").grid(row=8, column=0)

    def submit():
        mn = clicked.get()
        ty = click.get()
        amount2 = amount.get()
    
    # append the data to expenses.csv
        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([mn, ty, amount2])
        
        print("Expense added to expenses.csv: ", mn, ty, amount2)
        
        label=Label(root,text="Added successfully",bg="green",fg="white").grid(row=9,column=4)
            
        time.sleep(5)
        root.destroy()
        

    submit_button = Button(root, text="Submit", bg="black", fg="white", height=2, width=10, command=submit)
    submit_button.grid(row=7, column=4)
    
    '''def ext():
        root.destroy()
    
    exit_button=Button (root,text="EXIT",bg="black", fg="white", height=2, width=10, command=ext).grid(row=9,column=4)
'''

    root.mainloop()


def remove_exp():
    pass

def disp():
    root = Tk()
    root.title("DISPLAY EXPENSES")
    root.configure(bg="#4a6274")
    root.geometry('1000x600')

    label=Label(root,height=3,bg="#4a6274").pack()

    text = Text(root, bg="#e2725a", fg="black")
    text.pack()

    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            text.insert(END, row[0].center(25)+row[1].center(25)+row[2].center(25) + '\n' )
            
    with open('budget.txt', 'r') as file:
        budget = float(file.read())

    
    with open('expenses.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  
        next(reader)
        total_expenses = sum(float(row[2]) for row in reader)

    # calculate the remaining budget
    remaining_budget = budget - total_expenses
    
    xy=' '*100+"REMAINING BUDGET : ₹"+str(remaining_budget)
    label=Label(root,height=1,bg="#4a6274").pack()
    printingBudget=Label(root,text=xy,bg="#4a6274",fg="white", font=('bold')).pack()
    label=Label(root,height=4,bg="#4a6274").pack()
    
    def ext():
        root.destroy()
    
    exit_button = Button(root, text="EXIT", bg="black", fg="white", height=2, width=20, command=ext)
    exit_button.pack()

    root.mainloop()

    pass

def upd_budget():
    root = Tk()
    root.title("UPDATE BUDGET")
    root.configure(bg="#007ea7")
    root.geometry('700x300')

    budget_lbl = Label(root, text="Enter New Budget", fg="black", bg="#007ea7", height=2, width=20, font=('bold'))
    budget_lbl.grid(row=3, column=3)

    budget = Entry(root, width=25)
    budget.grid(row=3, column=4)

    def submit():
        new_budget = budget.get()
        with open('budget.txt', 'w') as file:
            file.write(new_budget)
            
        label=Label(root,text="Updated successfully",bg="#007ea7",fg="black").grid(row=12,column=4)
            
        time.sleep(5)
        root.destroy()
            
    lab=Label(root,text="",bg="#007ea7",height=1,width=5).grid(row=4,column=0)
    lab=Label(root,text="",bg="#007ea7",height=4).grid(row=7,column=4)

    submit_button = Button(root, text="SUBMIT", bg="black", fg="white", height=2, width=20, command=submit)
    submit_button.grid(row=6, column=4)
    
    
    '''def ext():
        root.destroy()


    exit_button=Button (root,text="EXIT",bg="black", fg="white", height=2, width=15, command=ext).grid(row=9,column=4)
'''

    root.mainloop()

def display_budget():
    root=Tk()
    root.title("REMAINING BUDGET")
    root.geometry("500x500")
    root.configure(bg="#eae2b7")
    
    with open('budget.txt', 'r') as file:
        budget = float(file.read())

    
    with open('expenses.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  
        next(reader)
        total_expenses = sum(float(row[2]) for row in reader)

    remaining_budget = budget - total_expenses
    
    
    lab=Label(root,height=2,bg="#eae2b7").pack()

    # create a label widget to display the remaining budget
    budget_label = Label(root, text=f"Remaining budget: ₹{remaining_budget}",bg="#eae2b7",fg="black", font=('bold'))
    budget_label.pack()

    lab=Label(root,height=4,bg="#eae2b7").pack()

    
    def ext():
        root.destroy()


    exit_button=Button (root,text="EXIT",bg="black", fg="white", height=2, width=15, command=ext).pack()
    
    
    root.mainloop()




def monthly_exp():
    root=Tk()
    root.title("MONTHLY EXPENSE")
    root.configure(bg="#79aeb2")
    root.geometry("500x200")
    
    options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
    clicked = StringVar()
    clicked.set("January")
    
    month = Label(root, text="Select Month", fg="black", bg="#79aeb2", height=2, width=20, font=('bold')).grid(row=3, column=3)
    mnth = OptionMenu(root, clicked, *options)
    mnth.grid(row=3, column=4)
    
    def submit():
        mnth=clicked.get()
        total = 0.0
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == mnth:
                    total += float(row[2])
        
        la.configure(text=f'Amount spent in {mnth} : {total}')
        
        
    la=Label(root,text="",pady=30,bg="#79aeb2",fg="white")
    la.grid(row=8,column=4)  
    
    submit_button = Button(root, text="Submit", bg="black", fg="white", height=2, width=10, command=submit)
    submit_button.grid(row=7, column=4)
    
    root.mainloop()


def ext():
    root.destroy()


root=Tk()
root.title("Personal Finance Manager")

add_exp=Button(root,text="ADD EXPENSE",bg="#39D1DC",fg="black",height=4,width=30,command=add, font=('bold')).pack()
display=Button(root,text="DISPLAY",bg="#e4a9e8",fg="black",height=4,width=30,command=disp, font=('bold')).pack()
month_expense=Button(root,text="MONTHLY EXPENSE",bg="#727ac2",fg="black",height=4,width=30,command=monthly_exp, font=('bold')).pack()
dispBUDGET=Button(root,text="REMAINING BUDGET",height=4,width=30,fg="black",bg="#39D1DC",command=display_budget, font=('bold')).pack()
budg=Button(root,text="UPDATE BUDGET",bg="#e4a9e8",fg="black",height=4,width=30,command=upd_budget, font=('bold')).pack()
ext=Button(root,text="EXIT",bg="#727ac2",fg="black",height=4,width=30,command=ext, font=('bold')).pack()

root.mainloop()
