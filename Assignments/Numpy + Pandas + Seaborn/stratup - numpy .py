import numpy as np

company, valuation, country, city, industry = np.genfromtxt(
                                            'CSV Files/startups.csv',
                                            delimiter=',',
                                            usecols=(1,2,4,5,6),
                                            unpack=True,
                                            dtype=None,
                                            encoding='utf-8',
                                            invalid_raise=False,
                                            skip_header=1,
                                            filling_values=''
                                            )

 
#===== Data: Global Unicorn Startups =====#
print('\n#===== Data: Global Unicorn Startups =====#\n')

print(company)
print(valuation)
print(country)
print(industry)

#Our valuation has $ and text like. So we must convert it to float:
valuation = np.char.replace(valuation, '$', '')
valuation = valuation.astype(float)

#====== Statistics on Valuation ======#

print('\n#===== Valuation Statistics =====#\n')

print(f'Mean valuation: {np.mean(valuation)}')
print(f'Median valuation: {np.median(valuation)}')
print(f'STD valuation: {np.std(valuation)}')
print(f'Percentile 25: {np.percentile(valuation, 25)}')
print(f'Percentile 50: {np.percentile(valuation, 50)}')
print(f'Min valuation: {np.min(valuation)}')
print(f'Max valuation: {np.max(valuation)}')

#====== Basic Arithmetic (Valuation vs index) ======#

index = np.arange(len(valuation))

addition = valuation + index
subtraction = valuation - index
multiply = valuation * index
division = valuation / (index + 1)

print('\n#===== Arithmetic Operations =====#\n')
print(addition)
print(subtraction)
print(multiply)
print(division)

#====== Mathematical Operations ======#

print('\n#===== Mathematical Operations =====#\n')

print("Square:", np.square(valuation))
print("Square Root:", np.sqrt(valuation))
print("Absolute:", np.abs(valuation))

#====== Trigonometric Functions ======#

print('\n#===== Trigonometric Functions =====#\n')

val_pi = (valuation / np.pi) + 1

print("Sin:", np.sin(val_pi))
print("Cos:", np.cos(val_pi))
print("Tan:", np.tan(val_pi))

#====== Logarithmic Operations ======#

print('\n#===== Logarithmic Operations =====#\n')

safe_val = np.where(valuation > 0, valuation, 1)

print("Log:", np.log(safe_val))
print("Log10:", np.log10(safe_val))

#====== Hyperbolic Functions ======#

print('\n#===== Hyperbolic Functions =====#\n')

print("Sinh:", np.sinh(val_pi))
print("Cosh:", np.cosh(val_pi))
print("Tanh:", np.tanh(val_pi))

#====== 2D Array ======#

print('\n#===== Numpy Array =====#\n')

arr = np.array([valuation, index])

print(f'Shape: {arr.shape}')
print(f'Size: {arr.size}')
print(f'NDIM: {arr.ndim}')
print(f'Dtype: {arr.dtype}')

#====== Slicing ======#

print('\n#===== Slicing =====#\n')

print(arr[:, :3])
print(arr[:, 2:5])
print(arr[:, ::2])

#====== Indexing ======#

print('\n#===== Indexing =====#\n')

print(arr[0, 1])
print(arr[1, 2])

#====== Loop with index ======#

print('\n#===== Loop with index =====#\n')

for i in np.ndenumerate(arr):
    print(i)

#====== Loop without index ======#

print('\n#===== Loop without index =====#\n')

for i in np.nditer(arr):
    print(i)


    