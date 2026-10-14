import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("--type")
args = parser.parse_args()

print(args.username)
print(args.type)