from pymongo import MongoClient

client = MongoClient()
my_collection = client.my_database.my_collection

my_dict = ('name': 'contact Name')

def find_object(my_key):
    """Finds and returns an object matching the primary key.
       Returns None if not found.
    """
    my_object = my_collection.findOne('name': my_key)
    return my_object


def update_object(my_object):
    """Updates an object if it exist, inserts if it does not exist.
    """
    obj_srch = {'name': my_object['name']}
    my_object = my_collection.update(obj_srch, my_objt, upsert=True)
    return None

def remove_object(my_key):
    """Deletes the object matching primary_key.
       Returns True if deleted, False if not found.                             """
    del_result = my_collection.delete_one({'name':my_key})'
    return del_result.deleted_count > 0
