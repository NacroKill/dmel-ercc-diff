#!/home/ivan/.conda/envs/my_root/bin/python
"""

####    Programmer: Ivan Jimenez

####    Universidad de Puerto Rico, Recinto de Rio Piedras
####    BIOL-4990 (Investigacion)

This program verifies that the total count of alingments obtained by running the TopHat program is accurate.
The Birnavirus genome was used as reference and 4 files were concatinated into a single FASTA file. The Screed
module for Python was used to simplify the comparison (using seperate databases for the genome and scytrim'ed 
FASTA file). All viral sequence records that are found are displayed on screen after running this script. 

This is a work in progress... Please be patient. The documentation for this script is sporadic.

"""
import time as t
import os, os.path
import glob
import platform
global array
import screed
import sys
from screed import ScreedDB
import string

#corriendo = "N"
bioinfo_path = "/Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO INTERNSHIP FILES/RESULTS/hulk_old_files/"

#while corriendo != 'Y' or corriendo != 'y' or corriendo != '1' or corriendo != 'yes' or corriendo != 'Yes':
    #print "\nDon't you wish to confirm Tophat ran correctly?\n"
#    corriendo = raw_input("Do you wish to run the program (Y/N): ")
#    if (corriendo == 'exit' or corriendo == 'Exit' or corriendo == 'e' or corriendo == 'E' or corriendo == 'n' or corriendo == 'N' or corriendo == 'no' or corriendo == 'No'):
#        raw_input("\nProgram Terminated...\n \nHave a nice day...  :)\n")
#        exit()
#    else :
#        break
 

#Function to quickly return the working directory where this python script is located.
def getpath():
    wd = os.path.dirname(os.path.abspath(__file__))
    if platform.system() == 'Windows':
        array = wd.split('\\')
        destination = "\\\\".join(array)
        destination += '\\\\'
    else:
        array = wd.split('//')
        destination = "////".join(array)
        destination += '////'
    return destination
   

####
# NOT USING THE GETPATH() FUNCTION YET:
####

sequence_path = bioinfo_path + "dmel_birnavirus.fa"


#NONEEDTOREAD!!!####    screed.read_fasta_sequences(sequence_path)


#PRODUCES: <ScreedDB, '/Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO INTERNSHIP FILES/RESULTS/hulk/dmel_birnavirus.fa_screed'>
birnadb = ScreedDB(sequence_path + "_screed")
#birnadb.keys()
#[u'gi|262225302|gb|GQ342962.1|', u'gi|262225305|gb|GQ342963.1|']

birnarecords = []
a=0
for record in birnadb.itervalues():
    birnarecords.append(record)
    print "\nPrinting added record\n"
    #print record['sequence']
    birnarecords[a]['sequence'] = str(record['sequence'])
    a+=1

print birnarecords
#typing: $ records
#   PRODUCES: [{'description': 'Drosophila melanogaster birnavirus SW-2009a strain DBV segment A, complete sequence', 'id': 0, 'name': 'gi|262225302|gb|GQ342962.1|', 'sequence': <_screed_attr 'sequence'>}, {'description': 'Drosophila melanogaster birnavirus SW-2009a strain DBV segment B, complete sequence', 'id': 1, 'name': 'gi|262225305|gb|GQ342963.1|', 'sequence': <_screed_attr 'sequence'>}]
#len(record['sequence'])
#   3014
#record['sequence']
#   <_screed_attr 'sequence'>
print "\n\n\n"
#print "Printing a count: all birna records (should equal to 2)...\n"
#print len(birnarecords)
print "\n\n\n"
#print "\nPrinting sequence of last record.\n\t"

#print record['sequence']

print "\nPrinting first record\n\t"
segmentA = birnadb[birnadb.keys()[0]]
print segmentA

#segment
#   {'description': 'Drosophila melanogaster birnavirus SW-2009a strain DBV segment A, complete sequence', 'id': 0, 'name': 'gi|262225302|gb|GQ342962.1|', 'sequence': <_screed_attr 'sequence'>}

print "\nPrinting second record...\n\t"
segmentB = birnadb[birnadb.keys()[1]]
print segmentB


####MUST READ FASTQ FILES FIRST INTO A DATABASE


#allscytrims_path = bioinfo_path + "scy_trim_files/all_unclean_scytrims.fastq"

#allscytrims_dump = screed.dump_to_fasta(scytrims_path)
#READS FASTQ AND CREATES A DB

#NONEEDTOREAD!!!####    screed.read_fastq_sequences(allscytrims_path)


#allscytrimdb = ScreedDB(allscytrims_path + "_screed")
#PRODUCES: d<ScreedDB, '/Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO INTERNSHIP FILES/RESULTS/hulk/dmel_birnavirus.fa_screed'>


###################
#   Converting the ScyTrim'd FASTQ reads to FASTA
###################
####SOLUTION: NO WAY TO CONVERT FASTQ TO FASTA IN SCRIPT, MUST RUN COMMAND IN TERMINAL.......
###### $ python -m screed.dump_to_fasta <path to fastq db> <converted fasta file>


#NONEEDTOREAD!!!####screed.read_fasta_sequences(bioinfo_path + "scy_trim_files/all_unclean_scytrims.fasta")

