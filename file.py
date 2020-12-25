import static
import openpyxl


class FileFunctions:

    def __init__(self, text):
        self.text = text
        FileFunctions.writeFile(self)

    def writeFile(self):
        rIndex = static.Foo.rowIndex(self)
        if rIndex % 100 == 1:
            path = "C:/Users/suley/PycharmProjects/iettsProject/canakkaleden_sonra.xlsx"
            workbook = openpyxl.load_workbook(path)
            sheet = workbook.active

        for r in range(1, 2, 1):
            for c in range(1, 2, 1):
                cIndex = static.Foo.columnIndexIncrease(self)
                rIndex = static.Foo.rowIndex(self)

                sheet.column_dimensions[chr(cIndex + 64)].width = 60
                sheet.cell(row=rIndex, column=cIndex, value=self.text)
                workbook.save(path)
