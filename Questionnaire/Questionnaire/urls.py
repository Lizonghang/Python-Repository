from django.conf.urls import url, handler404, handler500, include
from question_naire.views import *
from django.contrib import admin

handler404 = 'question_naire.views.bad_request'
handler500 = 'question_naire.views.server_error'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^regist/$', register),
    url(r'^select/$', choose_template),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^delete/$', delete),
    url(r'^head_sculpture/$', head_sculpture),
    url(r'^set_head_img/$', set_head_img),
    url(r'^delete_question/$', delete_question),
    url(r'^search/$', search),
    url(r'^search_result/$', search_result),
    # url(r'^clear_all_user/$', clear_all_user),
    url(r'^code/$', code),
    url(r'^interact/$', interact),
    url(r'^select/agreement/$', agreement),
    url(r'^select/template_1/$', template_1),
    url(r'^select/success/$', submit_success),
    url(r'^select/list/$', user_list),
    url(r'^select/collect/$', collect),
    url(r'^select/collect_log/$', collect_log),
    url(r'^select/isCollected/$', is_collected),
    url(r'^select/re_edit/$', re_edit),
    url(r'^select/template_1/edit/$', edit_template_1),
    url(r'^select/template_1/view/$', view),
    url(r'^select/template_1/analysis/$', analysis),
    url(r'^submit/welcome/$', welcome),
    url(r'^submit/welcome/realHandler/$', real_handler),
    url(r'^submit/welcome/realHandler/endPublish/$', end_publish),
    url(r'^$', home_page),
]
