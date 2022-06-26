from django.contrib import admin

from user.models import User as UserModel
from user.models import Celler as CellerModel
from user.models import Cart as CartModel
from user.models import PurchaseList as PurchaseListModel
from user.models import PurchaseHistory as PurchaseHistoryModel


admin.site.register(UserModel)
admin.site.register(CellerModel)
admin.site.register(CartModel)
admin.site.register(PurchaseListModel)
admin.site.register(PurchaseHistoryModel)
