#coding=UTF-8
import random
import os
class InvestmentStrategy:
    def __init__(self, deposit):
        self._deposit = deposit


    def the_kelly_criterion_Investment(self):
        winning_probability = 0.8
        play_times = 20
        for invest_rate in range(1,10):
            invest_rate = invest_rate/10
            deposit_record = []
            for index, times in enumerate(range(0,play_times)):
                random_result = random.randint(1,10)
                if random_result <= winning_probability*10:
                    self._deposit = self._deposit + self._deposit * invest_rate
                    print("Win the investment, remaining deposit:" + str(self._deposit))
                    deposit_record.append(self._deposit)
                else:
                    self._deposit = self._deposit - self._deposit * invest_rate
                    print("lose the investment, remaining deposit:" + str(self._deposit))
                    deposit_record.append(self._deposit)

            #write result to txt from deposit_record
            if os.path.exists("./the_kelly_criterion_Investment")==False:os.mkdir("./the_kelly_criterion_Investment")
            with open("./the_kelly_criterion_Investment/the_kelly_criterion_Investment_"+str(invest_rate)+".txt", 'w+', encoding='utf-8') as f:
                f.writelines('\n'.join(str(line) for line in deposit_record))

        #displaying graphic from the_kelly_criterion_Investment



if __name__ == "__main__":
    qs = InvestmentStrategy(deposit = 100)
    qs.the_kelly_criterion_Investment()


