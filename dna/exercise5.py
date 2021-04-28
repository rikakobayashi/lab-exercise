import re


def amino_acid_in_genbank(file_name):
    f = open(file_name, "r")
    is_origin = False
    seq = ''

    for line in f:
        if "ORIGIN" in line:
            is_origin = True
        elif is_origin:
            seq += re.sub('[^actg]', '', line)
        elif "//" in line:
            break

    return dna_to_amino_acid(seq)


def dna_to_amino_acid(dna_seq):
    dna_amino_acid = {
        'aaa': 'K', 'aac': 'N', 'aag': 'K', 'aat': 'N',
        'aca': 'T', 'acc': 'T', 'acg': 'T', 'act': 'T',
        'aga': 'R', 'agc': 'S', 'agg': 'R', 'agt': 'S',
        'ata': 'I', 'atc': 'I', 'atg': 'M', 'att': 'I',
        'caa': 'Q', 'cac': 'H', 'cag': 'Q', 'cat': 'H',
        'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'cct': 'P',
        'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgt': 'R',
        'cta': 'L', 'ctc': 'L', 'ctg': 'L', 'ctt': 'L',
        'gaa': 'E', 'gac': 'D', 'gag': 'E', 'gat': 'D',
        'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gct': 'A',
        'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggt': 'G',
        'gta': 'V', 'gtc': 'V', 'gtg': 'V', 'gtt': 'V',
        'taa': '*', 'tac': 'Y', 'tag': '*', 'tat': 'Y',
        'tca': 'S', 'tcc': 'S', 'tcg': 'S', 'tct': 'S',
        'tga': '*', 'tgc': 'C', 'tgg': 'W', 'tgt': 'C',
        'tta': 'L', 'ttc': 'F', 'ttg': 'L', 'ttt': 'F'
    }

    amino_acid_seq = ''
    for i in range(0, len(dna_seq), 3):
        amino_acid = dna_amino_acid[dna_seq[i:i + 3]]
        if amino_acid == "*":
            break
        amino_acid_seq += amino_acid

    return amino_acid_seq


# print(amino_acid_in_genbank("sequence.gb"))
