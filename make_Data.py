import pandas as pd
from pandas.core.frame import DataFrame

data = pd.read_csv('ko_office_dialog_data.txt',delimiter='\t',header = None)

column_name = ['type','text']

data = data.values.tolist()

data = pd.DataFrame(data, columns=column_name)

data_1 = data[data['type'] ==1].reset_index()

data_2 = data[data['type'] ==2].reset_index()

new_data = pd.concat([data_1, data_2], axis=1)

new_data = new_data.drop('index', axis=1)

new_data = new_data.drop('type', axis=1)

new_column_name = ['Q','A']

new_data = new_data.values.tolist()

new_data = pd.DataFrame(new_data, columns=new_column_name)

list = [0 for i in range(1325)]

list_df = pd.DataFrame(list)

final_data = pd.concat([new_data, list_df], axis=1)

final_column_name = ['Q','A','label']

final_data = final_data.values.tolist()

final_data = pd.DataFrame(final_data, columns=final_column_name)

print(final_data)

# final_data.to_csv('new_ko_office_dialog_data.csv', index=False)

final_data.to_csv('new_ko_office_dialog_data.txt',index=False, sep = '\t')