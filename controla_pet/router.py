from django.conf import settings


class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):

        if model._meta.app_label:
            if model._meta.app_label in settings.DATABASE_APPS_MAPPING.keys():
                return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
            return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label:
            if model._meta.app_label in settings.DATABASE_APPS_MAPPING.keys():
                return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
            return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label in settings.DATABASE_APPS_MAPPING.keys():
            return settings.DATABASE_APPS_MAPPING[obj1._meta.app_label]
        return None

    def allow_syncdb(self, db, model):
        pass

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in settings.DATABASE_APPS_MAPPING.keys():
            return db == settings.DATABASE_APPS_MAPPING[app_label]
        return None
