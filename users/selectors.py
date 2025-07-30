"""
    Bu yerdagi method lar faqat data ni olish (GET) uchun ishlatiladi.
    Database bilan ishlanadi lekin hech qanday action qilinmaydi yani CREATE UPDATE DELETE
"""
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
# from django.core.exeptions import ObjectDoesNotExist
User = get_user_model()

# hamma user ni olib keladi
def get_users_list():
    users = User.objects.all()
    return UserSerializer(users, many=True).data
    # return User.objects.filter(is_active=True)

""" 
    user id boyicha user olib keladi
    get_user_by_id() – berilgan user_id bo‘yicha userni qidiradi va topadi
    topolmasa — None qaytaradi
"""
def get_user_by_id(user_id):
    return User.objects.filter(id=user_id).first()

""" 
def get_user_by_id(user_id):
     try:
         User.objects.get(id=user_id)
     except:
         User.DoesNotExist
         return None
"""



