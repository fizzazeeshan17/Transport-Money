# The one where money need to be transported

# Language: Python

# Description:

A local bank office often transports bags of money to and from their main office. They have asked me to develop a script that can help them know beforehand how many bags will fit in the truck transporting the money, and what the value of all the bags combined is.

The size of the truck transporting the money bags can vary in size from transport to transport so the size must be read from the user each time running the script. If the user enters a volume less than 100L they shall be asked again until they give a volume larger than 100L.

After having read the size of the truck, the script shall calculate how many money bags of each size fits in the specified truck and display it.
 
There is a strict requirement that the number of bags of each type shall be calculated using three loops, one for finding out how many big bags can fit, one for how many medium bags can fit in the remaining space, and finally, one for calculating how many small bags fit after having stored as many big and medium bags as possible.

Having decided how many bags can be transported it is time to calculate how much the shipment is worth and display this information to the user. A small bag is worth 10.000kr, a medium bag 30.000kr, and a big bag is worth 60.000kr.
