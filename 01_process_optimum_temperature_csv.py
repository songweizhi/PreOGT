import matplotlib.pyplot as plt
import numpy as np


BacDiv_optimum_temperature_csv              = '/Users/songweizhi/Documents/Research/PreTR_ML/BacDiv_2022-03-19_optimum_temperature_1-100_type_strain_genome_ncbi.csv'
max_range                                   = 5

BacDiv_optimum_temperature_csv_reformatted  = '/Users/songweizhi/Documents/Research/PreTR_ML/BacDiv_2022-03-19_optimum_temperature_1-100_type_strain_genome_ncbi_reformatted_range%s.csv' % max_range
# ID,designation_header,strain_number_header,is_type_strain_header,is_type_strain,species,Temperature,"Kind of temperature","Genome Sequence database"

strain_to_species_dict = {}
strain_to_temperature_dict = {}
strain_to_strain_number_dict = {}
processed_strain_id = ''
for each_line in open(BacDiv_optimum_temperature_csv):
    each_line_split = each_line.strip().split(',')
    if each_line.startswith('"') or each_line.startswith('ID') or (len(each_line_split) == 1):
        pass
    elif each_line.startswith(',,,,,,'):
        temperature_col = each_line_split[6]
        strain_to_temperature_dict[processed_strain_id].append(temperature_col)
    else:
        dsmz_strain_id = each_line_split[0]
        temperature_col = each_line_split[-3]
        species = each_line_split[-4][1:-1]
        species = species.replace(' ', '_')

        strain_number = ','.join(each_line_split[2:-6])[1:-1]
        strain_number = strain_number.replace(', ', ',')
        strain_number = strain_number.replace(' ', '_')
        if '","' in strain_number:
            strain_number = strain_number.split('","')[1]


        strain_to_temperature_dict[dsmz_strain_id] = [temperature_col]
        strain_to_species_dict[dsmz_strain_id] = species
        strain_to_strain_number_dict[dsmz_strain_id] = strain_number
        processed_strain_id = dsmz_strain_id


csv_out_handle = open(BacDiv_optimum_temperature_csv_reformatted, 'w')
csv_out_handle.write('ID\tTemperature\n')
for each_strain in sorted(strain_to_temperature_dict.keys()):
    temperature_list = strain_to_temperature_dict[each_strain]
    strain_species = strain_to_species_dict[each_strain]
    strain_number = strain_to_strain_number_dict[each_strain]

    if len(temperature_list) == 1:

        # common case
        if '-' not in temperature_list[0]:
            csv_out_handle.write('%s\t%s\t%s\t%s\n' % (each_strain, float(temperature_list[0]), strain_species, strain_number))
        else:
            temperature_col_split = temperature_list[0].split('-')
            temperature_low = float(temperature_col_split[0])
            temperature_high = float(temperature_col_split[1])
            temperature_range = temperature_high - temperature_low
            temperature_mean = (temperature_low + temperature_high) / 2
            if temperature_range <= max_range:
                csv_out_handle.write('%s\t%s\t%s\t%s\n' % (each_strain, temperature_mean, strain_species, strain_number))

    elif len(temperature_list) == 2:

        # get temperature_1 range and mean
        temperature_1 = temperature_list[0]
        if '-' in temperature_1:
            temperature_1_split = temperature_1.split('-')
            temperature_1_low = float(temperature_1_split[0])
            temperature_1_high = float(temperature_1_split[1])
            temperature_1_range = temperature_1_high - temperature_1_low
            temperature_1_mean = (temperature_1_low + temperature_1_high) / 2
        else:
            temperature_1_range = 0
            temperature_1_mean = float(temperature_1)

        # get temperature_2 range and mean
        temperature_2 = temperature_list[1]
        if '-' in temperature_2:
            temperature_2_split = temperature_2.split('-')
            temperature_2_low = float(temperature_2_split[0])
            temperature_2_high = float(temperature_2_split[1])
            temperature_2_range = temperature_2_high - temperature_2_low
            temperature_2_mean = (temperature_2_low + temperature_2_high) / 2
        else:
            temperature_2_range = 0
            temperature_2_mean = float(temperature_2)

        # get two_temperature range and mean
        two_temperature_range = abs(temperature_1_mean - temperature_2_mean)
        two_temperature_mean = (temperature_1_mean + temperature_2_mean) / 2

        if (temperature_1_range <= max_range) and (temperature_2_range <= max_range) and (two_temperature_range <= max_range):
            csv_out_handle.write('%s\t%s\t%s\t%s\n' % (each_strain, two_temperature_mean, strain_species, strain_number))
    else:
        print('%s\t%s' % (each_strain, temperature_list))
csv_out_handle.close()


# plt.boxplot(temperature_range_list)
# plt.show()

'''
1215,"IDA 3632, R-15447","DSM 15602, CIP 108806, LMG 21834, JCM 21711, IAM 15260, KCTC 13573, NBRC 102452",1,1,"Neobacillus vireti",30,optimum,ncbi

1215	30.0	Neobacillus_vireti	R-15447","DSM_15602,CIP_108806,LMG_21834,JCM_21711,IAM_15260,KCTC_13573,NBRC_102452


'''