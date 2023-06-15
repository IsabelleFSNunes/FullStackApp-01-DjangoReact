from django.test import TestCase

class ExampleTestCase(TestCase):
    def test_something(self):
        '''
        Teste criado para exemplificar como criar um teste
        e quais são as possibilidades de asserts mais frequentes
        '''
        # Escreva seu teste aqui
        self.assertEqual(1, 1)
        # tipos de assert que você pode usar
        a = 1
        b = 1
        x = True

        self.assertEqual(a, b) # a == b
        self.assertNotEqual(a, b+2) # a != b
        self.assertTrue(x) # bool(x) # is True
        self.assertFalse(not x) # bool(x) is False
        self.assertIs(a, b) # a is b

        pass