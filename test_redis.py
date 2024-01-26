import redis

r = redis.Redis(host="localhost", port=6379, db=0) # Connect to redis
setter = r.set('foo', 'bar') # Sets the key value
getter = r.get('foo') # Retrieves the value from Key foo

print('setter:', setter, '\nGetter:', getter)
