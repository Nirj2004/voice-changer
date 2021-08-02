from tkinter import Frame, BooleanVar, Checkbutton, \
        Label, Scale, Button, Radiobutton, HORIZONTAL, \
        Entry, DISABLED, NORMAL, Tk, DoubleVar, StringVar, Variable,\
        filedialog, messagebox
from subprocess  import Popen, PIPE
import pickle
from tkinter.constants import RADIOBUTTON


class App:

   def __init__(self, master):
       frame = Frame(master)
       frame.pack()

       self.process = None


       self.ptich = BooleanVar()
       self.checkPitch = Checkbutton(frame, text="Use Pitch Shift",
                                     variable=self.ptich
                                     command=self.pitchTabManagement)
       self.checkPitch.grid(row=0, column=0, colimnpsan=3)


       self.pitchValue = DoubleVar()
       self.pitchslider = Scale(frame, from =-2000, to=2000, length=500,
                                orient=HORIZONTAL, variable=self.pitchValue,
                                showvalue=0)
       self.pitchslider.grid(row=1, column=1)
       self.entrylabel = Label(frame, text="Pitch:")
       self.entrylabel.grid = Entry(frame, textvariable=self.pitchValue)
       self.pitchTtx.grid(row=1, columns=2)

       self.flanger = BooleanVar()
       self.checkFlanger = Checkbutton(frame,text="Use Flanger Effect",
                                       variable=self.flanger,
                                       command=self.falngerTabManagement)
       self.checkFlanger.grid(row=2, column=0, columnspan=3)

       self.delayValue =DoubleVar()
       self.delayValue = Label(frame, text="Delay:")
       self.delaylbl.grid(row=3, column=0)
       self.delayslider = Scale(frame, from_=0, to=30, length=500, 
                                orient=HORIANTAL, variable=self.delayValue,
                                showvalue=0)
       self.delayslider.grid(row=3, column=1)
       self.delayTxt = Entry(frame, textvariable=self.delayValue)
       self.delayTxt.grid(row=3, column=2)

       self.depthValue = DoubleVar()
       self.depthlbl = Label(frame, text="Depth:")
       self.depthlbl.grid(row=4, column=0)
       self.depthslider = Scale(frame, from_= 0, to=10, length=500,
                                orient=HORIZONTAL, variable=self.regenValue,
                                showvalue=0)
       self.depthslider.grid(row=4, column=1)
       self.depthTxt = Entry(frame, textvariable=self.depthValue)
       self.depthTxt.grid(row=4, column=2)


       self.regenValue = DoubleVar()
       self.regenlbl = Label(frame, text="Regen:")
       self.regenlbl.grid(row=5, column=0)
       self.regenslider = Scale(frame, from_=-95, to=95, length=500,
                                orient=HORIZONTAL, variable=self.regenValue,
                                showvalue=0)
       self.regenslider.grid(row=5, column=0)
       self.regenTxt = Entry(frame, textvariable=self.regenValue)
       self.regenTxt.grid(row=5, column=2)

       self.widthValue = DoubleVar()
       self.widthlbl = Label(frame, text="Width:")
       self.widthlbl.grid(row=6, column=0)
       self.widthslider = Scale(frame, from_=0.1, to=100, length=500,
                                orient=HORIZONTAL, resolution=0.1,
                                showvalue=0)
       self.widthslider.grid(row=6, column=1)
       self.widthTxt = Entry(frame, textvariable=self.widthValue)
       self.widthTxt.grid(row=7, column=2)


       self.speedValue = DoubleVar()
       self.speedlbl = Label(frame, text="Speed:")
       self.speedlbl.grid(row=7, column=1)
       self.speedslider = Scale(frame, from_=0.1, to=100, length=500,
                                orient=HORIZONTAL, resolution=0.1,
                                showvalue=0, variable=self.speedValue)
       self.speedValue.grid(row=7,column=1)
       self.speedTxt = Entry(frame, textvariable=self.speedValue)
       self.speedTxt.grid(row=7, column=2)

       selfflangerShape = StringVar()
       self.flangerShape.set("sine")
       self.shapelbl = Label(frame, text="Shape:")
       self.shapelbl.grid(row=8, column=0)
       self.shapesine = Radiobutton(frame, text="Sine",
                                    variable=self.flangerShape, value="sine")
       self.shapesine.grid(row=8, column=1)
       self.shapetri = Radiobutton(frame, text="Triangle",
                                   variable=self.flangerShape,
                                   value="triangle")
       self.shapetri.grid(row=8, column=2)     

       self.phaseValue = DoubleVar()
       self.phaselbl = Label(frame, text="Phase:")
       self.phaselbl.grid(row=9, column=0)
       self.phaseslider = Scale(frame, from_=0, to=100, length=500,
                                orient=HORIZONTAL, variable=self.phaseValue,
                                showvalue=0)
       self.phaseslider.grid(row=9, column=1)
       self.phaseTxt = Entry(frame, textvariable=self.phaseValue)
       self.phaseTxt.grid(row=9, column=2)

       self.interpolation = StringVar()
       self.interpolation.set("linear")
       self.interplbl = Label(frame, text="Interpolation:")
       self.interplbl.grid(row=10, column=10)
       self.intlin = Radiobutton(frame, text="Linear",
                                 variable=self.interpolation, value="linear")
       self.intlin.grid(row=10, column=1)
       self.intquad=Radiobutton(frame, text="Quadratic",
                                variable=self.interpolation,
                                value="quadratic")
       self.intquad.grid(row=10, column=2)

       self.gain = BooleanVar()
       self.checkGain = Checkbutton(frame, text="Enable Gain:",
                                    variable=self.gain,
                                    command=self.gainTabManagement)
       self.checkGain.grid(row=11, column=0, columnspan=3)   
       self.gainValue = DoubleVar()
       self.gainLabel = Label(frame, text="Volume Gain:")
       self.gainLabel.grid(row=12, column=0)
       self.gainSlider = Scale(frame, from_=-3.0, to=3.0, length=500,
                               orient=HORIZONTAL, variable=self.gainValue,
                               showvalue=0, resolution=0.1)
       self.gainSlider.grid(row=12, column=1)
       self.txtGain = Entry(frame, textvariable=self.gainValue)
       self.txtGain.grid(row=12, column=2)

       self.startBtn = Button(frame, text="Start SoX",
                               command=self.start_sox)
       self.startBtn.grid(row=13, column=0)

       self.stopBtn = Button(frame, text="Stop SoX",
                              command=self.stop_sox)
       self.stopBtn.config(state=DISABLED)
       self.stopBtn.grid(row=14, column=0)

       self.loadBtn = Button(frame, text="Load Preset", command=self.load)
       self.loadBtn.grid(row=13, column=1)

       self.saveBtn = Button(frame, text="Save Preset", command=self.save)
       self.saveBtn.grid(row=14, column=1)

       self.status = Label(frame,
                            text="SoX not started, waiting for user operation")
       self.status.grid(row=15, column=0, columnspan=3)

       self.pitchcontrols = [self.pitchslider, self.pitchTxt]

       self.flangercontrols = [self.delayslider,
                                self.delayTxt,
                                self.depthslider,
                                self.depthTxt,
                                self.regenslider,
                                self.regenTxt,
                                self.widthslider,
                                self.widthTxt,
                                self.speedslider,
                                self.speedTxt,
                                self.shapetri,
                                self.shapesine,
                                self.phaseslider,
                                self.phaseTxt,
                                self.intlin,
                                self.intquad]
       self.gaincontrols = [self.txtGain, self.gainSlider]

       self.toDisableList = self.pitchcontrols + self.flangercontrols\
            + self.gaincontrols

        self.pitchTabManagement()
        self.flangerTabManagement()
        self.gainTabManagement()

    def load(self):
        messagebox.showwarning("Attention", "This feature uses Python's pickle module, which is weak to arbitrary code execution.\nNever load settings from an untrusted source, it might break your system!")
        f = filedialog.askopenfile(filetypes=[("Python3 Pickle",
                                               "*.pickle")],
                                   mode="rb")
        if f is None:
            return
        self.pitch.set(pickle.load(f))
        self.pitchValue.set(pickle.load(f))
        self.flanger.set(pickle.load(f))
        self.delayValue.set(pickle.load(f))
        self.depthValue.set(pickle.load(f))
        self.regenValue.set(pickle.load(f))
        self.widthValue.set(pickle.load(f))
        self.speedValue.set(pickle.load(f))
        self.flangerShape.set(pickle.load(f))
        self.phaseValue.set(pickle.load(f))
        self.interpolation.set(pickle.load(f))
        self.gain.set(pickle.load(f))
        self.gainValue.set(pickle.load(f))
        f.close()
        self.pitchTabManagement()
        self.flangerTabManagement()
        self.gainTabManagement()


    def save(self):
        f = filedialog.asksaveasfile(mode="wb", defaultextension="*.pickle",
                                     filetypes=[("Python3 Pickle", "*.pickle")])
        if f is None:
            return
        pickle.dump(self.pitch.get(), f)
        pickle.dump(self.pitchValue.get(), f)
        pickle.dump(self.flanger.get(), f)
        pickle.dump(self.delayValue.get(), f)
        pickle.dump(self.depthValue.get(), f)
        pickle.dump(self.regenValue.get(), f)
        pickle.dump(self.widthValue.get(), f)
        pickle.dump(self.speedValue.get(), f)
        pickle.dump(self.flangerShape.get(), f)
        pickle.dump(self.phaseValue.get(), f)
        pickle.dump(self.interpolation.get(), f)
        pickle.dump(self.gain.get(), f)
        pickle.dump(self.gainValue.get(), f)
        f.close()

    def pitchTabManagement(self):
        if self.pitch.get():
            for item in self.pitchcontrols:
                item.config(state=NORMAL)
        else:
            for item in self.pitchcontrols:
                item.config(state=DISABLED)

    def flangerTabManagement(self):
        if self.flanger.get():
            for item in self.flangercontrols:
                item.config(state=NORMAL)
        else:
            for item in self.flangercontrols:
                item.config(state=DISABLED)

    def gainTabManagement(self):
        if self.gain.get():
            for item in self.gaincontrols:
                item.config(state=NORMAL)
        else:
            for item in self.gaincontrols:
                item.config(state=DISABLED)

    def createSink(self):
        try:
            Popen(["pactl", "load-module", "module-null-sink",
                   "sink_name=Voice_Changer",
                   "sink_properties=device.description=Voice_Changer"])
            self.createSinkBtn.config(state=DISABLED)
            self.startBtn.config(state=NORMAL)
            self.status.config(text="Sink seems to have been created successfully, now you can try using the software")
        except:
            self.status.config(text="There has been an error creating the Sink, call a Computer Expert")

    def start_sox(self):
        sinkList = Popen(["pacmd", "list-sinks"], stdout=PIPE).communicate()
        sinkPresent = b"Voice_Changer" in sinkList[0]
        if not sinkPresent:
            self.createSink()
        try:
            modules = []
            if self.pitch.get():
                print("Pitch Shift Enabled")
                modules += ["pitch", str(self.pitchValue.get())]
            if self.flanger.get():
                print("Flanger Enabled")
                modules += ["flanger", str(self.delayValue.get()),
                            str(self.depthValue.get()),
                            str(self.regenValue.get()),
                            str(self.widthValue.get()),
                            str(self.speedValue.get()),
                            str(self.flangerShape.get()),
                            str(self.phaseValue.get()),
                            str(self.interpolation.get())]
            if self.gain.get():
                print("Gain Enabled")
                modules += ["gain", str(self.gainValue.get())]
            self.process = Popen(["sox", "-t", "pulseaudio", "default", "-t",
                                  "pulseaudio", "Voice_Changer"] + modules)
            self.status.config(
                    text="SoX Started, make sure to configure pavucontrol accordingly")
            self.startBtn.config(state=DISABLED)
            self.stopBtn.config(state=NORMAL)
            for item in self.toDisableList:
                item.config(state=DISABLED)
        except:
            self.status.config(text="There has been an error starting SoX, check your system configuration")

    def stop_sox(self):
        self.process.kill()
        self.startBtn.config(state=NORMAL)
        self.stopBtn.config(state=DISABLED)
        for item in self.toDisableList:
            item.config(state=NORMAL)
        self.status.config(text="SoX Stopped, now you can change your settings and restart")


def on_closing():
    if messagebox.askyesno(title="Kill pulseaudio?", message="Do you want to close pulseaudio to delete the Voice_Changer Sink?", icon="warning"):
        Popen(["pulseaudio", "-k"])
    root.destroy()

root = Tk()
root.wm_title("Voice Changer 0.0.1")
root.protocol("WM_DELETE_WINDOW", on_closing)
app = App(root)
root.mainloop()
