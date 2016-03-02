#!/home/ivan/.conda/envs/my_root/bin/python
"""

####    Programmer: Ivan Jimenez

####    Universidad de Puerto Rico, Recinto de Rio Piedras
####    BIOL-4990 (Investigacion)

This program verifies that the total count of alingments obtained by running the TopHat program is accurate.
A single FASTA file containing 19 genes was compared to the Drosophila Birnavirus and Xvirus genomes. The Screed
module for Python was used to simplify the comparison (using seperate databases for the genome and scytrim'ed 
FASTA file). All viral sequence records that were found are displayed on screen after running this script. 

This is a work in progress... Please be patient. The documentation for this script is still sporadic.

BEFORE RE-RUNNING THIS SCRIPT, MAKE SURE YOU DELETE ALL FILES THAT MEET THE FOLLOWING CRITERIA:
    - files ENDING IN _screed ......(e.i. <filename>_screed)
    - viral_sequences.csv ..........it will not be overwritten or deleted if NO viral sequences are found, delete it to avoid confusion :) 

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
bioinfo_path = "/Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO INTERNSHIP FILES/RESULTS/newresults/"
viralgenome_path = bioinfo_path + "copy_birna_x_virus.fa"

screed.read_fasta_sequences("/Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO INTERNSHIP FILES/RESULTS/newresults/copy_birna_x_virus.fa")
birna_x_virusdb = ScreedDB(viralgenome_path + "_screed")

#Setting the number of mismatches that are allowed...
k = 6

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

 
#Function to find the complement of a strand of DNA
def complementary_strand(strand):
    return strand.translate(string.maketrans('TAGCtagc', 'ATCGATCG'))


 
#Function to count the number of mismatches between two sequences, IF accepted MISMATCH_COUNT is exceeded, stops counting mismatches and returns current value
def mismatch(read , virus_seq):
        if len(read) != len(virus_seq):
            print "Tried to compare to read sequences that were not the same length: \n\nlength of read = " + len(str(read)) + "\n" + "length of virus = "+ str(len(str(virus_seq)))
        else:
            mismatch_count = 0
            for i in range(0, len(str(virus_seq))):
                if str(read[i]) != str(virus_seq[i]):
                    mismatch_count += 1
                elif mismatch_count > k:
                    break
            return mismatch_count
                

            # EXAMPLE:

            #   CGTAGCGATAGAGAGAGAAGGGACT 
            #   CTGAG

birnaxrecords = []
a=0
for record in birna_x_virusdb.itervalues():
    birnaxrecords.append(record)
    #print "\nPrinting added record\n"
    #print record['sequence']
    birnaxrecords[a]['sequence'] = str(record['sequence'])
    a+=1

print birnaxrecords
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
segmentA = birna_x_virusdb[birna_x_virusdb.keys()[0]]
#print segmentA

#segment
#   {'description': 'Drosophila melanogaster birnavirus SW-2009a strain DBV segment A, complete sequence', 'id': 0, 'name': 'gi|262225302|gb|GQ342962.1|', 'sequence': <_screed_attr 'sequence'>}

print "\nPrinting second record...\n\t"
segmentB = birna_x_virusdb[birna_x_virusdb.keys()[1]]
#print segmentB

print "\nPrinting third record\n\t"
segmentXA = birna_x_virusdb[birna_x_virusdb.keys()[2]]
#print segmentXA

print "\nPrinting fourth record...\n\t"
segmentXB = birna_x_virusdb[birna_x_virusdb.keys()[3]]
#print segmentXB

screed.read_fasta_sequences("/Users/ivanjimenez/Desktop/CLASES/INTERNSHIPS/BIOINFO INTERNSHIP FILES/RESULTS/newresults/Trinity_de_genes.fa")
alltrinitygenesdb = ScreedDB(bioinfo_path + "Trinity_de_genes.fa_screed")

#print "Now adding all records in scytrimfasta database into an array.\n\nPlease wait..."

#Initializing the array to keep all records of viral sequences found
viral_sequences = []
#Keeping count of how many records have been checked...
iterator = 0



birnasegmentA = birnaxrecords[0]['sequence']
#print "\nPrinting the first segment in reverse:\n"
birnarevsegA = birnasegmentA[::-1]
#print birnarevsegA
#print "\nPrinting the first segment's complement:\n"
birnacomplementA = complementary_strand(birnarevsegA)
#print birnacomplementA


birnasegmentB = birnaxrecords[1]['sequence']
#print "\nPrinting the second segment in reverse:\n"
birnarevsegB = birnasegmentB[::-1]
#print birnarevsegB

#print "\nPrinting the second segment's complement:\n"
birnacomplementB = complementary_strand(birnarevsegB)
#print birnacomplementB

xvirussegmentA = birnaxrecords[2]['sequence']
#print "\nPrinting the first segment in reverse:\n"
xvirusrevsegA = xvirussegmentA[::-1]
#print birnarevsegA

#print "\nPrinting the first segment's complement:\n"
xviruscomplementA = complementary_strand(xvirusrevsegA)
#print birnacomplementA


xvirussegmentB = birnaxrecords[3]['sequence']
#print "\nPrinting the second segment in reverse:\n"
xvirusrevsegB = xvirussegmentB[::-1]
#print birnarevsegB

#print "\nPrinting the second segment's complement:\n"
xviruscomplementB = complementary_strand(xvirusrevsegB)
#print birnacomplementB



#BEGINNING 4 nested FOR LOOPS 
#grouping all known virus_segments (including complements) into an array...
virus_segments=(birnasegmentA, birnasegmentB, birnacomplementA, birnacomplementB, xvirussegmentA, xvirussegmentB, xviruscomplementA, xviruscomplementB)

#Loop through ALL 49Million reads
for trinitygene in alltrinitygenesdb.itervalues():
    #ISOLATE THE SEQUENCE IN THE RECORD
    trinitygeneseq = str(trinitygene['sequence'])
    #Loop through ALL 4 viralsegments
    for birnax_segment in virus_segments:
        #loop through all bases of the segment (or complement)
        for i in range(0, (int(len(birnax_segment))-int(len(trinitygeneseq))+1)): #bp in virus
            #reset mismatch to 0 for next comparison
            mismatches = mismatch(trinitygeneseq , birnax_segment[i:i+len(trinitygeneseq)])
            if mismatches <= k:
                print "FOUND A VIRAL SEQUENCE WHERE NONE SHOULD BE! Printing it now: "
                print trinitygeneseq
                viral_sequences.append(trinitygene)
                break 
        if mismatches <=k:
            break
    #If viral sequence is found, should print a warning and then the sequence, followed by the number of the sequence (out of 49million inspected)        
    print "Checked record #" + str(int(iterator)+1) + " from array."
    iterator += 1     


# print "\n\n\n"
# print "Printing the total (count) of all ScyTrim records\n"
# print str(iterator)
print "\n\n\n"
#print "THIS SHOULD PRINT: 1131"
print len(viral_sequences)

#An empty viral_sequences.csv file needs to be created before running this script!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if len(viral_sequences) != 0:
    editingfile = open(bioinfo_path + "viral_sequences.csv", "w+")
    editingfile.write(str(viral_sequences))



