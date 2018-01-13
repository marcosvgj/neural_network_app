#!/usr/bin/python

from pymongo import errors, MongoClient


# Intenção: Desacoplar o acesso ao banco de dados da classe Coletor

class MongoDB:
    def __init__(self, host=None, port=None):

        self.session = MongoClient()

        # Default Host
        if host is None:
            self.host = 'localhost'
        else:
            self.host = host

        # Default Port
        if port is None:
            self.port = 27017
        else:
            self.port = port

    def iniciar_sessao(self):
        self.session = MongoClient(self.host, self.port)

    def fechar_sessao(self):
        self.session.close()

    def armazenar_dados(self, coletor):

        db = self.session['SmartCoinDB'].get_collection(coletor.request_type.market)

        try:
            db.insert_one(coletor.data)
            print("Data was successfully inserted in the follow Colletion: %s " % coletor.request_type.market)

        except errors.OperationFailure as error:
            print("Could not apply the operation %s" % error)

    def consultar(self, market=None, coin=None):
        if market is None:
            if coin is None:
                self.session['SmartCoinDB'].collection_names()

                """ Retornar todos os dados de todas as coleções"""
            else:
                """ Retornar as informações sobre a cryptomoeda selecionada de todos os mercados"""
        else:
            if coin is None:
                """ Retornar todas as informações sobre todas as cryptomoedas do mercado selecionado"""

            else:
                """ Retornar todas as informações sobre a cryptomoeda selecionada do mercado selecionado"""
