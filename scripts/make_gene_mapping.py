if __name__ == '__main__':
    with open('data/gene_mapping.csv', 'w+') as fout:
        print('gene_id,gene_name', file=fout)
        with open('data/gencode.v19.genes.v7_model.patched_contigs.gtf', 'r') as fin:
            for line in fin.readlines():
                if line.startswith('#'):
                    continue
                parts = line.strip().split('\t')
                if len(parts) < 9:
                    continue
                attributes = parts[8]
                gene_id = None
                gene_name = None
                for attr in attributes.split(';'):
                    attr = attr.strip()
                    if attr.startswith('gene_id'):
                        gene_id = attr.split('"')[1]
                    elif attr.startswith('gene_name'):
                        gene_name = attr.split('"')[1]
                if gene_id and gene_name:
                    print(f'{gene_id},{gene_name}', file=fout)
    print("Gene mapping file created successfully, saved to 'data/gene_mapping.csv'.")