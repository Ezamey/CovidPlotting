#! E:\3.6_envs\3.6_datascience\Scripts\python.exe
#covcompare.py  : my noobish comparaison script using matplot/pandas
import sys
import matplotlib.pyplot as plt
from covid19process import data as frames
from covsharing import naming,y_ticks


def evo(a_list_of_data_set):

    fig,ax = plt.subplots(nrows=len(a_list_of_data_set),squeeze=False,sharex=True, figsize=(19.20,10.80))

    plot = 0
    for i in range(len(a_list_of_data_set)):
        dset_keys = a_list_of_data_set[i].keys()
        ax[plot,0].plot(a_list_of_data_set[i][dset_keys[0]],color="b",label ="Cases")
        ax[plot,0].plot(a_list_of_data_set[i][dset_keys[1]],color="g",label="Recovery")
        ax[plot,0].plot(a_list_of_data_set[i][dset_keys[2]],color="r",label="Deaths")
        ax[plot,0].set_ylabel(f'\n{a_list_of_data_set[i].columns[0].split("_")[0]}\n\n',fontsize='large', 
                                                                     fontweight='bold')
        ax[plot,0].set_xticks([x for x in frames[1][::15]])
        ax[plot,0].set_yticks(y_ticks(a_list_of_data_set[i]))
        ax[plot,0].grid()
        plot +=1
    plot = 0

    ax[plot,0].legend(loc='upper center', shadow=True, fontsize='x-large')
    ax[plot,0].annotate("WHO announces COVID-19 outbreak a pandemic (2020-3-11)",xy=("2020-3-11",0),xytext=(0.5, 0.5), 
                        textcoords='axes fraction',
                        arrowprops=dict(facecolor='black', shrink=0.05))
    ax[plot,0].set_title("Evolution du Covid19 (2020/1/22 - 2020/5/27)\n")
 
    file_name = (naming(a_list_of_data_set))
    plt.savefig(file_name, dpi=1200)
    plt.show()
    
list_compare = []
for stuff in sys.argv[1:]:
    list_compare.append(frames[0][stuff])
evo(list_compare)

if __name__ == "__main__":
    '''
    print(frames[0].keys())
    '''
    print("In cov19compare.py")

