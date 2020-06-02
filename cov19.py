#! E:\3.6_envs\3.6_datascience\Scripts\python.exe
#cov19.py  : my noobish script using matplot/pandas
import sys
import matplotlib.pyplot as plt
from covid19process import data as frames
from covsharing import y_ticks,naming

def evo(a_dataset):
    fig,ax = plt.subplots()
    ax.plot(a_dataset[a_dataset.columns[0]],color="b",label ="Cases")
    ax.plot(a_dataset[a_dataset.columns[1]],color="g",label="Recovery")
    ax.plot(a_dataset[a_dataset.columns[2]],color="r",label="Deaths")

    title = a_dataset.columns[0].split("_")[0]

    ax.set_title(f'{title} Covid-19 evolutions\n')
    ax.set_ylabel("Nombre d'individus \n")

    ax.annotate("WHO announces COVID-19 outbreak a pandemic (2020-3-11)",xy=("2020-3-11",580),
                arrowprops=dict(facecolor='black', shrink=0.05))

    plt.xticks([x for x in frames[1][::15]])
    #y_ticks
    rates = y_ticks(a_dataset)
    plt.yticks(rates)

    plt.grid()
    legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    file_name = (naming(a_dataset))
    plt.savefig(file_name, dpi=1200)
    plt.show()


#For command line Arguments:

to_plot= sys.argv[1]
if to_plot in frames[0].keys():
    evo(frames[0][to_plot])
    sys.exit()



if __name__ == "__main__":
    print("In cov19.py")
    france = frames[0]["France"]
    #graph for France
    evo(france)
    #sys.exit()