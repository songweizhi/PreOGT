
df_aa_freq_txt = '/Users/songweizhi/Desktop/df_aa_pct.txt'
metadata_csv   = '/Users/songweizhi/Documents/Research/PreTR_ML/0_important_files/prokaryotes_2022-03-19_subset_2507_GCA_to_name.csv'
gnm_ogt_txt    = '/Users/songweizhi/Desktop/gnm_ogt.txt'


selected_gnm_set = set()
for each_gnm in open(df_aa_freq_txt):
    selected_gnm_set.add(each_gnm.strip().split('\t')[0])


gnm_ogt_txt_handle = open(gnm_ogt_txt, 'w')
for each in open(metadata_csv):
    each_split = each.strip().split('\t')
    gca_id = each_split[2]
    gca_id_no_dot = gca_id.split('.')[0]
    ogt = each_split[1]
    if gca_id_no_dot in selected_gnm_set:
        gnm_ogt_txt_handle.write('%s\t%s\n' % (gca_id_no_dot, ogt))
gnm_ogt_txt_handle.close()

