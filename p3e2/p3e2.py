import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt
G = nx.Graph()   #Graph asume bidireccionalidad en todos los arcos

G.add_node("0", pos=[1,2])
G.add_node("1", pos=[4,3])
G.add_node("2", pos=[1,6])
G.add_node("3", pos=[7,3])
G.add_node("4", pos=[10,1])
G.add_node("5", pos=[0,10])
G.add_node("6", pos=[4,0])
G.add_node("7", pos=[5,8])
G.add_node("8", pos=[9,7])
G.add_node("9", pos=[8,10])

pos = nx.get_node_attributes(G,"pos")

v1=120 #gris
v2=60 #verdes
v3=40#cafes

print(pos["0"][0])
def funcion_generar_costo(n1,n2,v):
    x1=n1[0]
    x2=n2[0]
    y1=n1[1]
    y2=n2[1]
    c=((x2-x1)**2)+((y2-y1)**2)
    cc=sqrt(c)
    ccc=cc/v
    return ccc
c1=1
G.add_edge("0","6", costo=funcion_generar_costo(pos["0"],pos["6"],v1))
G.add_edge("6","3", costo=funcion_generar_costo(pos["6"],pos["3"],v3))
G.add_edge("3","4", costo=funcion_generar_costo(pos["3"],pos["4"],v2 ))
G.add_edge("4","6", costo=funcion_generar_costo(pos["4"],pos["6"],v1))
G.add_edge("4","8", costo=funcion_generar_costo(pos["4"],pos["8"],v1 ))
G.add_edge("3","8", costo=funcion_generar_costo(pos["3"],pos["8"],v3 ))
G.add_edge("8","9", costo=funcion_generar_costo(pos["8"],pos["9"],v2 ))
G.add_edge("3","7", costo=funcion_generar_costo(pos["3"],pos["7"],v2 ))
G.add_edge("7","9", costo=funcion_generar_costo(pos["7"],pos["9"],v2 ))
G.add_edge("7","5", costo=funcion_generar_costo(pos["7"],pos["5"],v1 ))
G.add_edge("5","2", costo=funcion_generar_costo(pos["5"],pos["2"],v3 ))
G.add_edge("2","1", costo=funcion_generar_costo(pos["2"],pos["1"],v3 ))
G.add_edge("1","7", costo=funcion_generar_costo(pos["1"],pos["7"],v3 ))
G.add_edge("0","1", costo=funcion_generar_costo(pos["0"],pos["1"],v3 ))
G.add_edge("2","0", costo=funcion_generar_costo(pos["2"],pos["0"],v1 ))
G.add_edge("1","3", costo=funcion_generar_costo(pos["1"],pos["3"],v2))
#controlar el dibujo del grafo
# pos = nx.spring_layout(G)
# pos = nx.random_layout(G)
# pos = nx.circular_layout(G)

pos = nx.get_node_attributes(G,"pos")


labels = nx.get_edge_attributes(G,"costo")


def funcion_costo(ni, nf, atributos_arco):
	# print(f"ni = {ni} nf = {nf}, att={atributos_arco}")
	return atributos_arco["costo"]


# path = nx.shortest_path(G, source="A", target="D", weight="costo")
# path = nx.dijkstra_path(G, source="A", target="D", weight="costo")
ruta = nx.dijkstra_path(G, source="0", target="4", weight=funcion_costo)


costo_ruta = 0.
Nparadas = len(ruta)

print(f"Ruta Nparadas={Nparadas} ruta: {ruta}")
for i in range(Nparadas-1):
	parada_i = ruta[i]
	parada_f = ruta[i+1]
	costo_tramo_i = G.edges[parada_i, parada_f]["costo"]
	print(f"Tramo {i}  {parada_i} a {parada_f} costo={costo_tramo_i}")
	costo_ruta += costo_tramo_i

print(f"Costo de ruta = {costo_ruta}")



edgelist1 = [\
 	("1","3"),
 	("3","7"),
    ("3","4"),
    ("7","9"),
    ("8","9"),
 	]

colores1 = [\
"g",
"g"
]
    
edgelist2 = [\
	("0","6"),
 	("6","4"),
    ("4","8"),
    ("0","2"),
    ("5","7"),
 	]

colores2 = [\
"silver",
"silver",
"silver",
"silver",
"silver"
]
edgelist3 = [\
	("0","1"),
 	("1","2"),
    ("2","5"),
    ("1","7"),
    ("3","8"),
    ("6","3"),
 	
 	]

colores3 = [\
"saddlebrown",
"saddlebrown"
]
colores4 = [\
"r",
"r"
]

coloresr = []
coloresg = []
edgelist = []
for ni, nf in G.edges:
    if ni in ruta and nf in ruta:
        a=(str(ni),str(nf))
        coloresr.append(a) 
    else:
        b=(str(ni),str(nf))
        coloresg.append(b)
    edgelist.append((ni,nf))




plt.figure()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
#nx.draw_networkx_edges(G, pos, edgelist=edgelist, edge_color=colores)

#nx.draw_networkx_edges(G, pos, edgelist=edgelist1, edge_color=colores1,width=2)
#nx.draw_networkx_edges(G, pos, edgelist=edgelist2, edge_color=colores2,width=3) #comentar para ver las rutas minimas bien en rojo
#nx.draw_networkx_edges(G, pos, edgelist=edgelist3, edge_color=colores3,width=2)
#nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

nx.draw_networkx_edges(G, pos, edgelist=coloresr, edge_color=colores4,width=3) 
nx.draw_networkx_edges(G, pos, edgelist=coloresg, edge_color=colores2,width=2)



#grafico uso de memoria 

#plt.yticks(dts,labels_y)


plt.grid(True)
plt.xticks(visible=True)
plt.xlabel("X(Km)")



#plt.show()
plt.suptitle(f"Ruta minima: {ruta} costo={costo_ruta}")
plt.grid("on")
plt.show()


