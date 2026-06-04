import redis
import json

def process_event(event):
    print(f"Processing event: {event}")

redis_client = redis.StrictRedis(host='localhost', port=6379)

if __name__ == "__main__":
    print("Worker started...")
    while True:
        _, message = redis_client.blpop("event_queue")
        event = json.loads(message)
        process_event(event)