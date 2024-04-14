def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

def test_get_formatted_name():
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'