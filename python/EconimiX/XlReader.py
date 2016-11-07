__author__ = 'eladron'

import openpyxl
import Reader


path = 'input_Files/Economic_plan.xlsx'

class XlReader(Reader):
    def load(self, path):
        wb = openpyxl.load_workbook(path)
        return type(wb)




xlReader = XlReader()
print xlReader.load(path)