"""
Given an integer denoting a total number of wheels, help Amazon Logistics find the number of different ways to choose a
fleet of vehicles from an infinite supply of two-wheeled and four-wheeled vehicles such that the group of chosen vehicles
 has that exact total number of wheels. Two ways of choosing vehicles are considered to be different if and only if they
 contain different numbers of two-wheeled or four-wheeled vehicles.

For example, if our array wheels = [4,5,6] our return array would be res = [2, 0, 2]. Case by case, we can have 1
four-wheel or 2 two-wheel to have 4 wheels.We cannot have 5 wheels. We can have 1 four-wheel and 1 two-wheel or 3
two-wheel vehicles in the final case.

Function Description
Complete the function chooseFleets in the editor below. The function should return an array of integers representing the
answer for each wheels[i].
chooseFleets has the following parameter(s): wheels[wheels[0],..wheels[n-1]]: an array of integers

Constraints
• 1 ≤ n ≤ 10
• 1 ≤ wheels[i] ≤ 10^6

Sample Case 0
Sample Input
3
6
3
2
Sample Output 0
2
0
1
Explanation 0
We must find the number of ways of choosing fleets of vehicles whose total numbers of wheels correspond to the values in
wheels = [6, 3, 2].

• For wheels0 = 6, we can choose a fleet with 6 total wheels in two ways:

1. Choose 1 four-wheeled vehicle and 1 two-wheeled vehicle.
2. Choose 3 two-wheeled vehicles.
Thus, we store 2 in index 0 of our return array.

• There is no way to choose a fleet of vehicles with exactly wheels, = 3 total wheels because each vehicle has either
two or four wheels, so we store 0 in index 1 of our return array.
• For wheels2 = 2, we can only choose 1 two-wheeled vehicle to get a fleet with 2 total wheels.
Thus, we store 1 in index 2 of our return array.
"""


# class Solution:
#     def choose_fleets(self, wheels: list[int]):
#         vehicles = [2, 4]
#         result = []
#         for count in wheels:
#             dp = [0 for i in range(count + 1)]
#             dp[0] = 1
#             for i in range(1, len(dp)):
#                 for v in vehicles:
#                     dp[i] += dp[i - v] if i - v >= 0 else 0
#             result.append(dp[-1])
#         return result

# Combination Sum
class Solution:
    def choose_fleets(self, wheels: list[int]):
        vehicles = [2, 4]
        result = []

        def count_combinations(wheels_left, last_vehicle_idx):
            if wheels_left < 0:
                return 0
            if wheels_left == 0:
                return 1
            total = 0
            print("a", wheels_left, last_vehicle_idx)
            for idx in range(last_vehicle_idx, len(vehicles)):
                total += count_combinations(wheels_left - vehicles[idx], idx)
            print("b", wheels_left, total)
            return total

        for count in wheels:
            result.append(count_combinations(count, 0))

        return result


inputs = [
    [8]
]
for i in inputs:
    print(Solution().choose_fleets(i))
