class Tree:

    def __init__(self):
        self._node = Node()


class Node:

    def __init__(self, key=None, value=None, left=None, right=None, color=None, parent=None):

        self._key = key
        self._value = value
        self._left = left
        self._right = right
        self._color = color
        self._parent = parent

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, key):
        self._key = key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def __str__(self) -> str:
        return f'{self._key} --> {self._value} ({self._color})'

    def compareTo(self, other):
        if other is None:
            return None
        aux = [self._key, other.key]
        aux.sort()
        if aux[0] == self._key:
            return 0
        else:
            return 1

    def get_avo(self):
        if self._parent is None:
            return None
        return self._parent.parent

    def get_tio(self):
        avo = self.get_avo()
        if avo is None:
            return None
        pai = self.parent
        if pai.compareTo(avo) == 1:
            return avo.left
        else:
            return avo.right


no = Node(color='black')
print(no)