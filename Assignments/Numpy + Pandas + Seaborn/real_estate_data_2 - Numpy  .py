import numpy as np
assessed_value, sale_amount  = np.genfromtxt('CSV Files/real_estate_data_2.csv', 
                                            delimiter=',',
                                            usecols= (5,6),
                                            unpack=True,
                                            dtype=None,
                                            invalid_raise=False,
                                            skip_header=1,
                                            filling_values='' 
                                            )

 
#===== Data: Real Estate USA =====#
print('\n#===== Data: Real Estate USA =====#\n')

# print(year)
# print(address)
print(assessed_value)
print(sale_amount)
# print(property_type)

#====== Data: Real Estate USA: Sales Amount - Statistics operations ======# 
print('\n#===== Data: Real Estate USA: Sales Amount - Statistics operations =====#\n')
print(f'Mean of sale_amount: {np.mean(sale_amount)}')
print(f'Median of sale_amount: {np.median(sale_amount)}')
print(f'STD of sale_amount: {np.std(sale_amount)}')
print(f'Percentile 25 of sale_amount: {np.percentile(sale_amount, 25)}')
print(f'Percentile 50 of sale_amount: {np.percentile(sale_amount, 50)}')

#====== Data: Real Estate USA: Basic Arithematic Operations ======#
print('\n#===== Data: Real Estate USA: Basic Arithematic Operations =====#\n')
addition = sale_amount + assessed_value
subtraction = sale_amount - assessed_value
multiply = sale_amount * assessed_value
diviion = sale_amount / assessed_value

print(f'addition of sale_amount and assessed_value: {addition}')
print(f'subtraction of sale_amount and assessed_value: {subtraction}')
print(f'multiple sale_amount and assessed_value: {multiply}')
print(f'diviion of sale_amount and assessed_value: {diviion}')

#====== Data: Real Estate USA: Basic Mathematics Operations ======#
print('\n#===== Data: Real Estate USA: Basic Mathematics Operations =====#\n')
print("square of sale_amount: " , np.square(sale_amount))
print("sqrt of sale_amount: " , np.sqrt(sale_amount))
print("abs of sale_amount: " , np.abs(sale_amount))

#====== Trigonometric Functions ======#
print('\n#===== Trigonometric Functions =====#\n')
pricePie = (assessed_value/np.pi) +1

#====== Sine, Cosine, and Tangent ======#
print('\n#===== Sine, Cosine, and Tangent =====#\n')
print(f'sine vales of pricePie: {np.sin(pricePie)}')
print(f'cosine vales of pricePie: {np.cos(pricePie)}')
print(f'tanget vales of pricePie: {np.tan(pricePie)}')

#====== Natural Logarithm and Base-10 Logarithm ======#
print('\n#===== Natural Logarithm and Base-10 Logarithm =====#\n')
print(f'Natural logarithm values of pricePie: {np.log(pricePie)}')
print(f'Base-10 logarithm values of pricePie: {np.log10(pricePie)}')


#===== Hyperbolic & Inverse Hypebolic =====#
print('\n#===== Hyperbolic & Inverse Hypebolic =====#\n')
print(f'Hyperbolic Sine values of pricePie: {np.sinh(pricePie)}')
print(f'Hyperbolic Sine values of pricePie: {np.cosh(pricePie)}')
print(f'Hyperbolic Sine values of pricePie: {np.tanh(pricePie)}')
print(f'Inverse Hyperbolic Sine values of pricePie: {np.arcsinh(pricePie)}')
print(f'Inverse Hyperbolic Sine values of pricePie: {np.arccosh(pricePie)}')


#===== Numpy Array =====#
print('\n#===== Numpy Array =====#\n')
arr = np.array([sale_amount, assessed_value])
print(f' Shape of the Array: {arr.shape}')
print(f' Size of the Array: {arr.size}')
print(f' Number of Dimention of the Array: {arr.ndim}')
print(f' Data Type of the Array: {arr.dtype}')

chang_data_type  = np.astype(arr, np.float32)
print(chang_data_type)

#===== Slicing =====#
print('\n#===== Slicing =====#\n')
print(arr[:3, :3])
print(arr[2:4, :])
print(arr[2:5:2, 1::2])
print(arr[::3, ::2])

#===== Indexing =====#
print('\n#===== Indexing =====#\n')

print(arr[1,3])
print(arr[0,2])
print(arr[1,1])


#===== Loop with index number =====#
print('\n#===== Loop with index number =====#\n')
for i in np.ndenumerate(arr):
    print(i)

#===== Loop without index number =====#
print('\n#===== Loop without index number =====#\n')
for i in np.nditer(arr):
    print(i)

