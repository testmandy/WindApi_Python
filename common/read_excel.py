# coding=utf-8
# @Time    : 2019/12/11 18:21
# @Author  : Mandy
import xlrd
from xlutils.copy import copy


class ReadExcel:
    def __init__(self):
        self.filename = "E:\\PycharmProjects\\WindApi_Python\\data\\testcases.xls"
        self.workbook = xlrd.open_workbook(self.filename)
        self.sheet = self.get_sheet()

    def get_sheet(self, i=0):
        sheet = self.workbook.sheets()[i]
        return sheet

    def get_nrows(self):
        nrows = self.sheet.nrows
        return nrows

    def get_ncols(self):
        ncols = self.sheet.ncols
        return ncols

    def get_row(self, i):
        row = self.sheet.row_values(i)
        return row

    def get_col(self, i):
        col = self.sheet.col_values(i)
        return col

    def get_cell(self, rowNum, colNum):
        cell = self.sheet.cell_value(rowNum, colNum)
        return cell

    def write_cell(self, rowNum, colNum, data):
        wb = copy(self.workbook)
        ws = wb.get_sheet(0)
        ws.write(rowNum, colNum, data)
        wb.save(self.filename)

    def main(self):
        print("sheet行数为：" + str(self.get_nrows()))
        print("sheet列数为：" + str(self.get_ncols()))
        # print("sheet第一行数据为：" + str(self.get_row(0)))
        # print("sheet第一列数为：" + str(self.get_col(0)))
        print("sheet行数为：" + self.get_cell(0, 0))


# 测试数据
if __name__ == '__main__':
    read = ReadExcel()
    read.write_cell(1, TestConfig.ActualDataColNum, "123456")

