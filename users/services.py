from .serializers import (UserCreateSerializer,
                          UserUpdateSerializer,
                          UserDeleteSerializer,)


# CREATE USER

def create_user(data):
    serializer = UserCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

# PUT USER
# put/patch update lar farqi
def update_user(user, data):
    serializer = UserUpdateSerializer(instance=user, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()



# DELETE USER
def delete_user(user):
    serializer = UserDeleteSerializer(instance=user)
    user.delete()
    # user.is_active=False
    # user.save()