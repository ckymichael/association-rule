from pymining import itemmining, assocrules
import timeit
import numpy as np

class freq_mining(object):
    """docstring for ClassName"""
    def __init__(self, transactions, min_sup, min_conf):
        
        self.transactions = transactions  # database
        self.min_sup = min_sup  # minimum support
        self.min_conf = min_conf  # minimum support

    def freq_items(self):

        relim_input = itemmining.get_relim_input(self.transactions)
        item_sets = itemmining.relim(relim_input, self.min_sup)
        return item_sets

    def association_rules(self):

        item_sets = self.freq_items()
        rules = assocrules.mine_assoc_rules(item_sets, self.min_sup, self.min_conf)
        return rules

def main(transactions, min_sup, min_conf):

    item_mining = freq_mining(transactions, min_sup, min_conf)
    freq_items = item_mining.freq_items()
    #rules = item_mining.association_rules()
    rules = assocrules.mine_assoc_rules(freq_items, item_mining.min_sup, item_mining.min_conf)

    print(freq_items)
    #print(rules)
    

def getData():
    results = []
    with open('freq_items_datasets.txt','r') as inputfile:
        for line in inputfile:
            results.append(line.strip().split(' '))
    results_np = np.array([np.array(lines) for lines in results])
    return results_np


if __name__ == "__main__":
    
    t_start  =  timeit.default_timer()
    
    transactions = getData()

    min_sup = 150
    min_conf = 0.5

    main(transactions, min_sup, min_conf)
    t_end  =   timeit.default_timer()

    cost  =  t_end -t_start
    print ( 'Time cost of funl is  %f' %cost)   