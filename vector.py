from typing import TypeVar, Generic, Optional
import sys

T = TypeVar('T')

class Vector(Generic[T]):
    """Custom Vector implementation - dynamic array"""
    
    def __init__(self):
        self._data = [None] * 2  # Initial capacity of 2
        self._size = 0
        self._capacity = 2
    
    def add_element(self, element: T) -> None:
        """Add element to the end of vector"""
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = element
        self._size += 1
    
    def remove_element(self, index: int) -> bool:
        """Remove element at given index"""
        if not self._is_valid_index(index):
            return False
        
        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        
        self._size -= 1
        self._data[self._size] = None  # Clear reference
        
        # Shrink capacity if needed
        if self._size <= self._capacity // 4 and self._capacity > 2:
            self._resize(self._capacity // 2)
        
        return True
    
    def search_element(self, element: T) -> int:
        """Search for element and return index, -1 if not found"""
        for i in range(self._size):
            if self._data[i] == element:
                return i
        return -1
    
    def realize_new_capacity(self, new_capacity: int) -> None:
        """Manually set new capacity"""
        if new_capacity >= self._size:
            self._resize(new_capacity)
    
    def get(self, index: int) -> Optional[T]:
        """Get element at index"""
        if self._is_valid_index(index):
            return self._data[index]
        return None
    
    def get_size(self) -> int:
        """Get current size"""
        return self._size
    
    def _resize(self, new_capacity: int) -> None:
        """Resize internal array"""
        old_data = self._data
        self._data = [None] * new_capacity
        self._capacity = new_capacity
        
        # Copy old data
        for i in range(min(self._size, new_capacity)):
            self._data[i] = old_data[i]
    
    def _is_valid_index(self, index: int) -> bool:
        """Check if index is valid"""
        return 0 <= index < self._size
    
    def __iter__(self):
        """Make vector iterable"""
        for i in range(self._size):
            yield self._data[i]
    
    def __len__(self):
        """Return size when len() is called"""
        return self._size