#print "testing\n\n\n"
#print birnarecords
#print "TESTING\n\n\n"


#PRODUCES: <ScreedDB, '/Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO INTERNSHIP FILES/RESULTS/hulk/dmel_birnavirus.fa_screed'>
allscytrimdb = ScreedDB(bioinfo_path + "all_unclean_scytrims.fasta_screed")

#print "Now adding all records in scytrimfasta database into an array.\n\nPlease wait..."

#Function to find the complement of a strand of DNA
def complementary_strand(strand):
    return strand.translate(string.maketrans('TAGCtagc', 'ATCGATCG'))



viral_sequences = []
iterator = 0
birnasegmentA = birnarecords[0]['sequence']
birnasegmentB = birnarecords[1]['sequence']
birnarevsegA = birnasegmentA[::-1]
print "\nPrinting the first segment in reverse:\n"
print birnarevsegA
birnarevsegB = birnasegmentB[::-1]
print "\nPrinting the second segment in reverse:\n"
print birnarevsegB

birnacomplementA = complementary_strand(birnarevsegA)
print "\nPrinting the first segment's complement:\n"
print birnacomplementA

birnacomplementB = complementary_strand(birnarevsegB)
print "\nPrinting the second segment's complement:\n"
print birnacomplementB


for scytrimrec in allscytrimdb.itervalues():
    if str(birnasegmentA).find(str(scytrimrec['sequence'])) == -1 and str(birnasegmentB).find(str(scytrimrec['sequence'])) == -1 and str(birnacomplementA).find(str(scytrimrec['sequence'])) == -1 and str(birnacomplementB).find(str(scytrimrec['sequence'])) == -1:
        print "Checked record #" + str(int(iterator)+1) + " from array."
    else:
        viral_sequences.append(scytrimrec)
        print "FOUND A VIRAL SEQUENCE!!!"
    iterator+=1
 
print "\nPrinting first segment\n"
print birnarecords[0]['sequence']
print "\nPrinting last scytrim record\n"
print scytrimrec['sequence']
print "\nPrinting second sequence\n"
print birnarecords[1]['sequence']


print "\n\n\n"
print "Printing the total (count) of all ScyTrim records\n"
print str(iterator)
print "\n\n\n"
#THIS SHOULD PRINT "1131"
print len(viral_sequences)

#An empty viral_sequences.csv file needs to be created before running this script!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if len(viral_sequences) != 0:
    creatingfile = open(bioinfo_path + "viral_sequences.csv", "r+")
    creatingfile.write(str(viral_sequences))

#PRINTING 




#iterator=0
#segmentA = birnadb[birnadb.keys()[0]] 
#segmentB = birnadb[birnadb.keys()[1]]

# viral_sequences = []
# while iterator < len(allscytrimdb) :
#     astdb_record = allscytrimdb[allscytrimdb.keys()[iterator]]
#     if segmentA['sequence'].find(astdb_record['sequence']) == -1 or segmentB['sequence'].find(astdb_record['sequence']) == -1:
#         continue
#     else:
#         viral_sequences.append(astdb_record)
#     iterator=iterator+1
# print "\n\n\n"
# print viral_sequences



#print "\nPrinting sequence of last record.\n\t"
#print scytrimgenes['sequence']


###Printing sequence of last record.    
#ATTTAATAACAAACGGATACTCAACAGGTTACGGAA



# print len(allscytrimdb)

# #print "\nPrinting first record\n\t"
# astdb_record1 = allscytrimdb[allscytrimdb.keys()[0]]
# print astdb_record1

# ####Printing first record  
# ####{'description': 'HWI-EAS179:1:1:8:956 length=36', 'id': 0, 'name': 'SRR039458.9', 'sequence': <_screed_attr 'sequence'>}

# print "\nPrinting second record...\n\t"
# astdb_record2 = allscytrimdb[allscytrimdb.keys()[1]]
# print astdb_record2

# ####Printing second record...
# ####{'description': 'HWI-EAS179:1:1:8:268 length=36', 'id': 1, 'name': 'SRR039458.10', 'sequence': <_screed_attr 'sequence'>}



# print segmentB
#   {'description': 'Drosophila melanogaster birnavirus SW-2009a strain DBV segment B, complete sequence', 'id': 1, 'name': 'gi|262225305|gb|GQ342963.1|', 'sequence': <_screed_attr 'sequence'>}
# genomefile = raw_input("Type in the name of the genome file (ending in .fa): ")     #/ijimenez/hulk/birnavirus_genome/birnavirus.fa
# #while trying != done:
# try:
#     screed.read_fasta_sequences(getpath+genomefile)
# except IOError:
#     print "Cannot open: " + genomefile
#    genomefile = raw_input("Type in the name of the genome file (ending in .fa): ")
# #


# fadb = ScreedDB(getpath+genomefile)


# full_genome = []
# entries = []
# date = t.localtime(t.time())

# corriendo = raw_input("Ingrese '1' para correr el programa: ")

    
# filename = "dmel_birnavirus.fasta"
# #reference: birnavirus_genome
# reference = open(getpath() + filename, 'r')
# everyline = reference.readlines()


# reference.close()