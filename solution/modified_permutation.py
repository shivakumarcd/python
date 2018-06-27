'''
call generate_permutations("ABC", "PQR")
'''


'''This method generates new permutations by adding new possiblt elements to
new slot '''
def add_new_slot(existing_permutations_list, new_slot_elements):
    new_permutation_list = []
    if(len(existing_permutations_list) == 0):
        for i in range(0, len(new_slot_elements)):
            new_permutation_list.append(new_slot_elements[i])

    for i in range(0, len(new_slot_elements)):
        for j in range(0, len(existing_permutations_list)):
            new_element = existing_permutations_list[j] + new_slot_elements[i];
            new_permutation_list.append(new_element)

    return new_permutation_list
'''
generate permutations by appending new slot
{}- 0 slots
{A,P} - appending new slot with possible values A/B
{AB,PB,AQ,PQ} - appending new slot with possible values  B/Q
{ABC,PBC,AQC,PQC,ABR,PBR,AQR,PQR} - appending new slot with possible values C/R
'''
def generate_permutations(word1, word2):
    list = [];
    for i in range(0, len(word1)):
        new_slot_elements =[];
        new_slot_elements.append(word1[i])
        new_slot_elements.append(word2[i])
        list = add_new_slot(list, new_slot_elements)
    return list

