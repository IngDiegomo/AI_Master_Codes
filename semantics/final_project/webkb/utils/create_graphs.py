import os
import networkx as nx

def create_graph(content, cites):
    
    pages = [""] * len(content)
    G = nx.DiGraph()
    i = 0

    for page in content:
        parts = page.strip().split()
        pages[i] = parts[0]
        x = [int(y) for y in parts[1:-1]]
        G.add_node(i, name = parts[0], content = x, classification = parts[-1])
        i += 1

    for cite in cites:
        parts = cite.strip().split()
        G.add_edge(pages.index(parts[0]),pages.index(parts[1]))

    return G