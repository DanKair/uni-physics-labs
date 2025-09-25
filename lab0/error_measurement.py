# 1. Get the left and right measurement
# 2. Get their arithmetic mean
    # 0. Use a loop to get user input 10 times
    # 1) Get their sum, by storing each x1, x2 values in some array
    # 2)
# 3. Get the distance (right - left)
# 4. Arithmetic mean - distance
# 5. Square of difference of arithmetic mean and distance
# 6. Sum of step 5
# 7. Standard deviation = Root of step 6 / n(n-1)
import math

def get_arithmetic_mean(lst: list, n: int):
    return (sum(lst) / n)


def get_delta_x_values(distance_list: list, mean_value) -> list:
    delta_x = []
    for distance_value in distance_list:
        delta_x.append(mean_value - distance_value)
    print(f"Delta x values = {delta_x}")
    return delta_x


def get_standard_deviation(delta_x_list: list, n: int):
    # 1. square of each number
    # 2. get the sum of squared list
    # 3. square root of (squared list / n(n-1))
    squared_delta_x = [x**2 for x in delta_x_list]
    sum_of_delta_x = sum(squared_delta_x)
    print(f"Sum of {squared_delta_x} = {sum_of_delta_x}")
    print(f"{sum_of_delta_x}/{(n*(n-1))}")
    return math.sqrt(sum_of_delta_x / n * (n-1))


def get_absolute_error(standard_deviation_value: float):
    STUDENT_COEFFICENT = 1.83
    return standard_deviation_value * STUDENT_COEFFICENT


def get_relative_error(absolute_error, mean_value):
    return (absolute_error/abs(mean_value) * 100)

def print_final_result(mean_value, abs_error):
    print(f"x = {mean_value} +/- {abs_error}")


# Main part of program starts here:
def main():
    # Number of measurements user wanna make (number of loop iteration)
    n: int = int(input("Enter the number of measurements: "))
    distance_list = []
    left_values = right_values = []

    for i in range(n):
        x1 = float(input("Enter the number for left value: "))
        x2 = float(input("Enter the number for right value: "))
        left_values.append(x1)
        right_values.append(x2)
        distance = x2 - x1
        distance_list.append(distance)

    print(distance_list)
    x_mean = get_arithmetic_mean(distance_list, n)
    print(f"Arithmetic mean = {x_mean}")
    delta_x_values = get_delta_x_values(distance_list, x_mean)
    standard_deviation = get_standard_deviation(delta_x_values, n)
    print(f"Standard Deviation value: {standard_deviation}")
    absolute_error = get_absolute_error(standard_deviation)
    print(f"Absolute Error value: {absolute_error}")
    relative_error = get_relative_error(absolute_error, x_mean)
    print(f"Relative error value: {relative_error}%")
    print_final_result(x_mean, absolute_error)

main()