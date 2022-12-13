from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


if __name__=="__main__":
    carpur_data=pd.read_csv("../../afl_fuzz_out/readelf_plot_data.csv",parse_dates=["unix_time"] )
    former_time=int(carpur_data.loc[0]['unix_time'])-60
    first_time=former_time

    # 清洗数据，将两个相邻的数据之间的时间差值设位60s
    for x in carpur_data.index:
        if  int(carpur_data.loc[x, "unix_time"]) - int(former_time) < 60 :
            carpur_data.drop(x, inplace=True)
        else:
            former_time = carpur_data.loc[x,"unix_time"]
            carpur_data.loc[x, "unix_time"] = datetime.fromtimestamp(int(carpur_data.loc[x,"unix_time"]))

    carpur_data.plot(x="unix_time")

    plt.show()



