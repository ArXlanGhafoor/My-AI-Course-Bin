import numpy as np

# As CSV has mixed types, so we extract columns seperately
latitude, longitude = np.genfromtxt(
    'CSV Files/fast_food_resturants.csv',
    delimiter=',',
    usecols=(4,5),
    unpack=True,
    dtype=float,
    skip_header=1,
    encoding='utf-8',
    invalid_raise=False
)

city, name = np.genfromtxt(
    'CSV Files/fast_food_resturants.csv',
    delimiter=',',
    usecols=(1,6),
    unpack=True,
    dtype=str,
    skip_header=1,
    encoding='utf-8',
    invalid_raise=False
)

# Manually split columns
print(city[:5])
print(latitude[:5])
print(longitude[:5])
print(name[:5])

#===== Data: Fast Food Restaurants (USA) =====#
print('\n#===== Data: Fast Food Restaurants (USA) =====#\n')

print(city)
print(latitude)
print(longitude)
print(name)

# change data type for safe handling
latitude = latitude.astype(float)
longitude = longitude.astype(float)

#====== Statistics on Latitude ======#

print('\n#===== Latitude Statistics =====#\n')

print(f'Mean latitude: {np.mean(latitude)}')
print(f'Median latitude: {np.median(latitude)}')
print(f'STD latitude: {np.std(latitude)}')
print(f'Percentile 25: {np.percentile(latitude, 25)}')
print(f'Percentile 50: {np.percentile(latitude, 50)}')
print(f'Min latitude: {np.min(latitude)}')
print(f'Max latitude: {np.max(latitude)}')

#====== Basic Arithmetic (Latitude vs Longitude) ======#

print('\n#===== Basic Arithmetic Operations =====#\n')

addition = latitude + longitude
subtraction = latitude - longitude
multiply = latitude * longitude
division = latitude / (longitude + 1e-9)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiply)
print("Division:", division)

#====== Mathematical Operations ======#

print('\n#===== Mathematical Operations =====#\n')

print("Square Latitude:", np.square(latitude))
print("Square Longitude:", np.square(longitude))
print("Sqrt Latitude:", np.sqrt(np.abs(latitude)))

#====== Trigonometric Functions ======#

print('\n#===== Trigonometric Functions =====#\n')

coord_pi = (latitude / np.pi) + 1

print("Sin:", np.sin(coord_pi))
print("Cos:", np.cos(coord_pi))
print("Tan:", np.tan(coord_pi))

#====== Logarithmic Operations ======#

print('\n#===== Logarithmic Operations =====#\n')

safe_lat = np.where(latitude > 0, latitude, 1)

print("Log:", np.log(safe_lat))
print("Log10:", np.log10(safe_lat))

#====== Hyperbolic Functions ======#

print('\n#===== Hyperbolic Functions =====#\n')

print("Sinh:", np.sinh(coord_pi))
print("Cosh:", np.cosh(coord_pi))
print("Tanh:", np.tanh(coord_pi))

#====== Numpy Array ======#

print('\n#===== Numpy Array =====#\n')

arr = np.array([latitude, longitude])

print("Shape:", arr.shape)
print("Size:", arr.size)
print("NDIM:", arr.ndim)
print("Dtype:", arr.dtype)

#====== Slicing ======#

print('\n#===== Slicing =====#\n')

print(arr[:, :2])
print(arr[:, 1:3])
print(arr[:, ::2])

#====== Indexing ======#

print('\n#===== Indexing =====#\n')

print(arr[0, 0])
print(arr[1, 1])

#====== Loop with index ======#

print('\n#===== Loop with index =====#\n')

for i in np.ndenumerate(arr):
    print(i)

#====== Loop without index ======#

print('\n#===== Loop without index =====#\n')

for i in np.nditer(arr):
    print(i)