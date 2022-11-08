import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import *
import os
import os.path
import psutil
import shutil
from pathlib import Path
import XML_TEST as XT
from XML_TEST import failed
from XML_TEST import mod_file_cont
import tkinter.font as font


root = Tk()
root.configure(bg='light yellow')
root.title('VMT BestFit Visu Offset updater_HU v1.00')
label = Label(root, text='Válaszd ki az offsetfájlt:',
              font=('Arial', 13, 'bold'), bg='light yellow')
label.grid(row=0, columnspan=4)
no_backup = Label(root, bg='light yellow', fg='red', font=('Arial', 12, 'italic'),
                        text='FIGYELEM! Még nem készült biztonsági mentés!')
no_backup.grid(row=10, columnspan=4)
exact_time = datetime.now()
final_logfilevar = '[LOG]' + exact_time.strftime('%Y-%d-%m_%H_%M_%S') + '.txt'
login = False
path_list_W177 = ["D:\BestFit\AuditTypes_Left\\010_W177_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\010_W177_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FA_RE.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\010_W177_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\010_W177_KH_RE.xml",
                  "D:\BestFit\AuditTypes_RT\\010_W177_ND_RT.xml",
                  "D:\BestFit\AuditTypes_STS_Left\\011_W177_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_Right\\011_W177_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_MH\\010_W177_MH.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\020_W177_AMG_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\020_W177_AMG_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\020_W177_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_Left\\021_W177_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_Right\\021_W177_AMG_STS_vo_re.xml",
                  ]

path_list_W177_SME = ["D:\BestFit\AuditTypes\Type_W177\\11_W177_KV_LBR_Links.xml",
                      "D:\BestFit\AuditTypes\Type_W177\\11_W177_KV_LBR_Rechts.xml"
                      ]

path_list_W177_SME_AMG = ["D:\BestFit\AuditTypes\Type_W177_AMG\\12_W177_KV_LBR_Links_AMG.xml",
                          "D:\BestFit\AuditTypes\Type_W177_AMG\\12_W177_KV_LBR_Rechts_AMG.xml"
                          ]

path_list_C118 = ["D:\BestFit\AuditTypes_Left\\100_C118_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\100_C118_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\100_C118_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\100_C118_FA_RE.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\100_C118_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\100_C118_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\100_C118_MH.xml",
                  "D:\BestFit\AuditTypes_STS_Left\\101_C118_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_Right\\101_C118_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_MH\\120_C118_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_Left\\121_C118_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_Right\\121_C118_AMG_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\120_C118_AMG_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\120_C118_AMG_KH_RE.xml",
                  ]

path_list_C118_SME = ["D:\BestFit\AuditTypes\Type_C118\\21_C118_KV_LBR_Links.xml",
                      "D:\BestFit\AuditTypes\Type_C118\\21_C118_KV_LBR_Rechts.xml"
                      ]

path_list_C118_SME_AMG = ["D:\BestFit\AuditTypes\Type_C118_AMG\\22_C118_KV_LBR_Links_AMG.xml",
                          "D:\BestFit\AuditTypes\Type_C118_AMG\\22_C118_KV_LBR_Rechts_AMG.xml"
                          ]

path_list_X118 = ["D:\BestFit\AuditTypes_Left\\140_X118_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\140_X118_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\140_X118_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\140_X118_FA_RE.xml",
                  "D:\BestFit\AuditTypes\\140_X118_ND_RT.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\140_X118_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\140_X118_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\140_X118_MH.xml",
                  "D:\BestFit\AuditTypes_STS_Left\\141_X118_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_Right\\141_X118_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_MH\\160_X118_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_Left\\161_X118_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_Right\\161_X118_AMG_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\160_X118_AMG_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\160_X118_AMG_KH_RE.xml"
                  ]

path_list_X118_SME = ["D:\BestFit\AuditTypes\Type_X118\\31_X118_KV_LBR_Links.xml",
                      "D:\BestFit\AuditTypes\Type_X118\\31_X118_KV_LBR_Rechts.xml"
                      ]

path_list_X118_SME_AMG = ["D:\BestFit\AuditTypes\Type_X118_AMG\\32_X118_KV_LBR_Links_AMG.xml",
                          "D:\BestFit\AuditTypes\Type_X118_AMG\\32_X118_KV_LBR_Rechts_AMG.xml"
                          ]

