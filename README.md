# psychropy
psychrometric functions for moist air
This is a translated version of the visual basic psych function in our xls template to a python code function psychropy()

The function and subfunctions defined herein come with no warranty or certification of fitness for any purpose.

Do not use these functions for conditions outside boundaries defined by their original sources.  

Subfunctions use equations from the following sources: ASHRAE Fundamentals, 2005, SI Edition Singh et al. "Numerical Calculations of Psychrometric Properties on a Calculator". Building and Environment, 37, 2002. The function will calculate various properties of moist air. Properties calculated include Wet Bulb, Dew Point, relative Humidity, Humidity Ratio, Vapor Pressure, Degree of Saturation, enthalpy, specific volume of dry air, and moist air density.

The function requires input of: barometric pressure, and two other parameters, We recommend that one of these be Tdb and if not using that the other two must be h and HR.  These parameters along with Tdb can be Twb, DP, RH, or two mentioned previously.  

Sytax for function as follows:  

    psych(P,intype0,invalue0,intype1,invalue1,outtype,unittype)  
 
 Example:
 get enthalpy at 1 atm, 72.1 F dry bulb, 70% humidity in ~~imperial~~ freedom units
```python
from psychropy import psych
psych(14.7,'Tdb',72.1,'RH',.7,'h')
>>>30.19351939930006
```

**_Inputs can also be pandas dataframes, pandas series, or numpy arrays._**
 
 ### Available Inputs and Outputs
 | Parameter | Descriptions | Units| Data Type|
 |---------|--------------|------|----------|
 |**P** | Barometric Pressure | PSI or Pa| Float, numpy arrays, pandas DataFrame or Series |
 |**intype**| Indicator string for the corresponding values (i.e. invalue)| - | String|
 |**invalue**| Value for the corresponding indicator string | - | String|
 |**outtype**| Indicator string for the desired output| - | String|
 |**unittype**| Option unit selector, default is Imp. Imp for imperial and SI for standard. | - | String|
 
 #### Valid intypes
 |In Type | Description | Units| Notes | 
 |---------|--------------|:------:|--------|
 |**Tdb**| Dry Bulb Temperature | F or C | Required unless inputs are enthalpy and humidity ratio| 
 |**Twb**| Wet Bulb Temperature | F or C | -|
 |**DP**| Dew Point Temperature | F or C | -|
 |**RH**| Relative Humidity | - | Must fall between 0.0 - 1.0|
 |**W**| Humidity Ratio | Mass Water / Mass Dry Air | -|
 |**h**| Enthalpy | BTU / lb dry air or kJ / kg dry air|*Warning h = 0 state different for Imperial and SI.* <br>Imperial: ~0F, 0% RH , and 1 atm. <br>SI: 0C, 0%RH and 1 ATM |
  
#### valid outtypes:
|Out Type | Description | Units| Notes | 
 |---------|--------------|:------:|--------|
 |**Tdb**| Dry Bulb Temperature | F or C | Requires inputs to be enthalpy and humidity ratio| 
 |**Twb**| Wet Bulb Temperature | F or C | -|
 |**DP**| Dew Point Temperature | F or C | -|
 |**RH**| Relative Humidity | - | Must fall between 0.0 - 1.0|
 |**W**| Humidity Ratio | Mass Water / Mass Dry Air | -|
 |**h**| Enthalpy | BTU / lb dry air or kJ / kg dry air|*Warning h = 0 state different for Imperial and SI.* <br>Imperial: ~0F, 0% RH , and 1 atm. <br>SI: 0C, 0%RH and 1 ATM |
 |**WVP**| Water Vapor Pressure  | PSI or Pa|-|
 |**Dsat**| Degree of Saturation | 0-1|-|
 |**SV**| Specific Volume | ft^3/lbm dry air or m^3/kg dry air |-|
 |**MAD**| Moist Air Density | lbm moist air / ft^3 or kg moist air / m^3 |-|
 

