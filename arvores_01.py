# Árvores Binárias

from binarytree import Node

# Criar uma árvore binária simples
root = Node("A")    # Nível 0
root.left = Node("B")   # Nível 1
root.right = Node("C")  # Nível 1
root.left.left = Node("D")  # Nível 2
root.left.right = Node("E")  # Nível 2
root.right.left = Node("F")  # Nível 2
print(root) # Imprime a árvore
#teste GitHub
