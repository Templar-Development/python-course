import numpy as np
import matplotlib.pyplot as plt

def install_numpy():
    try:
        import numpy as np
        print("NumPy is already installed.")
    except ImportError:
        import subprocess
        subprocess.check_call(['pip', 'install', 'numpy'])
        print("NumPy has been installed.")

def basic_array_operations():
    # Create arrays
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])

    addition_result = np.add(arr1, arr2)
    subtraction_result = np.subtract(arr1, arr2)
    multiplication_result = np.multiply(arr1, arr2)

    print("Array 1:")
    print(arr1)
    print("\nArray 2:")
    print(arr2)
    print("\nAddition Result:")
    print(addition_result)
    print("\nSubtraction Result:")
    print(subtraction_result)
    print("\nMultiplication Result:")
    print(multiplication_result)

def advanced_features():
    random_array = np.random.rand(3, 3)
    reshaped_array = random_array.reshape(1, 9)
    transposed_array = random_array.T

    print("\nRandom Array:")
    print(random_array)
    print("\nReshaped Array:")
    print(reshaped_array)
    print("\nTransposed Array:")
    print(transposed_array)

def bonus_data_visualization():
    # Generate data for visualization
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot the sine function
    plt.plot(x, y)
    plt.title('Sine Function')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.show()

def main():
    install_numpy()

    basic_array_operations()

    advanced_features()

    bonus_data_visualization()

if __name__ == "__main__":
    main()
