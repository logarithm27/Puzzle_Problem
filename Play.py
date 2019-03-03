from Numpy import matrix


class ASearch:
    def __init__(self):
        self.g_function = 0
        self.h_function = 0
        self.f_function = 0
        self.parent_node = None
        self.child_node = None

    def calculate_f_function(self):
        return self.g_function + self.h_function

    def calculate_manhattan_distance(self, block):



