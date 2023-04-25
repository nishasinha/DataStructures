def get_overlapping_intervals(data):
    print("Input:", data)

    sorted_data = sorted(data, key=lambda x: x[1])
    print("Sorted data:", sorted_data)

    result = []
    window = []
    for entry in sorted_data:
        print("\nWorking on: ", entry)
        start = entry[0]
        end = entry[1]

        if len(window) == 0:
            window = [start, end]
            print("Current window:", window)
            continue

        if start <= window[1]:
            print("{} overlaps in: {}".format(entry, window))
            window[1] = end
            print("Current window:", window)
        else:
            print("{} NOT overlaps in: {}".format(entry, window))
            result.append(window)
            window = [start, end]
            print("Current window:", window)

    result.append(window)
    print("\nResult is:", result)


def main():
    data = [(10, 12), (9, 10), (10, 11), (10, 13), (20, 21)]
    get_overlapping_intervals(data)


if __name__ == '__main__':
    main()
