from time import gmtime,strftime,time

def naming(data_set):
        #The file name
        #a time based id
    time_id = time()
    if not isinstance(data_set,list):
        #Based on the first letter of the plotted country
        test = list(data_set.columns)#index to list
        country_first_letter = [test[0] for test in data_set]
    else:
        country_first_letter = [letter.keys()[1][0] for letter in data_set]
        #we join
    file_name = "Plot"+str(time_id)[::-3]+"".join(country_first_letter)+'.pdf'
    return file_name

def y_ticks(a_dataset):
    #building yticks
    rates = []
    all_cases = a_dataset[a_dataset.columns[0]].iloc[-1]
    if all_cases > 500_000:
        rates = [x*(all_cases/10) for x in range(20) ]
    if all_cases > 250_000:
        rates = [x*(all_cases/10) for x in range(15) ]
    if all_cases > 100_000:
        rates = [x*(all_cases/10) for x in range(10) ]
    if all_cases > 50_000:
        rates = [x*(all_cases/10) for x in range(10) ]
    else:
        rates = [x*(all_cases/10) for x in range(8) ]
    return rates