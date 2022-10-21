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

root = Tk()
root.configure(bg='light yellow')
root.title('VMT BestFit Visu Offset updater_HU v1.00')
label = Label(root, text='Válaszd ki az ofszetfájlt(.csv formátum)',
              font=('Arial', 13, 'bold'), bg='light yellow')
label.pack()
exact_time = datetime.now()
final_logfilevar = '[LOG]' + exact_time.strftime('%Y-%d-%m_%H_%M_%S') + '.txt'

path_list_W177 = ["D:\BestFit\AuditTypes_Left\\010_W177_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\010_W177_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FA_RE.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\010_W177_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\010_W177_KH_RE.xml",
                  "D:\BestFit\AuditTypes_RT\\010_W177_ND_RT.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\011_W177_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\011_W177_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_MH\\010_W177_MH.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\020_W177_AMG_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\020_W177_AMG_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\020_W177_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\021_W177_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\021_W177_AMG_STS_vo_re.xml",
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
                  "D:\BestFit\AuditTypes_STS_vo_Left\\101_C118_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\101_C118_STS_vo_re.xml", 
                  "D:\BestFit\AuditTypes_MH\\120_C118_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\121_C118_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\121_C118_AMG_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\120_C118_AMG_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\120_C118_AMG_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\120_C118_AMG_MH.xml"
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
                  "D:\BestFit\AuditTypes_STS_vo_Left\\141_X118_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\141_X118_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes_MH\\160_X118_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\161_X118_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\161_X118_AMG_STS_vo_re.xml",
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
        for mod_file in mod_files:
            for orig_file in orig_files:
                if str(orig_file) in str(mod_file):
                    shutil.copy2("D:\\BackupBestFit\\AbgleichBackup\\" + orig_file, mod_file)

        for file in path_list_W177:
            if os.path.exists(file):
                open_button_W177["state"] = "normal"
                open_button_W177['font'] = ('Arial', 22, 'bold')
                open_button_W177["text"] = "BestFit W177"
                open_button_W177["bd"] = 10
                open_button_W177["color"] = "SystemButtonFace"
                break
        for file in path_list_W177_SME:
            if os.path.exists(file):
                open_button_W177_SME["state"] = "normal"
                open_button_W177_SME['font'] = ('Arial', 22, 'bold')
                open_button_W177_SME["text"] = "SME W177"
                open_button_W177_SME["color"] = "SystemButtonFace"
                open_button_W177_SME["bd"] = 10
                break        
        for file in path_list_W177_SME_AMG:
            if os.path.exists(file):
                open_button_W177_SME_AMG["state"] = "normal"
                open_button_W177_SME_AMG['font'] = ('Arial', 22, 'bold')
                open_button_W177_SME_AMG["text"] = "SME W177 AMG"
                open_button_W177_SME_AMG["color"] = "SystemButtonFace"
                open_button_W177_SME_AMG["bd"] = 10
                break
        for file in path_list_C118:
            if os.path.exists(file):
                open_button_C118["state"] = "normal"
                open_button_C118["text"] = "BestFit C118"
                open_button_C118['font'] = ('Arial', 22, 'bold')
                open_button_C118["color"] = "SystemButtonFace"
                open_button_C118["bd"] = 10
                break
        for file in path_list_C118_SME:
            if os.path.exists(file):
                open_button_C118_SME["state"] = "normal"
                open_button_C118_SME['font'] = ('Arial', 22, 'bold')
                open_button_C118_SME["text"] = "SME C118"
                open_button_C118_SME["color"] = "SystemButtonFace"
                open_button_C118_SME["bd"] = 10
                break        
        for file in path_list_C118_SME_AMG:
            if os.path.exists(file):
                open_button_C118_SME_AMG["state"] = "normal"
                open_button_C118_SME_AMG['font'] = ('Arial', 22, 'bold')
                open_button_C118_SME_AMG["text"] = "SME C118 AMG"
                open_button_C118_SME_AMG["color"] = "SystemButtonFace"
                open_button_C118_SME_AMG["bd"] = 10
                break
        for file in path_list_X118:
            if os.path.exists(file):
                open_button_X118["state"] = "normal"
                open_button_X118["text"] = "BestFit X118"
                open_button_X118['font'] = ('Arial', 22, 'bold')
                open_button_X118["color"] = "SystemButtonFace"
                open_button_X118["bd"] = 10
                break
        for file in path_list_X118_SME:
            if os.path.exists(file):
                open_button_X118_SME["state"] = "normal"
                open_button_X118_SME['font'] = ('Arial', 22, 'bold')
                open_button_X118_SME["text"] = "SME X118"
                open_button_X118_SME["color"] = "SystemButtonFace"
                open_button_X118_SME["bd"] = 10
                break        
        for file in path_list_X118_SME_AMG:
            if os.path.exists(file):
                open_button_X118_SME_AMG["state"] = "normal"
                open_button_X118_SME_AMG['font'] = ('Arial', 22, 'bold')
                open_button_X118_SME_AMG["text"] = "SME X118 AMG"
                open_button_X118_SME_AMG["color"] = "SystemButtonFace"
                open_button_X118_SME_AMG["bd"] = 10
                break
        for file in path_list_X243:
            if os.path.exists(file):
                open_button_X243["state"] = "normal"
                open_button_X243["text"] = "SMA X243"
                open_button_X243['font'] = ('Arial', 22, 'bold')
                open_button_X243["color"] = "SystemButtonFace"
                open_button_X243["bd"] = 10
                break

        backup_button['state'] = 'disabled'
        messagebox.showinfo("Sikeres helyreállítás",
                            "Biztonsági mentés sikeresen visszatöltve. MINDEN offset az eredeti értékre állítva!")


def start_program_W177():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válaszd ki az CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                              ("all files", "*.*")))

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

            if "BF_W177" in str(final_path_to_txt):
                for file_path in existing_path_W177:
                    setmeasurement_pointc118(file_path)
                open_button_W177["text"] = "BestFit W177"
                open_button_W177['font'] = ('Arial', 22, 'italic')
                open_button_W177["state"] = "disabled"
                open_button_W177["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
            break


def start_program_W177_SME():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                            ("all files", "*.*")))

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

            if 'SME_W177' in str(final_path_to_txt):
                for file_path in existing_path_W177_SME:
                    setmeasurement_pointc118(file_path)
                open_button_W177_SME["text"] = "SME W177"
                open_button_W177_SME['font'] = ('Arial', 22, 'italic')
                open_button_W177_SME["state"] = "disabled"
                open_button_W177_SME["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
            break
            
            
            
def start_program_W177_SME_AMG():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                            ("all files", "*.*")))

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

            if 'SME_W177_AMG' in str(final_path_to_txt):
                for file_path in existing_path_W177_SME_AMG:
                    setmeasurement_pointc118(file_path)
                open_button_W177_SME_AMG["text"] = "SME W177 AMG"
                open_button_W177_SME_AMG['font'] = ('Arial', 22, 'italic')
                open_button_W177_SME_AMG["state"] = "disabled"
                open_button_W177_SME_AMG["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
            break


def start_program_C118():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válaszd ki a CSV fájlt', filetypes=[("csv files", "*.csv"),
                                                                                             ("all files", "*.*")])

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

            if "BF_C118" in str(final_path_to_txt):
                for file_path in existing_path_C118:
                    setmeasurement_pointc118(file_path)
                open_button_C118["text"] = "BestFit C118"
                open_button_C118['font'] = ('Arial', 22, 'italic')
                open_button_C118["state"] = "disabled"
                open_button_C118["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
            break


def start_program_C118_SME():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                            ("all files", "*.*")))

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

            if "SME_C118" in str(final_path_to_txt):
                for file_path in existing_path_C118_SME:
                    setmeasurement_pointc118(file_path)
                open_button_C118_SME["text"] = "SME C118"
                open_button_C118_SME['font'] = ('Arial', 22, 'italic')
                open_button_C118_SME["state"] = "disabled"
                open_button_C118_SME["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
            break
            
            
            
            
def start_program_C118_SME_AMG():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                            ("all files", "*.*")))

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

            if "C118_AMG" in str(final_path_to_txt):
                for file_path in existing_path_C118_SME_AMG:
                    setmeasurement_pointc118(file_path)
                open_button_C118_SME_AMG["text"] = "SME C118 AMG"
                open_button_C118_SME_AMG['font'] = ('Arial', 22, 'italic')
                open_button_C118_SME_AMG["state"] = "disabled"
                open_button_C118_SME_AMG["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
            break


def start_program_X118():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                            ("all files", "*.*")))

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

            if "X118" in str(final_path_to_txt):
                for file_path in existing_path_X118:
                    setmeasurement_pointc118(file_path)
                open_button_X118["text"] = "BestFit X118 "
                open_button_X118['font'] = ('Arial', 22, 'italic')
                open_button_X118["state"] = "disabled"
                open_button_X118["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
            break


def start_program_X118_SME():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                            ("all files", "*.*")))

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

            if "SME_X118" in str(final_path_to_txt):
                for file_path in existing_path_X118_SME:
                    setmeasurement_pointc118(file_path)
                open_button_X118_SME["text"] = "SME X118"
                open_button_X118_SME['font'] = ('Arial', 22, 'italic')
                open_button_X118_SME["state"] = "disabled"
                open_button_X118_SME["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break
        except:
            break            
            
            
            
def start_program_X118_SME_AMG():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válasz ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                            ("all files", "*.*")))

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

            if "SME_X118_AMG" in str(final_path_to_txt):
                for file_path in existing_path_X118_SME_AMG:
                    setmeasurement_pointc118(file_path)
                open_button_X118_SME_AMG["text"] = "SME X118 AMG"
                open_button_X118_SME_AMG['font'] = ('Arial', 22, 'italic')
                open_button_X118_SME_AMG["state"] = "disabled"
                open_button_X118_SME_AMG["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break
        except:
            break


def start_program_X243():
    while True:
        try:
            csv_rawdata = []
            replaced_char_list = []
            replaced_char_list_2 = []
            final_point_value_list = []
            filepath = filedialog.askopenfilename(title='Válaszd ki a CSV fájlt', filetypes=(("csv files", "*.csv"),
                                                                                             ("all files", "*.*")))

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

            if "X243" in str(final_path_to_txt):
                for file_path in existing_path_X243:
                    setmeasurement_pointc118(file_path)
                open_button_X243["text"] = "SMA X243"
                open_button_X243['font'] = ('Arial', 22, 'italic')
                open_button_X243["state"] = "disabled"
                open_button_X243["color"] = "light green"
                backup_button['state'] = 'normal'
                break
            else:
                messagebox.showerror('Helytelen fájl', 'Kérlek válaszd ki a megfelelő .CSV fájlt!')
                break

        except:
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

    for element in root.iter('Double'):
        get_tagName = element.get('name')
        get_pointValue = element.get('value')

        if get_tagName == 'Offset' and len(final_strlist) > 0:
            element.set('value', str(final_strlist[0]))

            with open(currtext, 'a+') as logfile:
                logfile.write(f'\nOffset {final_keylist[0]} felülírva {get_pointValue}-ról {element.get("value")}-ra'
                              f' itt:\n {document}\n')

            with open(final_logfilevar, 'a+') as logfile_2:
                logfile_2.write(f'\nOffset {final_keylist[0]} felülírva {get_pointValue}-ról {element.get("value")}-ra'
                                f'itt: \n {document} \n')

            final_strlist.pop(0)
            final_keylist.pop(0)

    with open(currtext, 'r+') as log:
        read = log.read()
        log.truncate(0)

    messagebox.showinfo('Log fájl felülírva', f' {read} ')
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


def on_leave_C118_SME_AMG(e):
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
    if backup_button['state'] == 'normal':
        backup_button['background'] = '#8CC9DE'


def on_leave_backup(e):
    backup_button['background'] = 'SystemButtonFace'


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
    for file_path in backup_pathlist:
        shutil.copy2(str(file_path), "D:\\BackupBestFit\\AbgleichBackup")

    backup_created = Label(root, bg='light yellow', fg='green', font=('Arial', 10, 'italic'),
                           text='Automatikus biztonsági mentés elkészült D:\BackupBestFit\AbgleichBackup')
    backup_created.pack(pady=10)


frame1 = Frame(root, bg='black')
frame1.pack()
open_button_W177 = Button(frame1, text='BestFit W117', font=('Arial', 22, 'bold'), bd='10',
                          command=start_program_W177, width=15, state='disabled')
open_button_W177.pack(padx=2, pady=2)
open_button_W177.bind("<Enter>", on_enter_W177)
open_button_W177.bind("<Leave>", on_leave_W177)

frame2 = Frame(root, bg='black')
frame2.pack()
open_button_C118 = Button(frame2, text='BestFit C118', font=('Arial', 22, 'bold'), bd='10',
                          command=start_program_C118, width=15, state='disabled')
open_button_C118.pack(padx=2, pady=1)
open_button_C118.bind("<Enter>", on_enter_C118)
open_button_C118.bind("<Leave>", on_leave_C118)

frame3 = Frame(root, bg='black')
frame3.pack()
open_button_X118 = Button(frame3, text='BestFit X118', font=('Arial', 22, 'bold'), bd='10',
                          command=start_program_X118, width=15, state='disabled')
open_button_X118.pack(padx=2, pady=2)
open_button_X118.bind("<Enter>", on_enter_X118)
open_button_X118.bind("<Leave>", on_leave_X118)

frame4 = Frame(root, bg='black')
frame4.pack()
open_button_X243 = Button(frame4, text='SMA X243', font=('Arial', 22, 'bold'), bd='10',
                          command=start_program_X243, width=15, state='disabled')
open_button_X243.pack(padx=2, pady=2)
open_button_X243.bind("<Enter>", on_enter_X243)
open_button_X243.bind("<Leave>", on_leave_X243)

frame122 = Frame(root, bg='black')
frame122.pack()
open_button_W177_SME = Button(frame122, text='SME W177', font=('Arial', 22, 'bold'), bd='10',
                                  command=start_program_W177_SME, width=15, state='disabled')
open_button_W177_SME.pack(padx=2, pady=2)
open_button_W177_SME.bind("<Enter>", on_enter_W177_SME)
open_button_W177_SME.bind("<Leave>", on_leave_W177_SME)

frame222 = Frame(root, bg='black')
frame222.pack()
open_button_C118_SME = Button(frame222, text='SME C118', font=('Arial', 22, 'bold'), bd='10',
                                  command=start_program_C118_SME, width=15, state='disabled')
open_button_C118_SME.pack(padx=2, pady=2)
open_button_C118_SME.bind("<Enter>", on_enter_C118_SME)
open_button_C118_SME.bind("<Leave>", on_leave_C118_SME)

frame333 = Frame(root, bg='black')
frame333.pack()
open_button_X118_SME = Button(frame333, text='SME X118', font=('Arial', 22, 'bold'), bd='10',
                                  command=start_program_X118_SME, width=15, state='disabled')
open_button_X118_SME.pack(padx=2, pady=2)
open_button_X118_SME.bind("<Enter>", on_enter_X118_SME)
open_button_X118_SME.bind("<Leave>", on_leave_X118_SME)

frame12 = Frame(root, bg='black')
frame12.pack()
open_button_W177_SME_AMG = Button(frame12, text='SME AMG W177', font=('Arial', 22, 'bold'), bd='10',
                                  command=start_program_W177_SME_AMG, width=15, state='disabled')
open_button_W177_SME_AMG.pack(padx=2, pady=2)
open_button_W177_SME_AMG.bind("<Enter>", on_enter_W177_SME_AMG)
open_button_W177_SME_AMG.bind("<Leave>", on_leave_W177_SME_AMG)

frame22 = Frame(root, bg='black')
frame22.pack()
open_button_C118_SME_AMG = Button(frame22, text='SME AMG C118', font=('Arial', 22, 'bold'), bd='10',
                                  command=start_program_C118_SME_AMG, width=15, state='disabled')
open_button_C118_SME_AMG.pack(padx=2, pady=2)
open_button_C118_SME_AMG.bind("<Enter>", on_enter_C118_SME_AMG)
open_button_C118_SME_AMG.bind("<Leave>", on_leave_C118_SME_AMG)

frame33 = Frame(root, bg='black')
frame33.pack()
open_button_X118_SME_AMG = Button(frame33, text='SME AMG X118', font=('Arial', 22, 'bold'), bd='10',
                                  command=start_program_X118_SME_AMG, width=15, state='disabled')
open_button_X118_SME_AMG.pack(padx=2, pady=2)
open_button_X118_SME_AMG.bind("<Enter>", on_enter_X118_SME_AMG)
open_button_X118_SME_AMG.bind("<Leave>", on_leave_X118_SME_AMG)

backup_button = Button(root, text='Biztonsági mentés visszatöltése', font=('Arial', 15), command=restore_xml_backup,
                       state='disabled')
backup_button.pack()
backup_button.bind("<Enter>", on_enter_backup)
backup_button.bind("<Leave>", on_leave_backup)

exit_button = Button(root, text="Kilépés", font=("Arial", 15), command=exit_program)
exit_button.pack(pady=30)
exit_button.bind("<Enter>", on_enter_exit)
exit_button.bind("<Leave>", on_leave_exit)

watermark = Label(root, text='<<<Created by ZMESTER>>>',
                  font=('Arial', 10, 'italic'), bg='light yellow')
watermark.pack(anchor='s')
watermark2 = Label(root, text='371_Kecskemet_Rohbau_Einführung', font=('Arial', 10), bg='light yellow')
watermark2.pack(anchor='s')

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
create_xml_backup()
root.mainloop()
