
from context import simpot

import unittest


from rdflib import Namespace, Literal, URIRef
from simpot import BNamespace, RdfsClass, graph
from rdflib.namespace import DC, FOAF

vcard = Namespace('https://www.w3.org/2006/vcard/ns#') #Trazendo uma nova ontologia
n = Namespace("http://linkedscience.org/teach/ns#")

class Curso ():

    # os nomes dessas variaveis de classe, precisam ser os mesmos das de instancia
    title = n.courseTitle # RdfProperty
    image = vcard.hasPhoto # RdfProperty

    @RdfsClass(n.Course, "http://lud.ufma.br/course/")
    @BNamespace("teach", n)
    @BNamespace("vcard", vcard)
    def __init__(self, id, title):
        self.id = id
        self.title = Literal(title)
        self.image = URIRef('urlimg')
 



class TestGraphs(unittest.TestCase):
    def test(self):
        c1 = Curso("1","Computação")
        c2 = Curso("2", "Mecanica")
        g = graph([c1,c2])
        self.assertTrue((URIRef('http://lud.ufma.br/course/1'), None, None) in g) # computação
        self.assertTrue((URIRef('http://lud.ufma.br/course/2'), None, None) in g) # mecanica

c1 = Curso("1","Computação")
c2 = Curso("2","mecanica")
print ((graph([c1,c2])).serialize())