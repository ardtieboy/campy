from flaskr.tripods import tripod, faketripod

_tripod = None

def set_tripod(tpod):
    global _tripod
    if tpod == 'fake':
        print('Returning a fake tripod')
        _tripod = faketripod.Faketripod()
    else:
        print('Returning a real tripod')
        _tripod = tripod.Tripod()

def get_tripod():
    global _tripod
    print(_tripod)
    return _tripod