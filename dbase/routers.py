from decouple import config

class DBRouter:
    """
        A router to control all database operations on models in the
        dbase application
    """
    maindb = config('BRD_MAIN_DB')
    blogdb = config('BRD_BLOG_DB')
    defaultdb = config('BRD_DJANGO_DB')

    def db_for_read(self, model, **hints):
        # print(f"Read: {self.router} - label: {model._meta.app_label}, model {model} matches, returning {self.thisdb}")
        if model._meta.app_label == 'dbase':
            return 'brd_main'
        elif model._meta.app_label == 'blog':
            return 'brd_blog'
        elif model._meta.app_label == 'mt_tools':
            return 'brd_pending'
        else:
            return 'default'
    
    def db_for_write(self, model, **hints):
        # print(f"Write: {self.router} - label: {model._meta.app_label}, model {model} matches, returning {self.thisdb}")
        if model._meta.app_label == 'dbase':
            return 'brd_main'
        elif model._meta.app_label == 'blog':
            return 'brd_blog'
        elif model._meta.app_label == 'mt_tools':
            return 'brd_pending'
        else:
            return 'default'
   
    def allow_relation(self, obj1, obj2, **hints):
        #rint(f"Relation: {self.router} - labels: {obj1._meta.app_label}/{obj2._meta.app_label} match {self.route_app_labels} - returning True")
        all_dbases = {'dbase', 'blog', 'mt_tools'}

        if obj1._meta.app_label == 'dbase' and obj2._meta.app_label == 'dbase':
            return True
        elif obj1._meta.app_label == 'blog' and obj2._meta.app_label == 'blog':
            return True
        elif obj1._meta.app_label == 'mt_tools' and obj2._meta.app_label == 'mt_tools':
            return True
        elif (
            obj1._meta.app_label not in all_dbases
                and
            obj2._meta.app_label not in all_dbases
        ):
            return True            

        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        #print(f"Migrate: {self.router} - label: {app_label}, model {model_name}, db {db} matches, returning {db==self.thisdb}")
        if app_label == 'dbase':
            return db == 'brd_main'
        elif app_label == 'blog':
            return db == 'brd_blog'
        elif app_label == 'mt_tools':
            return db == 'brd_pending'
        else:
            return db == 'default'
