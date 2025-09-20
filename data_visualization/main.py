import matplotlib.pyplot as plt

def main():
    print("Hello from data-visualization!")

    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Create a simple line plot
    plt.plot(x, y)
    plt.title("Sample Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


if __name__ == "__main__":
    main()
