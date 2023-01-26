import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    #  Read the csv file
    filename = input("Enter the filename:  ")
    df1 = pd.read_csv(filename)

    #  Build a Dataframe with data for one method
    method_name = input("Enter method name:  ")
    one_method = df1[df1['METHOD'] == method_name]

    #  Sort the data by call time, need logic to sort times correctly
    one_method_sorted = one_method.sort_values(by=['CALL TIME'], ascending=True)

    #  Plot the data
    fig, ax = plt.subplots()
    ax.plot(one_method_sorted['CALL TIME'], one_method['RUNTIME'])
    plt.show()
