import A1_kycheungav_20424915_code_relim as relim
import numpy as np
import timeit


class closed:
    def __init__(self):
        self.Freq = self.getFreq()
        self.Closed = None
        self.Max = None
    
    def getData(self):
        results = []
        with open('freq_items_datasets.txt','r') as inputfile:
            for line in inputfile:
                results.append(line.strip().split(' '))
        results_np = np.array([np.array(lines) for lines in results])
        return results_np
    
    
    def getFreq(self):
        item_mining = relim.freq_mining(self.getData(), 150, 0.5)
        return item_mining.freq_items()
    
    
    def filtering(self):
        self.Closed = self.Freq.copy()
        self.Max = self.Closed.copy()
        i = self.Freq
        j = self.Freq
        for set1, count1 in list(i.items()):
            for set2, count2 in list(j.items()):
                if set1 < set2:
                    self.Max.pop(set1, None)
                    if count1 <= count2:
                        self.Closed.pop(set1, None)
            
        
    #must run the closedPattern before running this function    
    def maxPattern(self):
        self.Max = self.Closed.copy()
        i = self.Closed
        j = self.Closed
        for set1, count1 in list(i.items()):
            for set2, count2 in list(j.items()):
                if set1 < set2:
                    self.Max.pop(set1, None)
        
        print(self.Max)
                    

if __name__ == "__main__":
    t_start  =  timeit.default_timer()
    pattern = closed()
    print("number of total frequent item set", len(pattern.Freq))
    pattern.filtering()
    print(pattern.Closed)
    print("number of closed frequent item set", len(pattern.Closed))
    print(pattern.Max)
    print("number of maximal frequent item set", len(pattern.Max))
    t_end  =   timeit.default_timer()

    cost  =  t_end -t_start
    print ( 'Time cost of funl is  %f' %cost)