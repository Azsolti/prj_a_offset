import csv
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import date
import os


root = Tk()


def start_program():
    while True:
        my_list = []
        anotherlist = []
        final_list = []
        list_tostrg = ''
        try:
            with open(open_File(), 'r') as csv_file:

                reader = csv.reader(csv_file)
                for n in reader:
                    my_list.append(n)

            for n in my_list:
                for character in n:
                    list_tostrg += character
                    strg_replace = list_tostrg.replace(";", ".", 1)
                    list_tostrg = ""
                    anotherlist.append(strg_replace)

                # Converting unwanted characters to readable/necessary ones
            for n in anotherlist:
                list_tostrg += n
                strg_replace2 = list_tostrg.replace(";", "=")
                final_list.append(strg_replace2)
                list_tostrg = ""

            for item in final_list:
                getindex = item.index("=")
                name_puff = item[:getindex]
                value_puff = item[getindex + 1:]
                CSV_ORIGDATA[name_puff] = value_puff

                # And finally we make a dictionary with the keys and values we need
            selectfile: str = open_xml()
            setmeasurement_pointc118(selectfile)

        except ValueError:

            if popup() == 'yes':
                continue
            else:
                messagebox.showinfo('Close program', 'Offsets has not changed. Closing program')
                root.destroy()
                break

        messagebox.showinfo('Close program', 'Offsets has been updated. Closing program')
        root.destroy()
        break


def open_File():
    filepath = filedialog.askopenfilename(title='Select the .txt file',
                                          filetypes=(("txt files", "*.txt"),
                                                     ("all files", "*.*")))
    return str(filepath)


def open_xml():
    xmlsource = filedialog.askopenfilename(title='Select the .xml file',
                                           filetypes=(("xml files", "*.xml"),
                                                      ("all files", "*.*")))
    return str(xmlsource)


def popup():
    return messagebox.askquestion('Error', 'Wrong file selected! Please select the correct .txt file!\nContinue?')


root.geometry('500x300')
root.title('Auto offset loader')
label = Label(root, text='Select the offset data(.txt) file\nthen select the .xml you want to overwrite',
                    font=('Arial', 17))
label.pack()
open_button = Button(root, text='Open file', font=('Arial', 30), command=start_program)
open_button.pack()
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
    currtext = 'Offset_update_log_'+str(CURR_DATE)+'.txt'
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
            messagebox.showinfo('Offset update notification', f'Offset {FINAL_KEYLIST[0]} updated to {get_pointValue}')
            with open(currtext, 'a+') as logfile:
                logfile.write(f'\nOffset {FINAL_KEYLIST[0]} updated to {get_pointValue}\n')

            FINAL_STRLIST.pop(0)
            FINAL_KEYLIST.pop(0)

    messagebox.showinfo('Log notification', f' Log file {currtext} created to {filepath}')

    tree.write(document)


root.mainloop()
