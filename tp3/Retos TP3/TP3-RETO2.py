#ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA

import re

aminoacidConvertionDictionary = {
  "F": "UUU",
  "F": "UUC",
  "L": "UUA",
  "L": "UUG",
  "L": "CUU",
  "L": "CUC",
  "L": "CUA",
  "L": "CUG",
  "I": "AUU",
  "I": "AUC",
  "I": "AUA",
  "M": "AUG",
  "V": "GUU",
  "V": "GUC",
  "V": "GUA",
  "V": "GUG",
  "S": "UCU",
  "S": "UCC",
  "S": "UCA",
  "S": "UCG",
  "P": "CCU",
  "P": "CCC",
  "P": "CCA",
  "P": "CCG",
  "T": "ACU",
  "T": "ACC",
  "T": "ACA",
  "T": "ACG",
  "A": "GCU",
  "A": "GCC",
  "A": "GCA",
  "A": "GCG",
  "Y": "UAU",
  "Y": "UAC",
#   "": "UAA",
#   "": "UAG",
  "H": "CAU",
  "H": "CAC",
  "E": "CAA",
  "E": "CAG",
  "D": "AAU",
  "D": "AAC",
  "K": "AAA",
  "K": "AAG",
  "N": "GAU",
  "N": "GAC",
  "Q": "GAA",
  "Q": "GAG",
  "C": "UGU",
  "C": "UGC",
#   "": "UGA",
  "W": "UGG",
  "R": "CGU",
  "R": "CGC",
  "R": "CGA",
  "R": "CGG",
  "S": "AGU",
  "S": "AGC",
  "R": "AGA",
  "R": "AGG",
  "G": "GGU",
  "G": "GGC",
  "G": "GGA",
  "G": "GGG"
}

def encodeARNFromAA(aminoacidString):
    aaList = re.findall('.',aminoacidString)
    arn = ''
    for aa in aaList:
        arn += aminoacidConvertionDictionary[aa]
    return arn
    
aaInput = input("Please enter an aminoacid sequence: ").upper()
print("You entered: " + aaInput)
print("Result: " + encodeARNFromAA(aaInput))