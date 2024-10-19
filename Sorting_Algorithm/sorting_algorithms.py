"""Sorting algorithms"""
from typing import List


class Sorting:
    """Sorting algorithms to sort an array of integers"""


    def __init__(self) -> None:
        """Get the input from user and make a list of that"""
        self._get_input()
        self.sorting_type: str


    def _get_input(self) -> None:
        """Get array of integers and sorting algorithm type from user"""
        inp = input("Insert an array on integers separated by ',': ").split(",")
        self.inputs = [int(val) for val in inp]


    def _sorter_validation(self) -> None:
        """Validate the type of sorting algorithm"""
        algorithms = ["bubble", "selection", "insertion", "merge", "quick", "counting", "radix", "bucket", "heap", "shell"] # pylint: disable=C0301
        if self.sorting_type not in algorithms:
            raise ValueError(f"Algorithm '{self.sorting_type}' does not exits.")


    def bubble(self) -> List[int]:
        """Implement bubble sorting algorithm"""
        inp = self.inputs.copy()
        for i in range(len(inp) - 1):
            swaped_flag = False
            for j in range(len(inp) - i - 1):
                if inp[j] > inp[j+1]:
                    inp[j], inp[j+1] = inp[j+1], inp[j]
                    swaped_flag = True
            if not swaped_flag:
                break

        return inp


    def selection(self) -> List[int]:
        """Implement selection sorting algorithm"""
        inp = self.inputs.copy()
        for i, _ in enumerate(inp):
            min_id = i
            for j in range(i + 1, len(inp)):
                if inp[min_id] > inp[j]:
                    min_id = j
            inp[i], inp[min_id] = inp[min_id], inp[i]

        return inp


    def insertion(self) -> List[int]:
        """Implement insertion sorting algorithm"""
        inp = self.inputs.copy()
        for i in range(1, len(inp)):
            key = inp[i]
            for j in range(i,0,-1):
                if inp[j-1] > key:
                    inp[j], inp[j-1] = inp[j-1], inp[j]

        return inp


    def merge_sort(self) -> List[int]:
        """Implement merge sort algorithm"""
        inp = self.inputs.copy()
        return self._merge_helper(inp)


    def _merge_helper(self, input_list: List[int]) -> List[int]:
        """Helper function for merge sorter to implement it recursively"""
        if len(input_list) > 1:
            left_half = input_list[:int(len(input_list)//2)]
            right_half = input_list[int(len(input_list)//2):]
            left_sort = self._merge_helper(left_half)
            right_sort = self._merge_helper(right_half)

            i = j = k = 0
            while i < len(left_sort) and j < len(right_sort):
                if left_sort[i] < right_sort[j]:
                    input_list[k] = left_sort[i]
                    i += 1
                    k += 1
                else:
                    input_list[k] = right_sort[j]
                    j += 1
                    k += 1

            while i < len(left_sort):
                input_list[k] = left_sort[i]
                i += 1
                k += 1

            while j < len(right_sort):
                input_list[k] = right_sort[j]
                j += 1
                k += 1

            output = input_list

        else:
            output = input_list

        return output


    def quick_sort(self) -> List[int]:
        """Implement quick sort algorithm"""
        inp = self.inputs.copy()
        inp_size = len(inp)
        self._quick_helper(inp, 0, inp_size - 1)
        return inp


    def _quick_helper(self, inp: List[int], low: int, high: int) -> None:
        """Helper function for quick sorter to implement it recursively"""
        if low < high:
            pivot_idx = self._quick_preparing(inp, low, high)
            self._quick_helper(inp, low, pivot_idx - 1)
            self._quick_helper(inp, pivot_idx + 1, high)


    def _quick_preparing(self, inp: List[int], low: int, high: int) -> int:
        """Helper function for quick sorter to run the partioning part"""
        pivot = inp[high]
        second_position_idx = low - 1
        for idx in range(low,high):
            if inp[idx] < pivot:
                second_position_idx += 1
                inp[idx], inp[second_position_idx] = inp[second_position_idx], inp[idx]
        inp[second_position_idx + 1], inp[high] = inp[high], inp[second_position_idx + 1]

        return second_position_idx + 1


    def counting(self):
        """Implement counting sort algorithm"""
        inp = self.inputs.copy()

        max_val = max(inp)
        count_list = [0] * (max_val + 1)
        output = [0] * len(inp)
        for idx,_ in enumerate(inp):
            count_list[inp[idx]] += 1

        for idx in range(1, len(count_list)):
            count_list[idx] += count_list[idx - 1]

        for val in inp:
            output[count_list[int(val)] - 1] = val
            count_list[int(val)] -= 1

        return output



    def main(self) -> List[int]:
        """Run appropirtae algorithm based on the sorting type"""
        self.sorting_type = input("Select the sorting algorithm bubble/selection/insertion/merge/quick/counting/radix/bucket/heap/shell: ") # pylint: disable=C0301
        self._sorter_validation()
        if self.sorting_type == "bubble":
            sorted_values = self.bubble()
        elif self.sorting_type == "selection":
            sorted_values = self.selection()
        elif self.sorting_type == "insertion":
            sorted_values = self.insertion()
        elif self.sorting_type == "merge":
            sorted_values = self.merge_sort()
        elif self.sorting_type == "quick":
            sorted_values = self.quick_sort()
        elif self.sorting_type == "counting":
            sorted_values = self.counting()

        print(f"Sorted values using {self.sorting_type} algorithm: {sorted_values}")

        return sorted_values



if __name__ == "__main__":
    sorter= Sorting()
    sorter.main()
