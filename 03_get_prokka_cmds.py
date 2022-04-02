
prokaryotes_csv_subset_GCA_to_name  = '/Users/songweizhi/Documents/Research/PreTR_ML/prokaryotes_2022-03-19_subset_GCA_to_name.csv'
prokka_cmd                          = '/Users/songweizhi/Documents/Research/PreTR_ML/prokaryotes_2022-03-19_subset_GCA_to_name_prokka_cmds.txt'


prokka_cmd_handle = open(prokka_cmd, 'w')
for each_gnm in open(prokaryotes_csv_subset_GCA_to_name):
    each_gnm_split = each_gnm.strip().split('\t')
    gca_id = each_gnm_split[2]
    gca_id_no_dot = gca_id.split('.')[0]
    gnm_domain = each_gnm_split[3]
    prokka_cmd = 'prokka --compliant --cpus 12 --kingdom %s --prefix %s --locustag %s --outdir %s_prokka_wd ../prokaryotes_2022-03-19_subset_2507_genomes/%s.fna\n' % (gnm_domain, gca_id, gca_id_no_dot, gca_id_no_dot, gca_id)
    prokka_cmd_handle.write(prokka_cmd)
prokka_cmd_handle.close()

