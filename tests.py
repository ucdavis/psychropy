from psychropy import psych
import pandas as pd
import timeit

test_data = pd.read_csv('test_data.csv')
Tdb = test_data['Dry Bulb']
Twb = test_data['Wet Bulb']
Tdp = test_data['Dew Point']
air_pressure = 14.7

def test_twb():
    psych(air_pressure,'Tdb',Tdb,'DP',Tdp,'Twb','Imp')


if __name__ == '__main__':

    secs=timeit.timeit("test_twb()", setup="from __main__ import test_twb",number=100)
    print("100 tests getting wet bulb from a dataframe 8760 rows long took {} seconds:".format(secs))

    Twb_test = psych(air_pressure,'Tdb',Tdb,'DP',Tdp,'Twb','Imp')
    max_error = (Twb-Twb_test).max()
    print("Max difference between test data and psych is {} degrees".format(max_error))




