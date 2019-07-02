from unittest import TestCase
from flask import url_for
from app.app import create_app


class TestFlaskBase(TestCase):
    def setUp(self):
        """Roda antes de todos os testes."""
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()


    def tearDown(self):
        """Roda depois de todos os testes."""
        self.app.db.drop_all()

    def test_cadastrar_deve_retornar_o_payload_enviado_sem_id(self):
        dado = {
            'livro': 'Python 3',
            'escritor': 'Eduardo'
        }

        response = self.client.post(url_for('books.cadastrar'), json=dado)

        response.json.pop('id')

        self.assertEqual(dado, response.json)
