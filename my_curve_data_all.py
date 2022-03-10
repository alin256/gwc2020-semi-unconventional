import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np


import matplotlib
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 14}
matplotlib.rc('font', **font)


def get_data_series_default(plot=False, return_plot_data=False):
    data_frame = pd.read_csv('logs.csv', index_col='offset_md')
    data_frame_reduced = data_frame
    start_tvd = data_frame_reduced.index[0]
    finish_tvd = data_frame_reduced.index[-1]

    my_arange = np.arange(start_tvd, finish_tvd+1e-5, 0.5) - start_tvd
    data_np = data_frame_reduced.to_numpy()

    # data_np = np.log10(data_np)
    sample_ind = 100
    print(data_np[sample_ind,:])
    scaler = MinMaxScaler()
    scaler.fit(data_np)
    print('min', scaler.data_min_)
    print('max', scaler.data_max_)
    data_np = scaler.transform(data_np)
    print(data_np[sample_ind, :])

    ref_data = data_np[:, 0]

    if plot:
        for i, col in enumerate(data_frame_reduced.columns):
            plt.plot(data_np[:, i], my_arange, label=col)
        # plt.yscale('log')
        plt.title('Scaled logs')
        plt.gca().set_ylim(my_arange[-1], my_arange[0])
        plt.ylabel('relative TVD, ft')
        plt.legend()
        plt.tight_layout()
        plt.savefig('figs/logs.png', dpi=600)
        plt.savefig('figs/logs.pdf')
        plt.show()
    if return_plot_data:
        return (ref_data, my_arange, data_np)

    return ref_data


if __name__ == '__main__':
    get_data_series_default(plot=True)

