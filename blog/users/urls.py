#进行users子应用的视图路由
from django.urls import path
from users.views import RegisterView, SmsCodeView, LoginView, LogoutView, ForgetPasswordView, UserCenterView, \
    WriteBlogView
from users.views import ImageCodeView
urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/',RegisterView.as_view(),name='register'),
    #图片验证
    path('imagecode/', ImageCodeView.as_view(),name='imagecode'),
    #短信验证
    path('smscode/', SmsCodeView.as_view(),name='smscode'),
    #登录路由
    path('login/', LoginView.as_view(),name='login'),
    #退出路由
    path('logout/', LogoutView.as_view(),name='logout'),
    #忘记密码
    path('forgetpassword/', ForgetPasswordView.as_view(),name='forgetpassword'),
    #个人中心
    path('center/', UserCenterView.as_view(),name='center'),
    #写文章
    path('writeblog/', WriteBlogView.as_view(),name='writeblog'),
]