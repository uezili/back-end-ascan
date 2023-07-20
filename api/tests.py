from django.test import TestCase

# Create your tests here.


from .serializer import  UserSerializer

class SendMessageViewTestCase(TestCase):

    def test_user_serializer(self):
        # Teste para verificar a serialização e desserialização adequada do UserSerializer
        user_data = {'full_name': 'Wesley Maciel'}
        user_serializer = UserSerializer(data=user_data)
        self.assertTrue(user_serializer.is_valid())
        user_object = user_serializer.save()

        serialized_user = UserSerializer(user_object)
        self.assertEqual(user_data['full_name'], serialized_user.data['full_name'])
        self.assertEqual(user_object.id, serialized_user.data['id'])
