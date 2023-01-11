from dag import DAG

d = DAG(user = 1, data = "./dag.json")
d.create_graph()
# res = d.g.bfsiter(vid = 0, mode='out',advanced = True)

# for r in res:
#     print(r)

print(d.g.summary())
# for i in d.g.vs():
#     print(f"index {i.index}")
#     res = d.g.incident(vertex = i.index, mode='out')
#     print(res)

for es in d.g.es():
    # print(es)
    print(es.source,es.target)

for vertex in d.g.vs:
    # print(vertex)
    print(d.g.neighborhood(vertices=vertex, order=1, mode='out',mindist = 1))

# print(d.g.get_adjacency())
# print(d.g.neighborhood(vertices=0, order=1, mode='out',mindist = 1))