from publish import publish as publish
from fetch import fetch as fetch
from update import append as append
from update import replace as replace

# This considers that you have an active hedgedoc instance running on http://localhost:3000
def test_publish():
    url = "http://localhost:3000"
    note_id = publish(url, "TEST", None, silent=True)
    assert note_id is not None

def test_replace():
    url = "http://localhost:3000"
    note_id = publish(url, "TEST", None, silent=True)
    replace(url, "DOOM", note_id, silent=True)    
    fetched = fetch(url, note_id, silent=True)
    assert "DOOM" == fetched #Yoda thinking reading this you can

def test_update():
    url = "http://localhost:3000"
    note_id = publish(url, "TEST", None, silent=True)
    new_content = append(url, "DOOM", note_id, silent=True)
    assert "TEST\nDOOM" == new_content #Yoda thinking reading this you can
