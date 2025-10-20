#Comment out the statements in the Question 4 of Contents of OS module

import os

#Select the Directory whose content you want to list
directory_path = '/'

#use the os module to list the directory path content

contents = os.listdir(directory_path)

#print the contents of the directory

print(contents)

"""
['!!dHCnc_qhlogs.txt', '!qhlogs.doc', '$RECYCLE.BIN', '1mUxSRU_qhlogs.csv', '4DefaultTemp', '4DefaultTempSaveScan', '4DThumb', 'ahRk5We_qhlogs.doc', 'Arduino_IDE', 'CAN_ BUS_sim', 'CFRBACKUP-ORALEBLG', 'Chinmay engineering memories', 'chinmay imp documents', 'Chinmay_Backup', 'Cloud_Computing', 'collage', 'Cultural_Championship', 'Microsoft VS Code', 'Mini_Project_sem6', 'msdownld.tmp', 'Network - Shortcut.lnk', 'python-3.13.7-amd64.exe', 'Python_Full_Course', 'Quick Heal', 'real me all photos', 'System Volume Information', 'TE - sem6', 'tqawFKI_qhlogs.log', 'VSCodeUserSetup-x64-1.104.1.exe', 'WhatsApp Installer.exe', 'zJ4wEPD_qhlogs.xls']
"""
#It prints the content in form of List [] 
