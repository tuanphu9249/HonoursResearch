import networkx as nx
import os, inspect, shutil
import random
import numpy as np, scipy.sparse as sp
import pickle
import pandas as pd
import copy
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt












def main():
    G1 = nx.read_graphml("Colt.graphml")
    print("Colt")
    print(nx.get_node_attributes(G1, 'type'))
    print(nx.get_node_attributes(G1, 'Country'))
    print('\n')

    G2 = nx.read_graphml("Amres.graphml")
    print("Amres")
    print(nx.get_node_attributes(G2, 'type'))
    print(nx.get_node_attributes(G2, 'Country'))
    print('\n')

    G3 = nx.read_graphml("Arpanet19723.graphml")
    print("Arpanet19723")
    print(nx.get_node_attributes(G3, 'type'))
    print(nx.get_node_attributes(G3, 'Country'))
    print('\n')

    G4 = nx.read_graphml("Carnet.graphml")
    print("Carnet")
    print(nx.get_node_attributes(G4, 'type'))
    print(nx.get_node_attributes(G4, 'Country'))
    print('\n')

    G5 = nx.read_graphml("Cernet.graphml")
    print("Cernet")
    print(nx.get_node_attributes(G5, 'type'))
    print(nx.get_node_attributes(G4, 'Country'))
    print('\n')

    G6 = nx.read_graphml("Fatman.graphml")
    print("Fatman")
    print(nx.get_node_attributes(G6, 'type'))
    print(nx.get_node_attributes(G6, 'Country'))
    print('\n')





if __name__ == '__main__':
    main()