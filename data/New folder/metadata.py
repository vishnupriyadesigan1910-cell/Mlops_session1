from dmle_common_redis_utils.redis_caching import Caching
import json

bam_coder_metrics_keys={"itemclearing_model": {"production_indicator": "true", "version_date": "2022-12-15T10:04:38:12", "version": "V1", "type": "MODEL", "country": "ANY"}}
# 
#Make a connection to Metadata_Cache
redis_metadata=Caching(
host="localhost",
port=6391,
password="",
is_sentinel=False
)
# 
#load the prediction keys to metadata
for key,value in bam_coder_metrics_keys.items():
   redis_metadata.set_value(key, json.dumps(value))
   print('key=',key)