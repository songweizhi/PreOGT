
max_range                                   = 5
BacDiv_optimum_temperature_csv_reformatted  = '/Users/songweizhi/Documents/Research/PreTR_ML/BacDiv_2022-03-19_optimum_temperature_1-100_type_strain_genome_ncbi_reformatted_range%s.csv' % max_range
prokaryotes_csv                             = '/Users/songweizhi/Documents/Research/PreTR_ML/prokaryotes_2022-03-19.csv'
prokaryotes_csv_subset                      = '/Users/songweizhi/Documents/Research/PreTR_ML/prokaryotes_2022-03-19_subset.csv'
prokaryotes_csv_subset_GCA_to_name          = '/Users/songweizhi/Documents/Research/PreTR_ML/prokaryotes_2022-03-19_subset_GCA_to_name.csv'


strain_to_temp_dict = {}
species_to_strain_dict = {}
total_gnm_num = 0
line_to_strain_dict = {}
for each_line in open(BacDiv_optimum_temperature_csv_reformatted):
    if not each_line.startswith('ID\t'):
        total_gnm_num += 1
        each_line_split = each_line.strip().split('\t')
        strain_id = each_line_split[0]
        temperature = each_line_split[1]
        strain_to_temp_dict[strain_id] = temperature
        line_to_strain_dict[each_line.strip()] = strain_id
        species_name = each_line_split[2].replace('_', ' ')
        strain_str = ''
        if len(each_line_split) == 4:
            strain_str = each_line_split[3]
        strain_list = strain_str.split(',')
        if species_name not in species_to_strain_dict:
            species_to_strain_dict[species_name] = strain_list
        else:
            for each_item in strain_list:
                species_to_strain_dict[species_name].append(each_item)


n = 0
found_strain_list = set()
found_organism_list = set()
GCA_to_domain_dict = {}
prokaryotes_csv_subset_GCA_to_name_handle = open(prokaryotes_csv_subset_GCA_to_name, 'w')
prokaryotes_csv_subset_handle = open(prokaryotes_csv_subset, 'w')
for each_line in open(prokaryotes_csv):
    if not each_line.startswith('#Organism Name'):
        organism_name = each_line.strip().split('","')[0][1:]
        organism_name_split = organism_name.split(' ')
        species_name = organism_name
        if len(organism_name_split) > 2:
            species_name = '%s_%s' % (organism_name_split[0], organism_name_split[1])
        strain_id = each_line.strip().split('","')[2]
        strain_id_no_space = strain_id.replace(' ', '_')
        gca_id = each_line.strip().split('","')[5]

        organism_domain = 'Bacteria'
        if 'Archaea' in each_line:
            organism_domain = 'Archaea'

        if (organism_name in species_to_strain_dict):
            found_organism_list.add(organism_name)
            strain_with_temp = species_to_strain_dict[organism_name]
            if (strain_id in strain_with_temp) or (strain_id_no_space in strain_with_temp):
                current_strain_id = ''
                current_strain_temp = ''
                for each_strain_line in line_to_strain_dict:
                    if (organism_name.replace(' ', '_') in each_strain_line) and (strain_id.replace(' ', '_') in each_strain_line):
                        current_strain_id = each_strain_line.split('\t')[0]
                        current_strain_temp = each_strain_line.split('\t')[1]
                prokaryotes_csv_subset_GCA_to_name_handle.write('%s\t%s\t%s\t%s\t%s %s\n' % (current_strain_id, current_strain_temp, gca_id, organism_domain, organism_name.replace(' ', '_'), strain_id.replace(' ', '_')))
                found_strain_list.add(current_strain_id)
                prokaryotes_csv_subset_handle.write(each_line)
                n += 1
prokaryotes_csv_subset_handle.close()
prokaryotes_csv_subset_GCA_to_name_handle.close()


print('Total number of genomes: %s' % total_gnm_num)
print('Total number of species: %s' % len(species_to_strain_dict))
print('found_organisms: %s' % len(found_organism_list))
print('found_strain: %s' % len(found_strain_list))
print('downloaded genomes: %s' % n)

