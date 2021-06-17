import argparse
import time
from train import *

def parse_args():

  parser = argparse.ArgumentParser(description="SPDS_FinalPJT", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--batchsize", default=10, type=int, dest="batchsize")
  parser.add_argument("--epochs", default=35, type=int, dest="epochs")
  parser.add_argument("--train_dir", default="../rps/rps/", type=str, dest="train_dir")
  parser.add_argument("--aug_train_dir", default="../rps/augmented_rps/", type=str, dest="aug_train_dir")
  parser.add_argument("--val_dir", default="../validation/", type=str, dest="val_dir")
  # parser.add_argument("--val_dir", default="../rps/rps-test-set/", type=str, dest="val_dir")

  return parser.parse_args()


def main():
  args = parse_args()
  train(args)

if __name__ == '__main__':
  start = time.time()
  main()
  end = time.time()
  print(f"Training time: {end-start}")