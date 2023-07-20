from django.test import TestCase
from .serializer import UserSerializer, StatusSerializer
from .models import Status


class SerializerTestCase(TestCase):

    def test_user_serializer(self):

        user_data = {'full_name': 'Wesley Maciel'}
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
