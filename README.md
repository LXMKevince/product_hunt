## Django项目创建说明
- 1.在主项目ph的settings.py注册app
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # 自己的app
        'products',
        'account',
    ]
    ```
- 2.主页
    + 2.1 >在主项目ph的urls.py中添加路由(导入include)
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('products.urls')),
    ]
    ```
    + 2.2 >在products中添加urls.py
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.product_list),
    ]
    ```
    + 2.3 >在products中创建文件夹templates，并在文件夹中创建product_list.html
- 3.模板的使用
    + 3.1 >在根目录product_hunt中创建templates文件夹，并创建一个主题模板theme.html中间为替换部分，两端为模板主题样式
    ```html
    这是所有网页的主题样式
    {% block content %}
    
    {% endblock content %}
    这是所有网页的主题样式
    ```
    + 3.2 >在product_list.html中继承主题模板
    这是所有网页的主题样式
    {% block content %}
    
    {% endblock content %}
    这是所有网页的主题样式
    ```
    {% extends "theme.html" %}

    {% block blockname %}
        这是产品页面的重要内容
    {% endblock blockname %}
    ```
    + 3.3 >在在主项目ph的settings.py设置TEMPLATES
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 添加templates路径，在根目录下
            'DIRS': ['templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

