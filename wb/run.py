from wb import create_app

app = create_app()
import sqlite3

def add_column(database_name, table_name, column_name, data_type):

  connection = sqlite3.connect(database_name)
  cursor = connection.cursor()


  base_command = ("ALTER TABLE user ADD COLUMN is_master BOOLEAN")
  # sql_command = base_command.format(table_name=tab, column_name=column_name, data_type="DATETIME")

  cursor.execute(base_command)
  connection.commit()
  connection.close()
#
# add_column('site.db', 'user', 'date', 'DateTime')
if __name__== '__main__':

  app.run(host="0.0.0.0", debug=True)




