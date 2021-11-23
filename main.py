import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

# def fct_mod_PDF(r, var=16):
def fct_mod_PDF(r, var=4):
    if r > 0:
        y = (r/var) * np.exp(-r**2/(2*var))
    else:
        y = 0
    return y

# def fct_mod_CDF(r, var=16):
def fct_mod_CDF(r, var=4):
    y = 1-np.exp(-r**2/(2*var))
    return y

def fct_reverse_CDF(y, var=4):
    if y>=0:
        r = np.sqrt(-2*var*np.log(1-y))
    else:
        r=0
    return r

def fct_angle():
    pass

def plot_PDF_CDF(r, PDF, CDF , d_r):
    plt.plot(r,PDF)
    plt.plot(r,CDF)
    plt.show()
    r = np.array(r)
    plt.plot(CDF,r)
    #plt.xlim(0,0.999)
    #plt.ylim(0,8)
    plt.show()

def get_PDF_CDF():
    length = 20
    d_r = 0.00001
    data_nbr = int(length / d_r)
    r = [r * d_r for r in range(data_nbr)]
    PDF = [fct_mod_PDF(i) for i in r]
    CDF = [fct_mod_CDF(i) for i in r]
    return r, PDF, CDF, d_r

# def get_random_r(CDF, r, d_r):
#     ran = np.random.uniform()
#     # Serialisation des donnees
#     # CDF = ((np.array(CDF) / d_r) // 1) * d_r
#     ran = ((ran / d_r) // 1) * d_r
#     a = np.where(CDF == ran)
#     a = a[0][0]
#     value = r[a]
#     return value

def get_random_r(qty, var, home_made=1):
    if home_made:
        return np.array([fct_reverse_CDF(np.random.uniform(), var) for _ in range(qty)])
    else:
        return np.array([np.random.rayleigh(scale=var) for _ in range(qty)])


def get_random_angle():
    ran = np.random.uniform()
    value = ran*2*np.pi
    return value

def generate_data_tuples(nbr_data):
    x = get_random_r(nbr_data, 4)
    y = np.array([get_random_angle() for _ in range(nbr_data)])
    return x,y


def show_dot_disp_graph(x,y,xlab, ylab,title):
    plt.plot(x,y,"o")
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.show()

def dist_angle_calc(origin, error):
    D = origin[0] + error[0]*np.cos(error[1])
    sigma = origin[1] + error[0]*np.sin(error[1])
    return D,sigma

def plot_gen_unif():
    nbr_data = 1000
    x = [i for i in range(nbr_data)]
    y = [np.random.uniform()*2*np.pi for _ in range(nbr_data)]

    plt.plot(x,y)
    plt.xlabel("Index")
    plt.ylabel("Valeur aleatoire")
    plt.title("Génération aléatoire de {} valeurs".format(nbr_data))
    plt.show()

    classes = int(nbr_data/100)
    plt.hist(y, bins=classes)
    plt.hist(y, bins=classes*10)
    plt.title("Histogramme de la distribution des {} valeurs aléatoires uniformes".format(nbr_data))
    plt.show()

def plot_rayleigh():
    length = 20
    d_r = 0.00001
    data_nbr = int(length / d_r)
    var = [0.25, 1, 4, 9, 16]
    r = [r * d_r for r in range(data_nbr)]
    for i in var:
        lab = "var = {}".format(i)
        PDF = [fct_mod_PDF(n,i) for n in r]
        plt.plot(r,PDF, label=lab)
    plt.legend()
    plt.title("PDF de Rayleigh pour différentes valeurs de variance")
    plt.xlabel("Valeur")
    plt.ylabel("Probabilité")
    plt.show()

def realisation_mod_erreur(): # 1)f)
    fig, ax1 = plt.subplots()
    ax_twin = ax1.twinx()
    qty_val = 10000
    y = get_random_r(qty_val, 4)
    ax1.hist(y, bins=100)

    r, PDF, CDF, d_r = get_PDF_CDF()
    color = 'tab:orange'
    ax_twin.plot(r, PDF, color=color)
    plt.xlabel("Valeurs")
    plt.ylabel("Probabilité")
    plt.title("Histogramme des 10 000 réalisations du module de l'erreur 'r'\n (variance = 4)")
    plt.show()

