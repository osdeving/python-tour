import matplotlib.pyplot as plt

def main():
    squares = [1, 4, 9, 16, 25]

    fig, ax = plt.subplots()
    ax.plot(squares)

    plt.show()

if __name__ == "__main__":
    main()
