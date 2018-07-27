from django.conf import settings


class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):
        pass

    def db_for_write(self, model, **hints):
        pass

    def allow_relation(self, obj1, obj2, **hints):
        pass

    def allow_syncdb(self, db, model):
        pass

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """

        if app_label in settings.DATABASE_APPS_MAPPING.keys():
            return db == settings.DATABASE_APPS_MAPPING[app_label]
        return None
