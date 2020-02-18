# Python for real tasks

1. The coffee cooling task

    The coffee cooling problem was discussed by Jearl Walker
    in Scientific Amerian in 1977. Is become a standard example of modeling and
    simulation. He is short app of simulation in Python of a cooling cup of coffee.

        More: https://github.com/AllenDowney/ModSimPy
              http://greenteapress.com/ModSimPy/ModSimPy.pdf

![coolingCoffee.png](cooling_cup_of_coffee/coolingCoffee.png)


2. Pandas/Python Data Analysis of UN site of population data:
           reference: csv refference: https://population.un.org/wpp/Download/Standard/CSV/
   Following operations:
      * Pandas DataFrame by reading csv file
      * select DataFrame profile
      * Show DataFrame selected data with Matplotlib graph
      * save plot image to *.png file

3. TableFrame : Table data frame
    
    class MyTable(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self)
 |      Create pandas Data Frame class
 |  
 |  fields(self, df)
 |      get fields names
 |  
 |  info(self, df)
 |      gen Table info
 |  
 |  read(self, name=None)
 |      get DataFrame from csv file
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

4. UN_population - Python for Data Atalysis

![MDpopulation.png](UNpopulation/MDpopulation.png)

5. Create Pythob script googlesearch

    Run the script by using its filename
            $ ./g_search.py 
