import argparse
parser = argparse.ArgumentParser(description='Run experiments on a dataset')
parser.add_argument('--dataset', type=str, required=True)
parser.add_argument("--data_dir", type=str, required=True)
parser.add_argument("--output_dir", type=str)
parser.add_argument('--attention', type=str, required=True)

args, extras = parser.parse_known_args()
args.extras = extras

from Transparency.Trainers.DatasetQA import *
from Transparency.ExperimentsQA import *

dataset = datasets[args.dataset](args)

if args.output_dir is not None :
    dataset.output_dir = args.output_dir

if args.attention == 'tanh' :
    train_dataset_on_encoders_tanh(dataset)
elif args.attention == 'dot' :
    train_dataset_on_encoders_dot(dataset)
else :
    raise LookupError("Attention not found ...")


