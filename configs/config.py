# Owned by Johns Hopkins University, created prior to 5/28/2020
import numpy as np
import os
import cv2
from easydict import EasyDict
config = EasyDict()
FOLD=1

config.exp_name = "bigset/fold{}big".format(FOLD)
config.model_name = "xception"
config.desc = "39 class classification"
config.pretrained = True
config.preload_data = False
config.wandb = True
config.wandb_project = "Vectech Classification - Network of Experts"		# "Vectech Classification - Network of Experts"
config.gpu = None
config.fp16 = False
config.num_workers = os.cpu_count()
config.fastai_data = False
config.one_hot_labels = False
if config.fastai_data:
	config.one_hot_labels = False
config.debug = False
# config.debug = True     ; config.reduce_dataset = False


# config.DATA_CSV_PATH = 'data/reduced_training/reduced_split_fold1.csv'
config.DATA_CSV_PATH = 'data/finale/datasplit_fold{}big.csv'.format(FOLD) # <--paper datasplit location

config.class_map = ['aedes aedes_aegypti',
                    'aedes aedes_albopictus',
                    'aedes aedes_atlanticus',
                    'aedes aedes_canadensis',
                    'aedes aedes_dorsalis',
                    'aedes aedes_flavescens',
                    'aedes aedes_infirmatus',
                    'aedes aedes_japonicus',
                    'aedes aedes_nigromaculis',
                    'aedes aedes_sollicitans',
                    'aedes aedes_taeniorhynchus',
                    'aedes aedes_triseriatus',
                    'aedes aedes_trivittatus',
                    'aedes aedes_vexans',
                    'anopheles anopheles_coustani',
                    'anopheles anopheles_crucians',
                    'anopheles anopheles_freeborni',
                    'anopheles anopheles_funestus',
                    'anopheles anopheles_gambiae',
                    'anopheles anopheles_pseudopunctipennis',
                    'anopheles anopheles_punctipennis',
                    'anopheles anopheles_quadrimaculatus',
                    'coquillettidia coquillettidia_perturbans',
                    'culex culex_coronator',
                    'culex culex_erraticus',
                    'culex culex_nigripalpus',
                    'culex culex_pipiens_sl',
                    'culex culex_restuans',
                    'culex culex_salinarius',
                    'culiseta culiseta_incidens',
                    'culiseta culiseta_inornata',
                    'deinocerites deinocerites_cancer',
                    'deinocerites deinocerites_cuba-1',
                    'mansonia mansonia_titillans',
                    'psorophora psorophora_ciliata',
                    'psorophora psorophora_columbiae',
                    'psorophora psorophora_cyanescens',
                    'psorophora psorophora_ferox',
                    'psorophora psorophora_pygmaea',
                     'aedes aedes_spp',
                      'anopheles anopheles_spp',
                      'culex culex_spp',
                      'psorophora psorophora_spp',
                      'mosquito']
# config.class_map = ['aedes','anopheles', 'culex', 'psorophora', 'mosquito']
config.class_map = [(i, config.class_map[i]) for i in range(len(config.class_map))]
config.unknown_classes = [39, 40, 41, 42, 43]
config.known_only = True

# config.num_genuses = 6
config.num_species = np.array([39 if config.known_only else 44])
# config.sphead_scaling = 1
# config.nofe_head_design = "combined" # separate or combined

config.loss_dict = {"FocalLoss": {'weight': 1.0, 'mag_scale': 1.0, 'gamma': 0}}

config.optimizer = "ranger"
config.lr = 1e-2
config.lr_finetune = 1e-4
config.weight_decay = 1e-2
config.alpha = 0.99
config.mom = 0.9 # Momentum
config.eps = 1e-6
config.sched_type = "one_cycle" # LR schedule type (one_cycle/flat_and_anneal)

# config.augment_prob = 0.9
config.blend_params = {
    'size': .15,            # range(0.-1.) You can indicate the size of the patched area/s
    'alpha': 1.,           # This is used to define a proba distribution
    'fixed_proba': 0,      # This overrides alpha proba distribution. Will fix the % of the image that is modified
    'grid': True,          # Determine if patches may overlap or not. With True they do not overlap
    'blend_type': 'cut',   # Options: 'zero', 'noise', 'mix', 'cut', 'random'
    'same_size': False,     # All patches may have the same size or not
    'same_crop': False,    # Cropping patches are from the same subregion as input patches (only with 'mix' and 'cut')
    'same_image': False,   # Cropping patches will be from the same or different images (only with 'mix' and 'cut')
}

config.swa = False
config.cosine_annealing = False
config.drop_rate = 0

config.batch_size = 16
config.epochs = 40
config.imsize = 299
config.augment_prob = 0.001

config.genus = False
# config.genus_weight = 0
# config.species_on = 100

config.phone_additions = False
config.False_additions = False
config.mixup = 0.4
config.ricap = 0    # 0.3
config.ann_start = 0.7 # Annealing start

config.lrfinder = False # Run learning rate finder
config.dump = 0 # Print model; don't train"
config.log_file = "./logs/{}".format(config.exp_name) # Log file name

if config.debug:
    config.wandb = False
