import requests
import sys
from datetime import datetime

class Metadata:
    """
    Attributes
    ----------
    id : str
        Desc.
    alias : str
        Desc.
    title : str
        Desc.
    description : str
        The description of this note.
    tags : [str]
        Desc.
    updateDate : datetime
        Desc.
    createDate : datetime
        Desc.
    viewCount : int
        Desc.

    """
    def __init__(self, json : dict):
        self.id = json['id']
        self.alias = json['alias']
        self.title = json['title']
        self.description = json['description']
        self.tags = json['tags']
        updateTime = json['updateTime']
        self.updateDate = datetime.strptime(updateTime, "%Y-%m-%dT%H:%M:%S.%fZ")
        createdTime = json['createTime']
        self.createDate = datetime.strptime(createdTime, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.viewCount = json['viewCount']

    def __str__(self):
        return f"Created At: {self.createDate}\nLast Update: {self.updateDate}\nID: {self.id}\nAlias: {self.alias}\nTitle: {self.title}\nDescription: {self.description}\nView Count: {self.viewCount}"


class Permission:
    def __init__(self, json : dict):
        self.owner = json['owner']
        self.users = json['sharedToUsers']
        self.groups = json['sharedToGroups']

    def __str__(self):
        return f"Owner: {self.owner}\nUsers: {','.join(self.users)}\nGroups: {','.join(self.groups)}"

def fetch(url: str, id: str, verbose: bool=False, silent: bool=False) -> str:
    """Fetches the content of the note with the given id.

    Parameters
    ----------
    url : str
        The URL of the hedgedoc instance to talk to.
    id: str
        The id or alias of the note to replace.
    verbose: bool
        Check if you want all the output.
    silent: bool
        Check if you want none of the output.

    Returns
    -------
    str
        The content of the requested note.

    """
    full_url = f"{url}/notes/{id}/content"
    if(verbose):
        print(f"[INFO] Fetching note: {full_url}")
    response = requests.get(full_url)
    if response.status_code != 200:
        print(f"[ERROR {response.status_code} {response.reason}] {response.json()['message']}")
        return
    content = response.text
    return content


def metadata(url: str, id: str, verbose: bool=False, silent: bool=False) -> Metadata:
    """Fetches the metadata of the note with the given id.

    Parameters
    ----------
    url : str
        The URL of the hedgedoc instance to talk to.
    id: str
        The id or alias of the note to replace.
    verbose: bool
        Check if you want all the output.
    silent: bool
        Check if you want none of the output.

    Returns
    -------
    str
        The content of the requested note.

    """
    full_url= f"{url}/notes/{id}/metadata"
    if(verbose):
        print(f"[INFO] GET {full_url}")
    response = requests.get(full_url)
    if response.status_code != 200:
        print(f"[ERROR {response.status_code} {response.reason}] {response.json()['message']}", file=sys.stderr)
        return
    meta = Metadata(response.json())
    return meta


def permissions(url: str, id: str, verbose: bool=False, silent: bool=False) -> Permission:
    full_url= f"{url}/notes/{id}/metadata"
    if(verbose):
        print(f"[INFO] GET {full_url}")
    response = requests.get(full_url)
    if response.status_code != 200:
        print(f"[ERROR {response.status_code} {response.reason}] {response.json()['message']}", file=sys.stderr)
        return
    perms = Permission(response.json()['permissions'])
    return perms