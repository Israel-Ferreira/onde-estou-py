class GmapsClientError(RuntimeError):

    GMAPS_CLIENT_ERROR_MSG = "Erro ao obter as coordenadas no google maps"

    def __init__(self):
        super.__init__(self.GMAPS_CLIENT_ERROR_MSG)