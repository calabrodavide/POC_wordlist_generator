from itertools import permutations

def generate_permutations(keywords : list[str], max_length : int) -> set:
    all_permutations = set()
    keywords_with_caps = keywords + [keyword.upper() for keyword in keywords]
    for length in range(1, max_length + 1):
        for perm in permutations(keywords_with_caps, length):
            all_permutations.add(''.join(perm))
    return all_permutations

def read_keywords(file : str) -> list:
    with open(file, 'r') as file:
        return file.read().splitlines()
    
def write_permutations(file : str, perms : set) -> None:
    with open(file, 'w') as file:
        for perm in perms:
            file.write(perm + '\n')
    
# read keywords from file
keywords = read_keywords('./keywords.txt')

max_length = 3

perms = generate_permutations(keywords, max_length)

# write permutations to file
write_permutations('./permutations.txt', perms)