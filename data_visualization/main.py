import matplotlib.pyplot as plt

def main():
    squares = [1, 4, 9, 16, 25]

    fig, ax = plt.subplots()
    ax.plot(squares, linewidth=3)

    ax.set_title('Square Numbers', fontsize=24)
    ax.set

    plt.show()

if __name__ == "__main__":
    main()
