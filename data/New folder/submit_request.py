# import redis
# import json
# from rsmq import RedisSMQ
# import uuid
# import logging
# from datetime import datetime
# from enum import IntEnum

# logging.getLogger().setLevel(logging.INFO)

# # Intialize redis queue,cache and metadata
# queue = redis.StrictRedis(
#     host="localhost",
#     port=6395,
# password=""
# )
# redis_queue = RedisSMQ(client=queue)

# redis_cache = redis.StrictRedis(
#     host="localhost",
#     port=6392,
# password=""
# )
# redis_metadata = redis.StrictRedis(
#     host="localhost",
#     port=6391,
# password=""
# )
