"""
household_power_consumption.txtの日時のフォーマットを変更する
 dd/mm/yyyy -> yyyy/mm/ddd
"""
import re

class ReformException(Exception):
    pass

def reform_date(date_string: str):
    """
    >> reform(21/10/2020)
    2020/10/21
    >> reform(05/01/2020)
    2020/01/05
    """
    result = re.search(r'(?P<day>\d+)\/(?P<month>\d+)\/(?P<year>\d+)', date_string)
    if result:
        return ("{}/{}/{}".format(result.group("year"), result.group("month"), result.group("day")))
    else:
        raise ReformException("日付データの要素抽出に失敗しました。(入力={})".format(date_string))

def reform_line(line: str):
    """
    >>> 16/12/2006;17:24:00;4.216;0.418;234.840;18.400;0.000;1.000;17.000
    2006/12/16;17:24:00;4.216;0.418;234.840;18.400;0.000;1.000;17.000
    """
    result = re.search(r'^(?P<date>\d+\/\d+\/\d+)(?P<etc>.*)$', line)
    if result:
        return "{}{}".format(reform_date(result.group("date")), result.group("etc"))
    else:
        raise ReformException("想定されたフォーマットの日付データの抽出に失敗しました。(入力={})".format(line))

def reform_file(filename="household_power_consumption.txt", skip_head=True):
    """
    ファイル中の日付のフォーマットをMySQLで読める様に変更する。
    先頭の行がカラム名の場合はskip_headをTrueにしてください。
    """
    is_head = True
    with open("reformed_{}".format(filename), "w", encoding="utf-8", newline="\n") as fout:
        with open(f"{filename}", "r", encoding="utf-8", newline="\r\n") as fin:
            for line in fin:
                if is_head and skip_head:
                    fout.write(line)
                    is_head = False
                    continue
                else:
                    fout.write(reform_line(line) + '\n')


if __name__ == "__main__":
    try:
        reform_file()
    except ReformException as err:
        print(err)
    except Exception as err:
        print(err)