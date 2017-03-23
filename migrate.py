import os
import re

from lib.db import DB

root_path = os.path.realpath(os.path.dirname(__file__))

file_path = os.path.join(root_path, 'data', 'cnarea20160320-2.sql')

# f = open(file_path, 'rb')
# line.decode()
f = open(file_path, 'r', encoding='utf8')
for line in f:
    if line:
        column = line.replace('\n', '')
        column = re.sub('([^,"\d]+),([^,"]+)', '\\1|\\2', column)
        column = re.sub('([^,"\d]+),([^,"]+)', '\\1|\\2', column)
        column = re.sub('([^,"\d]+),([^,"]+)', '\\1|\\2', column)
        column = column.replace('"', '').split(',')
        if column:
            sql = 'INSERT INTO `china_area`(`id`, `parent_id`, `level`, `area_code`, `zip_code`, `city_code`, `name`, `short_name`, `merger_name`, `pinyin`, `longitude`, `latitude`) ' \
                  'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            DB.connect().execute(sql, tuple(column))
        else:
            print('ignored:' + line)
f.close()

