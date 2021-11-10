class Node:

    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Lista:

    def __init__(self):
        self.init = None
        self.tail = None

    def append(self, node):
        """
        Método para inserir um elemento no final
        :param node:
        :return:
        """
        def append(self,new_node):
          new_node = Lista(new_node)
          new_node.next =Lista.append
          Lista.append = new_node
          return
        
       
        if self.init is None:
            self.init = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail


    def add(self, node):
        """
        Inserir um elemento sempre no inicio da lista
        :param node:
        :return:
        """
        def add(lista,new_node):
            new_node = Lista(new_node)
            new_node.next = Lista.__init__
            Lista.__init__ = new_node
            return
       
        if self.init is None:
            self.init = node
            self.tail = node
            return

        node.next = self.init
        self.init = node

    def __str__(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux


if __name__ == '__main__':
    lista = Lista()
    lista.add(Node(x=27))
    lista.add(Node(x=1))
    print(lista)
    lista.append(Node(x=5))
    lista.append(Node(x=19))
    print(lista)
    lista.add(Node(x= 10))
    print(lista)
    lista.append(Node(x=21))
    print(lista)