def compare_rayleigh(): # 1)g)
    qty_val = 10000
    y1 = get_random_r(qty_val, 4)
    y2 = get_random_r(qty_val ,2, 0)
    plt.hist([y1, y2], bins=100, label=["Fait main", "Python"])

    plt.xlabel("Valeurs")
    plt.ylabel("Probabilité")
    plt.title("Comparaison des générateurs Rayleigh\n (variance = 4)")
    plt.legend(loc='upper right')
    plt.show()

def ex_4_2():
    nbr_data = 1000
    x,y = generate_data_tuples(nbr_data)
    show_dot_disp_graph(x, y, "r (m)", "theta (rad)", "Nuage de point pour {} couples [r theta]".format(nbr_data))

def ex_4_3():
    origins = [(50, np.deg2rad(15), 4), (50, np.deg2rad(30), 4), (100, np.deg2rad(15), 16),(100, np.deg2rad(30), 16)]
    fig, axs = plt.subplots(2,2)
    qty_data = 1000
    distance = []
    angle = []
    for origin in origins:
        d=[]
        a=[]
        for _ in range(qty_data):
            error = (get_random_r(1, origin[2])[0], get_random_angle())
            dist, ang = dist_angle_calc(origin, error)
            d.append(dist)
            a.append(ang)
        distance.append(d)
        angle.append(a)

    axs[0,0].plot(distance[0], angle[0], "o")
    axs[0,1].plot(distance[1], angle[1], "o")
    axs[1,0].plot(distance[2], angle[2], "o")
    axs[1,1].plot(distance[3], angle[3], "o")
    axs[0,0].title.set_text('[50m 15deg]')
    axs[0,1].title.set_text('[50m 30deg]')
    axs[1,0].title.set_text('[100m 15deg]')
    axs[1,1].title.set_text('[100m 30deg]')
    fig.suptitle("Distributions des couples distances et angles \nà partir de paramètres d'origine")
    fig.text(0.5, 0.04, 'Distances (m)', ha='center')
    fig.text(0.04, 0.5, 'Angles (rad)', va='center', rotation='vertical')
    plt.show()

def ex_4_4():
    origins = [(50, np.deg2rad(15), 4), (50, np.deg2rad(30), 4), (100, np.deg2rad(15), 16), (100, np.deg2rad(30), 16)]
    fig, axs = plt.subplots(2, 2)
    fig2, axs2 = plt.subplots(2, 2)
    qty_data = 1000
    D_x_glob = []
    D_y_glob = []
    for origin in origins:
        Dx = []
        Dy = []
        origin_x = origin[0]*np.cos(origin[1])
        origin_y = origin[0]*np.sin(origin[1])
        print(origin, "\n",origin_x,"\t",origin_y)
        for _ in range(qty_data):
            error = (get_random_r(1, origin[2])[0], get_random_angle())
            dist, ang = error
            x = dist*np.cos(ang)+origin_x
            y = dist*np.sin(ang)+origin_y
            Dx.append(x)
            Dy.append(y)
        D_x_glob.append(Dx)
        D_y_glob.append(Dy)

    axs2[0, 0].plot(D_x_glob[0])
    axs2[0, 0].plot(D_y_glob[0])
    axs2[0, 1].plot(D_x_glob[1])
    axs2[0, 1].plot(D_y_glob[1])
    axs2[1, 0].plot(D_x_glob[2])
    axs2[1, 0].plot(D_y_glob[2])
    axs2[1, 1].plot(D_x_glob[3])
    axs2[1, 1].plot(D_y_glob[3])
    axs2[0, 0].title.set_text('[50m 15deg]')
    axs2[0, 1].title.set_text('[50m 30deg]')
    axs2[1, 0].title.set_text('[100m 15deg]')
    axs2[1, 1].title.set_text('[100m 30deg]')

    axs[0, 0].plot(D_x_glob[0], D_y_glob[0], "o")
    axs[0, 1].plot(D_x_glob[1], D_y_glob[1], "o")
    axs[1, 0].plot(D_x_glob[2], D_y_glob[2], "o")
    axs[1, 1].plot(D_x_glob[3], D_y_glob[3], "o")
    axs[0, 0].title.set_text('[50m 15deg]')
    axs[0, 1].title.set_text('[50m 30deg]')
    axs[1, 0].title.set_text('[100m 15deg]')
    axs[1, 1].title.set_text('[100m 30deg]')


    fig.suptitle("Distributions des couples Dx Dy \nà partir de paramètres d'origine")
    fig.text(0.5, 0.04, 'Dx (m)', ha='center')
    fig.text(0.04, 0.5, 'Dy (m)', va='center', rotation='vertical')

    fig2.suptitle("Dx Dy en fonction de leur index de génération aléatoire")
    fig2.text(0.5, 0.04, 'Index', ha='center')
    fig2.text(0.04, 0.5, 'Distance (m)', va='center', rotation='vertical')
    plt.show()


