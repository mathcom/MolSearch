import os
import pandas as pd


if __name__=='__main__':
    
    ## input
    input_dir = input_dir = os.path.join('results', 'gsk3b_jnk3_qed_sa_stage2', 'task1', 'seed_0')
    filenames = os.listdir(input_dir)
    print(len(filenames))
    
    ## output
    filepath_output = 'generated_MolSearch_gsk3b_jnk3_qed_sa.txt'
    
    ## read
    generated = set()
    for filename in filenames:

        filepath = os.path.join(input_dir, filename)
        df = pd.read_csv(filepath, sep=' ')
        generated = generated.union(set(df['smiles'].values.tolist()))

    generated = list(generated)
    print(len(generated))
    
    ## write
    with open(filepath_output, 'w') as fout:
        for smi in generated:
            fout.write(f'{smi}\n')
            
    print('Finish')