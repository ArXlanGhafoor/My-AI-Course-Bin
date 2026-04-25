import numpy as np

price, bed, bath, acre_lot, zip_code, house_size = np.genfromtxt(
                                            'CSV Files/real_estate_data.csv',
                                            delimiter=',',
                                            usecols=(2,3,4,5,9,10),
                                            unpack=True,
                                            dtype=float,
                                            invalid_raise=False,
                                            skip_header=1,
                                            filling_values=np.nan
                                            )

 
#===== Data: Real Estate USA =====#
print('\n#===== Data: Real Estate USA =====#\n')

print(price)
print(bed)
print(bath)

#====== Data: Real Estate USA: Price - Statistics operations ======# 
print('\n#===== Data: Zameen.com: Price - Statistics operations =====#\n')
print(f'Mean of price: {np.mean(price)}')
print(f'Median of price: {np.median(price)}')
print(f'STD of price: {np.std(price)}')
print(f'Percentile 25 of price: {np.percentile(price, 25)}')
print(f'Percentile 50 of price: {np.percentile(price, 50)}')

#====== Data: Real Estate USA: Basic Arithematic Operations ======#
print('\n#===== Data: Zameen.com: Basic Arithematic Operations =====#\n')

addition = bed + bath
subtraction = bed - bath
multiply = bed * bath
division = bed / bath

print(f'addition of bed and bath: {addition}')
print(f'subtraction of bed and bath: {subtraction}')
print(f'multiplication of bed and bath: {multiply}')
print(f'division of bed and bath: {division}')

#====== Data: Real Estate USA: Basic Mathematics Operations ======#
print('\n#===== Data: Zameen.com: Basic Mathematics Operations =====#\n')

print("square of price: ", np.square(price))
print("sqrt of price: ", np.sqrt(price))
print("abs of price: ", np.abs(price))

#====== Trigonometric Functions ======#
print('\n#===== Trigonometric Functions =====#\n')

pricePie = (price / np.pi) + 1

#====== Sine, Cosine, and Tangent ======#
print('\n#===== Sine, Cosine, and Tangent =====#\n')

print(f'sine values of pricePie: {np.sin(pricePie)}')
print(f'cosine values of pricePie: {np.cos(pricePie)}')
print(f'tangent values of pricePie: {np.tan(pricePie)}')

#====== Natural Logarithm and Base-10 Logarithm ======#
print('\n#===== Natural Logarithm and Base-10 Logarithm =====#\n')

safe_price = np.where(price > 0, price, 1)

print(f'Natural logarithm values of pricePie: {np.log(pricePie)}')
print(f'Base-10 logarithm values of pricePie: {np.log10(pricePie)}')

#===== Hyperbolic & Inverse Hyperbolic =====#
print('\n#===== Hyperbolic & Inverse Hyperbolic =====#\n')

print(f'Hyperbolic Sine values of pricePie: {np.sinh(pricePie)}')
print(f'Hyperbolic Cosine values of pricePie: {np.cosh(pricePie)}')
print(f'Hyperbolic Tangent values of pricePie: {np.tanh(pricePie)}')
print(f'Inverse Hyperbolic Sine values of pricePie: {np.arcsinh(pricePie)}')

safe_acosh = np.where(pricePie >= 1, pricePie, 1)
print(f'Inverse Hyperbolic Cosine values of pricePie: {np.arccosh(safe_acosh)}')


#===== Numpy Array =====#
print('\n#===== Numpy Array =====#\n')

arr = np.array([bed, bath, acre_lot])

print(f'Shape of the Array: {arr.shape}')
print(f'Size of the Array: {arr.size}')
print(f'Number of Dimension of the Array: {arr.ndim}')
print(f'Data Type of the Array: {arr.dtype}')

# safe type conversion
changed_data_type = arr.astype(np.float32)
print(changed_data_type)

#===== Slicing =====#
print('\n#===== Slicing =====#\n')

print(arr[:2])
print(arr[1:])
print(arr[::2])

#===== Indexing =====#
print('\n#===== Indexing =====#\n')

print(arr[0])
print(arr[1])
print(arr[2])


#===== Loop with index number =====#
print('\n#===== Loop with index number =====#\n')

for i in np.ndenumerate(arr):
    print(i)

#===== Loop without index number =====#
print('\n#===== Loop without index number =====#\n')

for i in np.nditer(arr):
    print(i)