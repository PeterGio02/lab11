import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allProducts = None
        self._grafo = nx.Graph()
        self.idMap = {}
        self._migliori = None


    def buildGraph(self, anno, colore):
        self._grafo.clear()

        #NODI
        self._allProducts = DAO.getProdotti(colore)
        for p in self._allProducts:
            self.idMap[p.Product_number] = p

        self._grafo.add_nodes_from(self._allProducts)

        #ARCHI: siccome il datebase è molto grosso non posso operare normalmente ma bensì passo due prodotti alla
        #volta e faccio la query su quei due
        for p1 in self._allProducts:
            for p2 in self._allProducts:
                if p1 != p2:
                    peso = DAO.getArchi(p1, p2, anno)
                    if peso > 0:
                        self._grafo.add_edge(p1, p2, weight=peso)

    def archi_maggiori(self):
        archi = sorted(self._grafo.edges(data=True), key=lambda x: x[2]['weight']) #data=true così prende anche il peso, [2] perchè voglio il peso
        self._migliori = archi[-3:] #volgio solo i migliori tre



    def getNumNodi(self):


        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

