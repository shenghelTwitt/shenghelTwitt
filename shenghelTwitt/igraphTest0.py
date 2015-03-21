from igraph import *

def draw_graph(topol, users):
    g = Graph()
    g.add_vertices(len(sers))
    g.add_edges(topol)
    for i in range(len(users)):
        g.vs[i]['name'] = passedUsers[i].name
        g.vs[i]['red'] = int(users[i].attraction[0] * 255)
        g.vs[i]['blue'] = users[i].attraction[1] * 255
    g.vs["label"] = g.vs["name"]
                   
    visual_style = {}
    g.vs["color"] = ["rgb("+str(g.vs[i]['red'])+", 0, "+str(g.vs[i]['blue'])+")" for i in range(len(users))]
    visual_style["vertex_label"] = g.vs["name"]
                  
    layout = g.layout("lgl")
    plot(g, layout = layout, margin = 20)
    plot(g, "social_network.pdf", **visual_style)
