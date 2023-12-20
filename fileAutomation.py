
import shutil
import os


filepath = 'C:\\Users\\Carter\\Downloads'

#functions for the different file types

def ExcelFunction(excelFiles):
    if not "downloadedExcelFiles" in os.listdir():
        os.mkdir("downloadedExcelFiles")
    newPath = 'C:\\Users\\Carter\\FileAutomation\\downloadedExcelFiles\\' + excelFiles
    oldPath = 'C:\\Users\\Carter\\Downloads\\' + excelFiles
    shutil.move(oldPath, newPath)

def WordFunction(WordFiles):
    if not "downloadedWordDocs" in os.listdir():
        os.mkdir("downloadedWordDocs")
    newPath = 'C:\\Users\\Carter\\FileAutomation\\downloadedWordDocs\\' + WordFiles
    oldPath = 'C:\\Users\\Carter\\Downloads\\' + WordFiles
    shutil.move(oldPath, newPath)

def TableauFunction(tableauFiles):
    if not "downloadedTableauFiles" in os.listdir():
        os.mkdir("downloadedTableauFiles")
    newPath = 'C:\\Users\\Carter\\FileAutomation\\downloadedTableauFiles\\' + tableauFiles
    oldPath = 'C:\\Users\\Carter\\Downloads\\' + tableauFiles
    shutil.move(oldPath, newPath)
def PDFFunction(PdfFile):
    if not "downloadedPdfFiles" in os.listdir():
        os.mkdir("downloadedPdfFiles")
    newPath = 'C:\\Users\\Carter\\FileAutomation\\downloadedPdfFiles\\' + PdfFile
    oldPath = 'C:\\Users\\Carter\\Downloads\\' + PdfFile
    shutil.move(oldPath, newPath)
def ImageFunction(imageFile):
    if not "downloadedImageFiles" in os.listdir():
        os.mkdir("downloadedImageFiles")
    newPath = 'C:\\Users\\Carter\\FileAutomation\\downloadedImageFiles\\' + imageFile
    oldPath = 'C:\\Users\\Carter\\Downloads\\' + imageFile
    shutil.move(oldPath, newPath)
def EXEFunction(exeFile):
    if not "downloadedExeFiles" in os.listdir():
        os.mkdir("downloadedExeFiles")
    newPath = 'C:\\Users\\Carter\\FileAutomation\\downloadedExeFiles\\' + exeFile
    oldPath = 'C:\\Users\\Carter\\Downloads\\' + exeFile
    shutil.move(oldPath, newPath)
def OtherFunction(otherFile):
    if not "downloadedOtherFiles" in os.listdir():
        os.mkdir("downloadedOtherFiles")
    newPath = 'C:\\Users\\Carter\\FileAutomation\\downloadedOtherFiles\\' + otherFile
    oldPath = 'C:\\Users\\Carter\\Downloads\\' + otherFile
    shutil.move(oldPath, newPath)


#Main Program
try:
    for file in os.listdir(filepath):
        if '.xlsx' in file.lower() or '.csv' in file.lower() or '.xls' in file.lower():
            ExcelFunction(file)
        elif '.docx' in file.lower() or '.doc' in file.lower():
            WordFunction(file)
        elif '.twbx' in file.lower():
            TableauFunction(file)
        elif '.pdf' in file.lower():
            PDFFunction(file)
        elif '.jpg' in file.lower() or '.png' in file.lower() or '.gif' in file.lower() or 'jpeg' in file.lower():
            ImageFunction(file)
        elif '.exe' in file.lower():
            EXEFunction(file)
        else:
            OtherFunction(file)
except:
    print("There are no files to transfer")

