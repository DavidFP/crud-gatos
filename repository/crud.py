import redis

class crud():
    def __init__(self):
        self.db = redis.Redis(host="localhost",
                              port=6379, db=0)
    pass
    def create(self, animal):
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
        animal = self.db.hgetall(f"animal:{animal_id}")
        animal_decoded = {k.decode('utf-8'): v.decode('utf-8') for k, v in animal.items()}
        return animal_decoded
    
    def getAll(self):
        keys = self.db.keys(f"animal:*")  
        animals = []
        for key in keys:
            animal = self.db.hgetall(key)
            animal_decoded = {k.decode('utf-8'): v.decode('utf-8') for k, v in animal.items()}
            animals.append(animal_decoded)
        return animals

    def update(self,animal_id=None, animal=None):
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
        if animal_id:
            self.db.delete(animal_id)
        return animal_id
        