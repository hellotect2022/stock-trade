import pandas as pd 

class PandasClass():

    def showDataFrame(self,data,filter=None):
        if filter is None:
            df = pd.DataFrame(data)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            print(df)
        else:
            df = pd.DataFrame(data)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            filtered_df = df[df[filter['column']] > filter['value']] if len(df) > 0 else df
            print(filtered_df)