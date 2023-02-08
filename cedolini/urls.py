from django.urls import path, re_path
from .views import Stipendi, CedoliniList, CreaCedolino, CedolinoDetailView, createIncForf
from .apiviews import getCedolino, saveCedolino, setOre

app_name = "cedolini"

urlpatterns= [ 
                
    #Cedolini
    path('stipendi/',Stipendi.as_view(), name="stipendi"),
    path('crea-cedolino/',CreaCedolino.as_view(), name="crea-cedolino"),
    path('cedolini/', CedoliniList.as_view(), name="cedolini"),
    path('cedolino/<int:id_cedolino>', CedolinoDetailView.as_view(), name="cedolino"),
    path('cedolino',getCedolino,name="getCedolino"),
    path('save-cedolino/<int:id_cedolino>',saveCedolino,name="saveCedolino"),
    path('set-ore/<int:id_cedolino>',setOre, name="setOre"),
    
    #Inline Formset
    path('add_inc_forf<int:id_cedolino>', createIncForf, name='add_inc_forf')

]