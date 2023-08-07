from api.views import SendMessageView
from api.models import Status
from unittest.mock import patch
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .serializer import UserSerializer, StatusSerializer

from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from rest_framework.test import APIClient
from unittest.mock import patch, MagicMock


class SerializerTestCase(TestCase):

    def test_user_serializer(self):

        user_data = {'full_name': 'John Doe'}
        user_serializer = UserSerializer(data=user_data)
        self.assertTrue(user_serializer.is_valid())
        user_object = user_serializer.save()

        serialized_user = UserSerializer(user_object)
        self.assertEqual(user_data['full_name'],
                        serialized_user.data['full_name'])
        self.assertEqual(user_object.id, serialized_user.data['id'])

    def test_status_serializer(self):

        status_active = Status.objects.create(name='active')
        status_canceled = Status.objects.create(name='canceled')

        status_serializer_active = StatusSerializer(status_active)
        status_serializer_canceled = StatusSerializer(status_canceled)

        self.assertEqual(status_active.id, status_serializer_active.data['id'])
        self.assertEqual('active', status_serializer_active.data['name'])

        self.assertEqual(status_canceled.id,
                        status_serializer_canceled.data['id'])
        self.assertEqual('canceled', status_serializer_canceled.data['name'])


class RegisterUserViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('pika.BlockingConnection')
    def test_register_user_view_success(self, mock_connection):
        mock_channel = MagicMock()
        mock_connection.return_value._enter_.return_value.channel.return_value = mock_channel

        data_user = {
            "full_name": "John Doe"
        }
        response = self.client.post('/users/', data_user, format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], data_user['full_name'])


class SendMessageViewTestCase(TestCase):
    def setUp(self):
        user_data = {
            "full_name": "John Doe"
        }
        self.factory = APIRequestFactory()
        self.client.post('/users/', user_data, format='json')

    def test_invalid_event_type(self):
        data_test = {
            "event_type": "INVALID_EVENT_TYPE",
            "data": {
                "user_id": 1,
            }
        }
        request = self.factory.post(
            '/send-message/', data=data_test, format='json')

        response = SendMessageView.as_view()(request)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)