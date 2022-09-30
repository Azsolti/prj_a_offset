import csv
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import date
import os
import os.path
import shutil

root = Tk()
root.geometry('600x600')
root.title('Auto offset loader')
label = Label(root, text='Select the offset data(.txt) file\nthen select the .xml you want to overwrite',
              font=('Arial', 17))
label.pack()


path_list_W177 = ["D:\BestFit\AuditTypes_Left\\010_W177_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\010_W177_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FA_RE.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\010_W177_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\010_W177_KH_RE.xml",
                  "D:\BestFit\AuditTypes_RT\\010_W177_ND_RT.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\011_W177_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\011_W177_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes\Type_W177\\11_W177_KV_LBR_Links.xml",
                  "D:\BestFit\AuditTypes\Type_W177\\11_W177_KV_LBR_Rechts.xml",
                  "D:\BestFit\AuditTypes_MH\\010_W177_MH.xml"
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
                  "D:\BestFit\AuditTypes\Type_C118\\21_C118_KV_LBR_Links.xml",
                  "D:\BestFit\AuditTypes\Type_C118\\21_C118_KV_LBR_Rechts.xml",
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
                  "D:\BestFit\AuditTypes\Type_X118\\31_X118_KV_LBR_Links.xml",
                  "D:\BestFit\AuditTypes\Type_X118\\31_X118_KV_LBR_Rechts.xml"
                  ]

existing_path_W177 = []
existing_path_C118 = []
existing_path_X118 = []
backup_pathlist = []


def check_fileexists_W177():
    for file in path_list_W177:
        if os.path.exists(file):
            existing_path_W177.append(file)
            backup_pathlist.append(file)
        else:
            pass


def check_fileexists_C118():
    for file in path_list_C118:
        if os.path.exists(file):
            existing_path_C118.append(file)
            backup_pathlist.append(file)
        else:
            pass


def check_fileexists_X118():
    for file in path_list_X118:
        if os.path.exists(file):
            existing_path_X118.append(file)
            backup_pathlist.append(file)
        else:
            pass


def create_xml_backup():
    for file_path_W177 in existing_path_W177:
        shutil.copy2(str(file_path_W177), "D:\\BestFit\\AbgleichBackup")

    for file_path_C118 in existing_path_C118:
        shutil.copy2(str(file_path_C118), "D:\\BestFit\\AbgleichBackup")

    for file_path_X118 in existing_path_X118:
        shutil.copy2(str(file_path_X118), "D:\\BestFit\\AbgleichBackup")


def restore_xml_backup():
    backup_files = os.listdir("D:\\BestFit\\AbgleichBackup")

    for file_path, backup_path in zip(backup_files, backup_pathlist):
        shutil.copy2("D:\\BestFit\\AbgleichBackup\\" + file_path, backup_path)

    messagebox.showinfo("Restore completed", "Offsets has been restored")


def start_program_W177():
    while True:
        csv_rawdata = []
        rawdata_chars = []
        final_list = []
        list_tostrg = ''
        try:
            with open(open_file(), 'r') as csv_file:

                reader = csv.reader(csv_file)
                for n in reader:
                    csv_rawdata.append(n)
        except:
            break

        try:
            for n in csv_rawdata:
                for character in n:
                    list_tostrg += character
                    strg_replace = list_tostrg.replace(";", ".", 1)
                    list_tostrg = ""
                    rawdata_chars.append(strg_replace)

                # Converting unwanted characters to readable/necessary ones
            for n in rawdata_chars:
                list_tostrg += n
                strg_replace2 = list_tostrg.replace(";", "=")
                final_list.append(strg_replace2)
                list_tostrg = ""

            for item in final_list:
                getindex = item.index("=")
                name_puff = item[:getindex]
                value_puff = item[getindex + 1:]
                CSV_ORIGDATA[name_puff] = value_puff

        except ValueError:

            if popup() == 'yes':
                continue
            else:
                messagebox.showinfo('Close program', 'Offsets has not changed. Closing program')
                root.destroy()
                exit_program()

        if "W177" in str(csv_file):
            for file_path in existing_path_W177:
                setmeasurement_pointc118(file_path)
            open_button_W177["text"] = "W177 file loaded"
            open_button_W177["state"] = "disabled"
            backup_button['state'] = 'active'
            backup_button['bg'] = 'green'
            break

        else:
            messagebox.showerror('Invalid file', 'Please select the correct TXT file')


def start_program_C118():
    while True:
        csv_rawdata = []
        rawdata_chars = []
        final_list = []
        list_tostrg = ''
        try:
            with open(open_file(), 'r') as csv_file:

                reader = csv.reader(csv_file)
                for n in reader:
                    csv_rawdata.append(n)
        except:
            break

        try:
            for n in csv_rawdata:
                for character in n:
                    list_tostrg += character
                    strg_replace = list_tostrg.replace(";", ".", 1)
                    list_tostrg = ""
                    rawdata_chars.append(strg_replace)

                # Converting unwanted characters to readable/necessary ones
            for n in rawdata_chars:
                list_tostrg += n
                strg_replace2 = list_tostrg.replace(";", "=")
                final_list.append(strg_replace2)
                list_tostrg = ""

            for item in final_list:
                getindex = item.index("=")
                name_puff = item[:getindex]
                value_puff = item[getindex + 1:]
                CSV_ORIGDATA[name_puff] = value_puff

        except ValueError:

            if popup() == 'yes':
                continue
            else:
                messagebox.showinfo('Close program', 'Offsets has not changed. Closing program')
                root.destroy()
                exit_program()

        if "C118" in str(csv_file):
            for file_path in existing_path_C118:
                setmeasurement_pointc118(file_path)
            open_button_C118["text"] = "C118 file loaded"
            open_button_C118["state"] = "disabled"
            backup_button['state'] = 'active'
            backup_button['bg'] = 'green'
            break

        else:
            messagebox.showerror('Invalid file', 'Please select the correct TXT file')


