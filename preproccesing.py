import pandas as pd
import os
import argparse
from tkinter import filedialog

"""
NOTE: Since Yahoo Finance no longer allows free downloads,
   this script focuses only on preprocessing. The data will be obtained from Nasdaq.com.

   
"""
#---------------------------------------- Preprocessing code ---------------------------------------#
class Preprocessing:
    def __init__(self,
                 args: argparse.Namespace) -> None:
        self.args = args
        self.revert_order = self.args.revert_order
        self.convert_to_float = self.args.convert_to_float
        self.move_col = self.args.move_col
        self.output_path = self.args.output_path
        self.verbose = args.verbose

#---------------------------------------- Open Dataset ---------------------------------------#                 
    def open_csv(self) -> pd.DataFrame: 
        """
        because we are using datasets from Nasdaq.com,
        this function is not only for opening the input dataset but for
        filtering $ usd simbols in the columns with price, and also
        for renaming the column "Close/Last" as "Adj Close".
        """
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        
        if not file_path:
            raise SystemExit(f"\n---> open_csv Error 1: csv file of not loaded, try again!")
        else:
            file = os.path.basename(file_path)
            print(f"\ncvs file: {file} loaded successfully!")
        
        # ** get the name of the file which assuming is the name of the stock, to rename the proccessed dataset.
        if file:
            self.filename = os.path.splitext(file)[0]
            print(f"\nfile name: {self.filename} | assuming is the name of the stock, to rename the proccessed dataset. ")
            
        df = pd.read_csv(file_path)
        df.rename(columns={"Close/Last": "Adj Close"}, inplace=True)

        price_columns = ["Adj Close", "Open", "High", "Low"]  # Lists of columns with "$"
        for col in price_columns:
            df[col] = df[col].astype(str).str.replace("$", "", regex=False).astype(float)

        if "Volume" in df.columns and self.convert_to_float: # this is the only col as int64 type, to avoid future warnings and problems should be converted.
            df["Volume"] = df["Volume"].astype("float64")
            print('*' * 50)
            print(f"\n---> ✅ Column Volume was coverted to float64 to avoid future problems and warnings.\n")
            print('*' * 50)

        # Sort the dataset by date in ascending order (oldest first, newest last)
        if "Date" in df.columns and self.revert_order:
            df["Date"] = pd.to_datetime(df["Date"])  
            df = df.sort_values(by="Date", ascending=True)  
            df["Date"] = df["Date"].dt.strftime("%Y-%m-%d") 
            print('*' * 50)
            print(f"\n---> ✅ the date order in the dataset was reverted in ascending order.\n")
            print('*' * 50)

        # move "Adj Close" to the end of the columns. 
        if "Adj Close" in df.columns and self.move_col:
            df = self.move_col_to_end(df)

        if self.verbose:
            print(f"\n{'=' * 90}")
            print(f'\n1).open_csv | input data visualization:\n\n{df.head(10)}') 
        
        csv_output_path = os.path.join(self.output_path, f"{self.filename}_proccessed.csv")
        df.to_csv(csv_output_path, index=True)
        print(f"\n---> ✅ 📊 test dataset saved successfully in the output folder!")

    def move_col_to_end(self,
                        df: pd.DataFrame,
                        col_name: str = 'Adj Close'):
        
        cols = [col for col in df.columns if col != col_name] + [col_name]  
        print('*' * 50)
        print(f"\n---> Column: {col_name} was moved at the final column of the dataset.\n")
        print('*' * 50)
        return df[cols]
    
#---------------------------------------- main ---------------------------------------#
    def main(self):
        self.open_csv()
    
if __name__ =='__main__':
    
    # ** Hyperparameters **#
    def args():
        parser = argparse.ArgumentParser()

        #** Verbose. **#
        parser.add_argument('--verbose', type=int, default=2,
                            help="""Visualize functions results depending on the number,
                            True means that the verbose in that function will be visualize if verbose is not None.

                            verbose = None ---> No prints for visualization in the terminal.
                            verbose = 1 ---> open_csv | visualize the opened dataset.
                            """)
        
        #** Windows and technical and others. **#
        # NOTE : if revert_order is True, Sort the dataset by date in ascending order,
        #        in other words the oldest date will be the first row in the dataset.
        parser.add_argument('--revert_order', type=bool, default=True, help='revert the date order in the dataset rows.')
        parser.add_argument('--convert_to_float', type=bool, default=True, help='convert volume column from int64 to float64 type.')
        parser.add_argument('--move_col', type=bool, default=True, help='move "Adj Close" column to the end.')
        
        parser.add_argument('--output_path', type=str, 
                             default= './output/', 
                             help='Save dataset path')
        
        args = parser.parse_args([])
        return args 
    
    pre_args = args() 
    pre = Preprocessing(pre_args)
    pre.main()
