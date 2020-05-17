mappings = {
    0: 'joy',
    1: 'fear',
    2: 'anger',
    3: 'sadness',
    4: 'disgust',
    5: 'shame',
    6: 'guilt'
}


def map_emoji(arr):
    new_arr = []
    for num in arr:
        new_arr.append(mappings[num])
    return new_arr
