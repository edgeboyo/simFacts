from re import split
from config import CredentialsManager

def handleArguments():
    import sys
    if len(sys.argv) != 2:
        raise Exception('The correct usage requires a single command line argument to the facts file. Got %s' % sys.argv)
    return sys.argv[1]

if __name__ == "__main__":
    api = CredentialsManager().createValidAPI()
    facts_path = handleArguments()
    with open(facts_path, "r") as f:
        facts = f.read()
    split_facts = facts.split('\n')
    api.PostUpdate(status=split_facts[0])
    del split_facts[0]
    with open(facts_path, "w") as f:
        f.write("\n".join(split_facts))
