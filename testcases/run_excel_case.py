# coding=utf-8
# @Time    : 2019/12/11 17:07
# @Author  : Mandy

import conftest
from common.read_excel import ReadExcel
from common.read_ini import ReadIni
from common.test_method import Method


class RunExcel:
    def __init__(self):
        self.excel = ReadExcel()
        self.method = Method()
        self.ini = ReadIni()
        self.total = self.excel.get_nrows()
        print(u'The total case is: %s' % self.total)

    def get_id(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.IdColNum)

    def get_model_name(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.ModelNameColNum)

    def get_api_name(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.ApiNameColNum)

    def get_url(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.UrlColNum)

    def get_method(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.MethodColNum)

    def get_is_run(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.IsRunColNum)

    def get_dependent_id(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.DependentIdColNum)

    def get_dependent_key(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.DependentKeyColNum)

    def get_response_key(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.ResponseKeyColNum)

    def get_request_data(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.RequestDataColNum)

    def get_expect_data(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.ExpectDataColNum)

    def get_actual_data(self, rowNum):
        return self.excel.get_cell(rowNum, conftest.ActualDataColNum)

    def main(self, rowNum):
        header = self.ini.get_value('header')
        method = self.get_method(rowNum)
        base_url = self.ini.get_value('api', 'base_url')
        data = self.get_request_data(rowNum)
        print(data)
        uri = self.get_url(rowNum)
        test_url = base_url + uri
        print(test_url)
        res = self.method.run_main(method, test_url, data, header)
        print(u'The running result: %s' % res)
        return res


if __name__ == '__main__':
    run = RunExcel()
    for i in range(1, run.total):
        run.main(i)

