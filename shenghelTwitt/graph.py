from igraph import *


def getIndex(username, users):
	for i in range(len(users)):
		if users[i].name == username:
			return i
	return -1
	
def getRelations(users):#bad time order
	relations = []
	for i in range(len(users)):
		followings = users[i].followingUsernames
		for following in followings:
			followingIndex = getIndex(following, users)
			if followingIndex != -1:
				relations.append((i, followingIndex))
	return relations
	
def draw_graph(users):
	print "processing relations ..."
	relations = getRelations(users)
	print "relations processed"
	print "relations is :&&&&", relations
	g = Graph()
	g.add_vertices(len(users))
	g.add_edges(relations)
	for i in range(len(users)):
		g.vs[i]['name'] = users[i].name
		g.vs[i]['red'] = int(users[i].attraction[0] * 255)
		g.vs[i]['blue'] = users[i].attraction[1] * 255
	g.vs["label"] = g.vs["name"]
	visual_style = {}
	g.vs["color"] = ["rgb("+str(g.vs[i]['red'])+", 0, "+str(g.vs[i]['blue'])+")" for i in range(len(users))]
	visual_style["vertex_label"] = g.vs["name"]
	layout = g.layout("lgl")
	plot(g, layout = layout, margin = 20)
	plot(g, "social_network.pdf", **visual_style)