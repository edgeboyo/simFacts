from re import split
from config import CredentialsManager


def handleArguments():
    import sys

    if len(sys.argv) != 2:
        raise Exception(
            "The correct usage requires a single command line argument to the facts file. Got %s"
            % sys.argv
        )
    return sys.argv[1]


def handleMessage(api, facts):
    message = facts[0]
    attachment_url = None
    del facts[0]

    if len(facts) > 0 and len(facts[0]) > 0 and facts[0][0] == "#":
        attachment_url = facts[0][1:]
        del facts[0]

    api.PostUpdate(status=message, media=attachment_url)
    return facts


if __name__ == "__main__":
    api = CredentialsManager().createValidAPI()
    facts_path = handleArguments()
    with open(facts_path, "r") as f:
        facts = f.read()
    remaining_facts = handleMessage(api, facts.split("\n"))
    with open(facts_path, "w") as f:
        f.write("\n".join(remaining_facts))
