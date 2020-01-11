from datetime import date
import uuid
from posts.models import User

def generate_users():
    users = [

        {
            'email': 'xvrgonzalez21_' +str(i) +'@gmail.com',
            'first_name': 'Javier_' + str(i),
            'last_name': 'Gonzalez_'+str(i),
            'password': uuid.uuid1(),
        }

        for i in range(100)
    ]

    for user in users:
        o = User.objects.create(**user)
    print ("done")
