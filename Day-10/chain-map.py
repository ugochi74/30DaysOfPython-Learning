from collections import ChainMap

defaults = {"debug": False}
env = {"debug": True}

config = ChainMap(env, defaults)

print(f"Resolved 'debug' value: {config['debug']}")

# 2. View the full underlying lookup chain
print("Full lookup maps:", config.maps)
