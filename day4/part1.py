def is_complete_overlap(sec1, sec2):
    if sec1[0] <= sec2[0] and sec1[1] >= sec2[1]:
        return True
    
    if sec2[0] <= sec1[0] and sec2[1] >= sec1[1]:
        return True
    
    return False

with open('input.txt') as f:
    lines = f.read().splitlines()

section_pairs = [[list(map(int, section.split("-"))) for section in line.split(",")] for line in lines]
completed_overlaps = list(filter(lambda pair: is_complete_overlap(pair[0], pair[1]), section_pairs))
print(len(completed_overlaps))