import matplotlib.pyplot as plt
import index

def main():
    df = index.exercici()
    df.plot.bar()
    plt.title("MITJA NOTA ALUMNAT CICLE")
    plt.xlabel("ALUMNAT")
    plt.ylabel("NOTES")
    plt.show()



def main2():
    df2 = index.exercici2()
    df2.plot()
    plt.plot('x-r')
    plt.xlabel("ALUMNAT")
    plt.ylabel("Faltes en %")
    plt.legend()
    plt.title("% de faltes DAW2")
    plt.show()

#main()
main2()