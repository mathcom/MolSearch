import os
import argparse
import pandas as pd

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--goal', type = str, default = 'gsk3b_jnk3_qed_sa')
    parser.add_argument('--start_mols', type = str, default = 'task1')
    parser.add_argument('--start_idx', type = int, default = 0)
    parser.add_argument('--end_idx', type = int, default = 96)
    parser.add_argument('--max_child', type = int, default = 7)
    parser.add_argument('--num_sims', type = int, default = 10)
    parser.add_argument('--scalar', type = float, default = 0.7)
    parser.add_argument('--seed', type = int, default = 0)
    return parser.parse_args()

if __name__=='__main__':
    args = parse_arguments()
    print(args.goal)
    print(__file__)
    
    input_dir = os.path.join('results_visulization', f'{args.goal}_stage1',  args.start_mols)
    output_dir = os.path.join('libs', f'{args.goal}_stage1')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    filepath_output = os.path.join(output_dir, f'result_start_mols_{args.start_mols}_seed_{args.seed}.csv')
    
    frames = []
    for mol_idx in range(args.start_idx, args.end_idx):
        filename = f'{args.goal}_maxchild_{args.max_child}_sim_{args.num_sims}_scalar_{args.scalar:.1f}_idx_{mol_idx}_seed_{args.seed}.txt'
        filepath = os.path.join(input_dir, filename)
        df = pd.read_csv(filepath, sep=' ')
        frames.append(df)
    
    df_merged = pd.concat(frames)
    
    df_merged = df_merged.loc[:, ['size', 'smiles'] + args.goal.split('_')]
    df_merged = df_merged.drop_duplicates(ignore_index=True)
    print(df_merged.shape)
    
    df_merged.to_csv(filepath_output, index=False)
    print(df_merged.head())