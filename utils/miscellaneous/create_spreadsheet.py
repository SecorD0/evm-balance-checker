import os
from typing import Union

from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pretty_utils.miscellaneous.files import join_path


def create_spreadsheet(path: Union[str, tuple, list], headers: Union[list, tuple], sheet_name: str = 'Sheet') -> bool:
    path = join_path(path)
    path_and_expansion = path.split('.')
    if len(path_and_expansion) == 1:
        path = path + '.xlsx'

    elif len(path_and_expansion) >= 2 and path_and_expansion[-1] != 'xlsx':
        path = '.'.join(path_and_expansion[:-1] + ['xlsx'])

    if not os.path.exists(path):
        spreadsheet = Workbook()
        spreadsheet['Sheet'].title = sheet_name
        sheet: Worksheet = spreadsheet[sheet_name]
        for column, header in enumerate(headers):
            sheet.cell(row=1, column=column + 1).value = header

        spreadsheet.save(path)
        return True

    return False