def ex_4_5():
    origins = [(50, np.deg2rad(15), 4), (50, np.deg2rad(30), 4), (100, np.deg2rad(15), 16), (100, np.deg2rad(30), 16)]
    fig, axs = plt.subplots(2, 2)
    qty_data = 1000
    D_x_glob = []
    D_y_glob = []
    for origin in origins:
        Dx = []
        Dy = []
        origin_x = origin[0]*np.cos(origin[1])
        origin_y = origin[0]*np.sin(origin[1])
        for _ in range(qty_data):
            error = (get_random_r(1, origin[2])[0], get_random_angle())
            dist, ang = error
            x = dist*np.cos(ang)+origin_x
            y = dist*np.sin(ang)+origin_y
            Dx.append(x)
            Dy.append(y)
        D_x_glob.append(Dx)
        D_y_glob.append(Dy)


    axs[0,0].hist([D_x_glob[0], D_y_glob[0]], bins=100)
    axs[0,1].hist([D_x_glob[1], D_y_glob[1]], bins=100)
    axs[1,0].hist([D_x_glob[2], D_y_glob[2]], bins=100)
    axs[1,1].hist([D_x_glob[3], D_y_glob[3]], bins=100)
    axs[0, 0].title.set_text('[50m 15deg]')
    axs[0, 1].title.set_text('[50m 30deg]')
    axs[1, 0].title.set_text('[100m 15deg]')
    axs[1, 1].title.set_text('[100m 30deg]')

    a = (np.mean(D_x_glob[0]), np.std(D_x_glob[0]), np.mean(D_y_glob[0]), np.std(D_y_glob[0]))
    b = (np.mean(D_x_glob[1]), np.std(D_x_glob[1]), np.mean(D_y_glob[1]), np.std(D_y_glob[1]))
    c = (np.mean(D_x_glob[2]), np.std(D_x_glob[2]), np.mean(D_y_glob[2]), np.std(D_y_glob[2]))
    d = (np.mean(D_x_glob[3]), np.std(D_x_glob[3]), np.mean(D_y_glob[3]), np.std(D_y_glob[3]))

    fig.suptitle("Histogrammes de Dx et Dy \nà partir de paramètres d'origine")
    fig.text(0.5, 0.04, 'Valeurs', ha='center')
    fig.text(0.04, 0.5, 'Probabilité', va='center', rotation='vertical')

    plt.show()

    print(a)
    print(b)
    print(c)
    print(d)




if __name__ == '__main__':
    ex_4_5()

    # x,y = generate_data_tuples(1000)
    # show_dot_disp_graph(x,y)
    # r, PDF, CDF, d_r = get_PDF_CDF()
    #
    #
    # nbr_data = 10000
    # y = [get_random_r(CDF, r, d_r) for _ in range(nbr_data)]
    #




