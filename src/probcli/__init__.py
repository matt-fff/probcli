import argparse


def main():
    # Create an argument parser object
    parser = argparse.ArgumentParser(
        description="Calculate the probability of the union of multiple independent events."
    )

    # Add command-line arguments
    parser.add_argument(
        "event_count", type=int, help="The number of independent events."
    )
    parser.add_argument(
        "probability", type=float, help="The probability of each individual event."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Calculate the probability of the union of the events
    complement_probability = 1 - args.probability
    union_probability = 1 - complement_probability**args.event_count

    # Print the result
    print(
        f"The probability of the union of {args.event_count} independent events, each with a probability of {args.probability}, is {union_probability}."
    )


if __name__ == "__main__":
    main()
