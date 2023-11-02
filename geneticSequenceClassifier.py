def classify(sequence):
    sequence = sequence.upper()
    valid_dna = set("ATGC")
    valid_rna = set("AUGC")
    if set(sequence) <= valid_dna:
        return "DNA"
    elif set(sequence) <= valid_rna:
        return "RNA"
    else:
        return "Invalid sequence"

while True:
    sequence = str(input("Enter the sequence: "))
    result = classify(sequence)
    if result != "Invalid sequence":
        print(f"The sequence is classified as {result}")
    else:
        print("Error: Invalid sequence")

