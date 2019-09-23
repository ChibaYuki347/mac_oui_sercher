import csv
import json
import os

import numpy as np
import pandas as pd
from urllib import request


def main():
    # ファイルの存在の確認
    if os.path.exists('oui.csv'):
        df = pd.read_csv('oui.csv', encoding='UTF-8')

        # ベンダーコードと組織名を取得しリスト化.macアドレスを:区切りにする.
        assignment_company_list = df.loc[:, ['Assignment', 'Organization Name']].values.tolist()
        for mac_info in assignment_company_list:
            mac_info[0] = ':'.join(a + b for a, b in zip(mac_info[0][::2], mac_info[0][1::2]))

        # ヘッダーを追記してCSVに書き出し
        header = ['Assignment', 'Organization Name']
        with open('mac_org.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for data_row in assignment_company_list:
                print(data_row)
                writer.writerow(data_row)

        # Json形式にもしておく。
        with open('mac_org.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open('mac_org.json', 'w') as f:
            json.dump(rows, f)
    else:
        print('oui.csvをIEEEのサイトからダウンロードします。ダウンロードしてから再度実行してください。')
        url = "http://standards-oui.ieee.org/oui/oui.csv"
        filename = 'oui.csv'
        request.urlretrieve(url,filename)



if __name__ == '__main__':
    main()
