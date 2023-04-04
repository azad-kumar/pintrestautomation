
# reused codes
from database import database as database_class
import constants as const


class links:
    def __init__(self):
        self.db_obj = None
        self.links = []

    def connect(self):
        host = const.HOST
        user = const.USER
        database = const.DATABASE
        password = const.PASSWORD
        self.db_obj = database_class(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        if self.db_obj.connection is None:
            print('uable to connect to the database with the dependencied')
            return False
        else:
            return True
        
    def fetch_links(self):
        if self.db_obj.connection is None:
            print('please connect to database before swaping data')
            return False
        else:
            data = self.db_obj.swap_table(const.TABLE_NAME)
            for i in data:
                self.links.append(i[0])
        if len(self.links == 0):
            print('link not found')
            return False
        else:
            print('links found')
            return True
    
    def clear_links(self):
        if self.db_obj.connection is None:
            print('please connect to database before erazing data')
            return False
        else:
            self.db_obj.eraze_table(const.TABLE_NAME)
            print('data erazed successfully')
        return True
    



            

        
    
        