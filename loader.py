import pandas as pd

def load_inputs(data_dir='data'):
    file_path = f"{data_dir}/Input File_MAY25.xlsx"
    
    month1 = pd.read_excel(file_path, sheet_name='No Data_Month 1')
    month2 = pd.read_excel(file_path, sheet_name='No Data_Month 2')
    malfunc = pd.read_excel(file_path, sheet_name='Malfunctions')
    providers = pd.read_excel(file_path, sheet_name='ASP List')
    
    return month1, month2, malfunc, providers
