
# plots in the paper

import sys
sys.path.append("../../src/")
from bias_metrics import count_groups_Organic, count_groups_org_edges
from graph_utils import read_instagram_genrace
from plot_utils import *
# DATAPATH= "../../data/la/"
#
# gender, race = read_instagram_genrace(DATAPATH + 'la.genrace')
#
# count_groups_Organic(DATAPATH, gender, race)
#
# count_groups_org_edges(DATAPATH, gender, race)


prec_reg=[0.000447687215676 ,
0.00256185563417 ,
0.0049253078671 ,
0.00869445829368 ,
0.0128294717559 ,
0.0157873817035 ,
0.018178587643 ,
0.018719604409]

recall_reg=[0.00493049004261 ,
0.0282124381875 ,
0.0542395372223 ,
0.0957485408611 ,
0.141286115632 ,
0.173860938618 ,
0.20019489742 ,
0.206153782358]

prec_geneq=[0.000204941417735 ,
0.00145327709346 ,
0.00325916991824 ,
0.00759598168258 ,
0.0119664141631 ,
0.0150090827271 ,
0.0173345483824 ,
0.0177720718154]

recall_geneq=[0.00223095344232 ,
0.0158157182696 ,
0.0354692570054 ,
0.0826717533511 ,
0.130239164014 ,
0.163355138346 ,
0.188664849006 ,
0.193427395528]


prec_race=[0.000198062508166 ,
0.00130575771337 ,
0.00293605273438 ,
0.00652636873764 ,
0.0102172617508 ,
0.0128676865813 ,
0.0149346331468 ,
0.0149580957547]

recall_race=[0.0020588631675 ,
0.0135743979432 ,
0.0305221799484 ,
0.0678471091944 ,
0.10621702035 ,
0.133770124714 ,
0.155258601922 ,
0.155503260385]


#plotQuality(prec_reg, prec_geneq, prec_race, recall_reg, recall_geneq, recall_race)
plotQualitysamecol(prec_reg, prec_geneq, prec_race, recall_reg, recall_geneq, recall_race)



lon_reg_f=[0.0003938002686403597,
 0.00034061467326024187,
 0.0003372165681677292,
 0.0005884175638279583]

lon_fair_f=[0.0003693357007625597,
 0.00039087346052230635,
 0.00037819478898574473,
 0.0005044881446090396]

# lon_fair=[0.36165230861085573,
#  0.2321086858545956,
#  0.22457983039124177,
#  0.18165917514330704]
#
# lon_reg=[0.38560830565444815,
#  0.20226418140175878,
#  0.20024631488333933,
#  0.21188119806045372]

la_reg_f=[0.00024226906849301465,
 0.00022935125382729575,
 0.0002189733047992702,
 0.0003864548849200953]

la_fair_f=[0.00022148786132747763,
 0.00026382006274499725,
 0.0002497125300692144,
 0.00033552374311646133]

# la_reg=[0.3737152072151035,
#  0.2114545197170426,
#  0.2018863826750644,
#  0.21294389039278955]
#
# la_fair=[0.341659101037179,
#  0.24323380637151437,
#  0.2302271046235964,
#  0.1848799879677101]

la_fair_f_race=[4.877635799134764e-06,
 3.905236869536752e-06,
 3.9584396074669645e-06,
 4.308224664717113e-06,
 3.152007706410502e-06,
 3.1456749108644328e-06,
 2.855910012778e-06,
 2.845054473713134e-06,
 3.2414239671136106e-06]

la_reg_f_race=[5.320705964147271e-06,
 3.1200580009622935e-06,
 2.993384815414168e-06,
 4.889275883050168e-06,
 1.9007561623505754e-06,
 2.604413594935772e-06,
 2.0702959708014434e-06,
 2.7684540738620818e-06,
 4.561020063015053e-06]


lon_reg_f_race=[2.5258071178125037e-05,
 9.574416790906735e-06,
 9.185699057359616e-06,
 9.699374958728956e-06,
 1.1405636682843086e-05,
 1.0102992354117619e-05,
 1.242297362314693e-05,
 1.0739335102282076e-05,
 3.461033135191986e-05]

lon_fair_f_race=[2.3154760482101068e-05,
 1.1983868711616494e-05,
 1.2147130159706283e-05,
 8.546682050485317e-06,
 1.8913869876071453e-05,
 1.220264309585849e-05,
 1.7137112402864738e-05,
 1.103648193622671e-05,
 2.4596856844277032e-05]




#plotGengroups(la_reg, la_fair, lon_reg, lon_fair, la_reg_f, la_fair_f, lon_reg_f, lon_fair_f)


plotcombiSP(la_fair_f, lon_fair_f, la_reg_f,  lon_reg_f, la_fair_f_race, lon_fair_f_race, la_reg_f_race,  lon_reg_f_race)


lon_fair=[374580.8, 240406.2, 232608.2, 188153.2]
la_fair=[563814.8, 401390.8, 379926.8, 305093.8]
la_reg=[616715.0, 348948.0, 333158.4, 351405.8]
lon_reg=[399392.8, 209494.6, 207404.6, 219455.4]
la_fair_race=[1514.8, 4007.8, 4062.4, 14609.6, 264.0, 870.6, 239.2, 787.4, 73.2]
la_reg_race=[1652.4, 3202.0, 3072.0, 16580.0, 159.2, 720.8, 173.4, 766.2, 103.0]
lon_fair_race=[1514.8, 4007.8, 4062.4, 14609.6, 264.0, 870.6, 239.2, 787.4, 73.2]
lon_reg_race=[1652.4, 3202.0, 3072.0, 16580.0, 159.2, 720.8, 173.4, 766.2, 103.0]
plotcombi_ER(la_fair, lon_fair, la_reg,  lon_reg, la_fair_race, lon_fair_race, la_reg_race,  lon_reg_race)