def start_program_X118():
    while True:
        csv_raw_data = []
        raw_data_chars = []
        final_list = []
        list_tostrg = ''
        try:
            with open(open_file(), 'r') as csv_file:

                reader = csv.reader(csv_file)
                for n in reader:
                    csv_raw_data.append(n)
        except:
            break

        try:
            for n in csv_raw_data:
                for character in n:
                    list_tostrg += character
                    strg_replace = list_tostrg.replace(";", ".", 1)
                    list_tostrg = ""
                    raw_data_chars.append(strg_replace)

                # Converting unwanted characters to readable/necessary ones
            for n in raw_data_chars:
                list_tostrg += n
                strg_replace2 = list_tostrg.replace(";", "=")
                final_list.append(strg_replace2)
                list_tostrg = ""

            for item in final_list:
                getindex = item.index("=")
                name_puff = item[:getindex]
                value_puff = item[getindex + 1:]
                CSV_ORIGDATA[name_puff] = value_puff

        except ValueError:

            if popup() == 'yes':
                continue
            else:
                messagebox.showinfo('Close program', 'Offsets has not changed. Closing program')
                root.destroy()
                exit_program()

        if "X118" in str(csv_file):
            for file_path in existing_path_X118:
                setmeasurement_pointc118(file_path)
            open_button_X118["text"] = "X118 file loaded"
            open_button_X118["state"] = "disabled"
            backup_button['state'] = 'active'
            backup_button['bg'] = 'green'

            break

        else:
            messagebox.showerror('Invalid file', 'Please select the correct TXT file')


def exit_program():
    exit()


def open_file():

    filepath = filedialog.askopenfilename(title='Select the .txt file',
                                                  filetypes=(("txt files", "*.txt"),
                                                             ("all files", "*.*")))

    if filepath:
        return str(filepath)


def popup():
    return messagebox.askquestion('Error', 'Wrong file selected! Please select the correct .txt file!\nContinue?')


pointnames_got = []
values_got = []
XML_ORIGDATA = {}
CSV_ORIGDATA = {}


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
            XML_ORIGDATA[element] = values_got[0]
            values_got.pop(0)

    CALCULATED_KEYVALUES = {key: float(CSV_ORIGDATA.get(key, 0))
                                + float(XML_ORIGDATA.get(key, 0))
                            for key in XML_ORIGDATA
                            }

    FINAL_LIST = [round(item, 2) for item in CALCULATED_KEYVALUES.values()]
    FINAL_STRLIST = [str(e) for e in FINAL_LIST]
    FINAL_KEYLIST = [e for e in CALCULATED_KEYVALUES.keys()]
    CURR_DATE = date.today()
    currtext = 'Offset_update_log_' + str(CURR_DATE) + '.txt'
    filepath = os.path.realpath(currtext)

    for element in root.iter('Double'):

        get_tagName = element.get('name')
        get_pointValue = element.get('value')

        if get_tagName == 'Offset' and len(FINAL_STRLIST) > 0:
            print(FINAL_KEYLIST[0], ' offset updated from ', element.get('value'), end='')
            element.set('value', str(FINAL_STRLIST[0]))
            print(' to ', element.get('value'), 'in file: ', str(document))
            result = float(get_pointValue) - float(element.get('value'))
            if abs(result) > 0.2:
                print('ATTENTION: more than 0.2 offset, check if correct')
            with open(currtext, 'a+') as logfile:
                logfile.write(f'\nOffset {FINAL_KEYLIST[0]} updated to {get_pointValue}\n')

            FINAL_STRLIST.pop(0)
            FINAL_KEYLIST.pop(0)

    pointnames_got.clear()
    values_got.clear()
    XML_ORIGDATA.clear()
    messagebox.showinfo('Log notification', f' Log file {currtext} created to {filepath}')

    tree.write(document)


open_button_W177 = Button(root, text='Open W177 file', font=('Arial', 30), command=start_program_W177)
open_button_W177.pack()
open_button_C118 = Button(root, text='Open C118 file', font=('Arial', 30), command=start_program_C118)
open_button_C118.pack()
open_button_X118 = Button(root, text='Open X118 file', font=('Arial', 30), command=start_program_X118)
open_button_X118.pack()
exit_button = Button(root, text="Exit program", font=("Arial", 15), command=exit_program)
exit_button.pack()
backup_button = Button(root, bg="Red", text='Restore backup', font=('Arial', 15), command=restore_xml_backup, state='disabled')
backup_button.pack()

check_fileexists_W177()
check_fileexists_C118()
check_fileexists_X118()
create_xml_backup()

root.mainloop()

