from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index_app'),
    path('upload/', views.upload, name='upload_app'),
    path('list_page/<int:ids>', views.list_page, name='list_page_app'),
    path('final_list_page/<int:ids>', views.final_list_page, name='final_list_page_app'),
    path('pdf_post/', views.pdf_post, name='pdf_post_app'),
    path('pdf_list_page/', views.pdf_list_page, name='pdf_list_page_app'),
    path('pdf_convert/<int:ids>', views.pdf_convert, name='pdf_convert_app'),
    path('pdf_delete/<int:ids>', views.pdf_delete, name='pdf_delete_app'),
    path('order_details_update/<int:ids>', views.order_details_update, name='order_details_update_app'),
    path('order_details_del/', views.order_details_del, name='order_details_del_app'),
]
