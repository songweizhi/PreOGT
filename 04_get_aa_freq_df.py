import os
import glob
from Bio import SeqIO


# file in
faa_folder = '/Users/songweizhi/Desktop/faa_files'

# file out
faa_df_num = '/Users/songweizhi/Desktop/df_aa_num.txt'
faa_df_pct = '/Users/songweizhi/Desktop/df_aa_pct.txt'

# file in
faa_folder = 'faa_files'

# file out
faa_df_num = 'df_aa_num.tab'
faa_df_pct = 'df_aa_pct.tab'



faa_file_re = '%s/*.faa' % faa_folder
faa_file_list = [os.path.basename(file_name) for file_name in glob.glob(faa_file_re)]

read_in_num = 1
aa_set = set()
faa_freq_dict_all_gnm = {}
total_aa_dict_all_gnm = {}
for each_faa in faa_file_list:
    print('Reading in %s/%s: %s' % (read_in_num, len(faa_file_list), each_faa))
    gnm_id = each_faa.split('.')[0]
    current_faa_freq_dict = {}
    current_gnm_total_aa = 0
    pwd_faa = '%s/%s' % (faa_folder, each_faa)
    for each_protein in SeqIO.parse(pwd_faa, 'fasta'):
        protein_seq = str(each_protein.seq)
        for each_aa in protein_seq:
            current_gnm_total_aa += 1
            aa_set.add(each_aa)
            if each_aa not in current_faa_freq_dict:
                current_faa_freq_dict[each_aa] = 1
            else:
                current_faa_freq_dict[each_aa] += 1
    faa_freq_dict_all_gnm[gnm_id] = current_faa_freq_dict
    total_aa_dict_all_gnm[gnm_id] = current_gnm_total_aa
    read_in_num += 1

aa_set_sorted = sorted([i for i in aa_set])
faa_file_list_sorted = sorted([i.split('.')[0] for i in faa_file_list])

wrote_out_num = 1
faa_df_num_handle = open(faa_df_num, 'w')
faa_df_pct_handle = open(faa_df_pct, 'w')
faa_df_num_handle.write('%s\t%s\n' % ('Genome', '\t'.join(aa_set_sorted)))
faa_df_pct_handle.write('%s\t%s\n' % ('Genome', '\t'.join(aa_set_sorted)))
for each_gnm in faa_file_list_sorted:
    print('Writing out %s/%s: %s' % (wrote_out_num, len(faa_file_list_sorted), each_gnm))
    gnm_aa_freq_dict = faa_freq_dict_all_gnm[each_gnm]
    gnm_total_aa = total_aa_dict_all_gnm[each_gnm]
    current_gnm_aa_num_list = []
    current_gnm_aa_pct_list = []
    for each_aa in aa_set_sorted:
        aa_num = gnm_aa_freq_dict.get(each_aa, 0)
        aa_pct = float("{0:.3f}".format(aa_num*100/gnm_total_aa))
        current_gnm_aa_num_list.append(aa_num)
        current_gnm_aa_pct_list.append(aa_pct)
    faa_df_num_handle.write('%s\t%s\n' % (each_gnm, '\t'.join([str(i) for i in current_gnm_aa_num_list])))
    faa_df_pct_handle.write('%s\t%s\n' % (each_gnm, '\t'.join([str(i) for i in current_gnm_aa_pct_list])))
    wrote_out_num += 1

faa_df_num_handle.close()
faa_df_pct_handle.close()
