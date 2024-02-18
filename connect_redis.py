import redis

def main():
  r = redis.Redis(
    host='redis-10436.c302.asia-northeast1-1.gce.cloud.redislabs.com',
    port=10436,
    password='2Z66YwyA2kdWtVxbAhP6G79u0A0tILrM')
  print(r.ping())
  print(r.set("my_name", "wangzirui"))
  print(r.get("my_name"))
  print(r.exists("my_name"))
  print(r.exists("random"))
  print(r.delete("my_name"))
  print(r.exists("my_name"))

if __name__ == '__main__':
    main()