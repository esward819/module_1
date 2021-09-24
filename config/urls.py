from app.views import hello_view, hey_you, how_old, Can_I_Take_Your_Order, near_hundred, string_splosion, cat_dog, lone_sum 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('hey/<name>', hey_you),
    path('age-in/<int:end>/<int:birthyear>', how_old),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>', Can_I_Take_Your_Order),
    path('logic-2/lone-sum/<int:a>/<int:b>/<int:c>', lone_sum),
    path('string-2/cat-dog/<str>', cat_dog),
    path('warmup-2/string-splosion/<str>', string_splosion),
    path('warmup-1/near-hundred/<int:n>', near_hundred),
]
