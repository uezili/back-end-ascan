from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

#    def ready(self):
#        from api.consumer import SubscriptionProcessor2
#        import sys
#        # from time import sleep
#        # sleep(10)
#        try:
#            SubscriptionProcessor2().start()
#        except:
#            # sys.exit(1)
#            print("deu não boy!")

    # SubscriptionProcessor2().start()
