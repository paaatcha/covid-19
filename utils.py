import matplotlib.pyplot as plt

MONTHS_EN = ["", "Jan", "Feb", "Mar", "Apr", "May"]
MONTHS_PT = ["", "Jan", "Fev", "Mar", "Abr", "Mai"]

def plot_cases (data, case, color, title, legend, x_label, y_label, save_path, lang="en",
                offset_x=-7.5, offset_y=0, y_lim=None):      
    
    fig, ax = plt.subplots()
    plt.plot(data[case].values, color=color)
    plt.grid(color='black', linestyle='dotted', linewidth=0.7)
    plt.title(title)
    plt.legend([legend], loc='upper left')
    plt.xlabel(x_label)
    plt.ylabel(y_label) 
    
    N = len(data)
    ticks_pos = [i for i in range(0, N, 10)]
    ticks_pos.append(N-1)
    if lang == 'en':
        months = MONTHS_EN
    else:
        months = MONTHS_PT
        
    ticks_name = ["{}-{}".format(data.iloc[i].name.to_pydatetime().day, 
                                 months[data.iloc[i].name.to_pydatetime().month]) for i in ticks_pos]
        
    plt.xticks(ticks_pos, ticks_name, rotation='vertical')
    
    ax.annotate(str(data[case].values[-1]), (len(data)+offset_x, data[case].values[-1]+offset_y))  
    ax.scatter(len(data)-1, data[case].values[-1], s=29, c=color)
    
    if y_lim is not None:
        ax.set_ylim(top=y_lim)
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
        
    
def plot_cases_marked (data, color, title, legend, x_label, y_label, save_path, 
                       ticks_pos, lang="en", offset_x=14.5, offset_y=30, y_lim=None):  
    
    fig, ax = plt.subplots()    
    plt.plot([i for i in range(len(data))], data.values, color=color,
              marker='s', markersize=3.5)

    for i, j in enumerate(data):
        ax.annotate(str(j), (i+offset_x, j+offset_y))    
    
    plt.grid(color='black', linestyle='dotted', linewidth=0.7)
    plt.title(title)
    plt.legend([legend], loc='upper left')
    plt.xlabel(x_label)
    plt.ylabel(y_label) 
    
    if ticks_pos is not None:
        if lang == 'en':
            months = MONTHS_EN
        else:
            months = MONTHS_PT
            
        ticks_name = ["{}-{}".format(data.index[i].to_pydatetime().day, 
                                     months[data.index[i].to_pydatetime().month]) for i in ticks_pos]
            
        plt.xticks(ticks_pos, ticks_name, rotation='vertical')
        
    if y_lim is not None:
        ax.set_ylim(top=y_lim)
        
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()   
    

def plot_together (data, legends, colors, case, title, x_label, y_label, 
                   save_path, ticks_pos, lang="en", y_lim=None):
    
        
    fig, ax = plt.subplots()    
    for d, color in zip(data, colors):    
        if case is None:
            plt.plot(d.values, color=color)
        else:
            plt.plot(d[case].values, color=color)
        
    
    plt.legend(legends)
    plt.grid(color='black', linestyle='dotted', linewidth=0.7)
    plt.xlabel(x_label)
    plt.ylabel(y_label) 
    plt.title(title)

    if ticks_pos is not None:
        if lang == 'en':
            months = MONTHS_EN
        else:
            months = MONTHS_PT
            
        ticks_name = ["{}-{}".format(data[0].iloc[i].name.to_pydatetime().day, 
                                     months[data[0].iloc[i].name.to_pydatetime().month]) for i in ticks_pos]
            
        plt.xticks(ticks_pos, ticks_name, rotation='vertical')
    else:
        plt.xticks([], [])
        
    if y_lim is not None:
        ax.set_ylim(top=y_lim)
        
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()     