path_list_X243 = ['D:\BestFit\AuditTypes\Type_X243\\10_X243.xml']

existing_path_W177 = []
existing_path_W177_SME = []
existing_path_W177_SME_AMG = []
existing_path_C118 = []
existing_path_C118_SME = []
existing_path_C118_SME_AMG = []
existing_path_X118 = []
existing_path_X118_SME = []
existing_path_X118_SME_AMG = []
existing_path_X243 = []
backup_pathlist = []
pointnames_got = []
values_got = []
xml_origdata = {}
csv_origdata = {}


def restore_xml_backup():
    ask_question = messagebox.askquestion('Figyelmeztetés', 'Valóban visszatöltöd a biztonsági másolatot?')
    if ask_question == 'yes':
        orig_files = os.listdir("D:\\BackupBestFit\\AbgleichBackup")
        mod_files_path = Path.cwd() / "D:\\BestFit"
        mod_files = list(mod_files_path.rglob("*xml*"))
        if len(orig_files) >= 1:
            for mod_file in mod_files:
                for orig_file in orig_files:
                    if str(orig_file) in str(mod_file):
                        shutil.copy2("D:\\BackupBestFit\\AbgleichBackup\\" + orig_file, mod_file)

            for file in path_list_W177:
                if os.path.exists(file):
                    open_button_W177["state"] = "normal"
                    open_button_W177['font'] = ('Arial', 19, 'bold')
                    open_button_W177["text"] = "BestFit W177"
                    open_button_W177["bd"] = 10

            for file in path_list_W177_SME:
                if os.path.exists(file):
                    open_button_W177_SME["state"] = "normal"
                    open_button_W177_SME['font'] = ('Arial', 19, 'bold')
                    open_button_W177_SME["text"] = "SME W177"
                    open_button_W177_SME["bd"] = 10

            for file in path_list_W177_SME_AMG:
                if os.path.exists(file):
                    open_button_W177_SME_AMG["state"] = "normal"
                    open_button_W177_SME_AMG['font'] = ('Arial', 19, 'bold')
                    open_button_W177_SME_AMG["text"] = "SME W177 AMG"
                    open_button_W177_SME_AMG["bd"] = 10

            for file in path_list_C118:
                if os.path.exists(file):
                    open_button_C118["state"] = "normal"
                    open_button_C118["text"] = "BestFit C118"
                    open_button_C118['font'] = ('Arial', 19, 'bold')
                    open_button_C118["bd"] = 10

            for file in path_list_C118_SME:
                if os.path.exists(file):
                    open_button_C118_SME["state"] = "normal"
                    open_button_C118_SME['font'] = ('Arial', 19, 'bold')
                    open_button_C118_SME["text"] = "SME C118"
                    open_button_C118_SME["bd"] = 10

            for file in path_list_C118_SME_AMG:
                if os.path.exists(file):
                    open_button_C118_SME_AMG["state"] = "normal"
                    open_button_C118_SME_AMG['font'] = ('Arial', 19, 'bold')
                    open_button_C118_SME_AMG["text"] = "SME C118 AMG"
                    open_button_C118_SME_AMG["bd"] = 10

            for file in path_list_X118:
                if os.path.exists(file):
                    open_button_X118["state"] = "normal"
                    open_button_X118["text"] = "BestFit X118"
                    open_button_X118['font'] = ('Arial', 19, 'bold')
                    open_button_X118["bd"] = 10
                    continue
            for file in path_list_X118_SME:
                if os.path.exists(file):
                    open_button_X118_SME["state"] = "normal"
                    open_button_X118_SME['font'] = ('Arial', 19, 'bold')
                    open_button_X118_SME["text"] = "SME X118"
                    open_button_X118_SME["bd"] = 10

            for file in path_list_X118_SME_AMG:
                if os.path.exists(file):
                    open_button_X118_SME_AMG["state"] = "normal"
                    open_button_X118_SME_AMG['font'] = ('Arial', 19, 'bold')
                    open_button_X118_SME_AMG["text"] = "SME X118 AMG"
                    open_button_X118_SME_AMG["bd"] = 10

            for file in path_list_X243:
                if os.path.exists(file):
                    open_button_X243["state"] = "normal"
                    open_button_X243["text"] = "SMA X243"
                    open_button_X243['font'] = ('Arial', 19, 'bold')
                    open_button_X243["bd"] = 10

            with open('text_box.txt', 'r+') as txt:
                txt.truncate(0)
            restore_backup_button['state'] = 'disabled'
            messagebox.showinfo("Sikeres helyreállítás",
                                "Biztonsági mentés sikeresen visszatöltve. MINDEN offset az eredeti értékre állítva!")
            failed.clear()
            mod_file_cont.clear()

        else:
            messagebox.showerror(title='Figyelmeztetés', message='Nem található fájl')


