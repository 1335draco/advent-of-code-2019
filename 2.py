
def parse_intcode(input_values):
    values = input_values.copy()
    for val_index in range(0, len(values) - 4, 4):
        # print(val_index)
        if values[val_index] == 1:
            # print("Encountered ADD op code")
            sum = values[values[val_index + 1]] + values[values[val_index + 2]]
            values[values[val_index + 3]] = sum
        elif values[val_index] == 2:
            # print("Encountered MULTIPLY op code")
            product = values[values[val_index + 1]] * values[values[val_index + 2]]
            values[values[val_index + 3]] = product
        elif values[val_index] == 99:
            # print("Encountered HALT op code")
            break
        else:
            print("Encountered UNKNOWN op code")

    return values


if __name__ == '__main__':
    input_file = "input_files/2.txt"
    with open(input_file, "r") as in_file:
        line = in_file.readline()
        values = line.split(",")
        true_values = [int(val) for val in values]

        for noun in range(0,99):
            for verb in range(0,99):
                test_values = true_values
                test_values[1] = noun
                test_values[2] = verb
                # print(test_values)
                output_values = parse_intcode(test_values)

                if output_values[0] == 19690720:
                    print("ENCOUNTERED!!")
                    print(100 * noun + verb)
                    break





