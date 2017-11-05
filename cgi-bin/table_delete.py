#!/home/mrdiz/anaconda3/bin/python

import sys
sys.path.append("/home/mrdiz/SQL/Lab5(2)")

from utils.site_manager import Manager
import utils.site_template as template

selected_table = Manager.cookie["table"].value

data_list = Manager.sql_select('*', selected_table)

data_list = template.reformat_list(data_list)
options_list = template.build_option_list(data_list)

content = """
<h2>Удалить данные из таблицы {0}</h2>
<p><a href='table.py'>Назад</a></p>
<p>Выберете строку для удаления</p>

<form action='table_delete_form.py' method='post'>
    <select name='row_delete' id='row_delete' size='10'>
    {1}
    </select>
    <br>
    <input type='submit' value='Удалить'>
</form>
""".format(selected_table, options_list)

template.build_with_content(content)
