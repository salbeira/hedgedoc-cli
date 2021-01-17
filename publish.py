import requests

def publish(url: str, content: str, id: str, verbose: bool=False, silent: bool=False) -> str:
    """Updates the content of the note with the given id by appending the given content to the note's content.

    Parameters
    ----------
    url : str
        The URL of the hedgedoc instance to talk to.
    content: str
        The content that should be appended to the given note.
    id: str
        The optional id or alias of the note to replace.
    verbose: bool
        Check if you want all the output.
    silent: bool
        Check if you want none of the output.

    Returns
    -------
    str
        The id of the note that got published.
    """
    header = {"content-type": "text/markdown"}
    full_url = f"{url}/notes" if id is None else f"{url}/nodes/{id}"
    if(verbose):
        print(f"[INFO] Publishing note to: {full_url}")
    response = requests.post(full_url, headers=header, data=content)
    if response.status_code != 201:
        print(f"[ERROR {response.status_code} {response.reason}] {response.json()['message']}")
        return
    response_json = response.json()
    response_id = response_json['metadata']['id']
    if(not silent):
        print(f"[SUCCESS] You can find the published note under: {url}/n/{response_id}")
    return response_id