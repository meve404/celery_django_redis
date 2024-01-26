import redis

def run():
    r = redis.Redis(host='localhost', port=6379, db=0)

    channel = "example_channel"
    message = "Redis is working as a message broker now"
    r.publish(channel, message)

    integer_message = 69.99
    r.publish(channel, integer_message)

    list_message = "[1,2,3,'a','b','c']"
    r.publish(channel, list_message)

    dict_message = "{'host': 'localhost', 'port':6379}"
    r.publish(channel, dict_message)

    print(f"Messages published to {channel}")

if __name__ == "__main__":
    run()
    