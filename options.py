import argparse

parser = argparse.ArgumentParser(description="PyTorch Implementation of Temporal Shift Module for Jester")
parser.add_argument('--train_list', type=str, default="")
parser.add_argument('--val_list', type=str, default="")
parser.add_argument('--test_list', type=str, default="")
parser.add_argument('--store_name', type=str, default="")
parser.add_argument('--mode', type=str, default="train")

# ========================= Model Configs ==========================
parser.add_argument('--arch', type=str, default="mobilenetv2")
parser.add_argument('--num_segments', type=int, default=8)
parser.add_argument('--dropout', default=0.5, type=float)
parser.add_argument('--img_feature_dim', default=256, type=int, help="the feature dimension for each frame")

# ========================= Learning Configs ==========================
parser.add_argument('--epochs', default=50, type=int, help='number of total epochs')
parser.add_argument('--batch_size', default=64, type=int)
parser.add_argument('--lr', default=0.01, type=float)
parser.add_argument('--lr_type', default='step', type=str)
parser.add_argument('--lr_steps', default=[20, 40], type=float, nargs="+")
parser.add_argument('--momentum', default=0.9, type=float)
parser.add_argument('--weight_decay', default=1e-4, type=float)
parser.add_argument('--no_partialbn', default=False, action="store_true")

# ========================= Monitor Configs ==========================
parser.add_argument('--print_freq', default=200, type=int)
parser.add_argument('--eval-freq', default=1, type=int, help='evaluation frequency')

# ========================= Runtime Configs ==========================
parser.add_argument('--workers', default=8, type=int, help='number of data loading workers')
parser.add_argument('--start_epoch', default=0, type=int, help='manual epoch number')
parser.add_argument('--root_log', type=str, default='log')
parser.add_argument('--root_model', type=str, default='checkpoint')
parser.add_argument('--shift', default=False, action="store_true", help='use shift for models')
parser.add_argument('--shift_div', default=8, type=int, help='number for shift')
