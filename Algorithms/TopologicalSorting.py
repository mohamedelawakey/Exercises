def topological_sort(graph):
    N = list(graph.keys())
    E = []
    
    for i in graph:
        for nabour in graph[i]:
            E.append((i, nabour))
    
    result = []
    
    while N:
        cycle = True
        
        for i in N[:]:
            has_incoming = any(edge[1] == i for edge in E)
            if not has_incoming:
                N.remove(i)
                E = [edge for edge in E if edge[0] != i]
                result.append(i)
                cycle = False
        
        if cycle:
            print("I cannot resolve cyclic dependencies!")
            break
    
    return result


graph = {
    'install_computer': ['connect_internet'],
    'connect_internet': ['buy_placebo_song'],
    'buy_placebo_song': ['burn_cd'],
    'go_city_center': ['buy_soap', 'buy_coke', 'library'],
    'buy_soap': ['do_dishes'],
    'library': ['write_essay'],
    'burn_cd': [],
    'buy_coke': [],
    'do_dishes': [],
    'write_essay': [],
    'empty_garbage': [],
    'shine_shoes': [],
    'print_math': ['answer_math'],
    'answer_math': [],
}

sorted_order = topological_sort(graph)
print("Topological Order:", sorted_order)
