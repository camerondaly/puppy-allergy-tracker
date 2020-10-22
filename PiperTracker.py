from tkinter import *
import sqlite3
import datetime

root = Tk()
root.title('Pet Allergy Tracker App')
root.geometry("600x450")


### DATABASE
# Create a database or connect to one
conn = sqlite3.connect('piperlog.db')
# Create a cursor (let's call it 'c')
c = conn.cursor()

# Submit Function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('piperlog.db')
    # Create a cursor (let's call it 'c')
    c = conn.cursor()
    #Insert selections into table
    c.execute("INSERT INTO Piper VALUES (:month, :day, :year, :food, :benadryl, :outside, :energy, :poo_count, :poo_quality, :itching_paws, :bumpiness, :rawspots, :lounge, :bugspray)",
            {
                'month': month_clicked.get(),
                'day': day_clicked.get(),
                'year': year_clicked.get(),
                'food': food_clicked.get(),
                'benadryl': benadryl_clicked.get(),
                'outside': outside_clicked.get(),
                'energy': energy_clicked.get(),
                'poo_count': poo_clicked.get(),
                'poo_quality': poo_q_clicked.get(),
                'itching_paws': itching_paws_clicked.get(),
                'bumpiness': bumpiness_clicked.get(),
                'rawspots': raw_spots_clicked.get(),
                'lounge': lounge_clicked.get(),
                'bugspray': bugspray_clicked.get()
            }
    )
    # Commit changes and close
    conn.commit()
    conn.close()
    # reset the input fields
    month_clicked.set(month_options[0])
    day_clicked.set(day_options[0])
    year_clicked.set(year_options[0])
    food_clicked.set(food_options[0])
    benadryl_clicked.set(benadryl_options[0])
    outside_clicked.set(outside_options[0])
    energy_clicked.set(energy_options[0])
    poo_clicked.set(poo_options[0])
    poo_q_clicked.set(poo_q_options[0])
    itching_paws_clicked.set(itching_paws_options[0])
    bumpiness_clicked.set(bumpiness_options[0])
    raw_spots_clicked.set(raw_spots_options[0])
    lounge_clicked.set(lounge_options[0])



# Query Function:
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('piperlog.db')
    # Create a cursor (let's call it 'c')
    c = conn.cursor()
    # Query the db!
    c.execute("SELECT *, oid FROM Piper")
    records = c.fetchall()

    # Commit changes and close
    conn.commit()
    conn.close()
    return



### MENU OPTIONS
# Boxes for date, food type, Benedryl (AM, PM, Both, None), Mood, Poo

'''
Perhaps there is a way to modularize this portion by making classes for the OptionMenu's that are very similar...
They all have: 
something =StringVar()
something.set(first index item)
somethingelse = OptionMenu(etc.)
somethingelse.grid(row and column)
'''


month_options = ["Month", *range(1, 13, 1)]
day_options = ["Day", *range(1,31)]
year_options = ["Year", *range(2019, 2022)]
month_clicked = StringVar()
month_clicked.set(month_options[0])
month = OptionMenu(root, month_clicked, *month_options)
month.grid(row = 0, column = 1)
day_clicked = StringVar()
day_clicked.set(day_options[0])
day = OptionMenu(root, day_clicked, *day_options)
day.grid(row = 0, column = 2)
year_clicked = StringVar()
year_clicked.set(year_options[0])
year = OptionMenu(root, year_clicked, *year_options)
year.grid(row = 0, column = 3)

food_options = [
    "Select Food:",
    "Rawwble Turkey", 
    "Rawwble Lamb",
    "Rawwble mixture", 
    "Home-made (yum!)"
]
food_clicked = StringVar()
food_clicked.set(food_options[0])
food = OptionMenu(root, food_clicked, *food_options)
food.grid(row = 1, column = 1)

benadryl_options = [
    "Select Benadryl Dosage:",
    "None", 
    "Yes - AM", 
    "Yes - PM", 
    "Yes - Both"
]
benadryl_clicked = StringVar()
benadryl_clicked.set(benadryl_options[0])
benadryl = OptionMenu(root, benadryl_clicked, *benadryl_options)
benadryl.grid(row = 2, column = 1)

outside_options = [
    "Time spent outside:",
    "Less than 30 minutes in the yard",
    "30 - 60 mins in the yard",
    "1 hour+ in the yard",
    "Walked around somewhere -- exposed to ~nature~ and mysterious plants!"
]
outside_clicked = StringVar()
outside_clicked.set(outside_options[0])
outside = OptionMenu(root, outside_clicked, *outside_options)
outside.grid(row = 3, column = 1)

energy_options = [
    "Describe energy levels:",
    "Lethargic",
    "Sleepy",
    "Acting weird. Low energy.",
    "Normal (:",
    "Playful",
    "Hyper!!!",
    "Acting like she did that one time when she ate a bag of coffee beans",
    "Cute as a button",
    "This is an extremely scientific endeavor"
]
energy_clicked = StringVar()
energy_clicked.set(energy_options[0])
energy = OptionMenu(root, energy_clicked, *energy_options)
energy.grid(row = 5, column = 1)

poo_options = ["Number of Poos: (0-10)", *range(0,11)]
poo_clicked = StringVar()
poo_clicked.set(poo_options[0])
poo_count = OptionMenu(root, poo_clicked, *poo_options)
poo_count.grid(row = 6, column = 1)

poo_q_options = ["Poo Quality (0 bad poo poo - 10 solid dooky)", *range(0,11)]
poo_q_clicked = StringVar()
poo_q_clicked.set(poo_q_options[0])
poo_quality = OptionMenu(root, poo_q_clicked, *poo_q_options)
poo_quality.grid(row = 7, column = 1)

itching_paws_options = ["Perceived paw itchiness level (0-10):", *range(0,11)]
itching_paws_clicked = StringVar()
itching_paws_clicked.set(itching_paws_options[0])
itching_paws = OptionMenu(root, itching_paws_clicked, *itching_paws_options)
itching_paws.grid(row = 8, column = 1)

bumpiness_options = ["Bumpiness (0-10):", *range(0, 11)]
bumpiness_clicked = StringVar()
bumpiness_clicked.set(bumpiness_options[0])
bumpiness = OptionMenu(root, bumpiness_clicked, *bumpiness_options)
bumpiness.grid(row = 9, column = 1)

raw_spots_options = ["Number of raw spots (0-10):", *range(0,11)]
raw_spots_clicked = StringVar()
raw_spots_clicked.set(raw_spots_options[0])
raw_spots = OptionMenu(root, raw_spots_clicked, *raw_spots_options)
raw_spots.grid(row = 10, column = 1)

lounge_options = ["About how many minutes did Piper spend lounging in the grass today?", *range(0,100, 10)]
lounge_clicked = StringVar()
lounge_clicked.set(lounge_options[0])
lounge = OptionMenu(root, lounge_clicked, *lounge_options)
lounge.grid(row = 11, column = 1)

bugspray_options = ["Did Piper have Bug Spray on today when she was outside?", "Yes", "No"]
bugspray_clicked = StringVar()
bugspray_clicked.set(bugspray_options[0])
bugspray = OptionMenu(root, bugspray_clicked, *bugspray_options)
bugspray.grid(row = 12, column = 1)

# Create a submit button
submit_btn = Button(root, text = "Add Record to the Database", command = submit)
submit_btn.grid(row = 13, column = 1, columnspan = 2, pady = 30, padx = 30, ipadx = 100)

# Create a Query Button
'''
query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 11, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx=100)
'''

# Commit changes and close
conn.commit()
conn.close()

root.mainloop()