from django.apps import AppConfig


class AryaConfig(AppConfig):
    name = 'arya'

    # Django启动时自动扫描所有app下面的arya模块
    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('arya')
