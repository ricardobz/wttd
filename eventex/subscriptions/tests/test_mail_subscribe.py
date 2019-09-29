from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Ricardo Beckert', cpf='12345678901', email='beckert.ricardo@gmail.com', phone='48-99999-0001')
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','beckert.ricardo@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Ricardo Beckert',
                    '12345678901',
                    'beckert.ricardo@gmail.com',
                    '48-99999-0001']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
