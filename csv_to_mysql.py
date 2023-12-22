"""
csv_to_mysql - 从csv读取数据，保存到mysql中

Author: hanayo
Date： 2023/12/22
"""

from config import user_name, user_pwd, host_inner, port_inner, db_name, tb_name
import pandas as pd
from sqlalchemy import text, create_engine
import time

db_columns = ['pos_year', 'pos_month', 'pos_week_char', 'pos_sche', 'pos_week_num', 'pos_brand_cn',
              'pos_brand_en', 'pos_category_id', 'pos_category_desc', 'pos_dept_id', 'pos_dept_desc', 'pos_class_id',
              'pos_class_desc', 'pos_supplier_id', 'pos_supplier_desc', 'pos_item_code', 'pos_item_desc',
              'pos_bar_code', 'pos_is_seasonal', 'pos_is_pog', 'pos_region_cn', 'pos_mkt_cn', 'pos_province',
              'pos_city', 'pos_sales_store_id', 'pos_sales_store_name', 'pos_online_flg', 'pos_order_store_id',
              'pos_order_store_name', 'pos_deliver_store_id', 'pos_deliver_store_name', 'pos_sales_quantity',
              'pos_no_tax', 'pos_sales_amt_vat', 'pos_srp', 'pos_price', 'pos_price_amt', 'pos_channel_1',
              'pos_channel_2', 'pos_tier']


def con_tax(item):
    """
    处理tax那一列可能有的千位分隔符
    :param item:df数据要处理的那一列
    :return:返回处理后的列
    """
    if isinstance(item, str):
        if "," not in item:
            return int(item)
        s = ""
        tmp = item.strip("").split(",")
        for i in range(len(tmp)):
            s += tmp[i]
        return int(s)


class PosUpPD:

    def __init__(self, file):
        conn_info = f"mysql+pymysql://{user_name}:{user_pwd}@{host_inner}:{port_inner}/{db_name}?charset=utf8mb4"
        self.engine = create_engine(conn_info)
        # 读取csv，自定义df对象的列名,指定了跳过第一行
        self.csv_df = pd.read_csv(file, index_col=False, encoding='gbk', names=db_columns, thousands=",",
                                  low_memory=False, skiprows=[0])
        self.csv_df['pos_no_tax'] = self.csv_df['pos_no_tax'].map(con_tax)
        self.csv_df.to_sql(tb_name, self.engine, chunksize=10000, index=False,
                           if_exists='append')


if __name__ == '__main__':
    st_time = time.time()
    PosUpPD('resource/test2.csv')
    print(f"用时{(time.time() - st_time)/1000:.3f}秒")
