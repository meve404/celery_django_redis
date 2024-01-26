import redis

def run():
    r = redis.Redis(host='localhost', port=6379, db=0)

    channel = "example_channel"
    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    print(f"Subscribed to {channel} channel. Waiting for messages...")

    # Infinate loop to listen for messages
    for message in pubsub.listen():
        if message["type"] == "message":
            decoded_message = message['data'].decode('utf-8')
            print(f"Received message: {decoded_message}")

if __name__ == "__main__":
    run()
    