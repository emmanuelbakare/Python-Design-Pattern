class Object:
    def __init__(self, id):
        self.id = id

    def reset(self):
        # Reset object state if necessary
        pass

class ObjectPoolManager:
    def __init__(self, max_objects):
        self.max_objects = max_objects
        self.available_objects = []
        self.in_use_objects = []

        for i in range(max_objects):
            self.available_objects.append(Object(i))

    def acquire_object(self):
        if self.available_objects:
            obj = self.available_objects.pop()
            self.in_use_objects.append(obj)
            return obj
        else:
            raise Exception("No objects available in the pool.")
        
    def release_object(self, obj):
        obj.reset()
        self.in_use_objects.remove(obj)
        self.available_objects.append(obj)


# Usage example
pool = ObjectPoolManager(5)

# Acquire objects from the pool
obj1 = pool.acquire_object()
obj2 = pool.acquire_object()

print(obj1.id)
print(obj2.id) 

print("Available Object: ",len(pool.available_objects), ",Object in Use: ", len(pool.in_use_objects))

# Release objects back to the pool
pool.release_object(obj1)
pool.release_object(obj2)

print("Object in Use: ", len(pool.in_use_objects), "Available Object: ",len(pool.available_objects))

# Acquire objects again
obj1 = pool.acquire_object()
obj2 = pool.acquire_object()
obj3 = pool.acquire_object()
obj4 = pool.acquire_object()
obj5 = pool.acquire_object()

print(f"Obj1:{obj1.id},Obj2:{obj2.id},Obj3:{obj3.id},Obj4:{obj4.id},Obj5:{obj5.id}")

print("Object in Use: ", len(pool.in_use_objects), "Available Object: ",len(pool.available_objects))

print("Check for more objects")
obj6 = pool.acquire_object()