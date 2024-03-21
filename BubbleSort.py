class BubbleSort:

    def __init__(self, draw_info):
        self.draw_info = draw_info
        self.current_list = draw_info.lst
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        lst = self.draw_info.lst
        while self.i < len(lst) - 1:
            if self.j < len(lst) - self.i - 1:
                if lst[self.j] > lst[self.j + 1]:
                    lst[self.j], lst[self.j + 1] = lst[self.j + 1], lst[self.j]
                    self.j += 1
                    self.modified = True  # Set flag to True when list is modified
                    return self.current_list.copy()  # Return a copy of the current list
                else:
                    self.j += 1
            else:
                self.i += 1
                self.j = 0
        if self.modified:
            self.modified = False  # Reset flag
            self.current_list = lst.copy()
            return self.current_list.copy()  # Return a copy of the updated list
        else:
            raise StopIteration