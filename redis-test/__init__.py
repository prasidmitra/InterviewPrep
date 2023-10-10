import redis

r = redis.Redis(
    host='localhost',
    port=32768,
    password='redispw')

r.set('foo', 'bar')
value = r.get('foo')
print(value)