def start_program_W177():

    while True:

        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válaszd ki a BF_W177.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('BF_W177', 0, 7):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------W177 BestFit Offset behívva------------------\n')
                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_W177:
                    setmeasurement_pointc118(file_path)
                open_button_W177["text"] = "BestFit W177"
                open_button_W177['font'] = ('Arial', 20, 'italic')
                open_button_W177["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'BestFit W177'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break

            elif filepath == "":
                break

            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')

        finally:
            break


def start_program_W177_SME():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a SME_W177_SERIE.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('SME_W177_SERIE', 0, 14):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------W177_SME Offset behívva------------------\n')
                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_W177_SME:
                    setmeasurement_pointc118(file_path)
                open_button_W177_SME["text"] = "SME W177"
                open_button_W177_SME['font'] = ('Arial', 20, 'italic')
                open_button_W177_SME["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'SME W177'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_W177_SME_AMG():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki az SME_W177_AMG.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('SME_W177_AMG', 0, 12):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------W177_SME_AMG Offset behívva------------------\n')
                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_W177_SME_AMG:
                    setmeasurement_pointc118(file_path)
                open_button_W177_SME_AMG["text"] = "SME W177 AMG"
                open_button_W177_SME_AMG['font'] = ('Arial', 20, 'italic')
                open_button_W177_SME_AMG["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'SME W177 AMG'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_C118():

    while True:
        try:

            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válaszd ki a BF_C118.csv fájlt',
                                                  filetypes=[("csv files", "*.csv"), ("all files", "*.*")])

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('BF_C118', 0, 7):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------C118 BestFit Offset behívva------------------\n')
                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_C118:
                    setmeasurement_pointc118(file_path)
                open_button_C118["text"] = "BestFit C118"
                open_button_C118['font'] = ('Arial', 20, 'italic')
                open_button_C118["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'BestFit C118'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_C118_SME():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki az SME_C118_SERIE.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('SME_C118_SERIE', 0, 14):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------C118_SME Offset behívva------------------\n')

                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_C118_SME:
                    setmeasurement_pointc118(file_path)
                open_button_C118_SME["text"] = "SME C118"
                open_button_C118_SME['font'] = ('Arial', 20, 'italic')
                open_button_C118_SME["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'SME C118'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_C118_SME_AMG():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki az SME_C118_AMG.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('SME_C118_AMG', 0, 12):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------C118_SME_AMG Offset behívva------------------\n')

                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_C118_SME_AMG:
                    setmeasurement_pointc118(file_path)
                open_button_C118_SME_AMG["text"] = "SME C118 AMG"
                open_button_C118_SME_AMG['font'] = ('Arial', 20, 'italic')
                open_button_C118_SME_AMG["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'SME C118 AMG'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_X118():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a BF_X118.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('BF_X118', 0, 7):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------X118 BestFit Offset behívva------------------\n')

                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_X118:
                    setmeasurement_pointc118(file_path)
                open_button_X118["text"] = "BestFit X118 "
                open_button_X118['font'] = ('Arial', 20, 'italic')
                open_button_X118["state"] = "disabled"
                restore_backup_button['state'] = 'normal'

                name = 'BestFit X118'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_X118_SME():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki az SME_X118_SERIE.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('SME_X118_SERIE', 0, 14):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------X118_SME Offset behívva------------------\n')

                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_X118_SME:
                    setmeasurement_pointc118(file_path)
                open_button_X118_SME["text"] = "SME X118"
                open_button_X118_SME['font'] = ('Arial', 20, 'italic')
                open_button_X118_SME["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'SME X118'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_X118_SME_AMG():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki az  SME_X118_AMG.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('SME_X118_AMG', 0, 12):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t---------------X118_SME_AMG Offset behívva------------------\n')

                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_X118_SME_AMG:
                    setmeasurement_pointc118(file_path)
                open_button_X118_SME_AMG["text"] = "SME X118 AMG"
                open_button_X118_SME_AMG['font'] = ('Arial', 20, 'italic')
                open_button_X118_SME_AMG["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'SME X118 AMG'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def start_program_X243():

    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válaszd ki az SMA_X243.csv fájlt',
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

            file_name = os.path.split(filepath)[1]
            if file_name.startswith('SMA_X243', 0, 8):
                with open("text_box.txt", 'a') as tb:
                    tb.write(f' \t\t\t\t---------------X243 Offset behívva------------------\n')
                txt_path = filepath[:len(filepath) - 4]
                final_path_to_txt = txt_path + ".txt"
                csv_copy = shutil.copyfile(filepath, final_path_to_txt)

                with open(csv_copy, 'r') as output_file:
                    for n in output_file:
                        csv_rawdata.append(n)

                for n in csv_rawdata:
                    replaced = n.replace(';', '.', 1)
                    replaced_char_list.append(replaced)

                for n in replaced_char_list:
                    replaced_2 = n.replace(';', '=')
                    replaced_char_list_2.append(replaced_2)

                for n in replaced_char_list_2:
                    replaced_3 = n.replace(',', '.')
                    final_point_value_list.append(replaced_3[:-1])

                for item in final_point_value_list:
                    getindex = item.index("=")
                    name_puff = item[:getindex]
                    value_puff = item[getindex + 1:]
                    csv_origdata[name_puff] = value_puff

                for file_path in existing_path_X243:
                    setmeasurement_pointc118(file_path)
                open_button_X243["text"] = "SMA X243"
                open_button_X243['font'] = ('Arial', 20, 'italic')
                open_button_X243["state"] = "disabled"
                restore_backup_button['state'] = 'normal'
                name = 'SMA_X243'
                messagebox.showinfo(f' Offset beadás kész', f'{name} Offsetek beadva')
                break
            elif filepath == "":
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
        finally:

            break


def ask_include():
    ask_includexml = messagebox.askquestion("Figyelmeztetés", "Érvényesítetted (include) az XML fájlt ?")
    if ask_includexml == "yes":
        return "yes"
    else:
        return "no"


def kill_visu_start_bf():
    visu = "BestFitVisu.exe"
    for proc in psutil.process_iter():
        if proc.name() == visu:
            messagebox.showinfo('Figyelem!', 'A Visu automatikusan újraindul')
            proc.kill()

    os.startfile("D://BestFit//BestFit_Start_Software.bat")


def exit_program():
    if ask_include() == "yes":
        kill_visu_start_bf()
        root.destroy()
        exit()
    else:
        messagebox.showinfo("Figyelmeztetés", "Kérlek érvényesítsd az XML fájt.")


def open_file():
    filepath = filedialog.askopenfilename(title='Válaszd ki a  .txt fájlt', filetypes=(("txt files", "*.txt"),
                                                                                       ("all files", "*.*")))
    if filepath:
        return str(filepath)


def value_popup(pname, pvalue):
    return messagebox.showinfo('Érték magas', f'FIGYELEM! Több mint 1.00mm offset: {pname}:{pvalue},'
                                              f' kérlek ellenörizd, hogy helyes-e')


def setmeasurement_pointc118(document):
    tree = ET.parse(document)
    root = tree.getroot()
    for element in root.findall('.//Container'):
        if 'ValueConfig' in element.get('name') or 'ValueEvalConf' in element.get('name'):

            for subelement in element:

                get_tagName = subelement.get('name')
                get_pointname = subelement.get('value')

                if get_tagName == 'MeasurementPosition':
                    pointnames_got.append(get_pointname)

                if get_tagName == 'Offset':
                    values_got.append(get_pointname)

    for element in pointnames_got:
        if len(pointnames_got) > 0:
            xml_origdata[element] = values_got[0]
            values_got.pop(0)

    calculated_keyvalues = {key: float(csv_origdata.get(key, 0)) + float(xml_origdata.get(key, 0))
                            for key in xml_origdata
                            }

    final_list = [round(item, 2) for item in calculated_keyvalues.values()]
    final_strlist = [str(e) for e in final_list]
    final_keylist = [e for e in calculated_keyvalues.keys()]
    curr_date = date.today()
    currtext = 'Offset_update_log_' + str(curr_date) + '.txt'
    with open(currtext, 'a+') as logfile:
        logfile.write(f'Fájl : {document} módosítva')

    for element in root.iter('Double'):
        get_tagName = element.get('name')
        get_pointValue = element.get('value')

        if get_tagName == 'Offset' and len(final_strlist) > 0:
            element.set('value', str(final_strlist[0]))

            val_1 = get_pointValue
            val_2 = element.get("value")
            result = float(val_2) - float(val_1)
            rounded = abs(round(result, 2))
            if rounded > 0:
                with open(currtext, 'a+') as logfile:
                    logfile.write(
                        f'\n\tOffset {final_keylist[0]} felülírva {get_pointValue}-ról {element.get("value")}-ra')

            with open(final_logfilevar, 'a+') as logfile_2:
                logfile_2.write(f'\nOffset {final_keylist[0]} felülírva {get_pointValue}-ról {element.get("value")}-ra'
                                f' itt:  {document} \n')

            final_strlist.pop(0)
            final_keylist.pop(0)

    with open(currtext, 'r+') as log:
        read = log.read()
        messagebox.showinfo('Offset beadva', read)
        log.truncate(0)

    pointnames_got.clear()
    values_got.clear()
    xml_origdata.clear()
    tree.write(document)
    os.remove(currtext)


def on_enter_W177(e):
    if open_button_W177['state'] == 'normal':
        open_button_W177['background'] = '#8CC9DE'


def on_leave_W177(e):
    open_button_W177['background'] = 'SystemButtonFace'


def on_enter_W177_SME(e):
    if open_button_W177_SME['state'] == 'normal':
        open_button_W177_SME['background'] = '#8CC9DE'


def on_leave_W177_SME(e):
    open_button_W177_SME['background'] = 'SystemButtonFace'


def on_enter_W177_SME_AMG(e):
    if open_button_W177_SME_AMG['state'] == 'normal':
        open_button_W177_SME_AMG['background'] = '#8CC9DE'


def on_leave_W177_SME_AMG(e):
    open_button_W177_SME_AMG['background'] = 'SystemButtonFace'


def on_enter_C118(e):
    if open_button_C118['state'] == 'normal':
        open_button_C118['background'] = '#8CC9DE'


def on_leave_C118(e):
    open_button_C118['background'] = 'SystemButtonFace'


def on_enter_C118_SME(e):
    if open_button_C118_SME['state'] == 'normal':
        open_button_C118_SME['background'] = '#8CC9DE'


def on_leave_C118_SME(e):
    open_button_C118_SME['background'] = 'SystemButtonFace'


def on_enter_C118_SME_AMG(e):
    if open_button_C118_SME_AMG['state'] == 'normal':
        open_button_C118_SME_AMG['background'] = '#8CC9DE'


def on_leave_C118_SME_AMG(e):
    open_button_C118_SME_AMG['background'] = 'SystemButtonFace'


def on_enter_X118(e):
    if open_button_X118['state'] == 'normal':
        open_button_X118['background'] = '#8CC9DE'


def on_leave_X118(e):
    open_button_X118['background'] = 'SystemButtonFace'


def on_enter_X118_SME(e):
    if open_button_X118_SME['state'] == 'normal':
        open_button_X118_SME['background'] = '#8CC9DE'


def on_leave_X118_SME(e):
    open_button_X118_SME['background'] = 'SystemButtonFace'


def on_enter_X118_SME_AMG(e):
    if open_button_X118_SME_AMG['state'] == 'normal':
        open_button_X118_SME_AMG['background'] = '#8CC9DE'


def on_leave_X118_SME_AMG(e):
    open_button_X118_SME_AMG['background'] = 'SystemButtonFace'


def on_enter_X243(e):
    if open_button_X243['state'] == 'normal':
        open_button_X243['background'] = '#8CC9DE'


def on_leave_X243(e):
    open_button_X243['background'] = 'SystemButtonFace'


def on_enter_exit(e):
    exit_button['background'] = '#F06868'


def on_leave_exit(e):
    exit_button['background'] = 'SystemButtonFace'


def on_enter_backup(e):
    if restore_backup_button['state'] == 'normal':
        restore_backup_button['background'] = '#8CC9DE'


def on_leave_backup(e):
    restore_backup_button['background'] = 'SystemButtonFace'


def on_enter_create_backup(e):
    if create_backup_button['state'] == 'normal':
        create_backup_button['background'] = '#8CC9DE'


def on_leave_create_backup(e):
    create_backup_button['background'] = 'SystemButtonFace'


def on_enter_func_test_button(e):
    if function_test_button['state'] == 'normal':
        function_test_button['background'] = '#8CC9DE'


def on_leave_func_test_button(e):
    function_test_button['background'] = 'SystemButtonFace'


def on_enter_login_butt(e):
    if login_button['state'] == 'normal':
        login_button['background'] = 'light green'


def on_leave_login_butt(e):
    login_button['background'] = 'SystemButtonFace'


def check_fileexists_W177():
    for file in path_list_W177:
        if os.path.exists(file):
            existing_path_W177.append(file)
            backup_pathlist.append(file)
            open_button_W177['state'] = ['normal']


def check_fileexists_W177_SME():
    for file in path_list_W177_SME:
        if os.path.exists(file):
            existing_path_W177_SME.append(file)
            backup_pathlist.append(file)
            open_button_W177_SME['state'] = ['normal']


def check_fileexists_W177_SME_AMG():
    for file in path_list_W177_SME_AMG:
        if os.path.exists(file):
            existing_path_W177_SME_AMG.append(file)
            backup_pathlist.append(file)
            open_button_W177_SME_AMG['state'] = ['normal']


def check_fileexists_C118():
    for file in path_list_C118:
        if os.path.exists(file):
            existing_path_C118.append(file)
            backup_pathlist.append(file)
            open_button_C118['state'] = ['normal']


def check_fileexists_C118_SME():
    for file in path_list_C118_SME:
        if os.path.exists(file):
            existing_path_C118_SME.append(file)
            backup_pathlist.append(file)
            open_button_C118_SME['state'] = ['normal']


def check_fileexists_C118_SME_AMG():
    for file in path_list_C118_SME_AMG:
        if os.path.exists(file):
            existing_path_C118_SME_AMG.append(file)
            backup_pathlist.append(file)
            open_button_C118_SME_AMG['state'] = ['normal']


def check_fileexists_X118():
    for file in path_list_X118:
        if os.path.exists(file):
            existing_path_X118.append(file)
            backup_pathlist.append(file)
            open_button_X118['state'] = ['normal']


def check_fileexists_X118_SME():
    for file in path_list_X118_SME:
        if os.path.exists(file):
            existing_path_X118_SME.append(file)
            backup_pathlist.append(file)
            open_button_X118_SME['state'] = ['normal']


def check_fileexists_X118_SME_AMG():
    for file in path_list_X118_SME_AMG:
        if os.path.exists(file):
            existing_path_X118_SME_AMG.append(file)
            backup_pathlist.append(file)
            open_button_X118_SME_AMG['state'] = ['normal']


def check_fileexists_X243():
    for file in path_list_X243:
        if os.path.exists(file):
            existing_path_X243.append(file)
            backup_pathlist.append(file)
            open_button_X243['state'] = ['normal']


def create_xml_backup():

    num_of_files = len(backup_pathlist)
    if messagebox.askquestion(title='Megerősítés', message='Valóban szeretnél biztonsági mentést készíteni?') == 'yes':
        for file_path in backup_pathlist:
            shutil.copy2(str(file_path), "D:\\BackupBestFit\\AbgleichBackup")

        backup_created = Label(root, bg='light yellow', fg='green', font=('Arial', 11, 'italic'),
                               text='Biztonsági mentés elkészült D:\BackupBestFit\AbgleichBackup')
        backup_created.grid(row=10, columnspan=4)
        restore_backup_button['state'] = 'normal'
    messagebox.showinfo(title='Rendben', message=f'{num_of_files} fájl biztonsági mentése elkészült')


def ask_exit():
    ask_user = messagebox.askquestion(title='Megerősítés', message='Biztosan kilépsz?')
    if ask_user == 'yes':
        root.destroy()


def login_popup():

    top = Toplevel(root)
    top.geometry = '350x300'
    top.title("Bejelentkezés")
    usr_label = Label(top, text="Felhasználónév", font=('Arial', 18))
    usr_label.pack()
    user_name_box = Entry(top, font=('Arial', 20))
    user_name_box.pack()

    pw_label = Label(top, text="Jelszó", font=('Arial', 18))
    pw_label.pack()
    password = StringVar()
    user_pass_box = Entry(top, font=('Arial', 20), textvariable=password, show='*')

    user_pass_box.pack()

    def afaszom(*args):
        get_name = user_name_box.get()
        get_pass = user_pass_box.get()

        my_font = font.Font(size=19, weight='bold')
        while True:
            if get_name == 'Admin' or get_name == 'acsepre' and get_pass == 'acsepre':

                check_fileexists_W177()
                check_fileexists_C118()
                check_fileexists_X118()
                check_fileexists_W177_SME()
                check_fileexists_C118_SME()
                check_fileexists_X118_SME()
                check_fileexists_W177_SME_AMG()
                check_fileexists_C118_SME_AMG()
                check_fileexists_X118_SME_AMG()
                check_fileexists_X243()
                login_button['text'] = 'Felh.:' + get_name
                login_button['font'] = my_font
                login_button['state'] = 'disabled'
                create_backup_button['state'] = 'normal'
                top.destroy()
                break

            else:
                messagebox.showerror('Helytelen jelszó', 'Kérlek add meg a helyes jelszót')
                break

    login_butt = Button(top, text="Bejelentkezés", font=('Arial', 12), bd=8, command=afaszom)
    user_pass_box.bind("<Return>", afaszom)
    login_butt.pack(pady=15)
    
    
def check_backup_files():
    backup_files = os.listdir("D:\\BackupBestFit\\AbgleichBackup")
    if len(backup_files) >= 1:
        restore_backup_button['state'] = 'normal'
        

        
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)
Grid.rowconfigure(root, 8, weight=1)
Grid.rowconfigure(root, 9, weight=1)
Grid.columnconfigure(root, 0, weight=2)
Grid.columnconfigure(root, 1, weight=2)
Grid.columnconfigure(root, 2, weight=2)
Grid.columnconfigure(root, 3, weight=2)
Grid.columnconfigure(root, 4, weight=2)


open_button_W177 = Button(root, text='BestFit W117', font=('Arial', 19, 'bold'), bd='10',
                          command=start_program_W177, height=1, width=15, state='disabled')
open_button_W177.grid(row=1, column=0)
open_button_W177.bind("<Enter>", on_enter_W177)
open_button_W177.bind("<Leave>", on_leave_W177)


open_button_C118 = Button(root, text='BestFit C118', font=('Arial', 19, 'bold'), bd='10',
                          command=start_program_C118, height=1, width=15, state='disabled')
open_button_C118.grid(row=2, column=0)
open_button_C118.bind("<Enter>", on_enter_C118)
open_button_C118.bind("<Leave>", on_leave_C118)


open_button_X118 = Button(root, text='BestFit X118', font=('Arial', 19, 'bold'), bd='10',
                          command=start_program_X118, height=1, width=15, state='disabled')
open_button_X118.grid(row=3, column=0)
open_button_X118.bind("<Enter>", on_enter_X118)
open_button_X118.bind("<Leave>", on_leave_X118)


open_button_X243 = Button(root, text='SMA X243', font=('Arial', 19, 'bold'), bd='10',
                          command=start_program_X243, height=1, width=15, state='disabled')
open_button_X243.grid(row=1, column=3)
open_button_X243.bind("<Enter>", on_enter_X243)
open_button_X243.bind("<Leave>", on_leave_X243)

function_test_button = Button(root, text='Teszt futtatása', font=('Arial', 19, 'bold'), bd='10',
                                    command=XT.run_program, height=1, width=32)
function_test_button.grid(row=4, column=1, columnspan=2, pady=5)
function_test_button.bind("<Enter>", on_enter_func_test_button)
function_test_button.bind("<Leave>", on_leave_func_test_button)

login_button = Button(root, text="Bejelentkezés", font=('Arial', 19, 'bold'), bd='10',
                      command=login_popup, height=1, width=15)
login_button.grid(row=4, column=0, pady=5)
login_button.bind("<Enter>", on_enter_login_butt)
login_button.bind("<Leave>", on_leave_login_butt)

open_button_W177_SME = Button(root, text='SME W177', font=('Arial', 19, 'bold'), bd='10',
                              command=start_program_W177_SME, height=1, width=15, state='disabled')
open_button_W177_SME.grid(row=1, column=1)
open_button_W177_SME.bind("<Enter>", on_enter_W177_SME)
open_button_W177_SME.bind("<Leave>", on_leave_W177_SME)


open_button_C118_SME = Button(root, text='SME C118', font=('Arial', 19, 'bold'), bd='10',
                              command=start_program_C118_SME, height=1, width=15, state='disabled')
open_button_C118_SME.grid(row=2, column=1)
open_button_C118_SME.bind("<Enter>", on_enter_C118_SME)
open_button_C118_SME.bind("<Leave>", on_leave_C118_SME)


open_button_X118_SME = Button(root, text='SME X118', font=('Arial', 19, 'bold'), bd='10',
                              command=start_program_X118_SME, height=1, width=15, state='disabled')
open_button_X118_SME.grid(row=3, column=1)
open_button_X118_SME.bind("<Enter>", on_enter_X118_SME)
open_button_X118_SME.bind("<Leave>", on_leave_X118_SME)


open_button_W177_SME_AMG = Button(root, text='SME AMG W177', font=('Arial', 19, 'bold'), bd='10',
                                  command=start_program_W177_SME_AMG, height=1, width=15, state='disabled')
open_button_W177_SME_AMG.grid(row=1, column=2)
open_button_W177_SME_AMG.bind("<Enter>", on_enter_W177_SME_AMG)
open_button_W177_SME_AMG.bind("<Leave>", on_leave_W177_SME_AMG)


open_button_C118_SME_AMG = Button(root, text='SME AMG C118', font=('Arial', 19, 'bold'), bd='10',
                                  command=start_program_C118_SME_AMG, height=1, width=15, state='disabled')
open_button_C118_SME_AMG.grid(row=2, column=2)
open_button_C118_SME_AMG.bind("<Enter>", on_enter_C118_SME_AMG)
open_button_C118_SME_AMG.bind("<Leave>", on_leave_C118_SME_AMG)


open_button_X118_SME_AMG = Button(root, text='SME AMG X118', font=('Arial', 19, 'bold'), bd='10',
                                  command=start_program_X118_SME_AMG, height=1, width=15, state='disabled')
open_button_X118_SME_AMG.grid(row=3, column=2)
open_button_X118_SME_AMG.bind("<Enter>", on_enter_X118_SME_AMG)
open_button_X118_SME_AMG.bind("<Leave>", on_leave_X118_SME_AMG)

restore_backup_button = Button(root, text='Biztonsági mentés visszatöltése', font=('Arial', 13),
                               command=restore_xml_backup,
                               state='disabled')
restore_backup_button.grid(row=6, column=0)
restore_backup_button.bind("<Enter>", on_enter_backup)
restore_backup_button.bind("<Leave>", on_leave_backup)

create_backup_button = Button(root, text='Biztonsági mentés készítése', font=('Arial', 14), command=create_xml_backup,
                              state='disabled')
create_backup_button.grid(row=5, column=0)
create_backup_button.bind("<Enter>", on_enter_create_backup)
create_backup_button.bind("<Leave>", on_leave_create_backup)

exit_button = Button(root, text="Kilépés", font=("Arial", 15), command=exit_program)
exit_button.grid(row=6, columnspan=4, pady=15)
exit_button.bind("<Enter>", on_enter_exit)
exit_button.bind("<Leave>", on_leave_exit)

watermark = Label(root, text='<<<Created by ZMESTER>>>',
                  font=('Arial', 11, 'italic'), bg='light yellow')
watermark.grid(row=7, columnspan=4)

watermark_name = Label(root, text='<<Mester Zsolt>>',
                             font=('Arial', 10, 'italic'), bg='light yellow')
watermark_name.grid(row=8, columnspan=4)

watermark2 = Label(root, text='<371_RB-EF>', font=('Arial', 10, 'italic'), bg='light yellow')
watermark2.grid(row=9, columnspan=4)

check_backup_files()

with open('text_box.txt', 'w') as txt:
    txt.truncate()


root.protocol("WM_DELETE_WINDOW", ask_exit)
root.mainloop()
