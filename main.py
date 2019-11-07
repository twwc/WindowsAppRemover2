from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess


def init_removal(command):
    subprocess.Popen(["powershell.exe", command], stdout=subprocess.PIPE)


def init_warning(message):
    messagebox.askyesno("Dangerous Operation", message=message)


def init_verification():
    messagebox.showinfo("Operation Completed", "Operation Successful!")


class WindowsAppRemover:
    def __init__(self):
        self.root = Tk()
        self.tab_menu = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tab_menu)
        self.utilities_checkbox_frame = Frame(self.tab1)
        self.utilities_buttons_frame = Frame(self.tab1)

        self.tab2 = ttk.Frame(self.tab_menu)
        self.comms_checkbox_frame = Frame(self.tab2)
        self.comms_buttons_frame = Frame(self.tab2)

        self.tab3 = ttk.Frame(self.tab_menu)
        self.entertainment_checkbox_frame = Frame(self.tab3)
        self.entertainment_buttons_frame = Frame(self.tab3)

        self.tab4 = ttk.Frame(self.tab_menu)
        self.advanced_checkbox_frame = Frame(self.tab4)
        self.advanced_buttons_frame = Frame(self.tab4)

    def main_window(self):
        self.root.title("Windows 10 Applications Remover")
        self.root.maxsize(width=290, height=210)
        self.root.minsize(width=290, height=210)
        self.root.attributes("-toolwindow", True)

        self.tab_menu.grid(row=0, column=0)
        self.tab_menu.add(self.tab1, text="Utilities")
        self.tab_menu.add(self.tab2, text="Comms")
        self.tab_menu.add(self.tab3, text="Entertainment")
        self.tab_menu.add(self.tab4, text="Advanced")

        self.utilities_checkbox_frame.grid(row=0, column=0, pady=5, padx=5)
        alarms_var1 = IntVar()
        alarms_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Alarms", variable=alarms_var1)
        alarms_checkbox.grid(row=0, column=0, padx=3, sticky=W)
        calculator_var2 = IntVar()
        calculator_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Calculator",
                                          variable=calculator_var2)
        calculator_checkbox.grid(row=1, column=0, padx=3, sticky=W)
        camera_var3 = IntVar()
        camera_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Camera", variable=camera_var3)
        camera_checkbox.grid(row=2, column=0, padx=3, sticky=W)
        finance_var4 = IntVar()
        finance_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Finance", variable=finance_var4)
        finance_checkbox.grid(row=3, column=0, padx=3, sticky=W)
        getstarted_var5 = IntVar()
        getstarted_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Get Started",
                                          variable=getstarted_var5)
        getstarted_checkbox.grid(row=4, column=0, padx=3, sticky=W)
        maps_var6 = IntVar()
        maps_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Maps", variable=maps_var6)
        maps_checkbox.grid(row=0, column=1, padx=30, sticky=W)
        office_var7 = IntVar()
        office_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Office Hub", variable=office_var7)
        office_checkbox.grid(row=1, column=1, padx=30, sticky=W)
        onenote_var8 = IntVar()
        onenote_checkbox = Checkbutton(self.utilities_checkbox_frame, text="OneNote", variable=onenote_var8)
        onenote_checkbox.grid(row=2, column=1, padx=30, sticky=W)
        photos_var9 = IntVar()
        photos_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Photos", variable=photos_var9)
        photos_checkbox.grid(row=3, column=1, padx=30, sticky=W)
        voicerecorder_var10 = IntVar()
        voice_recorder_checkbox = Checkbutton(self.utilities_checkbox_frame, text="Voice Recorder",
                                              variable=voicerecorder_var10)
        voice_recorder_checkbox.grid(row=4, column=1, padx=30, sticky=W)
        self.utilities_buttons_frame.grid(row=1, column=0, columnspan=2, pady=5, padx=41)

        def utilities_removal():
            if alarms_var1.get() == 1:
                init_removal("get-appxpackage *alarms* | remove-appxpackage")
                alarms_var1.set(0)
            if calculator_var2.get() == 1:
                init_removal("get-appxpackage *calculator* | remove-appxpackage")
                calculator_var2.set(0)
            if camera_var3.get() == 1:
                init_removal("get-appxpackage *camera* | remove-appxpackage")
                camera_var3.set(0)
            if finance_var4.get() == 1:
                init_removal("get-appxpackage *bingfinance* | remove-appxpackage")
                finance_var4.set(0)
            if getstarted_var5.get() == 1:
                init_removal("get-appxpackage *getstarted* | remove-appxpackage")
                getstarted_var5.set(0)
            if maps_var6.get() == 1:
                init_removal("get-appxpackage *maps* | remove-appxpackage")
                maps_var6.set(0)
            if office_var7.get() == 1:
                init_removal("get-appxpackage *officehub* | remove-appxpackage")
                office_var7.set(0)
            if onenote_var8.get() == 1:
                init_removal("get-appxpackage *onenote* | remove-appxpackage")
                onenote_var8.set(0)
            if photos_var9.get() == 1:
                init_removal("get-appxpackage *photos* | remove-appxpackage")
                photos_var9.set(0)
            if voicerecorder_var10.get() == 1:
                init_removal("get-appxpackage *soundrecorder* | remove-appxpackage")
                voicerecorder_var10.set(0)
            init_verification()

        def init_utilities_cancel():
            if alarms_var1.get() == 1:
                alarms_var1.set(0)
            if calculator_var2.get() == 1:
                calculator_var2.set(0)
            if camera_var3.get() == 1:
                camera_var3.set(0)
            if finance_var4.get() == 1:
                finance_var4.set(0)
            if getstarted_var5.get() == 1:
                getstarted_var5.set(0)
            if maps_var6.get() == 1:
                maps_var6.set(0)
            if office_var7.get() == 1:
                office_var7.set(0)
            if onenote_var8.get() == 1:
                onenote_var8.set(0)
            if photos_var9.get() == 1:
                photos_var9.set(0)
            if voicerecorder_var10.get() == 1:
                voicerecorder_var10.set(0)

        utilities_remove_button = Button(self.utilities_buttons_frame, text="REMOVE", width=12)
        utilities_remove_button.configure(command=utilities_removal)
        utilities_remove_button.grid(row=0, column=0, pady=5, padx=5)
        utilities_cancel_button = Button(self.utilities_buttons_frame, text="CANCEL", width=12)
        utilities_cancel_button.configure(command=init_utilities_cancel)
        utilities_cancel_button.grid(row=0, column=1, pady=5, padx=5)

        self.comms_checkbox_frame.grid(row=0, column=0, pady=5, padx=5, sticky=W)
        calendar_mail_var11 = IntVar()
        calendar_mail_checkbox = Checkbutton(self.comms_checkbox_frame, text="Calendar and Mail",
                                             variable=calendar_mail_var11)
        calendar_mail_checkbox.grid(row=0, column=0, padx=3, sticky=W)
        getskype_var12 = IntVar()
        get_skype_checkbox = Checkbutton(self.comms_checkbox_frame, text="Get Skype", variable=getskype_var12)
        get_skype_checkbox.grid(row=1, column=0, padx=3, sticky=W)
        phone_var13 = IntVar()
        phone_checkbox = Checkbutton(self.comms_checkbox_frame, text="Phone", variable=phone_var13)
        phone_checkbox.grid(row=2, column=0, padx=3, sticky=W)
        skype_var14 = IntVar()
        skype_checkbox = Checkbutton(self.comms_checkbox_frame, text="Skype", variable=skype_var14)
        skype_checkbox.grid(row=3, column=0, padx=3, sticky=W)
        self.comms_buttons_frame.grid(row=1, column=0, columnspan=1, pady=30, padx=41, sticky=E)

        def comms_removal():
            if calendar_mail_var11.get() == 1:
                init_removal("get-appxpackage *communicationsapps* | remove-appxpackage")
                calendar_mail_var11.set(0)
            if getskype_var12.get() == 1:
                init_removal("get-appxpackage *skypeapp* | remove-appxpackage")
                getskype_var12.set(0)
            if phone_var13.get() == 1:
                init_removal("get-appxpackage *phone* | remove-appxpackage")
                phone_var13.set(0)
            if skype_var14.get() == 1:
                init_removal("get-appxpackage *messaging* | remove-appxpackage")
                skype_var14.set(0)
            init_verification()

        def init_comms_cancel():
            if calendar_mail_var11.get() == 1:
                calendar_mail_var11.set(0)
            if getskype_var12.get() == 1:
                getskype_var12.set(0)
            if phone_var13.get() == 1:
                phone_var13.set(0)
            if skype_var14.get() == 1:
                skype_var14.set(0)

        comms_remove_button = Button(self.comms_buttons_frame, text="REMOVE", width=12)
        comms_remove_button.configure(command=comms_removal)
        comms_remove_button.grid(row=0, column=0, pady=5, padx=5)
        comms_cancel_button = Button(self.comms_buttons_frame, text="CANCEL", width=12)
        comms_cancel_button.configure(command=init_comms_cancel)
        comms_cancel_button.grid(row=0, column=1, pady=5, padx=5)

        self.entertainment_checkbox_frame.grid(row=0, column=0, pady=5, padx=5)
        movies_tv_var15 = IntVar()
        movies_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="Movies and TV", variable=movies_tv_var15)
        movies_checkbox.grid(row=0, column=0, padx=3, sticky=W)
        music_var16 = IntVar()
        music_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="Music", variable=music_var16)
        music_checkbox.grid(row=1, column=0, padx=3, sticky=W)
        news_var17 = IntVar()
        news_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="News", variable=news_var17)
        news_checkbox.grid(row=2, column=0, padx=3, sticky=W)
        solitaire_var18 = IntVar()
        solitaire_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="Solitaire", variable=solitaire_var18)
        solitaire_checkbox.grid(row=3, column=0, padx=3, sticky=W)
        sports_var19 = IntVar()
        sports_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="Sports", variable=sports_var19)
        sports_checkbox.grid(row=0, column=1, padx=30, sticky=W)
        sway_var20 = IntVar()
        sway_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="Sway", variable=sway_var20)
        sway_checkbox.grid(row=1, column=1, padx=30, sticky=W)
        xbox_var21 = IntVar()
        xbox_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="Xbox", variable=xbox_var21)
        xbox_checkbox.grid(row=2, column=1, padx=30, sticky=W)
        dddbuilder_var22 = IntVar()
        dddbuilder_checkbox = Checkbutton(self.entertainment_checkbox_frame, text="3D Builder",
                                          variable=dddbuilder_var22)
        dddbuilder_checkbox.grid(row=3, column=1, padx=30, sticky=W)
        self.entertainment_buttons_frame.grid(row=1, column=0, pady=30, padx=41)

        def entertainment_removal():
            if movies_tv_var15.get() == 1:
                init_removal("get-appxpackage *zunevideo* | remove-appxpackage")
                movies_tv_var15.set(0)
            if music_var16.get() == 1:
                init_removal("get-appxpackage *zunemusic* | remove-appxpackage")
                music_var16.set(0)
            if news_var17.get() == 1:
                init_removal("get-appxpackage *bingnews* | remove-appxpackage")
                news_var17.set(0)
            if solitaire_var18.get() == 1:
                init_removal("get-appxpackage *solitairecollection* | remove-appxpackage")
                solitaire_var18.set(0)
            if sports_var19.get() == 1:
                init_removal("get-appxpackage *bingsports* | remove-appxpackage")
                sports_var19.set(0)
            if sway_var20.get() == 1:
                init_removal("get-appxpackage *sway* | remove-appxpackage")
                sway_var20.set(0)
            if xbox_var21.get() == 1:
                init_removal("get-appxpackage *xboxapp* | remove-appxpackage")
                xbox_var21.set(0)
            if dddbuilder_var22.get() == 1:
                init_removal("get-appxpackage *3dbuilder* | remove-appxpackage")
                dddbuilder_var22.set(0)
            init_verification()

        def init_entertainment_cancel():
            if movies_tv_var15.get() == 1:
                movies_tv_var15.set(0)
            if music_var16.get() == 1:
                music_var16.set(0)
            if news_var17.get() == 1:
                news_var17.set(0)
            if solitaire_var18.get() == 1:
                solitaire_var18.set(0)
            if sports_var19.get() == 1:
                sports_var19.set(0)
            if sway_var20.get() == 1:
                sway_var20.set(0)
            if xbox_var21.get() == 1:
                xbox_var21.set(0)
            if dddbuilder_var22.get() == 1:
                dddbuilder_var22.set(0)

        entertainment_remove_button = Button(self.entertainment_buttons_frame, text="REMOVE", width=12)
        entertainment_remove_button.configure(command=entertainment_removal)
        entertainment_remove_button.grid(row=0, column=0, pady=5, padx=5)
        entertainment_cancel_button = Button(self.entertainment_buttons_frame, text="CANCEL", width=12)
        entertainment_cancel_button.configure(command=init_entertainment_cancel)
        entertainment_cancel_button.grid(row=0, column=1, pady=5, padx=5)

        self.advanced_checkbox_frame.grid(row=0, column=0, pady=5, padx=5)
        microsoft_store_var23 = IntVar()
        microsoft_store_checkbox = Checkbutton(self.advanced_checkbox_frame, text="Microsoft Store",
                                               variable=microsoft_store_var23)
        microsoft_store_checkbox.grid(row=0, column=0, padx=3, sticky=W)
        default_apps_var24 = IntVar()
        default_apps_checkbox = Checkbutton(self.advanced_checkbox_frame,
                                            text="All default apps from all user accounts", variable=default_apps_var24)
        default_apps_checkbox.grid(row=1, column=0, padx=3, sticky=W)
        modern_apps_var25 = IntVar()
        modern_apps_checkbox = Checkbutton(self.advanced_checkbox_frame,
                                           text="All modern apps from system account", variable=modern_apps_var25)
        modern_apps_checkbox.grid(row=2, column=0, padx=3, sticky=W)
        disable_defender_var26 = IntVar()
        disable_defender_checkbox = Checkbutton(self.advanced_checkbox_frame, text="Disable Microsoft Windows Defender",
                                                variable=disable_defender_var26)
        disable_defender_checkbox.grid(row=3, column=0, padx=3, sticky=W)
        enable_defender_var27 = IntVar()
        enable_defender_checkbox = Checkbutton(self.advanced_checkbox_frame, text="Enable Microsoft Windows Defender",
                                               variable=enable_defender_var27)
        enable_defender_checkbox.grid(row=4, column=0, padx=3, sticky=W)
        self.advanced_buttons_frame.grid(row=1, column=0, pady=5, padx=41)

        def advanced_removal():
            if microsoft_store_var23.get() == 1:
                if init_warning("Remove the Microsoft Store?") == TRUE:
                    init_removal("get-appxpackage *windowsstore* | remove-appxpackage")
                    microsoft_store_var23.set(0)
                else:
                    microsoft_store_var23.set(0)
            if default_apps_var24.get() == 1:
                if init_warning("Remove all default apps for all user accounts?") == TRUE:
                    init_removal("Get-AppxPackage -AllUsers | Remove-AppxPackage")
                    default_apps_var24.set(0)
                else:
                    default_apps_var24.set(0)
            if modern_apps_var25.get() == 1:
                if init_warning("Remove all modern apps from system account?") == TRUE:
                    init_removal("Get-AppxProvisionedPackage -online | Remove-AppxProvisionedPackage -online")
                    modern_apps_var25.set(0)
                else:
                    modern_apps_var25.set(0)
            if disable_defender_var26.get() == 1:
                if init_warning("Disable Microsoft Windows Defender?") == TRUE:
                    init_removal("Set-MpPreference -DisableRealtimeMonitoring $true")
                    disable_defender_var26.set(0)
                else:
                    disable_defender_var26.set(0)
            if enable_defender_var27.get() == 1:
                if init_warning("Enable Microsoft Windows Defender?") == TRUE:
                    init_removal("Set-MpPreference -DisableRealtimeMonitoring $false")
                    enable_defender_var27.set(0)
                else:
                    enable_defender_var27.set(0)
            init_verification()

        def init_advanced_cancel():
            if microsoft_store_var23.get() == 1:
                microsoft_store_var23.set(0)
            if default_apps_var24.get() == 1:
                default_apps_var24.set(0)
            if modern_apps_var25.get() == 1:
                modern_apps_var25.set(0)
            if disable_defender_var26.get() == 1:
                disable_defender_var26.set(0)
            if enable_defender_var27.get() == 1:
                enable_defender_var27.set(0)

        advanced_remove_button = Button(self.advanced_buttons_frame, text="REMOVE", width=12)
        advanced_remove_button.configure(command=advanced_removal)
        advanced_remove_button.grid(row=0, column=0, pady=5, padx=5)
        advanced_cancel_button = Button(self.advanced_buttons_frame, text="CANCEL", width=12)
        advanced_cancel_button.configure(command=init_advanced_cancel)
        advanced_cancel_button.grid(row=0, column=1, pady=5, padx=5)

        self.root.mainloop()


if __name__ == "__main__":
    WindowsAppRemover.main_window(WindowsAppRemover())
