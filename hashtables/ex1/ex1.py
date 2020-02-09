#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import HashTable
from hashtables import hash_table_insert
from hashtables import hash_table_retrieve


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index in range(0, len(weights)):
        weight = weights[index]

        match = hash_table_retrieve(ht, limit-weight)
        if match is not None:
            first_index = max(index, match)
            second_index = min(index, match)

            return (first_index, second_index)
        else:
            hash_table_insert(ht, weight, index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
