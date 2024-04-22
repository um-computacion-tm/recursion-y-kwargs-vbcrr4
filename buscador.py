import unittest
def buscador_datos(*args, **database):
    for key, person_data in database.items():
        if all(arg in person_data.values() for arg in args):
            return key  
    return None 
database = {

            "p1":{

                "nombre1":"Pablo",

                "nombre2":"Diego",

                "apellido1":"Ruiz",

                "apellido2":"Picasso"

            },

            "p2":{

                "nombre1":"Elio",

                "apellido1":"Anci"

            },

            "p3":{

                "nombre1":"Elias",

                "nombre2":"Marcos",

                "nombre3":"Luciano",

                "apellido1":"Marcelo",

                "apellido2":"Gonzalez"

            }

}
class TestBuscarDatos(unittest.TestCase):
    def test_pablo(self):
        resultado = buscador_datos("Pablo","Diego","Ruiz","Picasso",**database)
        self.assertEqual(resultado, "p1")
    def test_elio(self):
        resultado = buscador_datos("Elio", "Anci", **database)
        self.assertEqual(resultado, "p2")

    def test_elias(self):
        resultado = buscador_datos("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", **database)
        self.assertEqual(resultado, "p3")

    def test_none(self):
        resultado = buscador_datos("Mario", "Bros", "Lopez", **database)
        self.assertIsNone(resultado)

    def test_none1(self):
        resultado = buscador_datos("Edinson", "Cavani", "1", **database)
        self.assertIsNone(resultado)

    def test_none2(self):
        resultado = buscador_datos("Miguel", "Merentiel", "boca", "2", **database)
        self.assertIsNone(resultado)
    
if __name__ == '__main__':
    unittest.main()