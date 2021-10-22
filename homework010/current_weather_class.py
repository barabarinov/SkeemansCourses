import location
import current

class CurrentJsonResponse(object):

    _names = {
        "location":'location',
        "current":'current'
    }

    def __init__(self,
                 location=None,
                 current=None):
        self.location = location
        self.current = current

    def from_dictionary(cls,
                        dictionary):
        if dictionary is None:
            return None

        location = location.Location.from_dictionary(dictionary.get('location'))if dictionary.get('location') else None
        current = current.Current.from_dictionary(dictionary.get('current')) if dictionary.get('location') else None
