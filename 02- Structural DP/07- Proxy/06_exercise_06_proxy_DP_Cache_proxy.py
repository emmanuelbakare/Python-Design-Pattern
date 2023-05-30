from abc import ABC, abstractmethod

# Subject interface
class Subject(ABC):
    @abstractmethod
    def request(self, key):
        pass

# Real subject implementation
class RealSubject(Subject):
    def request(self, key):
        print(f"RealSubject: Processing request for key '{key}'")
        return f"Data for key '{key}'"
    
# Cache proxy
class CacheProxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject
        self.cache = {}

    def request(self, key):
        if key in self.cache:
            print(f"CacheProxy: Returning cached data for key '{key}'")
            return self.cache[key]
        else:
            data = self.real_subject.request(key)
            self.cache[key] = data
            print(f"CacheProxy: Caching data for key '{key}'")
            return data
        

cache_proxy = CacheProxy(RealSubject())

# First request - data will be fetched from the real subject and cached

result1 = cache_proxy.request("key1")
print(result1) 
print()
# Second request - data will be fetched from the cache
result2 = cache_proxy.request("key1")
print(result2)
print()


result3 = cache_proxy.request("key2")
print(result3) 
print()

result4 = cache_proxy.request("key2")
print(result4) 
print()