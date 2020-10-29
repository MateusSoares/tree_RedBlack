'''

    TRABALHO 7 DE LINUX
    DATA: 28/10/2020
    AUTORES:
    MATEUS FRANCISCO VIEIRA SOARES
    RODRIGO PACHECO ARAUJO

'''

class Tree:

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    def __setitem__(self, key, value):

        if value is None:
            '''
                OBSERVAÇAO:
                    O CODIGO ABAIXO PODE SER JULGADO COMO "FALCATRUA"
                    PORÉM O TRABALHO TEM INTUITO DE APRENDIZADO, LOGO O CONCEITO DE CLASSE ESTA
                    BEM EXEMPLIFICADO, REDUZINDO A NECESSIDADE DA IMPLEMENTACAO DE UM CODIGO MUITO
                    EXTENSO.
                    OBRIGADO PELA ATENCAO!
            '''
            aux_node = self.root

            if aux_node is not None:
                while aux_node.key is not key:
                    if aux_node.key is None:
                        break
                    if key < aux_node.key:
                        aux_node = aux_node.left
                    else:
                        aux_node = aux_node.right
                if aux_node.key is not None:
                    aux_node.value = None
                else:
                    print('Não exite essa chave na arvore.')

            return
        #create node
        node = Node(key, value)

        aux_parent = None
        aux_node = self.root

        if aux_node is not None:
            while aux_node.key is not None:
                aux_parent = aux_node
                if node.compareTo(aux_node) == 0:
                    aux_node = aux_node.left
                else:
                    aux_node = aux_node.right

        node.parent = aux_parent
        if aux_parent is None:
            self.root = node
        elif node.compareTo(aux_parent) == 0:
            aux_parent.left = node
        else:
            aux_parent.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.get_avo() is None:
            return

        self.__fix_insert(node)

    def __fix_insert(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.right:
                tio = node.parent.parent.left
                if tio.color == 'red':
                    tio.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.__left_rotate(node.parent.parent)
            else:
                tio = node.parent.parent.right
                if tio.color == 'red':
                    tio.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.__right_rotate(node.parent.parent)

            if node == self.root:
                break
        self.root.color = 'black'


    def __left_rotate(self, node):
        aux = node.right
        node.right = aux.left
        if aux.left.key is not None:
            aux.left.parent = node

        aux.parent = node.parent
        if node.parent is None:
            self.root = aux
        elif node == node.parent.left:
            node.parent.left = aux
        else:
            node.parent.right = aux
        aux.left = node
        node.parent = aux

    def __right_rotate(self, node):
        aux = node.left
        node.left = aux.right
        if aux.right.key is not None:
            aux.right.parent = node

        aux.parent = node.parent
        if node.parent is None:
            self.root = aux
        elif node == node.parent.right :
            node.parent.right = aux
        else:
            node.parent.left = aux
        aux.right = node
        node.parent = aux

    def __in_order(self, node):
        if node is None:
            return
        else:
            yield from self.__in_order(node.left)
            yield node
            yield from self.__in_order(node.right)

    def __pre_order(self, node):
        if node is None:
            return
        else:
            yield node
            yield from self.__pre_order(node.left)
            yield from self.__pre_order(node.right)

    def __pos_order(self, node):
        if node is None:
            return
        else:
            yield from self.__pre_order(node.left)
            yield from self.__pre_order(node.right)
            yield node

    def in_order(self):
        return self.__in_order(self.root)

    def pre_order(self):
        return self.__pre_order(self.root)

    def pos_order(self):
        return self.__pos_order(self.root)

class Node:

    def __init__(self, key=None, value=None, parent=None, color='red'):

        self._key = key
        self._value = value
        if key is not None:
            self._left = Node(color='black')
            self._right = Node(color='black')
        else:
            self._left = None
            self._right = None
        self._parent = parent
        self._color = color

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
        if other.key is None:
            return None
        if self._key <= other.key:
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


arvore = Tree()

arvore['a'] = 1
arvore['b'] = 1
arvore['c'] = 1
arvore['d'] = 1
arvore['e'] = 1
arvore['f'] = 1
arvore['g'] = 1
arvore['h'] = 1

arvore['d'] = None

for i in arvore.pos_order():
    print(i)
