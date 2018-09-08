# shuffle two list
def shuffle_list(list_1, list_2):
    from random import shuffle
    shuffle(list_1)
    shuffle(list_2)
    length = len(list_1)
    # make sure there is no collision
    for i in range(length):
        if(list_1[i] == list_2[i]):
            shuf(list_1, list_2)
        else:
            return zip(list_1, list_2)
        
def main(*people):
    giver = []
    giver.extend(people)
    receiver = []
    receiver.extend(people)
    the_list = shuffle_list(giver, receiver)
    gifting = dict(the_list)
    return gifting


if __name__ == "__main__":
    main("red",  "orange", "yellow", "green", "blue", "indigo", "violet")