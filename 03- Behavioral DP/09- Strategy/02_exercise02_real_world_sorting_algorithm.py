from abc import ABC, abstractmethod

class SortingStrategy(ABC):

    @abstractmethod
    def sort(self, data):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        self._quick_sort(data, 0, len(data) - 1)

    def _quick_sort(self, data, low, high):
        if low < high:
            pivot_index = self._partition(data, low, high)
            self._quick_sort(data, low, pivot_index - 1)
            self._quick_sort(data, pivot_index + 1, high)

    def _partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1



class Sorter:
    def __init__(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy
    
    def set_sorting_strategy(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def sort_data(self, data):
        self.sorting_strategy.sort(data)


#client usage
data = [5, 2, 8, 1, 9]
sorter  = Sorter(BubbleSortStrategy())

sorter.sort_data(data)
print("Sorted data using Bubble Sort:", data)

data2= ["James","Ryan", "Tyrene", "Ben"]

sorter.set_sorting_strategy(QuickSortStrategy())
sorter.sort_data(data2)
print("Sorted data using Quick Sort:", data2)

