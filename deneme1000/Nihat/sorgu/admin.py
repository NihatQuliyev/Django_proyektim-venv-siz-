from django.contrib import admin

from .models import Sual,Cavab             # modellerin tanitimi

admin.site.register(Sual)                  # admin panele sual modelini qeyd etmek

admin.site.register(Cavab)                 # admin panele cavab modelini qeyd etmek