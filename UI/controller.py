import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        colori = DAO.getColori()
        for c in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))



    def handle_graph(self, e):
        self._view.txtOut.controls.clear()

        anno = int(self._view._ddyear.value)
        colore = self._view._ddcolor.value

        self._model.buildGraph(anno, colore)
        self._view.txtOut.controls.append(ft.Text(f"numero di nodi {self._model.getNumNodi()} numero di archi {self._model.getNumArchi()}"))




        self._view._page.update()


    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
