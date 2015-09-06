from Tkinter import *
import ScrolledText

class TheFirstOne:
    def __init__(self, parent):
        self.addButton = Button(text='Add', width=6,
                                command=self.add_state).grid(row=0,column=0,sticky=W)
        
        self.quitButton = Button(text='Quit', width=6,
                                 command=self.quit_main).grid(row=0,column=1,sticky=E)

        self.deleteButton = Button(text='Delete',width=6,
                                   command = self.delete_command).grid(row=0,column=6)
        
        self.addLabel = Label(text='Add: ').grid(row=1,column=0,sticky=W)

        self.addInput = Text(height=1,width=30)
        
        self.addInput.grid(row=1,column=1)
        
        self.outputLabel = Label(text='Traits:').grid(row=2, column=0)
        
        self.output = ScrolledText.ScrolledText(parent,
                                width = 30, height = 20)
        
        self.output.grid(row=3,column=0,columnspan=2)
        
        self.save_button = Button(text='Save',width=6,
                                  command=self.save_trait).grid(row=0,column=2)
        
        self.open_button = Button(text='Open',width=6,
                                  command = self.open_traits).grid(row=0,column=3)
    def add_state(self):
        trait = self.addInput.get("1.0",'end-1c')
        self.output.insert(END, trait)
        self.output.insert(END, '\n')
        self.addInput.delete("1.0",END)
        
    def save_trait(self):
        traits = self.output.get("1.0",END)
        myfile = open('textDoc.txt', 'w')
        myfile.write(traits)
        myfile.close()

    def delete_command(self):
        self.output.delete("1.0",END)
        self.addInput.delete("1.0",END)

    def open_traits(self):
        myfile = open('textDoc.txt', 'r')
        traits = myfile.read()
        myfile.close()
        self.output.delete("1.0",END)
        self.output.insert(END,traits)
    
    def quit_main(self):
        root.destroy()

        
root = Tk()
Bwenoa = TheFirstOne(root)
root.mainloop()
