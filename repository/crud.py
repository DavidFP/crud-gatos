import redis
class crud():
    def __init__(self):
        self.db = redis.Redis(host="localhost",
                              port=6379, db=0)
    pass

    def create(self, animal):
        """
        The function creates a new entry for an animal in a database with its attributes and returns the
        animal's ID.
        
        :param animal: It looks like the `create` method is a function that creates a new entry for an
        animal in a database. The function takes an `animal` object as a parameter, which likely has
        attributes such as `nombre`, `edad`, `color`, and `peso`
        :return: The `create` method is returning the `animal_id` of the newly created animal in the
        database.
        """
        animal_id = self.db.incr('animal_counter')
        self.db.hmset(f"animal:{animal_id}",
                      {
                          "nombre":animal.nombre,
                          "edad":animal.edad,
                          "color":animal.color,
                          "peso":animal.peso
                      })
        return animal_id
    
    def get(self, animal_id):
        """
        The `get` function retrieves and decodes information about a specific animal from a database.
        
        :param animal_id: The `get` method in the code snippet is used to retrieve information about an
        animal from a database based on the provided `animal_id`. The method fetches the data stored in the
        database for the specified animal ID, decodes the byte strings to UTF-8 format, and returns the
        information as
        :return: The `get` method is returning a dictionary containing the decoded key-value pairs of an
        animal record fetched from a Redis database using the `hgetall` command. The keys and values are
        decoded from bytes to UTF-8 strings before being returned.
        """
        animal = self.db.hgetall(f"animal:{animal_id}")
        animal_decoded = {k.decode('utf-8'): v.decode('utf-8') for k, v in animal.items()}
        return animal_decoded
    
    def getAll(self):
        """
        The `getAll` function retrieves all animal data from a database and returns it as a list of
        dictionaries with decoded keys and values.
        :return: The `getAll` method returns a list of dictionaries, where each dictionary represents an
        animal stored in the database. The keys of the dictionaries are decoded from bytes to strings using
        UTF-8 encoding.
        """
        keys = self.db.keys(f"animal:*")  
        animals = []
        for key in keys:
            animal = self.db.hgetall(key)
            animal_decoded = {k.decode('utf-8'): v.decode('utf-8') for k, v in animal.items()}
            animals.append(animal_decoded)
        return animals

    def update(self,animal_id=None, animal=None):
        """
        The `update` function takes an `animal_id` and an `animal` object, and updates the corresponding
        fields in a database based on the attributes of the `animal` object.
        
        :param animal_id: The `animal_id` parameter in the `update` method is used to specify the identifier
        of the animal that needs to be updated in the database. It is a unique identifier that helps to
        locate the specific animal record in the database for updating its information
        :param animal: The `update` method in the code snippet is designed to update information about an
        animal in a database. The method takes two parameters:
        :return: The `animal_id` is being returned.
        """
        if animal_id and animal:
            if animal.nombre:
                self.db.hset(animal_id,animal.nombre)
            if animal.edad:
                self.db.hset(animal_id,animal.edad)
            if animal.color:
                self.db.hset(animal_id,animal.color)
            if animal.peso:
                self.db.hset(animal_id,animal.peso)
        return animal_id
    
    def delete(self, animal_id=None):
        """
        The `delete` function deletes an animal record from the database based on the provided `animal_id`.
        
        :param animal_id: The `delete` method in the code snippet you provided is a method that deletes an
        animal record from a database based on the `animal_id` provided. If an `animal_id` is provided as an
        argument to the method, it will call the `delete` method of the `db` object
        :return: The `animal_id` variable is being returned. If `animal_id` is provided and not `None`, the
        method will delete the corresponding animal record from the database and then return the
        `animal_id`. If `animal_id` is `None`, then `None` will be returned without deleting anything from
        the database.
        """
        if animal_id:
            self.db.delete(animal_id)
        return animal_id