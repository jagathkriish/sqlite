import wx
from wx.lib.masked import NumCtrl

class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Background Reset Tutorial",size=wx.Size(500,500))
 
        # Add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        #self.txt = wx.Button(self.panel,id=wx.ID_ANY,pos=(0,30),size=(100,30))
        sampleList = ['Input string', 'Input number','Checkbox','Dropdown','Toggle']
        self.txt = wx.ComboBox(self.panel, 500, "", (0,0), 
                         (170,50), sampleList,
                         wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        Btn = wx.Button(self.panel, label="Submit")
        Btn.Bind(wx.EVT_BUTTON, self.onEnter)

        Btn1 = wx.Button(self.panel, label="Reset")
        Btn1.Bind(wx.EVT_BUTTON, self.onReset)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        btnSizer.Add(Btn, 0, wx.ALL|wx.CENTER, 5)
        btnSizer.Add(Btn1, 0, wx.ALL|wx.LEFT, 5)
        topSizer.Add(self.txt, 0, wx.ALL|wx.CENTER, 10)
        
        
        
        topSizer.Add(btnSizer, 0, wx.CENTER)
        self.panel.SetSizer(topSizer)

    def onEnter(self, event):
        label = self.txt.GetValue()
        if label == "Input string":
            #print("Input string it's working")
            self.txtstring = wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(190,110))

            self.btn = wx.Button(self.panel,id=wx.ID_ANY,label="Show",pos=(350,110))
            self.btn.Bind(wx.EVT_BUTTON,self.onShow)
            self.static = wx.TextCtrl(self.panel,id=1,pos=(10,200),size=(460,240),style=wx.TE_READONLY)
        elif label == "Input number":
            #print("Input number it's working")
            self.txtnum = NumCtrl(self.panel,id=wx.ID_ANY,pos=(200,110))

            self.btn1 = wx.Button(self.panel,id=wx.ID_ANY,label="Show",pos=(350,110))
            self.btn1.Bind(wx.EVT_BUTTON,self.onShow1)
            self.static1 = wx.TextCtrl(self.panel,id=1,pos=(10,200),size=(460,100),style=wx.TE_READONLY)
        elif label  == "Checkbox":
            #print("Checkbox it's working")
            self.CB1 = wx.CheckBox(self.panel,id=wx.ID_ANY,label="Example1",pos=(200,110))
            self.CB2 = wx.CheckBox(self.panel,id=wx.ID_ANY,label="Exmaple2",pos=(200,130))
            self.Bind(wx.EVT_CHECKBOX,self.onShow2)
            self.static2 = wx.TextCtrl(self.panel,id=1,pos=(10,200),size=(460,100),style=wx.TE_READONLY)
        elif label == "Dropdown":
            #print("Dropdown it's working")
            sampleList1 = ['Sample1','Sample2','Sample3']
            self.dod = wx.ComboBox(self.panel, 500, "", (160,110), 
                         (170,50), sampleList1,
                         wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
            self.btn2 = wx.Button(self.panel,id=wx.ID_ANY,label="Show",pos=(350,110))
            self.btn2.Bind(wx.EVT_BUTTON,self.onShow3)
            self.static3 = wx.TextCtrl(self.panel,id=1,pos=(10,200),size=(460,100),style=wx.TE_READONLY)
        elif label == "Toggle":
            #print("Toggle it's working")
            self.Toggle = wx.ToggleButton(self.panel,id=1,label="default",pos=(200,110))
            self.Toggle.Bind(wx.EVT_TOGGLEBUTTON,self.onShow4)
            self.static4 = wx.TextCtrl(self.panel,id=1,pos=(10,200),size=(460,100),style=wx.TE_READONLY)
        #self.btn = wx.Button(self.panel,id=wx.ID_ANY,label="Show",pos=(350,110))
        #self.btn.Bind(wx.EVT_BUTTON,self.onShow)
        #self.static = wx.TextCtrl(self.panel,id=1,pos=(10,200),size=(460,100),style=wx.TE_READONLY)
    def onShow(self,event):
        value = self.txtstring.GetValue() 
        self.static.SetValue(value)
    def onShow1(self,event):
        value = self.txtnum.GetValue() 
        self.static1.SetValue(str(value))
    def onShow2(self,event):
        cb = event.GetEventObject() 
        lab = cb.GetLabel()
        self.static2.SetValue(lab)
    def onShow3(self,event):
        value = self.dod.GetValue()
        self.static3.SetValue(value)
    def onShow4(self,event):
        TO = self.Toggle.GetValue()
        self.static4.SetValue(str(TO))
    def onReset(self,event):
        pass
# Run the program
if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()
