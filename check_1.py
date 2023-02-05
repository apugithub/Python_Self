import win32com.client
import time

excelapp = win32com.client.Dispatch("Excel.Application")
wb = excelapp.Workbooks.Open("D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/MF Investments tracker.xlsx")
wb.RefreshAll()
time.sleep(2)
wb.Save()
excelapp.Quit()




