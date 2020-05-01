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
 
 ### Defs:  
 

 - **P** is the barometric pressure in PSI or Pa . 
 - **intypes** indicator string for the corresponding invalue parameter (ie Tdb, RH etc.)
 - **invalues** is the actual value associated with the type of parameter (ie value of Wet bulb, Dew point, RH, or Humidity Ratio etc.)
 - **outType** indicator string for the corresponding invalue parameter 
- **unittype** is the optional unit selector.  Imp for Imperial, SI for SI.
Imp is    default if omitted.    valid intypes:
- **Tdb** Dry Bulb Temp F or C Valid for Input *it is highly    Recommended Tdb be used    as an input (can only output/not use, if both other inputs are h and    HR)*  
- **Twb**    Web Bulb Temp            F or C        Valid for Input    
- **DP**     Dew point                F or C                   Valid for    input     
- **RH**     RH                       between 0 and 1             Valid for input     
- **W**      Humidity Ratio           Mass Water/ Mass    Dry    Air     Valid for input     
- **h**      Enthalpy                    BTU/lb dry    air or kJ/kg DA   Valid for input *Warning 0 state    for Imp is ~0F,    0% RH ,and  1 ATM, 0 state for SI is 0C, 0%RH and    1 ATM*

### valid outtypes:

 - **Tdb**    Dry Bulb Temp            F or C
 - **Twb**    Web Bulb Temp            F or C                       Valid for Input 
 - **DP**     Dew point                F or C                       Valid for input 
 - **RH**     Relative Humidity        between 0 and 1              Valid for input 
 - **W**      Humidity Ratio           Mass Water/ Mass Dry Air     Valid for input 
 - **h**      Enthalpy                 BTU/lb dry air or kJ/kg DA   Valid for input Warning 0 state for Imp is ~0F, 0% RH ,and  1 ATM, 0 state for SI is 0C, 0%RH and 1 ATM 
 - **WVP**    Water Vapor Pressure     PSI or Pa 
 - **Dsat**   Degree of Saturation     between 0 and 1 s      NOT VALID, Should be entropy 
 - **SV**     Specific Volume          ft^3/lbm or m^3/kg dry air 
 - **MAD**    Moist Air Density        lb/ft^3 or m^3/kg  
