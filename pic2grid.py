#%%
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from tqdm.auto import tqdm
#%%
col_dpi=267

width_A4 = 595/72
height_A4 = 842/72

ncol = 3
nrows = 8

input_folder = "sample_images"
output_folder = "output"


#%%
def make_single_gird(files, nrows, ncol, offset=0, index=0, hspace=0.01):
    fig, axes = plt.subplots(nrows,ncol, figsize=(width_A4, height_A4)) # righe, colonne, (colonne, righe)
    for ax, img, i in zip(axes.transpose().reshape(-1), files, np.arange(0, len(files))):
        ax.axis('off')
        sample=plt.imread(img)
        ax.imshow(sample)
        ax.set_xlabel("",fontsize=1)
        ax.set_ylabel("",fontsize=1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.annotate("{:04d}".format(i+1+offset), xycoords="axes fraction", xy=(1.02, 0.1), rotation=-90 )

    # fig.set_tight_layout(True)
    plt.subplots_adjust(hspace=hspace)
    plt.savefig(f"{output_folder}/output_{index}.png", dpi=col_dpi*ncol, bbox_inches = "tight")
    plt.close()

def process_input(nrows, ncol):
    files = glob(f"{input_folder}/*.png")
    step = nrows*ncol
    try:
        assert len(files) % (nrows*ncol) == 0
    except:
        print(f"The number of input files must be a multiple of {nrows*ncol}, {len(files)} provided.")
        return
    nmin_array = np.arange(0, len(files), step=step)
    for i, nmin in enumerate(tqdm(nmin_array)):
        make_single_gird(files[nmin:(nmin+step)], nrows, ncol, offset=i*step, index=i)

# %%
process_input(6, 2)
# %%
