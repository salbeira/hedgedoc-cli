import requests
from fetch import fetch as fetch

def replace(url: str, content: str, id: str, verbose: bool=False, silent: bool=False) -> None:
    """Replaces the content of the note with the given id with the given content.

    Parameters
    ----------
    url : str
        The URL of the hedgedoc instance to talk to.
    content: str
        The content that should replace the former content of the given note.
    id: str
        The id or alias of the note to replace.
    verbose: bool
        Check if you want all the output.
    silent: bool
        Check if you want none of the output.

    Returns
    -------
    None

    """
    header = {"content-type": "text/markdown"}
    full_url = f"{url}/notes" if id is None else f"{url}/notes/{id}"
    if(verbose):
        print(f"[INFO] Updating note: {full_url}")
    response = requests.put(full_url, headers=header, data=content)
    print(response)
    if response.status_code != 200:
        print(f"[ERROR {response.status_code} {response.reason}] {response.json()['message']}")
        return
    print(response.text)
    return


def append(url: str, content: str, id: str, verbose: bool=False, silent: bool=False) -> str:
    """Updates the content of the note with the given id by appending the given content to the note's content.

    Parameters
    ----------
    url : str
        The URL of the hedgedoc instance to talk to.
    content: str
        The content that should be appended to the given note.
    id: str
        The id or alias of the note to replace.
    verbose: bool
        Check if you want all the output.
    silent: bool
        Check if you want none of the output.

    Returns
    -------
    str
        The content of the new note.

    """
    previous_content = fetch(url, id, verbose, silent)
    new_content = previous_content + "\n" + content
    replace(url, new_content, id, verbose, silent)
    return new_content


