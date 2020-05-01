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

def test_rh():
    psych(air_pressure,'Tdb',Tdb,'DP',Tdp,'RH','Imp')

if __name__ == '__main__':
    number_of_tests=100

    secs=timeit.timeit("test_twb()", setup="from __main__ import test_twb",number=number_of_tests)/number_of_tests
    print("{} tests getting wet bulb from a dataframe 8760 rows long took an average of {} seconds:".format(number_of_tests,secs))

    Twb_test = psych(air_pressure,'Tdb',Tdb,'DP',Tdp,'Twb','Imp')
    max_error = abs(Twb-Twb_test).max()
    print("Max difference between test data Wet Bulb and psych is {} degrees".format(max_error))

    secs = timeit.timeit("test_rh()", setup="from __main__ import test_rh", number=number_of_tests)/number_of_tests
    print("{} tests getting RH from a dataframe 8760 rows long took an average of {} seconds:".format(number_of_tests,secs))




