#my_settings.property

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'passu',
        'USER': 'moo',
        'HOST': 'ls-ec3cf2622c477164fd649319d251bcffbc0f7ab7.cjq3ivmixgfe.ap-northeast-2.rds.amazonaws.com',
        'PASSWORD': '1234',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}