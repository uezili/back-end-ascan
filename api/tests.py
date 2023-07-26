from django.test import TestCase
from .serializer import UserSerializer, StatusSerializer
from .models import Status

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
        self.assertEqual(user_data['full_name'], serialized_user.data['full_name'])
        self.assertEqual(user_object.id, serialized_user.data['id'])

    def test_status_serializer(self):

        status_active = Status.objects.create(name='active')
        status_canceled = Status.objects.create(name='canceled')

        status_serializer_active = StatusSerializer(status_active)
        status_serializer_canceled = StatusSerializer(status_canceled)

        self.assertEqual(status_active.id, status_serializer_active.data['id'])
        self.assertEqual('active', status_serializer_active.data['name'])

        self.assertEqual(status_canceled.id, status_serializer_canceled.data['id'])
        self.assertEqual('canceled', status_serializer_canceled.data['name'])

class RegisterUserViewTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
    
    @patch('pika.BlockingConnection')
    def test_register_user_view_success(self, mock_connection):
        mock_channel = MagicMock()
        mock_connection.return_value.__enter__.return_value.channel.return_value = mock_channel

        data = {
            "full_name": "John Doe"
        }
        response = self.client.post('/users/', data, format='json')
        
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], data['full_name'])


class SendMessageViewTestCase(TestCase):


    # @patch('pika.BlockingConnection')
    # def test_send_message_view_success(self, mock_connection):
    #     # mock_channel = MagicMock()
    #     # mock_connection.return_value.__enter__.return_value.channel.return_value = mock_channel

    #     data = {
    #         "event_type": "SUBSCRIPTION_PURCHASED",
    #         "data": {
    #             "user_id": 1
    #         }
    #     }
    #     response = self.client.post('/send_message/', data, format='json')
    #     print("response.status_code: ", response.status_code)
    #     # print("response.data: ", response.data)

    #     self.assertEqual(response.status_code, HTTP_201_CREATED)
    #     self.assertEqual(
    #         response.data, {"success": "Message sent successfully."})

    #     # Assert that the mocked RabbitMQ was called with the correct data
    #     mock_channel.basic_publish.assert_called_once_with(
    #         exchange='event_history', routing_key='',
    #         body='{"event_type": "SUBSCRIPTION_PURCHASED", "data": {"user_id": 1}}'
    #     )

    # @patch('pika.BlockingConnection')
    # def test_send_message_view_bad_request(self, mock_connection):
    #     # Test POST without data
    #     response = self.client.post('/send-message/', {}, format='json')
    #     self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    #     # Test POST with unknown event_type
    #     data = {
    #         "event_type": "UNKNOWN_EVENT",
    #         "data": {
    #             "user_id": 1
    #         }
    #     }
    #     response = self.client.post('/send_message/', data, format='json')
    #     self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

# class RegisterNewUserViewTestCase(TestCase):

#     def setUp(self):
#         self.client = APIClient()

# from django.test import TestCase
# from rest_framework.test import APIRequestFactory
# from rest_framework import status
# from django.urls import reverse
# from .models import User, Subscription, EventHistory, Status
# from .views import SendMessageView

# class SendMessageViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.url = reverse('send-message')
#         self.user = User.objects.create(id=1, username='test_user')

#     def test_subscription_purchased(self):
#         data = {
#             'event_type': 'SUBSCRIPTION_PURCHASED',
#             'data': {'user_id': self.user.id}
#         }
#         request = self.factory.post(self.url, data, format='json')
#         response = SendMessageView.as_view()(request)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Subscription.objects.count(), 1)
#         self.assertEqual(EventHistory.objects.count(), 1)

#     def test_subscription_canceled(self):
#         status_canceled = Status.objects.create(name='canceled')
#         subscription = Subscription.objects.create(user=self.user, status=status_canceled)

#         data = {
#             'event_type': 'SUBSCRIPTION_CANCELED',
#             'data': {'subscription_id': subscription.id}
#         }
#         request = self.factory.post(self.url, data, format='json')
#         response = SendMessageView.as_view()(request)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         subscription.refresh_from_db()
#         self.assertEqual(subscription.status.name, 'canceled')
#         self.assertEqual(EventHistory.objects.count(), 2)

#     def test_subscription_restarted(self):
#         status_active = Status.objects.create(name='active')
#         subscription = Subscription.objects.create(user=self.user, status=status_active)

#         data = {
#             'event_type': 'SUBSCRIPTION_RESTARTED',
#             'data': {'subscription_id': subscription.id}
#         }
#         request = self.factory.post(self.url, data, format='json')
#         response = SendMessageView.as_view()(request)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         subscription.refresh_from_db()
#         self.assertEqual(subscription.status.name, 'active')
#         self.assertEqual(EventHistory.objects.count(), 3)

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from api.models import Subscription, Status
from api.views import SendMessageView


class SendMessageViewTest(TestCase):

    def test_process_subscription_purchased(self):
        factory = APIRequestFactory()
        request = factory.post('/localhost/send_message/', {
            'event_type': 'SUBSCRIPTION_PURCHASED',
            'data': {
                'user_id': 1,
            },
        }, content_type='application/json')

        view = SendMessageView()
        response = view.post(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['success'], 'Register successfully.')

        subscription = Subscription.objects.get(id=1)
        self.assertEqual(subscription.status_id, Status.objects.get(name='active').id)
