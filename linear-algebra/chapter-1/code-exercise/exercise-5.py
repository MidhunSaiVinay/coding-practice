# exercise_2_5.py

def transpose_row_to_column(vector):
    column_vector = []
    for element in vector:
        column_vector.append([element])
    return column_vector

# Example usage
row_vector = [1, 2, 3, 4]
column_vector = transpose_row_to_column(row_vector)
print("Column Vector:", column_vector)