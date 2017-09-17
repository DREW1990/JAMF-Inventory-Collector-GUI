import Tkinter as tk
import ttk
import AppKit
import base64
from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import subprocess
import tkMessageBox
import sys
import time

# Base 64 image of the logo
inventory_collector_logo = '''
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
'''
# Base 64 image of the asset tag
asset_tag_image = '''
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
'''

# ************ Main Class ************
class InventoryCollector(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        # Set pack to give a standard padding of 30 pixels on the sides and top and bottom
        self.pack(padx=30, pady=30)

        # Set title to "Inventory Collector"
        self.master.title("Inventory Collector")

        # Disables the window to be resized
        self.master.resizable(False, False)

        #Changes background to default of OS
        self.master.tk_setPalette(background='#e6e6e6')

        # ************ Set app resolution and window placement ************
        # Main app resolution
        w = 660
        h = 600

        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen

        # Dividing the width of the screen by 2 and heigh by 3 for proper window placement
        x = (ws/2) - (w/2)
        y = (hs/3) - (h/3)

        # Sets window placement
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Hide menu bar
        self.master.config(menu=tk.Menu(self.master))

        # Assign logo to a variable
        self.logo = tk.PhotoImage(data=inventory_collector_logo)

        # Place logo at the top
        tk.Label(self, image = self.logo).grid(row=0, columnspan=4, pady=15, sticky='s')


        # ************ Retrieve user's Full name ************
        tk.Label(self, text='First and last name:').grid(sticky='e') # Label

        self.full_name_entry = tk.Entry(self, bg='white', width=30) # Entry box
        self.full_name_entry.grid(row=1, column=1, pady=15, columnspan=2) # Entry box placement

        # ************ Retrieve user's work email address ************
        tk.Label(self, text='Work email address:').grid(sticky='e')

        self.emailaddress_entry = tk.Entry(self, bg='white', width=30)
        self.emailaddress_entry.grid(row=2, column=1, pady=15, columnspan=2)

        # ************ Retrieve user's position ************
        tk.Label(self, text='Job title:').grid(sticky='e')

        self.position_entry = tk.Entry(self, bg='white', width=30)
        self.position_entry.grid(row=3, column=1, pady=15, columnspan=2)

        # ************ Retrieve user's Department ************
        tk.Label(self, text='Department:').grid(sticky='e')

        # Create a "department" list and fill it with the specific departments
        departments = ['HR',
             'Legal',
             'Finance',
             'Sales',
             'Marketing',
             'Engineering',
             'IT']

        self.departmentSelection = tk.StringVar() # Assign string variable for drop down selection
        self.departmentSelection.set(departments[0]) # By default set drop down box to show the first department

        # Create the drop down and fill it with the department list
        self.department_entry = tk.OptionMenu(self, self.departmentSelection, *departments).grid(row=4, column=1, columnspan=2, pady=15, sticky='ew')

        # ************ Retrieve user's building ************
        tk.Label(self, text='Office location:').grid(sticky='e')

        # Create a "buildings" list and fill it with the different offices
        buildings = ['Chicago',
            'Los Angeles',
            'New York',
            'San Francisco',
            'London']

        self.buildingSelection = tk.StringVar() # Assign string variable for drop down selection
        self.buildingSelection.set(buildings[0]) # By default set drop down box to show the first building

        # Create the drop down and fill it with the list of buildings
        self.building_entry = tk.OptionMenu(self, self.buildingSelection, *buildings).grid(row=5, column=1, columnspan=2, pady=15, sticky='ew')

        # ************ Retrieve user's asset tag ************
        tk.Label(self, text="Your computer's asset tag number\n(barcode under your computer):").grid(sticky='e')

        self.assetTag_entry = tk.Entry(self, bg='white', width=30)
        self.assetTag_entry.grid(row=6, column=1, pady=(15,0), columnspan=2)

        # Assign asset tag image to a variable
        self.asset_tag_picture = tk.PhotoImage(data=asset_tag_image)

        # Place asset tag image
        tk.Label(self, image = self.asset_tag_picture).grid(row=7, columnspan=1, sticky='n')

        # ************ OK and SUBMIT buttons ************

        # Create a 'Cancel' button and have it run the click_cancel function if pressed
        tk.Button(self, text='Cancel', height=1, width=6, command=self.click_cancel).grid(row=7, column=2, sticky='e', pady=(30,1))

        # Create a 'Submit' button and have it run the click_submit function if pressed
        tk.Button(self, text='Submit', height=1, width=6, default='active', command=self.click_submit).grid(row=7, column=3, pady=(30,1))

        # ************ Defines what the Submit button does ************
    def click_submit(self, event=None):
        print("The user clicked 'Submit'. Here are the results...")

        # Return Full name
        fullName = str(self.full_name_entry.get()) # Assign entry box to a variable
        print("Full name: {}".format(fullName))

        # Retrieve BuzzFeed email address
        emailAddress = str(self.emailaddress_entry.get())# Assign entry box to a variable
        print("BuzzFeed email address: {}".format(emailAddress))

        # Retrieve position
        position = str(self.position_entry.get()) # Assign entry box to a variable
        print("Position: {}".format(position))

        # Retrieve department
        department = str(self.departmentSelection.get()) # Assign chosen option to a variable
        print("Department: {}".format(department))

        # Retrieve building
        building = str(self.buildingSelection.get()) # Assign chosen option to a variable
        print("Building: {}".format(building))

        # Retrieve asset tag
        assetTag = str(self.assetTag_entry.get()) # Assign entry box to a variable
        print("Asset tag: {}".format(assetTag))

        # Retrieve logged in username

        # Clears console variables just incase they were assigned by another app
        name, uid, gid = SCDynamicStoreCopyConsoleUser(None, None, None)
        username = str(name) # Assign logged in username to a variable
        print("Username: {}".format(username))

        # ************ Defines what the OK button does ************
        def click_ok():
            print("The user clicked 'OK!'")
            print("Running: jamf recon....")

            root.withdraw() # Hides main window
            self.destroy() # Hides confirmation window

            time.sleep(3) # Delay the app for 3 seconds to make sure subprocess runs

            # Subprocess runs JAMF recon command
            subprocess.call(["jamf", "recon", "-verbose",
                "-endUsername", emailAddress,
                "-realname", fullName,
                "-email", emailAddress,
                "-position", position,
                "-assetTag", assetTag,
                "-department", department,
                "-building", building])

            sys.exit(0) # Exit application after subprocess is done running


        # ************ Confirmation Window ************
        top = tk.Toplevel(self)
        top.title("Inventory Collector")

        # Set the size of the window
        w2 = 360
        h2 = 140

        ws2 = top.winfo_screenwidth() # width of the screen
        hs2 = top.winfo_screenheight() # height of the screen

        # Set specific placement of the window
        x2 = (ws2/2) - (w2/2)
        y2 = (hs2/3) - (h2/3)

        top.geometry('%dx%d+%d+%d' % (w2, h2, x2, y2))

        # Confirmation message at the top of the box
        self.confirmation_message = tk.Message(top, text="Sending information to IT", justify='center', font='System 14 bold', aspect=1000).grid(row=0, column=0, columnspan=3, padx=15, pady=15, sticky='e'+'w'+'n'+'s')

        # Confirmation information
        self.confirmation_label = tk.Label(top, text="The information will now be sent to the IT team!").grid(row=1, column=0, columnspan=3, padx=15, sticky='e'+'w'+'n'+'s' )

        # Place the OK button
        self.ok_button = tk.Button(top, text='OK!', height=1, width=6, default='active', command=click_ok).grid(row=2, column=2, sticky='e', pady=10)


        # ************ Define what the Cancel button does ************
    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        self.master.destroy()


# ************ Function that actually 'runs' the app ************
if __name__ == '__main__':
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True

    root = tk.Tk()

    app = InventoryCollector(root)

    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)

    app.mainloop()
